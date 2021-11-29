'''
@Author: Pavan Nakate
@Date: 2021-11-29 11:30
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Index 
'''
import mysql.connector
import json
from LoggerIndex import logging

class Index_Sql:
    """
        Description: This class having function of all basic queries
    """

    def __init__(self):
        with open('/home/pavan-linux/Documents/MySQL Programs/info.json','r') as jf:
            data = json.load(jf)

        h = data['HOST']
        un = data['USER']
        ps = data['PASS']


        # Passing the variables holding the data from JSON file
        self.mydb = mysql.connector.connect(
        host = h,
        user = un,
        passwd = ps
        )
        self.cursor=self.mydb.cursor()

    def create_index(self):
        """
        Description: This function is to create a index for name column.
        
        """

        try:

            self.cursor.execute("USE foodcustomer")
            self.cursor.execute("""CREATE INDEX idx_namedetails 
                                    ON details(name)""")
            logging.info("index created for name")

        except Exception as e:
            logging.error(e)

    def show_index(self):
        """
        Description: This function is to describe the index.
        
        """
        try:

            self.cursor.execute("SHOW INDEX FROM details")
            for i in self.cursor:
                print(i)
            logging.info("index diplayed for name")

        except Exception as e:
            logging.error(e)

    def find_name(self):
        """
        Description: This function is to find the row, based on department.
        
        """
        try:

            self.cursor.execute("SELECT * FROM details WHERE name = 'rakhi'")
            for details in self.cursor:
                print(details)
            logging.info("name displayed")

        except Exception as e:
            logging.error(e)

    def drop_index(self):
        """
        Description: This function is to delete the created index.
        
        """
        try:

            self.cursor.execute("ALTER TABLE details DROP INDEX idx_namedetails")
            logging.info("Index dropped")

        except Exception as e:
            logging.error(e)

if __name__ == "__main__":
    index = Index_Sql()
    index.create_index()
    index.show_index()
    index.find_name()
    index.drop_index()