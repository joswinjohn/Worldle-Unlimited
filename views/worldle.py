import string
import random
import json
from locations.country import Country
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('worldle', __name__, url_prefix='/worldle')

@bp.route('/worldle')
def worldle():
  selected_country=get_random_country()
  print(selected_country)
  return render_template('index.html', selected_country=selected_country)

def get_random_country():
    raw_json = open('locations/countries-position.json','r')
    json_objs = json.loads(raw_json.read())

    country_dict = random.choice(json_objs['values'])
    return country_dict