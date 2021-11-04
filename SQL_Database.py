#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector
from mysql.connector import Error
import sys


# In[ ]:


class Database:
    
    TABLE_QUESTIONS = """
    CREATE TABLE questions (
      question_id INT PRIMARY KEY,
      question CARCHAR(8000) NOT NULL
    );
    """
    
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
        self.sqlServer = None
        self.connected = False
        
        try:
            self.sqlServer = mysql.connector.connect(
                host = argHost,
                user = argUser,
                passwd = argPswd
            )
            self.connected = True
        except Error as err:
            print(f"Error: '{err}'")
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
        if(self.sqlServer != None):
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
    def CreateDB(self, argDb):
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
    
    #----------------------------------------------------------------
    # DeleteTable(self, argTbl)
    # DESC:
    #   Attempts to delete table named [argTbl]. Fails if table does 
    #   not exist.
    #
    # ARGUMENT:
    #   argTbl - STRING Name of table to delete.
    # RETURN:
    #   BOOLEAN - True if successful, False otherwise
    #----------------------------------------------------------------
    def DeleteTable(self, argTbl):
        query = "DROP TABLE " + argTbl + ";"
        
        return self.__runCommand(query)
    
    #----------------------------------------------------------------
    # NewTable_Question(self)
    # DESC:
    #   Creates a new table based off the SQL command constant 
    #   TABLE_QUESTIONS defined at the beginning of the class.
    #
    # ARGUMENT:
    #   
    # RETURN:
    #   BOOLEAN - True if successful, False otherwise
    # ASSUMPTION:
    #   Table does not already exist.
    #----------------------------------------------------------------
    def NewTable_Question(self):
        query = TABLE_QUESTIONS
        
        return self.__runCommand(query)
    
    #----------------------------------------------------------------
    # Insert_Question(self, argID, argQuestion)
    # DESC:
    #   Inserts new question in to 'questions' table with an ID of 
    #   [argID] and a question string of [argQuestion]. Error checks 
    #   that no other ID of the same number has been entered already.
    #
    # ARGUMENT:
    #   argID - INT Unique integer ID number for question.
    #   argQuestion - STRING Formated question string from internal 
    #     data structure.
    # RETURN:
    #   BOOLEAN - True if successful, False otherwise
    # ASSUMPTION:
    #   'questions' table exists in current database.
    #----------------------------------------------------------------
    def Insert_Question(self, argID, argQuestion):
        check = self.Select("questions", "question_id = " + argID, "*")
        
        if(len(check) > 0):
            print(f"Error: Question ID already exists.")
            return False
        
        insert = "(" + argID + ", '" + argQuestion + "')"
        
        return self.Insert("questions", insert)
    
    #----------------------------------------------------------------
    # Delete_Question(self, argID)
    # DESC:
    #   Deletes question with ID of [argID].
    #
    # ARGUMENT:
    #   argID - INT Unique integer ID number for question.
    # RETURN:
    #   BOOLEAN - True if successful, False otherwise
    # ASSUMPTION:
    #   'questions' table exists in current database.
    #----------------------------------------------------------------
    def Delete_Question(self, argID):
        return self.Delete("questions", "question_id = " + argID)
    
    #----------------------------------------------------------------
    # Select_Question(self, argID)
    # DESC:
    #   Returns question with ID of [argID].
    #
    # ARGUMENT:
    #   argID - INT Unique integer ID number for question.
    # RETURN:
    #   STRING - Question correlating to the ID number. 
    #     None if ID does not exist.
    # ASSUMPTION:
    #   'questions' table exists in current database.
    #----------------------------------------------------------------
    def Select_Question(self, argID):
        return self.Select("questions", "question_id = " + argID, "question")
    
    #----------------------------------------------------------------
    # Update_Question(self, argID, argQuestion)
    # DESC:
    #   Attempts to update question at ID [argID] to question [argQuestion].
    #
    # ARGUMENT:
    #   argID - INT Unique integer ID number for question.
    #   argQuestion - STRING Formated question string from internal 
    #     data structure.
    # RETURN:
    #   BOOLEAN - True if successful, False otherwise
    # ASSUMPTION:
    #   'questions' table exists in current database.
    #----------------------------------------------------------------
    def Update_Question(self, argID, argQuestion):
        return self.Insert("questions", "question_id = " + argID, "question = '" + argQuestion + "'")
    
    #----------------------------------------------------------------
    # TestClass(argHost, argUser, argPswd)
    # DESC:
    #   Simple test class that tests each major external function and 
    #   returns true or false for each that passes it's test. All
    #   results are stored in an array and return
    #
    # ARGUMENT:
    #   argHost - STRING Host name to be used for SQL server log in.
    #   argUser - STRING User name to be used for SQL server log in.
    #   argPswd - STRING Password to be used for SQL server log in.
    #
    # RETURN:
    #   LIST BOOLEAN - True for each successful test, False if one failed.
    # ASSUMPTION:
    #   The provided MySQL info connects to a valid server
    #----------------------------------------------------------------
    def TestClass(argHost, argUser, argPswd):
        ret = []
        
        #Test __init__()
        sql = Database(argHost, argUser, argPswd);
        
        ret.append(not sql.IsConnected())
        
        #Test Close()
        sql.Close()
        
        ret.append(sql.IsConnected())
        
        #Test Reconnect()
        sql.Reconnect(argHost, argUser, argPswd)
        
        ret.append(not sql.IsConnected())
        
        #Test CreateDB()/DoesDBExist()
        sql.CreateDB("Test")
        
        ret.append(sql.DoesDBExist("Test"))
        
        #Test NewTable_Question()/DeleteTable()
        sql.NewTable_Question()
        
        sql.DeleteTable("questions")
        
        #Test INSERT/DELETE/SELECT/UPDATE for questions
        sql.NewTable_Question()
        
        sql.Insert_Question(1, "This is a test")
        ret.append(sql.Select_Question(1) == "This is a test")
        sql.Update_Question(1, "Now this is a question")
        ret.append(sql.Select_Question(1) == "Now this is a question")
        sql.Delete_Question(1)
        ret.append(sql.Select_Question(1) == None)
        
        return ret


# In[ ]:


if __name__ == "__main__":
    try:
        ret = Database.TestClass(sys.argv[0], sys.argv[1], sys.argv[2])
        print(ret)
    except Error as err:
            print(f"Error: '{err}'")


# In[ ]:




