from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

orders = []


@app.route('/')
def home():
   return 'This is Home!'

@app.route('/mypage')
def mypage():
   return render_template('index.html')


@app.route('/post', methods=['POST'])
def post():
   global orders
   name_receive = request.form['name_receive']
   amount_receive = request.form['amount_receive']
   address_receive = request.form['address_receive']
   contact_receive = request.form['contact_receive']

   order = {'name':name_receive,'amount':amount_receive,'address':address_receive,'contact':contact_receive}

   orders.append(order)

   return jsonify({'result':'success'})

@app.route('/post', methods=['GET'])
def view():
   global orders
   return jsonify({'result': 'success','orders': orders})

if __name__ == '__main__':
   app.run('127.0.0.1',port=5000,debug=True)
