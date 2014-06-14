from entities import *

sqlhub.processConnection = connectionForURI('sqlite:///tmp/db/mozEngagement.db')

def init_db():
  Mozillian.createTable()
  Engagement.createTable()
  Checkin.createTable()
  #We only need init_db to create the database and tables
