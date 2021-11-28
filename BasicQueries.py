'''
@Author: Pavan Nakate
@Date: 2021-11-27 11:30
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : BasicQueries 
'''
import mysql.connector
import json
from LoggerSQL import logging

class Basic_Queries:
    """
        Description: This class having function of all basic queries
    """

    def __init__(self):
        with open('info.json','r') as jf:
            data = json.load(jf)

        h = data['HOST']
        un = data['USER']
        ps = data['PASS']
        db = data['DATABASE']


        # Passing the variables holding the data from JSON file
        self.mydb = mysql.connector.connect(
        host = h,
        user = un,
        passwd = ps,
        database= db
        )
        self.cursor=self.mydb.cursor()

    def create_database(self):
        """
        Description: This function is to create a database.
        """        

        try:

            self.cursor.execute("CREATE DATABASE user_info")
            self.cursor.execute("CREATE DATABASE order_info")
            self.cursor.execute("SHOW DATABASES")

            for db in self.cursor:
                print(db[0])
            logging.info("database created")
        except Exception as e:
            logging.error(e)

    def create_table(self):
        """
        Description: This function is to create a table.
        """ 

        try:

            self.cursor.execute("USE order_info")
            self.cursor.execute("CREATE TABLE order_details(order_id INT, Name VARCHAR(20), Price INT)")
            self.mydb.commit()
            logging.info("table created")

        except Exception as e:
            logging.error(e)

    def insert_into(self):
        """
        Description: This function is to insert the details into the table.
        
        """ 

        try:
            self.cursor.execute("USE order_info")
            self.cursor.execute("INSERT INTO order_details(order_id,Name,Price) VALUES (111,'Pavan',8800),(106,'Rahul',540),(99,'Samiksha',1000)")
            self.mydb.commit()
            logging.info("data inserted")

        except Exception as e:
            logging.error(e)

    def display_table(self):
        """
        Description: This function is to dispaly all values in table.
        
        """

        try: 
            self.cursor.execute("USE order_info")
            self.cursor.execute("SELECT * FROM order_details")

            for details in self.cursor:
                print(details)
            logging.info("data dispayed")

        except Exception as e:
            logging.error(e)

    def alter_table(self):
        """
        Description: This function is to alter the existing table.
        """
        try:
            self.cursor.execute("USE order_info")
            self.cursor.execute("ALTER TABLE order_details ADD Location VARCHAR(30) AFTER Name")    
            self.mydb.commit()
            logging.info("column added")

        except Exception as e:
            logging.error(e)

    def update_details(self):
        """
        Description: This function is to update existing table taking name as the reference.
        
        """

        try:
            self.cursor.execute("USE order_info")
            self.cursor.execute("UPDATE order_details SET Name = 'Dada' WHERE Name = 'Rahul'")
            self.cursor.execute("UPDATE order_details SET Location = 'Mumbai' WHERE order_id = 111")
            self.cursor.execute("UPDATE order_details SET Location = 'Kashi' WHERE order_id = 106")
            self.mydb.commit()
            logging.info("table details updated")
            
        except Exception as e:
            logging.error(e)

    def delete_details(self):
        """
        Description: This function is to delete a row from table using name.
        
        """
        try:

            self.cursor.execute("USE order_info")
            self.cursor.execute("DELETE FROM order_details WHERE Name = 'Rahul'")
            self.mydb.commit()
            self.display_table()
            logging.info("data deleted")

        except Exception as e:
            logging.error(e)
    
    def drop_table(self):
        """
        Description: This function is to remove the existing tabel.
        
        """

        try:
            self.cursor.execute("USE order_info")
            self.cursor.execute("DROP TABLE order_details")
            self.mydb.commit()
            logging.info("table dropped")

        except Exception as e:
            logging.error(e)
    
    def orderby_details(self):
        """
        Description: This function is to order the table with respect to grade.
        
        """

        try:
            print("Using OerderBy Clause : ")
            self.cursor.execute("USE order_info")
            self.cursor.execute("SELECT * FROM order_details ORDER BY Price")
            
            for details in self.cursor:
                print(details)
            logging.info("Orderby clause")

        except Exception as e:
            logging.error(e)
    
    def group_by(self):
        """
        Description: This function is to group the rows based on Price.
        
        """
        try:
            self.cursor.execute("USE order_info")
            self.cursor.execute("SELECT Name,SUM(Price) FROM order_details GROUP BY Name")
            result = self.cursor.fetchall()
            print("Using  Group By printing name : ")
            for details in result:
                print(details[0],' ',details[1])
            logging.info("Use of groupby clause")

        except Exception as e:
            logging.error(e)
    
    def limit_details(self):
        """
        Description: This function is to limit the return of rows.
        
        """
        try:
            self.cursor.execute("USE order_info")
            self.cursor.execute("SELECT * FROM order_details LIMIT 2")
            result = self.cursor.fetchall()
            print("Using Limit to print frist 2 details :")
            for details in result:
                print(details)
            logging.info("Use of limit clause")

        except Exception as e:
            logging.error(e)


    def aggregate_functions(self):
        """
        Description: 
            This function is to perform the aggregate funtions.
            Aggregate funtions are: COUNT, SUM, MAX, MIN, AVG
        
        """

        try:
            self.cursor.execute("USE order_info")
            self.cursor.execute("SELECT COUNT(Name) FROM order_details")
            result = self.cursor.fetchall()
            print("Total count: ",result[0][0])

            self.cursor.execute("SELECT SUM(Price) FROM order_details")
            result = self.cursor.fetchall()
            print("Sum of Price: ",result[0][0])

            self.cursor.execute("SELECT MAX(Price) FROM order_details")
            result = self.cursor.fetchall()
            print("Maximum Price: ",result[0][0])

            self.cursor.execute("SELECT MIN(Price) FROM order_details")
            result = self.cursor.fetchall()
            print("Minimum Price: ",result[0][0])

            self.cursor.execute("SELECT AVG(Price) FROM order_details")
            result = self.cursor.fetchall()
            print("Average Price: ",result[0][0])
            logging.info("Use of Count,Sum,Max,Min and Avg")

        except Exception as e:
            logging.error(e) 
    
if __name__ == "__main__":
    queries = Basic_Queries()
    queries.create_database()
    queries.create_table()
    queries.insert_into()
    queries.display_table()
    queries.alter_table()
    queries.update_details()
    queries.delete_details()
    queries.drop_table()
    queries.orderby_details()
    queries.group_by()
    queries.limit_details()
    queries.aggregate_functions()

