from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    orderer_receive = request.form['orderer_give']
    ordernum_receive = request.form['ordernum_give']
    adress_receive = request.form['adress_give']
    phonenum_receive = request.form['phonenum_give']

    doc = {
        'orderer':orderer_receive,
        'ordernum':ordernum_receive,
        'adress':adress_receive,
        'phone':phonenum_receive
    }

    db.orderform.insert_one(doc)
    return jsonify({'msg': '이 요청은 POST!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    orders = list(db.orderform.find({},{'_id' : False}))
    print(orders)
    return jsonify({'whole_order': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)