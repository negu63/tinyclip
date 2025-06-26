from typing import Optional, Dict, Any
from cog import BasePredictor, Input
from transformers import CLIPModel, CLIPProcessor
from PIL import Image
import torch
import requests
import io

CACHE_DIR = "weights"
MODEL_NAME = "wkcn/TinyCLIP-ViT-8M-16-Text-3M-YFCC15M"

class Predictor(BasePredictor):
    def setup(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = CLIPModel.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR, local_files_only=True)
        self.model.to(self.device)
        self.processor = CLIPProcessor.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR, local_files_only=True)

    def predict(
        self,
        url: Optional[str] = Input(description="URL of the image to be vectorized.", default=None),
        image_base64: Optional[str] = Input(description="Base64 encoded image (webp, 224x224)", default=None),
        text: Optional[str] = Input(description="Text to be vectorized.", default=None)
    ) -> Dict[str, Any]:
        if not url and not image_base64 and not text:
            raise ValueError("Either 'url', 'image_base64', or 'text' must be provided.")

        result = {}

        # image embedding
        if url or image_base64:
            if image_base64:
                import base64
                image_data = base64.b64decode(image_base64)
                image = Image.open(io.BytesIO(image_data)).convert("RGB")
            else:
                response = requests.get(url, stream=True)
                response.raise_for_status()
                image = Image.open(io.BytesIO(response.content)).convert("RGB")
            inputs = self.processor(images=image, return_tensors="pt", padding=True)
            inputs = {k: v.to(self.device) for k, v in inputs.items()}

            with torch.no_grad():
                image_features = self.model.get_image_features(**inputs)
            result["image_vector"] = image_features[0].tolist()

        # text embedding
        if text:
            inputs = self.processor(text=[text], return_tensors="pt", padding=True)
            inputs = {k: v.to(self.device) for k, v in inputs.items()}

            with torch.no_grad():
                text_features = self.model.get_text_features(**inputs)
            result["text_vector"] = text_features[0].tolist()

        return result
