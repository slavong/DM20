# https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask


import flask
from flask import request, jsonify
import datetime as dt

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
@app.route('/', methods=['GET'])
def home():
    return '''<h1>IDS - Analysis and Reporting Services</h1>
<p>Investment Data Services</p>
<p>REST API</p>
<p>see docs .... here TBD</p>
'''


def reply(input, audit, output=None):
    return jsonify({'input': input, 'audit': audit, 'output': output})


def error(audit, error_no, error_msg):
    ret = dict(audit)
    ret['status'] = 'ERROR'
    ret['error_no'] = error_no
    ret['error_msg'] = error_msg
    return ret


@app.route('/api/v1/ids/rating', methods=['GET'])
def api_ids_rating():
    version = 1
    ts = dt.datetime.now()
    audit = {'version': version, 'timestamp': ts}
    input = {}
    #
    if 'orig_rating' in request.args:
        orig_rating = request.args['orig_rating']
    else:
        audit = error(audit, 1, 'Field orig_rating is required.')
        return reply(input, audit)
    input['orig_rating'] = orig_rating
    #
    rule = None
    #
    if orig_rating in ['AAA']:
        rule = 1
        stan_rating = 'AAA'
    elif orig_rating in ['AA+', 'AA', 'AA-']:
        rule = 2
        stan_rating = 'AA'
    elif orig_rating in ['A+', 'A', 'A-']:
        rule = 3
        stan_rating = 'A'
    # TBD: to be done
    else:
        rule = 99
        stan_rating = '#ND'
    status = 'OK'
    output = {'stan_rating': stan_rating}
    #
    audit = {'rule': rule, 'version': version, 'timestamp': ts, 'status': status}
    #
    return reply(input, audit, output)


app.run()
