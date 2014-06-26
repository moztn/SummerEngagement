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

|       Resource             |              Description                     | Authenficiation |
|----------------------------|----------------------------------------------|-----------------|
| `GET` api/mozillians       | Returns a collection of engaged mozillians.  |  Not Required   |
| `GET` api/mozillians/:id   | Returns a mozillian specified by `id`.       |  Not Required   |
| `POST` api/mozillians      | Will create a mozillian.                     |    Required     |
| `GET` api/engagements      | Returns a collection of engagements.         |  Not Required   |
| `GET` api/engagements/:id  | Returns an engagement specified by `id`.     |  Not Required   |
| `POST` api/engagements     | Will create and assign engagement to user.   |    Required     |
| `GET` api/checkins         | Returns a collection of checkins.            |  Not Required   |
| `GET` api/checkins/:id     | Returns a checkin specified by `id`.         |  Not Required   |
| `POST` api/checkins        | Create a checkin.                            |    Required     |




