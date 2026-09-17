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

