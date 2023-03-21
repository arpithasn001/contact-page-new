from flask import Flask,render_template,request 
import requests
# import mysql.connector as conn
# from db_connect import insert_table




# mydb=conn.connect(host="localhost",user="root",password="12345678",database="Contact_I")
# print(mydb)
# cursor = mydb.cursor()
# # dataBaseName="Contact_I"
# customer_comments="contact"
# # create_db(cursor,dataBaseName)
# # create_table(cursor,customer_comments)
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
        product = request.form["product_name"]
        location = request.form["location"]
        date_of_enquiry=request.form["date_of_enquiry"]
        estimated_quote=request.form["estimated_quote"]
        ivoice_name=request.form["invoice_name"]
        profit=request.form["profit"]

    

        mydict={'Client_Name':client_name,"Contact_Number":contact_number,"Product_Name":product,"Location":location,"Date_Of_Enquiry":date_of_enquiry,"Estimated_Quote":estimated_quote,"Ivoice_Amount":invoice_name,"Profit":profit}
        reviews.append(mydict)
        # insert_query=f"INSERT INTO {customer_comments}(Client_Name,Contact_Number,Product_Name,Location,Date_Of_Enquiry,Estimated_Quote,Ivoice_Amount,Profit) VALUES (%(Client_Name)s, %(Contact_Number)s, %(Product_Name)s, %(Location)s, %(Date_Of_Enquiry)s, %(Estimated_Quote)s, %(Ivoice_Amount)s, %(Profit)s);"  
        # cursor.executemany(insert_query, reviews)
        # mydb.commit()
        
    
        
        return render_template('results.html',reviews=reviews[0:len(reviews)-1])


        

    else:
        return render_template('index.html')        

  
if __name__=='__main__':
   app.run(debug=True)
