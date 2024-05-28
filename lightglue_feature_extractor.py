from LightGlue.lightglue import LightGlue, SuperPoint, DISK, SIFT, ALIKED, DoGHardNet
from LightGlue.lightglue.utils import load_image, rbd

import torch

class LightGlueExtractor:
    
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.extractor = SuperPoint(max_num_keypoints=2048).eval().to(self.device)  # load the extractor
        self.matcher = LightGlue(features="superpoint").eval().to(self.device)