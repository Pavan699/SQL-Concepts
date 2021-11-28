'''
@Author: Pavan Nakate
@Date: 2021-11-27 11:30
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Views 
'''
from logging import log
import mysql.connector
import json
from LoggersView import logging

class Views:
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

    def create_view(self):
        """
        Description: This function is to create a view for college table.
        
        """

        try:

            self.cursor.execute("USE foodcustomer")
            self.cursor.execute("""CREATE VIEW vw_names AS
                                    SELECT name,address
                                    FROM details""")
            logging.info("view created")

        except Exception as e:
            logging.error(e)

    def display_view(self):
        """
        Description: This function is to display the created view.
        
        """

        try:

            self.cursor.execute("SELECT * FROM details")

            for details in self.cursor:
                print(details)
            logging.info("view created for display")   

        except Exception as e:
            logging.error(e)

    def alter_view(self):
        """
        Description: This function is to update the created view.
        
        """
        try:
            self.cursor.execute("""ALTER VIEW vw_names AS
                                    SELECT name,address
                                    FROM details
                                    WHERE name = 'Names'""")
            logging.info("view created for alter display")   

        except Exception as e:
            logging.error(e)
    
    def drop_view(self):
        """
        Description: This function is to delete the created view.
        
        """
        try:

            self.cursor.execute("DROP VIEW vw_names")
            logging.info("view dropped")

        except Exception as e:
            logging.error(e)

if __name__ == "__main__":
    view = Views()
    view.create_view()
    view.display_view()
    view.alter_view()
    view.drop_view()