MozTn Summer Engagement :
========================
TODO

Description (French): https://mozillatunisia.etherpad.mozilla.org/summerEngagement


Running : 
=========

Make sure you have `python2.7`, `pip` and `virtualenv`

1. Setting a virtual envirement :
  <pre>
    mkdir venv
    virtualenv venv
    source venv/bin/activate
  </pre>

2. Cloning the project :
  <pre>
    cd venv
    git clone https://github.com/moztn/SummerEngagement
  </pre>
2. Installing dependencies :
  <pre>
    cd SummerEngagement
    pip install -r requirements.txt
  </pre>

3. Init database:
  <pre>
    cd src
    python first_run.py
  </pre>

4. Running the server :
  <pre>
    python app.py
  </pre>

  Then you can access it on : https://localhost:5000/

REST API :
==========

v1:
--

|       Resource             |              Description                     |
|----------------------------|----------------------------------------------|
| `GET` api/mozillians       | Returns a collection of engaged mozillians.  |
| `GET` api/mozillians/:id   | Returns a mozillian specified by `id`.       |
| `GET` api/engagements/     | Returns a collection of engagements.         |
| `GET` api/engagements/:id  | Returns an engagement specified by `id`.     |
| `GET` api/checkins/        | Returns a collection of checkins.            |
| `GET` api/checkins/:id     | Returns a checkin specified by `id`.         |





