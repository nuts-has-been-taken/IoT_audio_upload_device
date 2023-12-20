from dotenv import load_dotenv
load_dotenv()

import gradio as gr
from service.upload_audio import upload_audio_to_iottalk


with gr.Blocks() as upload_page:
    gr.Markdown("""
                # IoTtalk 音訊收集系統
                將上傳的音訊轉換成 string 傳送到 iottalk 進行下一步處理
                """)
    file_output = gr.File(interactive=False, file_types=["file"], label="上傳 MP3 檔案")
    upload_button = gr.UploadButton("上傳檔案", file_types=["file"])
    upload_messagebox = gr.Textbox(label="上傳結果", info="顯示上傳情況")
    upload_button.upload(upload_audio_to_iottalk, upload_button, [file_output, upload_messagebox])

iface = gr.TabbedInterface([upload_page], ["上傳頁面"])
iface.launch(server_name="0.0.0.0")