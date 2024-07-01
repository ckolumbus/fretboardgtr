from dataclasses import dataclass
from typing import Optional, Tuple

from fretboardgtr.constants import BLACK, WHITE

TEXT_OFFSET = "0.3em"
TEXT_STYLE = "text-anchor:middle"
import svgwrite

from fretboardgtr.base import ConfigIniter
from fretboardgtr.elements.base import FretBoardElement


@dataclass
class OpenNoteConfig(ConfigIniter):
    """OpenNote element configuration."""

    radius: int = 20
    color: str = WHITE
    stroke_color: str = BLACK
    stroke_width: int = 3
    text_color: str = BLACK
    fontsize: int = 20
    fontweight: str = "bold"


class OpenNote(FretBoardElement):
    """Open notes elements to be drawn in the final fretboard."""

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
        """Convert the OpenNote to a svgwrite object.

        This maps the OpenNoteConfig configuration attributes to the svg
        attributes
        """
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
    """Fretted notes elements to be drawn in the final fretboard."""

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
        """Convert the FrettedNote to a svgwrite object.

        This maps the FrettedNoteConfig configuration attributes to the
        svg attributes
        """
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

@dataclass
class BarreConfig(ConfigIniter):
    radius: int = 20
    color: str = BLACK
    stroke_color: str = BLACK
    stroke_width: int = 3
    text_color: str = WHITE
    fontsize: int = 20
    fontweight: str = "bold"


class Barre(FretBoardElement):
    """Barre elements to be drawn in the final fretboard."""

    def __init__(
        self,
        position: Tuple[float, float],
        size: Tuple[float, float],
        text: str,
        config: Optional[BarreConfig] = None,
    ):
        self.config = config if config else BarreConfig()
        self.pos = position
        self.size = size
        self.text = text

    def get_svg(self) -> svgwrite.base.BaseElement:
        """Convert the Barre to a svgwrite object.

        This maps the BarreConfig configuration attributes to the
        svg attributes
        """
        barre = svgwrite.container.Group()

        print(self.pos)
        print(self.size)

        rect = svgwrite.shapes.Rect(
            self.pos,
            self.size,
            rx=self.config.radius,
            ry=self.config.radius,
            fill=self.config.color,
            stroke=self.config.stroke_color,
            stroke_width=self.config.stroke_width,
        )

        text = svgwrite.text.Text(
            self.text,
            insert=(self.pos[0] + self.size[0]/2, self.pos[1]+self.size[1]/2),
            dy=[TEXT_OFFSET],
            font_size=self.config.fontsize,
            fill=self.config.text_color,
            font_weight="bold",
            style=TEXT_STYLE,
        )

        barre.add(rect)
        barre.add(text)
        return barre