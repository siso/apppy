#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO -- implement required params check

import MySQLdb

from flask import Flask
from flask import request
from werkzeug.contrib.fixers import ProxyFix
import ConfigParser

# ##########
# Flask'ing
app = Flask(__name__)

# ########################################
# AUTHENTICATION

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    '''
    landing page
    '''
    out = '¡Hola!'
    return out, 200

@app.route('/db', methods=['GET'])
def db():
    '''
    test db connection
    '''
    out = 'connecting to MySQL db... '

    config = None
    try:
        config = ConfigParser.ConfigParser()
        config.read('/opt/apppy/etc/apppy.conf')
    except:
        out += 'failed'
        return out, 500
    
    try:
        db = MySQLdb.connect(host=config.get('db', 'host'),
                             user=config.get('db', 'user'),
                             passwd=config.get('db', 'passwd'),
                             db=config.get('db', 'db'))

#         cur = db.cursor() 
#     
#         sql = '''select key_, val_ from keyval;'''
#     
#         cur.execute(sql)
#     
#         out += '<table><th>key_</th><th>val_</th>'
#         for row in cur.fetchall() :
#             out += "<tr><td>%s</td><td>%s</td></tr>" % (row[0], row[1])
#         out += '</table>'

        out += 'success'
    except:
        out += 'failed'

    return out, 200

@app.route('/ip', methods=['GET'])
def ip():
    '''
    test db connection
    '''
    out = "Your IPv4 address is: %s" % request.remote_addr
    return out, 200

app.wsgi_app = ProxyFix(app.wsgi_app)

def main():
    # ##########
    # FLASK
    app.run(port=5000, debug=True)

if __name__ == '__main__':
    main()
