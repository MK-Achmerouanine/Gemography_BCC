# Gemography Backend Coding Challenge

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Django?style=flat-square)](https://www.python.org/downloads/)

[![PyPI](https://img.shields.io/pypi/v/django?label=Django)](https://www.djangoproject.com)

[![PyPI - Django Version](https://img.shields.io/pypi/djversions/djangorestframework?label=djangorestframework)](https://www.django-rest-framework.org)

[![PyPI](https://img.shields.io/pypi/v/requests?label=requests)](https://requests.readthedocs.io/)

[![Build Status](https://travis-ci.org/MK-Achmerouanine/Gemography_BCC.svg?branch=master)](https://travis-ci.org/MK-Achmerouanine/Gemography_BCC)

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Run in local machine

First make sure you have python3 installed in your local machine, if you don't please visit [this website](https://www.python.org)

### Clone this repository

- let's clone this repository using this command

```bash
  $ git clone https://github.com/MK-Achmerouanine/Gemography_BCC.git
```

### Configure virtual environement

- let's create a virtual environement using this command:

```bash
$ py -3 -m venv .venv
Or
$ python3 -m venv .venv
```

- Activate the environement using the following command (Linux & Mac Os):

```bash
$ source .venv/bin/activate
```

- Activate the environement using the following command (Windows):

```bash
$ .venv\Scripts\activate
```

### Install dependencys

- Install the dependencys using the following command:

```bash
pip3 install -r requirements.txt
```

### Run Project

- To start project run the following command:

```bash
$ python manage.py runserver
```

> After starting the server successifuly you can check the results here : [http://localhost:8000/]

### Unit tests

- To test the project run the following command:

```bash
$ python manage.py test apps.repotrend.tests
```

## Run on docker

First make sure you installed docker on your machine.

```bash
$ docker-compose up
```

## Tasks

- [x] Number of repos using this language
- [x] The list of repos using the language
