
from models.database import *
from models.entities import *
from flask import Flask, url_for, render_template, session, escape, request, redirect, jsonify

app = Flask(__name__)


@app.route('/api/mozillians', methods = ['GET'])
def getMozillians():
  return jsonify({'mozillians':map(lambda em: em.toDict(), Mozillian.select())})

@app.route('/api/mozillians/<int:mozillian_id>', methods = ['GET'])
def getMozillianById(mozillian_id):
  try:
    return jsonify(Mozillian.selectBy(id = mozillian_id).getOne().toDict())
  except SQLObjectNotFound:
    return '{}'


@app.route('/api/engagements', methods = ['GET'])
def getEngagements():
  return jsonify({'engagements':map(lambda e: e.toDict(), Engagement.select())})

@app.route('/api/engagements/<int:engagement_id>', methods = ['GET'])
def getEngagementById(engagement_id):
  try:
    return jsonify(Engagement.selectBy(id = engagement_id).getOne().toDict())
  except SQLObjectNotFound:
    return '{}'

@app.route('/api/checkins', methods = ['GET'])
def getCheckins():
  return jsonify({'checkins':map(lambda c: c.toDict(), Checkin.select())})

@app.route('/api/checkins/<int:checkin_id>', methods = ['GET'])
def getCheckinById(checkin_id):
  try:
    return jsonify(Checkin.selectBy(id = checkin_id).getOne().toDict())
  except SQLObjectNotFound:
    return '{}'


@app.route('/')
def home():
  return 'Hello World'

if __name__ == '__main__':
  app.run(debug = True, host = '0.0.0.0')

