import time
from tempfile import _TemporaryFileWrapper
from util.mp3_to_base import mp3_to_base64

from service import DAN

from service.register import IDF_list, IDF_funcs

def upload_audio_to_iottalk(audio:_TemporaryFileWrapper):
    
    try:
        if audio.name[-3:] != "mp3":
            return f"{audio.name}",f"Only support mp3 file"
        
        base64_string = mp3_to_base64(audio)

        print("string length : {}".format(len(base64_string)))

        ### 上傳到 iottalk
        for idf in IDF_list:
            if not IDF_funcs.get(idf):
                print('IDF function "{}" is not existed.'.format(idf))
                continue
            IDF_data = IDF_funcs.get(idf)(base64_string)
            if IDF_data == None: continue
            if type(IDF_data) is not tuple: IDF_data=[IDF_data]
            DAN.push(idf, IDF_data)
            time.sleep(0.001)

        return f"{audio.name}",f"Success upload"
    except Exception as e:
        return f"{audio.name}",f"Error: {e}"
