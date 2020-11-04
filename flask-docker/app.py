from flask import Flask, request, render_template
from redis import Redis, RedisError, StrictRedis
import json

app = Flask(__name__)

def add_user(uid, fname, lname):
    status = 'success'
    user = {'first_name': fname,
            'last_name': lname,
            'credit': 0 }
    try:
        redis_client.set(uid, json.dumps(user))
    except RedisError:
        status = 'failed'
    return status

def add_credit(uid, credit):
    status = 'success'
    user = ''
    try:
        user = redis_client.get(uid)
    except RedisError:
        status = 'failed'
    if user is None or user is '':
        status = 'failed'
    else:
        user = json.loads(user)
        user['credit'] = float(user['credit']) + float(credit)
        redis_client.set(uid, json.dumps(user))        
    return status

def view_user(uid):
    status = ''
    user = ''
    try:
        user = redis_client.get(uid)
    except RedisError:
        status = 'failed'
    if user is None or user is '':
        status = 'failed'
    elif user is not '':
        user = json.loads(user)
        status = "fname: {}, lname: {}, credits: {}".format(
            user['first_name'],
            user['last_name'],
            user['credit'])     
    return status
    

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        details = request.form
        if details['form_type'] == 'add_user':
            return add_user(details['uid'],
                            details['fname'],
                            details['lname'])

        elif details['form_type'] == 'add_credit':
            return add_credit(details['uid'],
                            details['credit'])

        elif details['form_type'] == 'view_user':
            return view_user(details['uid'])

    return render_template('index.html')

if __name__ == '__main__':
    redis_client = StrictRedis(host='redis', db=0, port=6379)
    app.run(host='0.0.0.0')
