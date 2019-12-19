from flask import Flask, request
import string
import random
import os
import sqlite3

app = Flask('app')

@app.route('/')
def title():
    return  'HW lesson 4'


def gen():
    p = request.args['param']
    if int(p) < 0 or int(p) > 500:
        return 'Input number from 1 to 500'
    else:
        return ''.join(random.choice(string.ascii_uppercase) for i in range(int(p)))


@app.route('/gen')
def get_gen():
    return gen()


def exec_req(req):
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    conn = sqlite3.connect(db_pass)
    cur = conn.cursor()
    cur.execute(req)
    record = cur.fetchall()
    return  record


@app.route('/customers')
def customers():
    req = f'select * from customers where City = \'{request.args["city"]}\' and State = \'{request.args["state"]}\';'
    result = exec_req(req)
    return str(result)


@app.route('/first_names')
def get_fn():
    req = 'select count(distinct FirstName) from Customers;'
    result = str(exec_req(req))[2::]
    n = result.find(',')
    result = result[:n]
    return f'Number of unique First Name : {result}'


@app.route('/income')
def get_income():
    req = 'select sum(UnitPrice * Quantity) from invoice_items;'
    result = str(exec_req(req))[2::]
    n = result.find(',')
    result = result[:n]
    return f'Total income: {result}'


if __name__ == '__main__':
    app.run(port=5000, debug=True)
