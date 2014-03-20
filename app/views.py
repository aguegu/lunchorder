# -*- coding: utf-8 -*-

from app import app, models, db
from flask import json, abort, make_response, request
from models import Restaurant

@app.route('/')
@app.route('/index')
def index():
  return 'Lunch Order'

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
  return json.dumps([m.to_dict() for m in Restaurant.query.all()], ensure_ascii = False)


@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
  r = Restaurant.query.get(id)
  if r:
    return json.dumps(r.to_dict(), ensure_ascii = False)
  else:
    abort(404)

@app.route('/restaurants', methods=['POST'])
def create_restaurant():
  r = request.json
  if not r or 'name' not in r or type(r['name']) is not unicode or len(r['name'].strip()) < 2:
    abort(400)

  name = r['name'].strip().lower()

  if Restaurant.query.filter_by(name = name).count(): 
    abort(409)
  else:
    restaurant = Restaurant(**r)
    db.session.add(restaurant)
    db.session.commit()
    return json.dumps(restaurant.to_dict(), ensure_ascii = False)

@app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
  r = Restaurant.query.get(restaurant_id)
  if r:
    db.session.delete(r)
    db.session.commit()
    return json.dumps({'result': 'successed'})
  else:
    abort(404)
  

@app.errorhandler(404)
def not_found(error):
  return make_response(json.dumps({'error': 'not found'}), 404)
