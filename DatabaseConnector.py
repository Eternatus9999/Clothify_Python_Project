import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="python_clothify"
)

mycursor = db.cursor()

def init():
    try:
        mycursor.execute("DESCRIBE product")
        mycursor.fetchall()
    except:
        mycursor.execute("CREATE TABLE product (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), size VARCHAR(255), quantity INT, price INT, category VARCHAR(255), supplier VARCHAR(255))")
    try:
        mycursor.execute("DESCRIBE orders")
        mycursor.fetchall()
    except:
        mycursor.execute("CREATE TABLE orders (id INT AUTO_INCREMENT PRIMARY KEY, customer_name VARCHAR(255), total_price INT)")
    try:
        mycursor.execute("DESCRIBE supplier")
        mycursor.fetchall()
    except:
        mycursor.execute("CREATE TABLE supplier (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), company VARCHAR(255), contact VARCHAR(255))")
    try:
        mycursor.execute("DESCRIBE employee")
        mycursor.fetchall()
    except:
        mycursor.execute("CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), address VARCHAR(255), contact VARCHAR(255), password VARCHAR(255))")

    db.commit()

# Insert Queries

def insertProduct(name,size,quantity,price,category,supplier):
    mycursor.execute("INSERT INTO product (name, size, quantity, price, category, supplier) VALUES (%s, %s, %s, %s, %s, %s)", (name,size,quantity,price,category,supplier))
    db.commit()

def insertSupplier(name,company,contact):
    mycursor.execute("INSERT INTO supplier (name, company, contact) VALUES (%s, %s, %s)", (name,company,contact))
    db.commit()

def insertOrder(customer_name,total_price):
    mycursor.execute("INSERT INTO orders (customer_name, total_price) VALUES (%s, %s)", (customer_name,total_price))
    db.commit()

def insertEmployee(name,email,address,contact,password):
    mycursor.execute("INSERT INTO employee (name, email, address, contact, password) VALUES (%s, %s, %s, %s, %s)", (name,email,address,contact,password))
    db.commit()

# Update Queries

def updateProduct(id,name,size,quantity,price,category,supplier):
    mycursor.execute("UPDATE product SET name = %s, size = %s, quantity = %s, price = %s, category = %s, supplier = %s WHERE id = %s", (name,size,quantity,price,category,supplier,id))
    db.commit()

def updateSupplier(id,name,company,contact):
    mycursor.execute("UPDATE supplier SET name = %s, company = %s, contact = %s WHERE id = %s", (name,company,contact,id))
    db.commit()

def updateEmployee(id,name,email,address,contact,password):
    mycursor.execute("UPDATE employee SET name = %s, email = %s, address = %s, contact = %s, password = %s WHERE id = %s", (name,email,address,contact,password,id))
    db.commit()

# Delete Queries

def deleteProduct(id):
    mycursor.execute("DELETE FROM product WHERE id = %s", (id,))
    db.commit()

def deleteSupplier(id):
    mycursor.execute("DELETE FROM supplier WHERE id = %s", (id,))
    db.commit()

def deleteEmployee(id):
    mycursor.execute("DELETE FROM employee WHERE id = %s", (id,))
    db.commit()

def deleteOrder(id):
    mycursor.execute("DELETE FROM orders WHERE id = %s", (id,))
    db.commit()

# View Queries

def viewProduct():
    mycursor.execute("SELECT * FROM product")
    result = mycursor.fetchall()
    return result

def viewSupplier():
    mycursor.execute("SELECT * FROM supplier")
    result = mycursor.fetchall()
    return result

def viewEmployee():
    mycursor.execute("SELECT * FROM employee")
    result = mycursor.fetchall()
    return result

def viewOrder():
    mycursor.execute("SELECT * FROM orders")
    result = mycursor.fetchall()
    return result
