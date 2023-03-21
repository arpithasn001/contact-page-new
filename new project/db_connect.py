def create_db(cursor,dataBaseName):
    db=f"create database {dataBaseName}"
    cursor.execute(db)

def create_table(cursor,customer_comments):
    tb=f"CREATE TABLE IF NOT EXISTS {customer_comments} (Client_Name varchar(1000),Contact_Number int,Product_Name varchar(30),Location varchar(400),Date_Of_Enquiry int,Estimated_Quote int,Ivoice_Amount int,profit int);"
    cursor.execute(tb)

def insert_table(cursor,customer_comments,lst):
    insert_query=f"INSERT INTO {customer_comments}(Client_Name,Contact_Number,Product_Name,Location,Date_Of_Enquiry,Estimated_Quote,Ivoice_Amount,Profit) VALUES (%(Client_Name)s, %(Contact_Number)s, %(Product_Name)s, %(Location)s, %(Date_Of_Enquiry)s, %(Estimated_Quote)s, %(Ivoice_Amount)s, %(Profit)s);"  
    cursor.executemany(insert_query,lst)
