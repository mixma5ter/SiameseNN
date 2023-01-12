import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, 'models')
IMAGES_DIR = os.path.join(BASE_DIR, 'images')
DATA_DIR = os.path.join(BASE_DIR, 'data')

IMAGE_SIZE = 128
