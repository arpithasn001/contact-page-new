from flask import Flask,render_template, request

import mysql.connector as conn  
import pymysql
from db_connect import *
mydb=conn.connect(host="localhost",user="root",password="12345678",database="Contact_I")
print(mydb)
cursor = mydb.cursor()
dataBaseName="Contact_I"

customer_comments="contact"
app = Flask(__name__)
@app.route('/',methods=['POST', 'GET'])      
def index():
    return render_template('index.html')
@app.route("/review",methods=['POST', 'GET'])
def results():
    if request.method=="POST":
         reviews=[]
         client_name = request.form["client_name"]
         contact_number =  request.form["contact_number"]
         product_name = request.form["Product_Name"]
         location = request.form["location"]
         date_of_enquiry=request.form["date_of_enquiry"]
         estimated_quote=request.form["estimated_quote"]
         ivoice_name=request.form["ivoice_name"]
         profit=request.form["profit"]

         mydict={"Client_Name":client_name,"Contact_Number":contact_number,"Product_Name":product_name,"Location":location,"Date_Of_Enquiry":date_of_enquiry,"Estimated_Quote":estimated_quote,"Ivoice_Amount":ivoice_name,"Profit":profit}
         reviews.append(mydict)
        #  print(reviews)
         insert_query=f"INSERT INTO {customer_comments}(Client_Name,Contact_Number,Product_Name,Location,Date_Of_Enquiry,Estimated_Quote,Ivoice_Amount,Profit) VALUES (%(Client_Name)s, %(Contact_Number)s, %(Product_Name)s, %(Location)s, %(Date_Of_Enquiry)s, %(Estimated_Quote)s, %(Ivoice_Amount)s, %(Profit)s);"  
         cursor.executemany(insert_query, reviews)
         mydb.commit()

         return render_template('results.html',reviews=reviews[0:len(reviews)])

    else:
        return render_template('index.html')

@app.route("/review3",methods=['POST', 'GET'])
def jio():
            host = "localhost"
            user = "root"
            password = "12345678"
            db = "Contact_i"
            
        
            conn=pymysql.connect(host=host,user=user,password=password,db=db)
             

            mycursor = conn.cursor()
            mycursor.execute('select * from contact')
            data=mycursor.fetchall()
            print(data)

            return render_template("results2.html", data=data)

if __name__=='__main__':
  app.run(debug=True)

