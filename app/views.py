# -*- coding: utf-8 -*-

from app import app, models, db
from flask import json

@app.route('/')
@app.route('/index')
def index():
  return 'Lunch Order'

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
#  print models.Restaurant.query.all()
  return json.dumps([m.to_dict() for m in models.Restaurant.query.all()], ensure_ascii = False)


@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
  r = models.Restaurant.query.filter_by(id=int(id))
  return json.dumps(r[0].to_dict(), ensure_ascii = False)

