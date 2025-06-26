# TinyCLIP-ViT-8M-16-Text-3M-YFCC15M Embeddings 🚀

A lightweight model for generating 512-dimensional embeddings from images and/or text. Deployed on [Replicate](https://replicate.com/negu63/tinyclip).

## How to Use

**Inputs:**
You can provide:

- **Image URL** (for hosted images)
- **Base64-encoded image** (for quick inference)
- **Text** (for text embeddings)

**Outputs:**

- **If both image and text are provided:**
    - `image_vector`: 512D embedding of the image
    - `text_vector`: 512D embedding of the text
- **If only one is provided:**
    - Only the corresponding vector is returned

**Priority:**
If both image URL and base64 image are given, the base64 image is used.

## Why Use Base64 Images?

TinyCLIP preprocesses images to 224x224 pixels for inference.
To minimize cloud inference time, you can resize and crop your image locally to 224x224, then encode it as base64.
This avoids the download and resize steps on the server, making predictions faster and more efficient!

**Best practice for base64 images:**

- Resize the shorter side of your image to 224px (keeping aspect ratio)
- Crop the center to 224x224px
- Encode the result as base64

## Still Accepts Image URLs

You can still use image URLs. The model will download, resize, and process the image automatically.

Performance & Precision

This model is designed for speed and simplicity, not ultra-high accuracy.
The returned embeddings are in full precision (float32), but you can use or store them as half-precision (float16) if desired—this is efficient and works well for most use cases!

⚡ **Have fun embedding!**

🚀 **Try it now:** [TinyCLIP on Replicate](https://replicate.com/negu63/tinyclip)
🔗 **GitHub:** [TinyCLIP for Replicate](https://github.com/negu63/tinyclip)
