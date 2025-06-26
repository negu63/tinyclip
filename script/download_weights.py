#!/usr/bin/env python

import os
import shutil
from transformers import CLIPModel, CLIPProcessor

CACHE_DIR = "weights"

if os.path.exists(CACHE_DIR):
    shutil.rmtree(CACHE_DIR)

os.makedirs(CACHE_DIR)

print("Downloading TinyCLIP model and processor to cache directory...")

model = CLIPModel.from_pretrained("wkcn/TinyCLIP-ViT-8M-16-Text-3M-YFCC15M", cache_dir=CACHE_DIR)
processor = CLIPProcessor.from_pretrained("wkcn/TinyCLIP-ViT-8M-16-Text-3M-YFCC15M", cache_dir=CACHE_DIR)

print("Done.")
