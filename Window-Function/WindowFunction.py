'''
@Author: Pavan Nakate
@Date: 2021-11-29 02:16
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : WindowFunction 
'''
import mysql.connector
import json
from LoggerWindow import logging

class Window_functions:
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

    def normal_fun(self):
        """
        Description: This function create the window function and add new column for MAX ID
        
        """

        try:
            self.cursor.execute("USE foodcustomer")
            self.cursor.execute(""" SELECT d.*,
                                    MAX(id) over() AS Max_id
                                    FROM details d""")
            print("Max id at last : ")
            for details in self.cursor:
                print(details)
            logging.info("windows function for max id")

        except Exception as e:
            logging.error(e)

    def partition_by(self):
        """
        Description: This function is to perform partition by window function for row number.
        
        """
        try:
            self.cursor.execute("USE foodcustomer")
            self.cursor.execute(""" SELECT d.*,
                                    row_number() over(PARTITION BY name) AS row_n
                                    FROM details d""")
            print("Number of rows for perticuler names : ")
            for details in self.cursor:
                print(details)
            logging.info("windows function for row number")
        
        except Exception as e:
            logging.error(e)

    def rank_by(self):
        """
        Description: This function is to perform ranking window function.
        
        """

        try:
            print("Ordering id's using rank() :")
            self.cursor.execute("USE foodcustomer")
            self.cursor.execute("""SELECT *, 
                                    RANK() OVER(ORDER BY id) AS RankID
                                    FROM details""")

            for details in self.cursor:
                print(details)

            print("After using dense ranking : ")
            self.cursor.execute("""SELECT *, 
                                    DENSE_RANK() OVER(ORDER BY id) AS RankID
                                    FROM details""")

            for details in self.cursor:
                print(details)
            
            logging.info("windows function for ranking")

        except Exception as e:
            logging.error(e)

    def analytical_function(self):
        """
        Description: This function is to perform analytical window function.
            NTILE :- takes a integer and groups the rows according to entered value.
            LEAD :- function takes the value of next row.
            LAG :- function takes the value from previous row.
        
        """
        try:
            self.cursor.execute("USE foodcustomer")
            print("Grouping by 2 by using ntile() : ")
            self.cursor.execute(""" SELECT *,
                                    NTILE(2) OVER() AS twogroups
                                    FROM details""")
                                    # 2 divide the 5 details in 2 groups 

            for details in self.cursor:
                print(details)

            print("After applying lead function to id : ")
            self.cursor.execute(""" SELECT *,
                                    LEAD(id,1) OVER(ORDER BY name) AS next_id
                                    FROM details""")
                                    # 1 is for the next record
            for details in self.cursor:
                print(details)

            print("After applying lag function to id column : ")
            self.cursor.execute(""" SELECT *,
                                    LAG(id, 1, 0) OVER(ORDER BY name) AS previous_id
                                    FROM details""")
                                    # 1 is for the previous record and 0 indicates the null(Defoult)
            for details in self.cursor:
                print(details)

            logging.info("windows function for ranking")

        except Exception as e:
            logging.error(e)
    
if __name__ == "__main__":
    win_fun = Window_functions()
    win_fun.normal_fun()
    win_fun.partition_by()
    win_fun.rank_by()
    win_fun.analytical_function()
    