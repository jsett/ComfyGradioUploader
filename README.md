# gradioUploader

Use gradio to upload to your local computer. This probect is mainly for those running ComfyUI in the cloud. This project includes a comfyUI extention along with a server app to use locally. Since gradio can create shared links that cross over the firewall, you can run the server half of this on your local computer without any special settings. Then give the link to comfy along with a subfolder and thats it.

## ComfyUI Setup

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/jsett/ComfyGradioUploader.git
```

Now Restart ComfyUI.

## Server Setup

see `server/readme.md`
