# DelionServer

## MYSQL DB
### MYSQL DB export file
* deliondb0911.sql
### Django MYSQL configuration
```
# app/delionserver/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysq',
        'NAME': ‘<db_name>',
        'HOST': ‘<server_address>',
        'PORT': ‘<port_number>',
        'USER': ‘<user_name>',
        'PASSWORD': ‘<pw>'
    }
}
```
## Django, uWSGI and Nginx in a container, using Supervisord
### Build and run
#### Build with python2
* `docker build -f Dockerfile-py2 -t delionserver .`
* `docker run -d -p 80:80 delionserver` or (if mysql is installed via docker) 'docker run -d -p 80:80 --link <mysql_container> delionserver' 

## Django
### /admin
* id:'delion'
* pw:'forif0228'
### /category
* category_id
* category
* shop_or_lifeinfo
* img
### /shop
* shop_lifeinfo_id
* category
* name
* img
* phone
* openhour
* branch
* address
* address_url
