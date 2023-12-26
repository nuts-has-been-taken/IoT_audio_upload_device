import time
from tempfile import _TemporaryFileWrapper
from util.audio_to_base import m4a_to_base64

from service import DAN

from service.register import IDF_list, IDF_funcs

def upload_audio_to_iottalk(audio:_TemporaryFileWrapper):
    
    try:
        audio_file_type = audio.name[-3:]
        if audio_file_type != "mp3" and audio_file_type != "m4a":
            return f"{audio.name}",f"Only support mp3 or m4a file"
        
        base64_string = m4a_to_base64(audio)

        print("string length : {}".format(len(base64_string)))

        ### 上傳到 iottalk
        print(IDF_list)
        print(IDF_funcs)
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
