#!/bin/sh -x

sudo pip install --upgrade django gunicorn
sudo /etc/init.d/mysql restart

sudo nginx -c $PWD/etc/nginx.conf
gunicorn -c $PWD/etc/hello.py hello:app

cd ask
gunicorn -c $PWD/../etc/ask.py ask.wsgi

