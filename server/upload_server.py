import gradio as gr
import shutil
import os
import uuid

def upload_file(file):
    hex_uuid = uuid.uuid4().hex
    shutil.copy2(file.name, os.path.join("./data/", hex_uuid + "_" + os.path.basename(file.name)))
    return "File uploaded successfully!"

demo = gr.Interface(
    upload_file,
    gr.File(label="Upload a file"),
    "text",
    title="File Uploader",
    description="Upload a file to a specified location",
)

if __name__ == "__main__":
    demo.launch(share=True)
