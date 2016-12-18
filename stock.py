from flask import Flask, request, jsonify, render_template
import db_util
import json
import market_util

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():
    ticker = request.args['ticker']
    # connect to database and find data
    db = db_util.get_db()
    market = market_util.get_market(ticker)
    if market is None:
        return jsonify({'error': 'Invalid Ticker!'})
    print(market)
    market = market.replace(" ", "_")

    cur = db.execute("SELECT * FROM " + market)
    entries = cur.fetchall()
    data = {}
    for item in entries:
        data[item[0]] = item[1]
    if data.__len__() == 0:
        return jsonify({'error': 'Don\'t buy it'})
    json_data = json.dumps(data)

    if ticker:
        return json_data
    return jsonify({'error': 'Missing Data!'})


if __name__ == '__main__':
    app.debug = True
    app.run()
