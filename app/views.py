# -*- coding: utf-8 -*-

from app import app, sock, models, db
from flask import json, abort, make_response, request, render_template, url_for
from models import Restaurant
from datetime import datetime
import time
from flask.ext.socketio import emit

@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/api/restaurants', methods=['GET'])
def get_restaurants():
  return json.dumps({"restaurants": [to_public(m.to_dict()) for m in Restaurant.query.all()]}, ensure_ascii = False)


@app.route('/api/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
  r = Restaurant.query.get(id)
  if r:
    return json.dumps(to_public(r.to_dict()), ensure_ascii = False)
  else:
    abort(404)

@app.route('/api/restaurants', methods=['POST'])
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

@app.route('/api/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
  r = Restaurant.query.get(restaurant_id)
  if r:
    db.session.delete(r)
    db.session.commit()
    return json.dumps({'result': 'successed'})
  else:
    abort(404)

@app.route('/api/restaurants/<int:restaurant_id>', methods=['PUT'])
def update_restaurant(restaurant_id):
  restaurant = Restaurant.query.get(restaurant_id)
  if restaurant:
    r = request.json

    op = r['op'].strip().lower()
    if op == 'rankup':
      restaurant.rating += 1
    elif op == 'rankdown':
      restaurant.rating -= 1

    db.session.commit()
    return json.dumps({'restaurant': to_public(restaurant.to_dict())})
  else:
    abort(404)

@app.errorhandler(404)
def not_found(error):
  return make_response(json.dumps({'error': 'not found'}), 404)

def to_public(restaurant_from):
  restaurant_to = restaurant_from.copy()
  restaurant_to['uri'] = url_for('get_restaurant', id = restaurant_from['id'], _external = True)
  del(restaurant_to['id'])
  return restaurant_to

def background_thread():
  while True:
    t = str(datetime.now())
    sock.emit('my response', {'data': t}, namespace='/test')
    time.sleep(10)

@sock.on('connect', namespace='/test')
def test_connect():
  print "connected"
#    emit('my response', {'data': 'Connected'})

@sock.on('rank event', namespace='/test')
def test_message(message):
  print message['data']
  emit('my response', {'data': message['data']}, namespace='/test', broadcast=True)
