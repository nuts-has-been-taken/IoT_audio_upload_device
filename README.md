# IoT_audio_upload_device
Upload mp3 and transfer to base64 string for iottalk class in NYCU

### To use:

```bash
git clone https://github.com/nuts-has-been-taken/IoT_audio_upload_device.git
```

### Install the requirement
```bash
pip install -r requirements.txt
```

### Rename the file
rename the file name from `.env_example` to `.env` and modify the environment variables inside. When starting the server, the environment variables will be automatically loaded through 
```python
load_dotenv()
```

### Start the server
```bash
python main_page.py
```
this will start the server with host 0.0.0.0, if you want to change the IP address, rewrite the host name in here [main_page.py](https://github.com/nuts-has-been-taken/IoT_audio_upload_device/blob/main/main_page.py)
