import os

from PIL import Image, ImageDraw, ImageFont
from PIL.ImageFont import FreeTypeFont
from PIL.PngImagePlugin import PngImageFile

from utils import draw_text_relative_to_point

BASE_X = 829.33
GREY = "#51504F"
RUBIK = "fonts/Rubik/Rubik-Medium.ttf"
ROBOTO = "fonts/Roboto_Mono/RobotoMono-Medium.ttf"


def generate_speaker_template(
    name: str,
    association: str,
    path_to_picture: str,
    city: str = "Warsaw",
    event: str = "Airflow Meetup",
    dest: str = None,
) -> PngImageFile:
    img = Image.open("templates/speaker-template.png")
    draw = ImageDraw.Draw(img)

    # Event info
    font = ImageFont.truetype(RUBIK, 50)
    draw_text_relative_to_point(draw, BASE_X, 625, city, font, GREY, axis="x")
    draw_text_relative_to_point(draw, BASE_X, 687, event, font, GREY, axis="x")

    # Speaker info
    name = name + ","
    font = ImageFont.truetype(ROBOTO, 36)
    draw_text_relative_to_point(draw, BASE_X, 761, name, font, GREY, axis="x")
    draw_text_relative_to_point(draw, BASE_X, 810, association, font, GREY, axis="x")

    # Speaker image
    speaker_img = Image.open(path_to_picture)
    small_face = speaker_img.resize((520, 520)).convert("LA")
    img.paste(small_face, (54, 504))

    file_name = f"speaker-{name.lower().replace(' ', '-').replace(',', '')}.png"
    path = os.path.join(dest, file_name) if dest else file_name
    img.save(path)
    return img


def generate_speakers(city: str, event: str, dest: str = "content"):
    with open("speakers.csv", "r+") as f:
        for i, l in enumerate(f.readlines()):
            if i == 0:
                continue
            name, association, path = l.split(",")
            generate_speaker_template(
                name, association, path.strip(), city, event, dest
            )
