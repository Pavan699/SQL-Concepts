#importing logging 
import logging

# setting BasicConfig for the INFO
logging.basicConfig(filename='databaseinfo.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(funcName)s:%(message)s')
# setting BasicConfig for the ERROR
logging.basicConfig(filename='databaseinfo.log',level=logging.ERROR,format='%(asctime)s:%(levelname)s:%(funcName)s:%(lineno)s')