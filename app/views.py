# -*- coding: utf-8 -*-

from app import app, models, db
from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
  return 'Lunch Order'

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
  print models.Restaurant.query.all()
  return '%r' % models.Restaurant.query.all()[0].name

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
  r = models.Restaurant.query.filter_by(id=int(id))
  return "%r" % r[0].name

