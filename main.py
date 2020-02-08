import os

from background import generate_background
from speaker import generate_speakers


EVENT = "Airflow Meetup"
CITY = "Warsaw"
MONTH = "January"
DAY = 21
YEAR = 2020


if not os.path.isdir("content"):
    os.mkdir("content")

if not os.path.isdir("content/speakers"):
    os.mkdir("content/speakers")

generate_background(event=EVENT, city=CITY, day=DAY, month=MONTH, year=YEAR, dest="content")
generate_speakers(event=EVENT, city=CITY, dest="content/speakers")