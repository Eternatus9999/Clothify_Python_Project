import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345",
    database="python_clothify"
)

mycursor = db.cursor()

def load():
    try:
        mycursor.execute("DESCRIBE product")
        mycursor.fetchall()
    except:
        mycursor.execute("CREATE TABLE product (id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), size VARCHAR(255), quantity INT, price INT, category VARCHAR(255), supplier VARCHAR(255))")
    try:
        mycursor.execute("DESCRIBE orders")
        mycursor.fetchall()
    except:
        mycursor.execute("CREATE TABLE orders (id VARCHAR(255) PRIMARY KEY, customer_name VARCHAR(255), method VARCHAR(255), total_price INT, order_date DATE)")
    try:
        mycursor.execute("DESCRIBE supplier")
        mycursor.fetchall()
    except:
        mycursor.execute("CREATE TABLE supplier (id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), company VARCHAR(255), contact VARCHAR(255), supply_times INT)")
    try:
        mycursor.execute("DESCRIBE employee")
        mycursor.fetchall()
    except:
        mycursor.execute("CREATE TABLE employee (id VARCHAR(255) PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), address VARCHAR(255), contact VARCHAR(255), password VARCHAR(255))")

    db.commit()

# Insert Queries

def insertProduct(product_id,name,size,quantity,price,category,supplier):
    mycursor.execute("INSERT INTO product (id, name, size, quantity, price, category, supplier) VALUES (%s, %s, %s, %s, %s, %s, %s)", (product_id,name,size,quantity,price,category,supplier))
    db.commit()

def insertSupplier(supplier_id,name,company,contact):
    mycursor.execute("INSERT INTO supplier (id, name, company, contact, supply_times) VALUES (%s, %s, %s, %s, 0)", (supplier_id,name,company,contact))
    db.commit()

def insertOrder(order_id,customer_name,method,total_price,date):
    mycursor.execute("INSERT INTO orders (id,customer_name, method, total_price, order_date) VALUES (%s, %s, %s, %s, %s)", (order_id, customer_name, method, total_price, date))
    db.commit()

def insertEmployee(employee_id,name,email,address,contact,password):
    mycursor.execute("INSERT INTO employee (id, name, email, address, contact, password) VALUES (%s, %s, %s, %s, %s, %s)", (employee_id,name,email,address,contact,password))
    db.commit()

# Update Queries

def updateProduct(id,name,size,quantity,price,category,supplier):
    mycursor.execute("UPDATE product SET name = %s, size = %s, quantity = %s, price = %s, category = %s, supplier = %s WHERE id = %s", (name,size,quantity,price,category,supplier,id))
    db.commit()

def updateAllProducts(items):
    for item in items:
        mycursor.execute("UPDATE product SET quantity = %s WHERE id = %s", (item[3],item[0]))
        db.commit()

def updateSupplier(id,name,company,contact,times):
    mycursor.execute("UPDATE supplier SET name = %s, company = %s, contact = %s, supply_times = %s WHERE id = %s", (name,company,contact,times,id))
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

# Get Id

def getOrderId():
    mycursor.execute("SELECT id FROM orders ORDER BY id DESC LIMIT 1")
    result = list(mycursor.fetchone())
    if result == None:
        return (0,)
    return len(result)

def getProductId():
    mycursor.execute("SELECT id FROM product ORDER BY id DESC LIMIT 1")
    result = list(mycursor.fetchone())
    if result == None:
        return (0,)
    return len(result)

def getSupplierId():
    mycursor.execute("SELECT id FROM supplier ORDER BY id DESC LIMIT 1")
    result = list(mycursor.fetchone())
    if result == None:
        return (0,)
    return len(result)

def getEmployeeId():
    mycursor.execute("SELECT id FROM employee ORDER BY id DESC LIMIT 1")
    result = list(mycursor.fetchone())
    if result == None:
        return (0,)
    return len(result)

# Get Details

def getProduct(id):
    mycursor.execute("SELECT * FROM product WHERE id = %s", (id,))
    result = mycursor.fetchone()
    return result

def getSupplier(id):
    mycursor.execute("SELECT * FROM supplier WHERE id = %s", (id,))
    result = mycursor.fetchone()
    return result

def getEmployee(id):
    mycursor.execute("SELECT * FROM employee WHERE id = %s", (id,))
    result = mycursor.fetchone()
    return resul

# Get Ids

def getProductIds():
    mycursor.execute("SELECT id FROM product")
    result = mycursor.fetchall()
    return result

def getSupplierIds():
    mycursor.execute("SELECT id FROM supplier")
    result = mycursor.fetchall()
    return result

def getEmployeeIds():
    mycursor.execute("SELECT id FROM employee")
    result = mycursor.fetchall()
    return result

# Get one Entity

def searchSupplier(id):
    mycursor.execute("SELECT * FROM supplier WHERE id = %s", (id,))
    result = mycursor.fetchone()
    return result