from flask import Flask
import os
from faker import Faker
import requests

app = Flask('app')


@app.route('/')
def home1512():
    return 'home1512'


@app.route('/reade_file')
def f():
    f_path = os.path.join(os.getcwd(), 'requirements.txt')
    with open(f_path) as ff:
        return ff.read()


@app.route('/fake')
def get_fake():
    fake = Faker()
    return '<br>'.join(
        f'{fake.name()}, {fake.email()}' for i in range(100)
    )


def metrix():
    metrix_path = os.path.join(os.getcwd(), 'hw.csv')
    with open(metrix_path) as mm:
        content = mm.read()
        content = content.split('\n')[1:]
        cnt = 0
        h = 0
        w = 0

        for row in content:
            if not row:
                continue
            cnt += 1
            hh = float(row.split(',')[1])
            ww = float(row.split(',')[2])
            h += hh
            w += ww

        avg_h = h / cnt * 2.54
        avg_w = w / cnt * 0.454
    return f'Средний вес: {avg_w} и Средний рост: {avg_h}'


@app.route('/avg')
def get_avg():
    return metrix()


@app.route('/spaseman')
def get_spaseman():
    result = requests.get('http://api.open-notify.org/astros.json')
    j = result.json()
    num_spaseman = j['number']
    return f'number of spaseman online: {num_spaseman}'


if __name__ == '__main__':
    app.run(port=5000)

