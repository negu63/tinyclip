# TinyCLIP-ViT-8M-16-Text-3M-YFCC15M Embeddings 🚀

<img src="https://github.com/user-attachments/assets/1ba89e72-f86c-4dd3-b272-51d7c80424ed" width="20%" alt="tinyclip-cover">

A lightweight model for generating 512-dimensional embeddings from images and/or text.  
Deployed on [Replicate](https://replicate.com/negu63/tinyclip).

## How to Use

**Inputs**
At least one of the following is required:

- **`url`** (string, optional): A publicly accessible image URL.  
- **`image_base64`** (string, optional): A base64-encoded image string.  
- **`text`** (string, optional): Any text string for embedding.  

> **Note:**  
> - If both `url` and `image_base64` are provided, only `image_base64` will be used.  
> - At least one input is required.  

**Outputs**
Depending on your input, the model returns:

- **`image_vector`** (array of 512 floats): The embedding vector for the provided image (if any).  
- **`text_vector`** (array of 512 floats): The embedding vector for the provided text (if any).  

If both image and text are provided, both vectors are returned.  
If only one input is given, only the corresponding vector is returned.

## Best Practices

- **Base64 Images:**
    - TinyCLIP preprocesses images to 224x224 pixels for inference.  
    - To minimize cloud inference time, resize and crop your image locally to 224x224 (keeping aspect ratio), then encode as base64.  
    - This avoids extra download and resize steps, making predictions faster.  
- **Image URL:**
    - You can still use image URL. The model will download, resize, and process the image automatically.  


## Performance \& Precision

This model is designed for speed and simplicity, not ultra-high accuracy.  
The returned embeddings are in full precision (float32), but you can use or store them as half-precision (float16) if desired—this is efficient and works well for most use cases!

⚡ **Have fun embedding!**

🚀 **Try it now:** [TinyCLIP on Replicate](https://replicate.com/negu63/tinyclip)  
🔗 **GitHub:** [TinyCLIP for Replicate](https://github.com/negu63/tinyclip)
