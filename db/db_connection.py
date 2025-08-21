import configparser
import pymysql
from pymysql.err import MySQLError


class DBConnection:
    """Establish a singleton connection with the database."""

    __instance = None  # to store the single instance

    def __new__(cls):
        if cls.__instance is None:  # if no instance created yet
            cls.__instance = super(DBConnection, cls).__new__(cls)
            cls.__instance._initialize()  # initialize the connection once
        return cls.__instance

    def _initialize(self):
        """Initialize the database connection using properties from db_config.ini"""
        try:
            # load the configuration file
            config = configparser.ConfigParser()
            config.read("db_config.ini")

            # establish the mysql connection
            self.connection = pymysql.connect(
                host=config.get("mysql", "host"),
                user=config.get("mysql", "user"),
                password=config.get("mysql", "password"),
                database=config.get("mysql", "database")
            )
            print("Database connection established successfully.")
        except MySQLError as e:
            print(f"Failed to establish database connection. Error: {e}")
            self.connection = None

    def get_connection(self):
        return self.connection
