'''
@Author: Pavan Nakate
@Date: 2021-11-28 02:30
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : ImportExport 
'''
import mysql.connector
import os
import json
from LoggerImpExp import logging

class Import_Export:
    """
        Description: This class having function of import and export the databases
    """

    def __init__(self):
        with open('info.json','r') as jf:
            data = json.load(jf)

        h = data['HOST']
        un = data['USER']
        ps = data['PASS']
        db = data['DATABASE']


        # Passing the variables holding the data from JSON file
        self.impexp = mysql.connector.connect(
        host = h,
        user = un,
        passwd = ps,
        database= db
        )
        self.cursor=self.impexp.cursor()

    
    def export_database(self):
        """
        Description: This function is to export the database.
        
        """
        try:
            os.system('mysqldump -u root order_info > backup.sql')
            logging.info("Data Exported")
           
        except Exception as e:
            logging.error(e)

    def import_database(self):
        """
        Description: This function is to import the database.
        
        """

        try:
            self.cursor.execute("CREATE DATABASE duplicate1_import")
            os.system('mysql -u root -p duplicate1_import < backup.sql')
            self.cursor.execute("SHOW DATABASES")

            for db in self.cursor:
                print(db[0])
            logging.info("Data Imported")
           
        except Exception as e:
            logging.error(e)

if __name__ == "__main__":
    imp_exp = Import_Export()
    imp_exp.export_database()
    imp_exp.import_database()