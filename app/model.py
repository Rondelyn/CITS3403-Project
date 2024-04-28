
from typing import List

class image:
    def __init__(self, imageurl:str , imagecatagroy:str) -> None:
        self.imageurl:str = imageurl
        self.imagecatagroy:str = imagecatagroy


class topimages:
    def __init__(self, images:List[image]) -> None:
        self.images:List[image] = images