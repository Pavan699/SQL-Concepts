'''
@Author: Pavan Nakate
@Date: 2021-11-27 11:30
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : Views 
'''
import mysql.connector
import json
from LoggersProcedure import logging

class Proceders_SQL:
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

    def create_procedure(self):
        """
        Description: This function is to create a procedure for get user names
        
        """
        try:
            
            self.cursor.execute("USE foodcustomer")
            self.cursor.execute("DROP PROCEDURE get_usernames")
            self.cursor.execute("""CREATE PROCEDURE get_usernames()
                                    BEGIN
                                    SELECT * FROM details WHERE id > 2;
                                    SELECT COUNT(name) AS 'Total_Users' FROM details;
                                    END""")

            self.cursor.execute("CALL get_usernames()")
            print("Printing id's greter then 2")
            for result in self.cursor:
                print(result)
            
            logging.info("procedure created")

        except Exception as e:
            logging.error(e)

    def procedure_in(self):
        """
        Description: This function is to create a procedure to get limited rows,
        
        """
        try:
            self.cursor.execute("USE foodcustomer")
            self.cursor.execute("DROP PROCEDURE get_userid")
            self.cursor.execute("""CREATE PROCEDURE get_userid(IN lim INT)
                                    BEGIN
                                    SELECT * FROM details LIMIT lim;
                                    SELECT COUNT(id) AS 'Total_IDs' FROM details;
                                    END""")

            self.cursor.execute("CALL get_userid(2)")
            print("Printing 2(limit) id's :")
            for result in self.cursor:
                print(result)
            logging.info("procedure created for id")

        except Exception as e:
            logging.error(e)

    def procedure_out(self):
        """
        Description: This function is to create a procedure to get highest id,
        """

        try:
            self.cursor.execute("USE foodcustomer")
            self.cursor.execute("DROP PROCEDURE get_highid")
            self.cursor.execute("""CREATE PROCEDURE get_highid(OUT high INT)
                                    BEGIN
                                    SELECT MAX(id) INTO high FROM details;                         
                                    END""")

            self.cursor.execute("CALL get_highid(@M)")
            self.cursor.execute("SELECT @M")
            print("Printing highesr id :")
            for result in self.cursor:
                print("Higest id :",result[0]) # id is at 0th index

            logging.info("procedure get highestid")

        except Exception as e:
            logging.error(e)

if __name__ == "__main__":
    proc = Proceders_SQL()
    #proc.create_procedure()
    #proc.procedure_in()
    proc.procedure_out()