from PIL import ImageDraw
from PIL.ImageFont import FreeTypeFont


def adjust_font_to_width(
    draw: ImageDraw.Draw, font: FreeTypeFont, text: str, start_size: int, width: float
) :
    for size in range(start_size, int(start_size / 2), 2):
        text_width, _ = draw.textsize(text, font)
        if text_width < width:
            FreeTypeFont.size = size
            break


def draw_text_relative_to_point(
    draw: ImageDraw.Draw,
    x: float,
    y: float,
    text: str,
    font: FreeTypeFont,
    color: str,
    axis=None,
):
    text_width, text_heigth = draw.textsize(text, font)
    if axis == "x":
        position = (x - text_width / 2, y)
    elif axis == "y":
        position = (x, y - text_heigth / 2)
    else:
        position = (x - text_width / 2, y - text_heigth / 2)
    draw.text(position, text, color, font=font)
