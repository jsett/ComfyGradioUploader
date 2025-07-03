from inspect import cleandoc
from cryptography.fernet import Fernet
import os

class GradioUploader:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE", { "tooltip": "This is an image"}),
                "url": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "folder": ("STRING", {
                    "multiline": False,
                    "default": ""
                })
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Status",)
    FUNCTION = "upload"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    CATEGORY = "GradioUploader"

    def upload(self, image, url, folder):
        from io import BytesIO
        import requests
        import time
        import json
        import io
        import uuid
        from PIL import Image
        import numpy as np

        url = url.rstrip('/')

        for idx, image2 in enumerate(image):
            i = 255. * image2.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            byte_io = BytesIO()
            img.save(byte_io, 'png')
            byte_io.seek(0)

            site = url

            full_url = f"{url}/gradio_api/upload"
            params = {"upload_id": "dg5oan1rojl"}

            headers = {
                "accept": "*/*",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "sec-gpc": "1"
            }

            fp = byte_io
            files = {"files": fp}

            response = requests.post(full_url, params=params, headers=headers, files=files)

            uploadpath = response.json()[0]

            full_url = f"{url}/gradio_api/upload_progress"

            headers = {
                "accept": "text/event-stream",
                "content-type": "application/json",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "sec-gpc": "1"
            }

            response = requests.get(full_url, params=params, headers=headers, cookies=None)

            full_url = f"{url}/gradio_api/queue/join?"
            headers = {
                "accept": "*/*",
                "content-type": "application/json",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "sec-gpc": "1"
            }

            data = {
                "data": [
                    {
                        "path": uploadpath,
                        "url": f"{url}/gradio_api/file={uploadpath}",
                        "orig_name": "min.txt",
                        "mime_type": "image/png",
                        "meta": {"_type": "gradio.FileData"}
                    },
                    folder
                ],
                "event_data": None,
                "fn_index": 0,
                "trigger_id": 10,
                "session_hash": "3jor3k0v1nf"
            }

            headers["content-type"] = "application/json"
            response = requests.post(full_url, headers=headers, data=json.dumps(data))

        return ("Done",)

class GradioUploaderEncrypt:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE", { "tooltip": "This is an image"}),
                "url": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "folder": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
                "key": ("STRING", {
                    "multiline": False,
                    "default": ""
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Status",)
    FUNCTION = "uploadEncrypt"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    CATEGORY = "GradioUploader"

    def uploadEncrypt(self, image, url, folder, key):
        from io import BytesIO
        import requests
        import time
        import json
        import io
        import uuid
        from PIL import Image
        import numpy as np

        url = url.rstrip('/')

        for idx, image2 in enumerate(image):
            i = 255. * image2.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            byte_io = BytesIO()
            img.save(byte_io, 'png')
            byte_io.seek(0)

            site = url

            full_url = f"{url}/gradio_api/upload"
            params = {"upload_id": "dg5oan1rojl"}

            headers = {
                "accept": "*/*",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "sec-gpc": "1"
            }

            bytes_io_encrypt = io.BytesIO()
            cipher_suite = Fernet(key)
            encrypted_data = cipher_suite.encrypt(bytes_io.getvalue())
            bytes_io_encrypt.write(encrypted_data)
            bytes_io_encrypt.seek(0)

            fp = bytes_io_encrypt
            files = {"files": fp}

            response = requests.post(full_url, params=params, headers=headers, files=files)

            uploadpath = response.json()[0]

            full_url = f"{url}/gradio_api/upload_progress"

            headers = {
                "accept": "text/event-stream",
                "content-type": "application/json",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "sec-gpc": "1"
            }

            response = requests.get(full_url, params=params, headers=headers, cookies=None)

            full_url = f"{url}/gradio_api/queue/join?"
            headers = {
                "accept": "*/*",
                "content-type": "application/json",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "sec-gpc": "1"
            }

            data = {
                "data": [
                    {
                        "path": uploadpath,
                        "url": f"{url}/gradio_api/file={uploadpath}",
                        "orig_name": "min.txt",
                        "mime_type": "image/png",
                        "meta": {"_type": "gradio.FileData"}
                    },
                    folder
                ],
                "event_data": None,
                "fn_index": 0,
                "trigger_id": 10,
                "session_hash": "3jor3k0v1nf"
            }

            headers["content-type"] = "application/json"
            response = requests.post(full_url, headers=headers, data=json.dumps(data))

        return ("Done",)

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "GradioUploader": GradioUploader,
    "GradioUploaderEncrypt": GradioUploaderEncrypt,
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "GradioUploader": "Gradio Uploader"
    "GradioUploaderEncrypt": "GradioUploaderEncrypt"
}

