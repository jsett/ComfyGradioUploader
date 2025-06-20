#!/home/user/.pyenv/shims/python3
import gradio as gr
import shutil
import os
import uuid

def upload_file(file, folder_name):
    hex_uuid = uuid.uuid4().hex
    if folder_name == "":
        dir_path = os.getcwd()
    else:
        dir_path = os.path.join(os.getcwd(), folder_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    shutil.copy2(file.name, os.path.join(dir_path, hex_uuid + "_" + os.path.basename(file.name)))
    return "File uploaded successfully!"

demo = gr.Interface(
    upload_file,
    [gr.File(label="Upload a file"),
    gr.Textbox(label="Folder")],
    "text",
    title="File Uploader",
    description="Upload a file to a specified location",
)

if __name__ == "__main__":
    demo.launch(share=True)
