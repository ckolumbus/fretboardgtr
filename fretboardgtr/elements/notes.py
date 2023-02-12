from fretboardgtr.constants import BLACK, WHITE

from dataclasses import dataclass
from typing import Tuple
from typing import Optional

TEXT_OFFSET = "0.3em"
TEXT_STYLE = "text-anchor:middle"
from fretboardgtr.elements.base import FretBoardElement
from fretboardgtr.base import ConfigIniter
import svgwrite


@dataclass
class OpenNoteConfig(ConfigIniter):
    radius: int = 20
    color: str = WHITE
    stroke_color: str = BLACK
    stroke_width: int = 3
    text_color: str = BLACK
    fontsize: int = 20
    fontweight: str = "bold"


class OpenNote(FretBoardElement):
    def __init__(
        self,
        name: str,
        position: Tuple[float, float],
        config: Optional[OpenNoteConfig] = None,
    ):
        self.config = config if config else OpenNoteConfig()
        self.name = name
        self.x = position[0]
        self.y = position[1]

    def get_svg(self) -> svgwrite.base.BaseElement:
        note = svgwrite.container.Group()
        circle = svgwrite.shapes.Circle(
            (self.x, self.y),
            r=self.config.radius,
            fill=self.config.color,
            stroke=self.config.stroke_color,
            stroke_width=self.config.stroke_width,
        )
        text = svgwrite.text.Text(
            self.name,
            insert=(self.x, self.y),
            dy=[TEXT_OFFSET],
            font_size=self.config.fontsize,
            fill=self.config.text_color,
            font_weight=self.config.fontweight,
            style=TEXT_STYLE,
        )
        note.add(circle)
        note.add(text)
        return note


@dataclass
class FrettedNoteConfig(ConfigIniter):
    radius: int = 20
    color: str = WHITE
    stroke_color: str = BLACK
    stroke_width: int = 3
    text_color: str = BLACK
    fontsize: int = 20
    fontweight: str = "bold"


class FrettedNote(FretBoardElement):
    def __init__(
        self,
        name: str,
        position: Tuple[float, float],
        config: Optional[FrettedNoteConfig] = None,
    ):
        self.config = config if config else FrettedNoteConfig()
        self.name = name
        self.x = position[0]
        self.y = position[1]

    def get_svg(self) -> svgwrite.base.BaseElement:
        note = svgwrite.container.Group()
        circle = svgwrite.shapes.Circle(
            (self.x, self.y),
            r=self.config.radius,
            fill=self.config.color,
            stroke=self.config.stroke_color,
            stroke_width=self.config.stroke_width,
        )

        text = svgwrite.text.Text(
            self.name,
            insert=(self.x, self.y),
            dy=[TEXT_OFFSET],
            font_size=self.config.fontsize,
            fill=self.config.text_color,
            font_weight="bold",
            style=TEXT_STYLE,
        )
        note.add(circle)
        note.add(text)
        return note