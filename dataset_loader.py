"""
Dataset loader and feature extraction utility script.
"""


import cv2
import numpy as np


class LeafFeatureExtractor:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)

    def extract_color_features(self):
        """Extract HSV color moments."""
        if self.image is None:
            return None
        hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        return np.mean(hsv_image, axis=(0, 1))

    def extract_texture_features(self):
        """Extract GLCM texture features."""
        from skimage.feature import graycomatrix, graycoprops

        if self.image is None:
            return None
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        glcm = graycomatrix(
            gray,
            distances=[5],
            angles=[0],
            levels=256,
            symmetric=True,
            normed=True,
        )
        return {
            "contrast": graycoprops(glcm, "contrast")[0, 0],
            "homogeneity": graycoprops(glcm, "homogeneity")[0, 0],
        }

    def extract_shape_features(self):
        """Extract simple morphological attributes."""
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
        return {"area": np.sum(thresh == 255)}

    def get_augmented_images(self):
        """Generate augmented images (rotation, flip, brightness)."""
        if self.image is None:
            return []
        
        images = []
        # Rotation
        (h, w) = self.image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, 45, 1.0)
        rotated = cv2.warpAffine(self.image, M, (w, h))
        images.append(rotated)
        
        # Flip
        flipped = cv2.flip(self.image, 1)
        images.append(flipped)
        
        return images
