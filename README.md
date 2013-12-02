# Django RequireJS example project

To accompany the [RequireJS](http://requirejs.org/) talk given to [Isotoma](https://github.com/isotoma/) devs on 2013-12-02.

See requirejs.odp for the slides. Install the example django project to play around with the code from the slides.

## Installation

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run server

`./manage.py runserver`

Or for production mode with the r.js optimiser:

`DEBUG=false ./manage.py runserver`