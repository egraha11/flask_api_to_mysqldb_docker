from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# GET all orders
@app.route('/orders', methods=['GET'])
def get_orders():
     try:
         mydb = mysql.connector.connect(
             host="SQL_Container",
             user="user",
             password="password",
             database="Online_Store"
         )

         if mydb.is_connected():
             cursor = mydb.cursor()
             cursor.execute("SELECT * FROM orders")
             results = cursor.fetchall()
             return jsonify({'orders': results})
     except mysql.connector.Error as err:
         return jsonify({'error': err})

# GET a specific order
@app.route('/orders/<int:order_id>', methods=['GET'])
def get_task(order_id):
     try:
         mydb = mysql.connector.connect(
             host="SQL_Container",
             user="user",
             password="password",
             database="Online_Store"
         )

         if mydb.is_connected():
             select = """SELECT * FROM orders WHERE Order_Id = %s"""
             order = (order_id)
             cursor = mydb.cursor()
             cursor.execute(select,order)
             results = cursor.fetchall()
             return jsonify({'orders': results})
     except mysql.connector.Error as err:
         return jsonify({'error': err})

# POST a new order
@app.route('/orders/<int:order_id>/price/<int:price>/productid/<int:product_id>', methods=['POST'])
def create_task(order_id, price, product_id):
     try:
         mydb = mysql.connector.connect(
             host="SQL_Container",
             user="user",
             password="password",
             database="Online_Store"
         )

         if mydb.is_connected():
             cursor = mydb.cursor()

             sql = "INSERT INTO orders (Order_Id, Price, Product_Id) VALUES (%s, %s, %s)"
             val = (order_id, price, product_id)
             cursor.execute(sql, val)
             results = cursor.fetchall()
             return jsonify({'orders': "Order Successfully added"})
     except mysql.connector.Error as err:
         return jsonify({'error': err})

# DELETE a task
@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_task(order_id):
     try:
         mydb = mysql.connector.connect(
             host="SQL_Container",
             user="user",
             password="password",
             database="Online_Store"
         )

         if mydb.is_connected():
             delete = """DELETE FROM orders WHERE Order_Id = %s"""
             order = (order_id)
             cursor = mydb.cursor()
             cursor.execute(delete, order)
             results = cursor.fetchall()
             return jsonify({'orders': results})
     except mysql.connector.Error as err:
         return jsonify({'error': err})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25565, debug=True)