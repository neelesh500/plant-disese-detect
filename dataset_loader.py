"""
Dataset loader and feature extraction utility script.
"""
import cv2
import numpy as np
import os

class LeafFeatureExtractor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)

    def extract_color_features(self):
        """Extract HSV color moments."""
        if self.image is None: return None
        hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        return np.mean(hsv_image, axis=(0, 1))

    def extract_texture_features(self):
        """Placeholder for GLCM extraction."""
        # GLCM requires skimage.feature.graycoprops
        return {"contrast": 0.0, "homogeneity": 0.0}

    def extract_shape_features(self):
        """Extract simple morphological attributes."""
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
        return {"area": np.sum(thresh == 255)}

