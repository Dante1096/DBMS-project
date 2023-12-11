import pymysql

HOST = "127.0.0.1"
HOST2 = "10.0.0.87"
# Connect to MySQL database
conn = pymysql.connect(
    host=HOST,
    user="root",
    password="",
    database="cs509"
)

try:

    cursor = conn.cursor()

    # Get all products from the product table
    # The select statement select data from the product table
    # Execute the query and return all tables.
    def getProducts():
        products = "SELECT * FROM products;"
        cursor.execute(products)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    # get the product using its ID 
    def getProductcostById(id):
        prod = f"SELECT * from products where productid='{id}'" 
        cursor.execute(prod)
        row = cursor.fetchone()
        return row[2]



    # The make sale function, will allow saler to update the sale table
    # The function will display list of customer
    # The user will enter, customer ID 
    # Display the product list.
    # chose product id from the list

    def makesale():
        customer = input("Enter Customer ID:\n")
        getProducts()
        product = input("Enter Product ID:\n")
        
        cost = getProductcostById(product)
       
        quantity = int(input("Enter Quantity:\n"))
        total = (quantity * cost)
        insert = "INSERT INTO sales() values( %s, %s, %s )"
        data = (customer, product, total)
        cursor.execute(insert, data)

        print(f"{customer} {product} {total}")

    # Table to get all users table
    def getUsers():
        users = "SELECT * FROM users;"
        cursor.execute(users)
        rows = cursor.fetchall()
        for row in rows:
            print(row)

    # Function to get all data from the sale table
    # and Print each row
    def getSales():
        sales = "SELECT * FROM sales;"
        cursor.execute(sales)
        rows = cursor.fetchall()
        for row in rows:
            print(row)


    print("*************Welcome CS509 Shop*************")

    # Loop for the Menu
    # The start of the menu loop
    while True:
        print("MENU")
        print("1. Invetory")
        print("2. Sales")
        print("3.View Sales")
        print("4. Customers")
        print("5. Quit")
    
    #    Prompt user to enter his choice.
        choice = int(input("SELECT OPTION\n"))

        # if choice is one list all products
        if(choice == 1):
            print("************* Product Table ******************")
            getProducts()
        elif(choice == 2):
            print("************* All Users ******************")
            getUsers()
            makesale()
        elif(choice == 3):
            print("************* Sales Table ******************")
            getSales()
        elif(choice == 4):
            print("************* All Users ******************")
            getUsers()
        elif(choice == 5):
            print("Thank you. Bye")
            break
        else:
            print("invalid choice")
except pymysql.Error as e:
    print(e)
finally:
    cursor.close()
    conn.commit()
    conn.close()



# Commit and close the connection when you're done
