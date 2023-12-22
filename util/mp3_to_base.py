from tempfile import _TemporaryFileWrapper
import base64

# mp3 轉換成 string
def mp3_to_base64(file:_TemporaryFileWrapper):
    try:
        with open(file.name, 'rb') as mp3_file:
            mp3_binary_data = mp3_file.read()
            print("type of mp3 file : {}".format(type(mp3_binary_data)))
            print("length of mp3 file : {}".format(len(mp3_binary_data)))
            
            base64_encoded = base64.b64encode(mp3_binary_data)
            
            base64_string = base64_encoded.decode('utf-8')
        
        return base64_string
    except Exception as e:
        print(f"Error: {e}")
        return None

# 從 string 轉換為 mp3
def base64_to_mp3(base64_string, output_file_path):
    try:
        mp3_binary_data = base64.b64decode(base64_string)
        
        with open(output_file_path, 'wb') as mp3_file:
            mp3_file.write(mp3_binary_data)
        
        print(f"檔案成功轉換並儲存於 {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")