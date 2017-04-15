# CodeZeus

Flexible enough to use a CMS and Django itself.
Giving a CMS a whirl where custom Django is not interrupted hopefully - [Wagtail](http://wagtail.io)

## Install

Required Drivers
```
apt-get install libmysqlclient-dev
apt-get install redis-server
apt-get install letsencrypt
```

Not Required, but for rememberance:
```
pip3 install wagtail
```

Make Virtualenv Wrapper
```
mkproject -p /usr/bin/python3 codezeus.com
```

Install Dependencies
```
pip install -r requirements.txt
```

## Configure
Make a local.py which is ignored by git.
```
cp codezeus/settings/local.py.example codezeus/settings/local.py
```

Edit the file, you can delete the MySQL Connection to default to SQLite3
```
vim codezeus/settings/local.py
```

Whip up a database
```
mysql -u root -proot -e "CREATE DATABASE mydatabase CHARACTER SET utf8 COLLATE utf8_general_ci"
```

## Migrate
```
./manage.py migrate
```

## Create Admin
```
./manage.py createsuperuser
```

Runserver
```
./manage.py runserver
```

## Login to CMS
The main page will be blank until one is created.

```
http://localhost:8000/admin
```

## Create Page

- Create a Home page.
- Create a Blog page.
- Create a Blog post.

---

CodeZeus
