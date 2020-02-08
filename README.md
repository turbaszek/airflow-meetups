# Materials for Airflow meetups

Using this simple repo you can generate background image (facebook, meetup.com etc)
for your Airflow event. Additionally you can create speakers cards to promote
the event. 

The work is based on materials that were used during [Warsaw Airflow Meetup](https://www.meetup.com/pl-PL/Warsaw-Airflow-Meetup/) and are available on [Airflow cwiki](https://cwiki.apache.org/confluence/display/AIRFLOW/Promo+stuff).

## Installation and usage

Install requirements (for now only Pillow):
```sh
pip install -r requirements.txt
```

Usage:
- update `speakers.csv` with information about your speakers and with valid paths to 
their photos. Note that the format of the csv should be `name,association,path_to_pic`.
Header is ignored and the file is parsed in primitive way but I wanted to skip additional
deps like pandas.
- run `main.py`

All pictures should appear in `content/`.

