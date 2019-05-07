import enum
from dataclasses import dataclass, field
from typing import Tuple, List, Union, Optional

from PIL import ImageColor, FontFile, Image

Color = Union[Tuple[int, int, int], Tuple[int, int, int, int]]
white_color = (255, 255, 255)


@dataclass
class ImageElement(object):
    x: int
    y: int

    @property
    def location(self):
        return self.x, self.y


class TextAlignment(enum.Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class TextDirection(enum.Enum):
    RTL = "rtl"
    LTR = "ltr"
    TTB = "ttb"
    BBT = "bbt"

@dataclass
class TextElement(ImageElement):
    text: str
    font: FontFile
    text_color: Color = white_color
    background_color: Optional[Color] = None
    align: TextAlignment = TextAlignment.LEFT
    direction: TextDirection = TextDirection.LTR




@dataclass
class WrappingTextElement(TextElement):
    pass


@dataclass
class ImageTemplate(object):
    height: int
    width: int
    background_image: Image
    background_color: ImageColor
    elements: List[ImageElement]

