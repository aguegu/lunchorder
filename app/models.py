from app import db
from flask import json

class Restaurant(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(32), index = True, unique = True)
  telephone = db.Column(db.String(64), index = True, nullable = False)
  address = db.Column(db.String(128), default = '')
  rating = db.Column(db.SmallInteger, default = 0)
  dishes = db.relationship('Dish', backref = 'suppiler', lazy = 'dynamic')

  def __repr__(self):
    return "Restaurant <%r>" % self.title.encode('utf-8')

  def to_dict(self):
    return {
      "id": self.id,
      "title": self.title,
      "telephone": self.telephone,
      "address": self.address,
      "rating": self.rating
    }

class Dish(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(32))
  price = db.Column(db.Numeric(8, 2))
  rating = db.Column(db.SmallInteger, default = 0)
  restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))

  def __repr__(self):
    return "Dish <%r>" % self.title
