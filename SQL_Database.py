#!/usr/bin/env python
# coding: utf-8

# In[1]:


import mysql.connector
from mysql.connector import Error


# In[2]:


class Database:
    
    #----------------------------------------------------------------
    # __init__(self, argHost, argUser, argPswd)
    # DESC:
    #   Initilaizes a connection to a SQL server. Object contains 
    #   connection and will continue to maintain connection until 
    #   object is sent a closed command or falls out of scope.
    #
    # ARGUMENT:
    #   argHost - STRING Host name to be used for SQL server log in.
    #   argUser - STRING User name to be used for SQL server log in.
    #   argPswd - STRING Password to be used for SQL server log in.
    #
    # RETURN:
    #   BOOLEAN - True if successfully connected. False otherwise.
    #----------------------------------------------------------------
    def __init__(self, argHost, argUser, argPswd):
        self.sqlSever = None
        self.connected = False
        
        try:
            self.sqlServer = mysql.connector.connect(
                host = argHost,
                user = argUser,
                passwd = argPswd
            )
            self.connected = True
            return True
        except Error as err:
            print(f"Error: '{err}'")
            return False
    #----------------------------------------------------------------
    # __del__(self)
    # DESC:
    #   Ensures that the SQL server connection is closed before fully 
    #   allowing object to be deleted.
    #
    # ARGUMENT:
    #   
    # RETURN:
    #   
    #----------------------------------------------------------------    
    def __del__(self):
        if(self.connected == True):
            self.sqlServer.disconnect()
            self.sqlServer = None
            self.connected = False 
    
    #----------------------------------------------------------------
    # Reconnect(self, argHost, argUser, argPswd)
    # DESC:
    #   Attempts to connect to the provided SQL server, closing the 
    #   old connection if there is one.
    #
    # ARGUMENT:
    #   argHost - STRING Host name to be used for SQL server log in.
    #   argUser - STRING User name to be used for SQL server log in.
    #   argPswd - STRING Password to be used for SQL server log in.
    #
    # RETURN:
    #   BOOLEAN - True if successfully connected. False otherwise.
    #----------------------------------------------------------------
    def Reconnect(self, argHost, argUser, argPswd):
        if(self.sqlServer != None):
            self.sqlServer.disconnect()
        
        self.sqlSever = None
        self.connected = False
        
        try:
            self.sqlServer = mysql.connector.connect(
                host = argHost,
                user = argUser,
                passwd = argPswd
            )
            self.connected = True
            return True
        except Error as err:
            print(f"Error: '{err}'")
            return False
    
    #----------------------------------------------------------------
    # Close(self)
    # DESC:
    #   Closes connect to SQL server.
    #
    # ARGUMENT:
    #   
    # RETURN:
    #   
    #---------------------------------------------------------------- 
    def Close(self):
        self.sqlServer.disconnect()
        self.sqlServer = None
        self.connected = False
        
    #----------------------------------------------------------------
    # IsConnected(self)
    # DESC:
    #   Returns if a connection is currently initiated to a SQL server
    #
    # ARGUMENT:
    #   
    # RETURN:
    #   BOOLEAN - True if successfully connected. False otherwise.
    #---------------------------------------------------------------- 
    def IsConnected(self):
        return self.connected
    
    #----------------------------------------------------------------
    # __runCommand(self, argCmd)
    # DESC:
    #   Generic frame function that accepts a SQL command in the form 
    #   of a string, then attempts to run it on the server.
    #   Requires SQL connection.
    #
    # ARGUMENT:
    #   argCmd - STRING Command in the form of SQL code.
    # RETURN:
    #   BOOLEAN - True if the command successfully ran, false otherwise
    #---------------------------------------------------------------- 
    def __runCommand(self, argCmd):
        if(self.connected == False):
            print(f"Error: Connection Not Established")
            raise ValueError ("Connection Not Established")
        
        cursor = self.sqlServer.cursor()
        
        try:
            cursor.execute(argCmd)
            self.sqlServer.commit()
            cursor.close()
            return True
        except Error as err:
            print(f"Error: '{err}'")
            return False
    
    #----------------------------------------------------------------
    # __runQuestion(self, argCmd)
    # DESC:
    #   Generic frame function that accepts a SQL command in the form 
    #   of a string, then attempts to run it on the server. This 
    #   differes from __runCommand in that the return should be the 
    #   value of the data queried from the server.
    #   Requires SQL connection.
    #
    # ARGUMENT:
    #   argCmd - STRING Command in the form of SQL code.
    # RETURN:
    #   LIST STRING - Contents of cell if succsessful. None if failed.
    #---------------------------------------------------------------- 
    def __runQuestion(self, argCmd):
        if(self.connected == False):
            print(f"Error: Connection Not Established")
            raise ValueError ("Connection Not Established")
        
        cursor = self.sqlServer.cursor()
        ret = None
        
        try:
            cursor.execute(argCmd)
            self.sqlServer.commit()
            ret = cursor.fethcall()
            cursor.close()
            return ret
        except Error as err:
            print(f"Error: '{err}'")
            return None
    
    #----------------------------------------------------------------
    # DoesDBExist(self, argDb)
    # DESC:
    #   Checks if a server by the name of [argDb] exists.
    #
    # ARGUMENT:
    #   argDb - STRING Name of database to check for.
    # RETURN:
    #   BOOLEAN - True if the database exists, flase otherwise.
    #----------------------------------------------------------------
    def DoesDBExist(self, argDb):
        query = "SHOW DATABASES LIKE " + argDb + ";"
        
        db = self.__runQuestion(query)
        
        if(len(db) > 0):
            return True
        else:
            return False
    
    #----------------------------------------------------------------
    # CreateDb(self, argDb)
    # DESC:
    #   Creates a new database of name [argDb]
    #
    # ARGUMENT:
    #   argDb - STRING Name of database to create.
    # RETURN:
    #   BOOLEAN - True if successful, False otherwise
    # ASSUMPTION:
    #   argDb does not already exist as a database.
    #----------------------------------------------------------------
    def CreateDb(self, argDb):
        query = "CREATE DATABASE " + argDb + ";"
        
        return self.__runCommand(query)
    
    #----------------------------------------------------------------
    # Insert(self, argTable, argData)
    # DESC:
    #   Inserts [argData] into arg[Table]
    #
    # ARGUMENT:
    #   argDb - STRING Name of table to add to.
    #   argData - STRING Data to add to table. Formated to SQL insert 
    #     for table.
    # RETURN:
    #   BOOLEAN - True if successful, False otherwise
    # ASSUMPTION:
    #   argTable exists in current database.
    #----------------------------------------------------------------
    def Insert(self, argTable, argData):
        query = "INSERT INTO " + argTable + " VALUES\n" + argData + ";"
        
        return self.__runCommand(query)
    
    #----------------------------------------------------------------
    # Delete(self, argTable, argData)
    # DESC:
    #   Tries to delete [argData] from [argTable]
    #
    # ARGUMENT:
    #   argDb - STRING Name of table to delete from.
    #   argData - STRING Data to delete from table. Formated to SQL 
    #     search for table.
    # RETURN:
    #   BOOLEAN - True if successful, False otherwise
    # ASSUMPTION:
    #   argTable exists in current database.
    #----------------------------------------------------------------
    def Delete(self, argTable, argData):
        query = "DELETE FROM " + argTable + "\nWHERE " + argData + ";"
        
        return self.__runCommand(query)
    
    #----------------------------------------------------------------
    # Select(self, argTable, argData)
    # DESC:
    #   Finds and returns all data of [argData] type from [argTable] 
    #   where [argWhere] is true.
    #
    # ARGUMENT:
    #   argDb - STRING Name of table to search in.
    #   argWhere - STRING Qualifier to narrow down which entires to 
    #     return. Formated to SQL search for table.
    #   argData - STRING Data to search for. Formated to SQL 
    #     search for table.
    # RETURN:
    #   LIST STRING - List of datacells that match query. None if 
    #     command failed.
    # ASSUMPTION:
    #   argTable exists in current database.
    #----------------------------------------------------------------
    def Select(self, argTable, argWhere, argData):
        query = "SELECT " + argData + "\nFROM " + argTable + "\nWHERE " + argWhere + ";"
        
        return self.__runQuestion(query)
    
    #----------------------------------------------------------------
    # Update(self, argTable, argWhere, argData)
    # DESC:
    #   Finds and replaces all data of [argData] type from [argTable] 
    #   where [argWhere] is true.
    #
    # ARGUMENT:
    #   argDb - STRING Name of table to search in.
    #   argWhere - STRING Qualifier to narrow down which entires to 
    #     return. Formated to SQL search for table.
    #   argData - STRING Data to search for. Formated to SQL 
    #     search for table.
    # RETURN:
    #   BOOLEAN - True if successful, False otherwise
    # ASSUMPTION:
    #   argTable exists in current database.
    #----------------------------------------------------------------
    def Update(self, argTable, argWhere, argData):
        query = "UPDATE " + argTable + "\nSET " + argData + "\nWHERE " + argWhere + ";"
        
        return self.__runCommand(query)


# In[ ]:




