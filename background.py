import os
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from PIL.PngImagePlugin import PngImageFile

from utils import draw_text_relative_to_point

GREY = "#51504F"
ROBOTO = "fonts/Roboto_Mono/RobotoMono-Medium.ttf"


def generate_background(
    city: str,
    month: str,
    day: int,
    year: int = None,
    event: str = "Airflow Meetup",
    dest: str = None,
) -> PngImageFile:
    img = Image.open("templates/event-cover-fb.png")
    img_w, _ = img.size

    # City name
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(ROBOTO, 120)
    draw_text_relative_to_point(draw, img_w / 2, 326, city, font, GREY, axis="x")
    draw_text_relative_to_point(draw, img_w / 2, 456, event, font, GREY, axis="x")

    # Date
    year = year or datetime.now().year

    day_map = {
        1: "1st",
        2: "2nd",
        3: "3rd",
        21: "21st",
        22: "22nd",
        23: "23rd",
        31: "31st",
    }
    day_text = day_map.get(day, f"{day}th")
    date_text = f"{month.capitalize()} {day_text}, {year}"
    font = ImageFont.truetype(ROBOTO, 60)
    draw_text_relative_to_point(draw, img_w / 2, 610, date_text, font, GREY, axis="x")

    name = f"{city}-{event}-cover.png"
    path = os.path.join(dest, name) if dest else name
    img.save(path)

    return img
