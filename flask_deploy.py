# from flask import Flask, render_template, redirect, url_for, request, escape, jsonify, flash
from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL
# import json
# import time
#import mysql
# import pickle
# from werkzeug.utils import secure_filename
# import cv2
# import os
# from os import listdir
# from os.path import isfile, join
# import numpy as np
# import yaml
# db = yaml.safe_load(open('db.yaml'))

app = Flask(__name__)
#
# app.config['MYSQL_HOST'] = 'mettps.mysql.pythonanywhere-services.com'
# app.config['MYSQL_USER']= 'mettps'
# app.config['MYSQL_PASSWORD']= 'qazwsxedc'
# app.config['MYSQL_DB']= 'mettps$db'
# mysql = MySQL(app)

# class Database:
#     def __init__(self):
#         #self.conn = pymysql.connect('localhost', 'root', '', 'db')
#         self.conn = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12366811', password='KRH1CUnFBb', database='sql12366811')
#         self.cur = self.conn.cursor()
#
#     def insert(self, command, value):
#         self.cur.execute(command, value)
#         #rows = self.cur.fetchone()
#         self.conn.commit()
#         self.conn.close()
#         #return rows




@app.route('/<string:name_token>')
def index(name_token):
    print(name_token)
    return render_template('indextest1.html', name_token = name_token)

@app.route('/sender/<string:name_token>')
def form_sender(name_token):
    print(name_token)
    return render_template('form_sendertest1.html', name_token = name_token)

@app.route('/receiver/<string:name_token>')
def form_receiver(name_token):
    print(name_token)
    return render_template('form_receivertest1.html', name_token = name_token)


@app.route('/result_sender/<string:name_token>', methods=['POST'])
def result_sender(name_token):
    if request.method == "POST":
        print(name_token)
        phonenumber_sender = request.form['phonenumber_sender']
        name_receiver = request.form['name_receiver']
        lastname_receiver = request.form['lastname_receiver']
        phonenumber_receiver = request.form['phonenumber_receiver']
        print(phonenumber_sender, name_receiver, lastname_receiver, phonenumber_receiver)
        # cur = mysql.connection.cursor()
        # cur.execute("INSERT INTO html_sender(id, phonenumber_sender, name_receiver, lastname_receiver, phonenumber_receiver, name_token) VALUES(NULL, %s, %s, %s, %s, %s)",
        #             (phonenumber_sender, name_receiver, lastname_receiver, phonenumber_receiver, name_token))
        # mysql.connection.commit()
        # cur.close()


        #Database().insert("INSERT INTO `html_sender` (`id`,`phonenumber_sender`,`name_receiver`,`lastname_receiver`,`phonenumber_receiver`,`name_token`) VALUES (NULL, %s, %s, %s, %s, %s);",
                        #(phonenumber_sender, name_receiver, lastname_receiver, phonenumber_receiver, name_token))
        return redirect(url_for('success'))


@app.route('/result_receiver/<string:name_token>', methods=['POST'])
def result_receiver(name_token):
    if request.method == "POST":
         print(name_token)
         username_receiver = request.form['username_receiver']
         name_otp = request.form['name_otp']
         phonenumber_receiver = request.form['phonenumber_receiver']
         #Database().insert("INSERT INTO `html_receiver` (`id`, `username_receiver`, `name_otp`, `phonenumber_receiver`, `name_token`) VALUES (NULL, %s, %s, %s, %s);",
                           #(username_receiver, name_otp, phonenumber_receiver, name_token))
         # cur = mysql.connection.cursor()
         # cur.execute("INSERT INTO html_receiver(id, username_receiver, name_otp, phonenumber_receiver, name_token) VALUES(NULL, %s, %s, %s, %s)",
         #            (username_receiver, name_otp, phonenumber_receiver, name_token))
         # mysql.connection.commit()
         return redirect(url_for('success'))


@app.route('/success')
def success():
    #print("ss")
    return render_template('successtest1.html')

@app.route('/failed')
def failed():
    return render_template('failedtest1.html')
if __name__ == "__main__":
    app.run(debug=True)

