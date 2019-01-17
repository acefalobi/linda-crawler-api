# Linda Crawler API

## Retrieve code

* `$ git clone https://github.com/acefalobi/linda-crawler-api/dashboard.git`
* `$ cd linda-crawler-api`


## Installation

* Setup Postgres database for project and update database config `src/crawler/settings/base.py`

* `$ virtualenv -p /usr/bin/python3 virtualenv`
* `$ source virtualenv/bin/activate`
* `$ pip install -r py-requirements/base.txt`

* `$ cd src`
* `$ python manage.py migrate`

## Running

* `$ cd src`
* `$ python scheduler.py` (on separate process)
* `$ python manage.py runserver`