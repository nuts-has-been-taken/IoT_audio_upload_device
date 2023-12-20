from tempfile import _TemporaryFileWrapper
from util.mp3_to_base import mp3_to_base64

def upload_audio_to_iottalk(audio:_TemporaryFileWrapper):
    
    try:
        base64_string = mp3_to_base64(audio)

        ### 上傳到 iottalk 

        return f"{audio.name}",f"Success upload"
    except Exception as e:
        return f"{audio.name}",f"Error: {e}"