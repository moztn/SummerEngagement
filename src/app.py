
from models.database import *
from models.entities import *
from datetime import datetime
from flask import Flask, url_for, render_template, session, escape, request,\
       redirect, jsonify, abort, make_response
from flask.ext.login import LoginManager, login_required, current_user
from flask.ext.browserid import BrowserID
from flask.ext.cors import cross_origin

def get_user_by_id(aId):
  try:
    m = Mozillian.selectBy(id = aId).getOne()
    return m
  except SQLObjectNotFound:
    return None

def get_user(kwargs):
  try:
    m = Mozillian.selectBy(email= kwargs['email']).getOne()
    return m
  except SQLObjectNotFound:
    return create_user(kwargs)



def create_user(kwargs):
  if kwargs['status'] == 'okay':
    m = Mozillian(nickname = None, engagement = None, email = kwargs['email'])
    return m
  else:
    return None



app = Flask(__name__)

app.config['SECRET_KEY'] = "deterministic"

login_manager = LoginManager()
login_manager.user_loader(get_user_by_id)
login_manager.init_app(app)

browser_id = BrowserID()
browser_id.user_loader(get_user)
browser_id.redirect_url = '/u/me'
browser_id.init_app(app)


@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify({'error':'Not found'}), 404)

@app.route('/api/mozillians', methods = ['GET'])
@cross_origin(headers=['Content-Type'])
def getMozillians():
  moz = map(lambda em: em.toDict(), Mozillian.select())

  if len(moz) == 0:
    abort(404)

  return jsonify({'mozillians':moz})

@app.route('/api/mozillians/<int:mozillian_id>', methods = ['GET'])
@cross_origin(headers=['Content-Type'])
def getMozillianById(mozillian_id):
  try:
    return jsonify(Mozillian.selectBy(id = mozillian_id).getOne().toDict())
  except SQLObjectNotFound:
    return abort(404)

@app.route('/api/mozillians', methods = ['POST'])
@login_required
@cross_origin(headers=['Content-Type'])
def create_mozillian():
  if not request.json or not 'nickname' in request.json:
    abort(400)

  email = current_user.email
  try:
    m = Mozillian.selectBy(email = email).getOne()
    m.nickname = request.json['nickname']
    return jsonify(m.toDict()), 201
  except SQLObjectNotFound:
    return abort(400)


@app.route('/api/engagements', methods = ['GET'])
@cross_origin(headers=['Content-Type'])
def getEngagements():
  engagements = map(lambda e: e.toDict(), Engagement.select())
  
  if len(engagements) == 0:
    abort(404)

  return jsonify({'engagements':map(lambda e: e.toDict(), Engagement.select())})

@app.route('/api/engagements/<int:engagement_id>', methods = ['GET'])
@cross_origin(headers=['Content-Type'])
def getEngagementById(engagement_id):
  try:
    return jsonify(Engagement.selectBy(id = engagement_id).getOne().toDict())
  except SQLObjectNotFound:
    return abort(404)


@app.route('/api/engagements', methods = ['POST'])
@cross_origin(headers=['Content-Type'])
@login_required
def createEngagement():
  if not request.json or not ('numberOfDays' in request.json and\
                               'numberOfHours' in request.json and\
                               'startingDay' in request.json):
    abort(400)

    days = None
    hours = None
    start = None
    startDate = None
  try:
    days = int(request.json['numberOfDays'])
    hours = int(request.json['numberOfHours'])
    start = request.json['startingDay']

    startDate = datetime.strptime(start, '%Y/%m/%d')
  except ValueError:
    abort(400)

  eng = Engagement(numberOfDays = days, numberOfHours = hours, startingDay = startDate)

  # We assigne the created engagement to the logged user.
  current_user.engagement = eng.id
  return jsonify(eng.toDict()), 201

@app.route('/api/checkins', methods = ['GET'])
@cross_origin(headers=['Content-Type'])
def getCheckins():
  checkins = map(lambda c: c.toDict(), Checkin.select())

  if len(checkins) == 0:
    abort(404)

  return jsonify({'checkins':map(lambda c: c.toDict(), Checkin.select())})

@app.route('/api/checkins/<int:checkin_id>', methods = ['GET'])
@cross_origin(headers=['Content-Type'])
def getCheckinById(checkin_id):
  try:
    return jsonify(Checkin.selectBy(id = checkin_id).getOne().toDict())
  except SQLObjectNotFound:
    return abort(404)

@app.route('/api/checkins', methods = ['POST'])
#@login_required
@cross_origin(headers=['Content-Type'])
def checkin():
  if not request.json or not 'duration' in request.json:
    abort(400)


  duration = None
  note = None
  if('note' in request.json):
    note = request.json['note']

  try:
    duration = int(request.json['duration'])
  except ValueError:
    abort(400)

  checkin = Checkin(duration = duration, note = note,\
        checkinDate = datetime.now(), mozillian = current_user.id)

  return checkin.toDict(), 201

@app.route('/')
def home():
  #return 'Hello World'
  return render_template('index.html')

# example of login with persona, will be deleted when UI later.
@app.route('/login')
def logg():
  return render_template('login.html')
if __name__ == '__main__':
  app.run(debug = True, host = '0.0.0.0')

