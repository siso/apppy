# application_python

## Quick-start

Dependencies:

```
$ pip install flask MySQL-python gnunicorn
```

Run Gnunicorn:

```
# /etc/init.d/apppy start
```

and connect on port *8000*:

```
$ http http://localhost:8000/index
$ http http://localhost:8000/db
$ http http://localhost:8000/ip
```

## Flask

Run Flask app:

```
$ python -m apppy.flask.app
```

Connect to Flask webserver on port *5000*:

```
$ http http://localhost:5000/index
$ http http://localhost:5000/db
$ http http://localhost:5000/ip
```

## MySQL

```
create database apppy;
CREATE USER 'apppy'@'localhost' IDENTIFIED BY 'qwerty';
GRANT ALL PRIVILEGES ON apppy.* TO 'apppy'@'localhost' WITH GRANT OPTION;
CREATE TABLE keyval (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, key_ VARCHAR(100), val_ VARCHAR(100));
insert into keyval (key_, val_) VALUES ('foo', 'bar');
```

