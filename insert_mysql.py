def add_data(self):
        
    conn=mysql.connector.connect(host="localhost",username="root",password="Har18dik!",database="dbms")
    my_cursor=conn.cursor()
    my_cursor.execute("INSERT INTO billing_details values(%s,%s,%s,%s,%s,%s)",(
        self.var_bill_id.get(),
        self.var_cust_no.get(),
        self.var_cylinder.get(),
        self.var_del_date.get(),
        self.var_booking_date.get(),
        self.var_amount.get()
                    
    ))
    conn.commit()
    
    conn.close()
                
  