
from models.database import *
from models.entities import *
from flask import Flask, url_for, render_template, session, escape, request,\
       redirect, jsonify, abort, make_response
from flask.ext.login import LoginManager, login_required
from flask.ext.browserid import BrowserID

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
def getMozillians():
  moz = map(lambda em: em.toDict(), Mozillian.select())

  if len(moz) == 0:
    abort(404)

  return jsonify({'mozillians':moz})

@app.route('/api/mozillians/<int:mozillian_id>', methods = ['GET'])
def getMozillianById(mozillian_id):
  try:
    return jsonify(Mozillian.selectBy(id = mozillian_id).getOne().toDict())
  except SQLObjectNotFound:
    return abort(404)

@app.route('/api/mozillians', methods = ['POST'])
@login_required
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
def getEngagements():
  engagements = map(lambda e: e.toDict(), Engagement.select())
  
  if len(engagements) == 0:
    abort(404)

  return jsonify({'engagements':map(lambda e: e.toDict(), Engagement.select())})

@app.route('/api/engagements/<int:engagement_id>', methods = ['GET'])
def getEngagementById(engagement_id):
  try:
    return jsonify(Engagement.selectBy(id = engagement_id).getOne().toDict())
  except SQLObjectNotFound:
    return abort(404)

@app.route('/api/checkins', methods = ['GET'])
def getCheckins():
  checkins = map(lambda c: c.toDict(), Checkin.select())

  if len(checkins) == 0:
    abort(404)

  return jsonify({'checkins':map(lambda c: c.toDict(), Checkin.select())})

@app.route('/api/checkins/<int:checkin_id>', methods = ['GET'])
def getCheckinById(checkin_id):
  try:
    return jsonify(Checkin.selectBy(id = checkin_id).getOne().toDict())
  except SQLObjectNotFound:
    return abort(404)


@app.route('/')
def home():
  return 'Hello World'

# example of login with persona, will be deleted when UI later.
@app.route('/login')
def logg():
  return render_template('login.html')
if __name__ == '__main__':
  app.run(debug = True, host = '0.0.0.0')

