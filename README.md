# TinyCLIP-ViT-8M-16-Text-3M-YFCC15M Embeddings 🚀

<img src="https://github.com/user-attachments/assets/f01fe5fe-9ec3-467c-a880-3996f04184e4" width="20%" alt="tinyclip-cover">

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
    - TinyCLIP uses images preprocessed to 224x224 pixels for inference.  
    - **To prepare your image:**  
        - **Resize the shorter side of your image to 224 pixels** while maintaining the original aspect ratio.  
        - **Crop the center of the resized image** to exactly 224x224 pixels.  
        - **Encode the resulting image as base64.**  
    - This process avoids extra download and resize steps on the server, making predictions much faster.  
- **Image URL:**  
    - You can still use an image URL. In this case, the model will automatically download the image, preprocess it as described above, and run inference.


## Performance \& Precision

This model is designed for speed and simplicity, not ultra-high accuracy.  
The returned embeddings are in full precision (float32), but you can use or store them as half-precision (float16) if desired—this is efficient and works well for most use cases!

⚡ **Have fun embedding!**

🚀 **Try it now:** [TinyCLIP on Replicate](https://replicate.com/negu63/tinyclip)  
🔗 **GitHub:** [TinyCLIP for Replicate](https://github.com/negu63/tinyclip)
