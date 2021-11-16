Files:

class Question.py  - contains the the code for the question container
Question_Test.py           - contains tests for class Question



Description of class Question.py:
#---------------------------------------------------------------------------------------------------------------------------------------
# Class Question: 
#                      receives a string of one/multiple questions in a specified format
#                      saves each question in the dictionary as a value with the coresponding question id as the key
# Format of the input: 
#                      {id - integer} {question_number - integer} {question - string}
#                      {list_of_answers - list of strings} {correct_answer_position - int or list of ints}

# Example:             '#4567: 3: What is orange? Answers: [color] [fruit] [vegetable] Correct: {1} {2} 
#                       #452: 9: Which of the following are caller saved registers? Answers: [RAX] [RDI] [RSI] [RDX] Correct: {2} {4}'
#---------------------------------------------------------------------------------------------------------------------------------------


    #-------------------------------------------------------------------------------------------------------------------------------------
    #Constructor: receives a string of one/multiple questions in a specified format
                  containes a list for each question
                  containes dictionary: 
                                        key- question ID
                                        value - list of bits for each question:
                                                                                question number at [0] as int
    #                                                                           question itself at [1] as string
    #                                                                           answer choices at [2] as list of strings
    #                                                                           correct answers positions at [3] as int or list of ints
    #-------------------------------------------------------------------------------------------------------------------------------------


    #--------------------------------------------------------------------------------------------------------------------
    #Name:        save_collection(self,passed_list):
    #Receives:    a string of questions in expected format:
    #             {Question ID} {Question Number} {Question} {list of answers} {indexes of the correct answer positions}
    #             '#4567: 3: What is orange? Answers: [color] [fruit] [vegetable] Correct: {1} {2}'
    #Description: iterates throught the string and separates each question, stores in a list, returns a list
    #Assumptions: questions passed in a specified format
    #--------------------------------------------------------------------------------------------------------------------


    #--------------------------------------------------------------------------------------------------------
    #Name:        create_dict(self, modified_list):
    #Receives:    list with each question stored separately
    #Description: the function extracts the id from each question
    #             the question creates a list for each question extracts and stores:
    #                                                question number at [0] as int
    #                                                question itself at [1] as string
    #                                                answers at [2] as list of strings
    #                                                correct answers positions at [3] as int or list of ints
    #             the function creates a dictionary from corresponding question id and a list for each question
    #             the function returns dictionary        
    #Assumptions: questions passed in a specified format above 
    #--------------------------------------------------------------------------------------------------------


    #--------------------------------------------------------------------------------------------------------
    #Name:        print_dictionary(self):
    #Receives:    -
    #Description: the function prints content of a dictionary  
    #Assumptions: -
    #--------------------------------------------------------------------------------------------------------


    #--------------------------------------------------------------------------------------------------------------------
    #Name:        retrieve_full_question(self, id):
    #Receives:    id (int) of a question desired to retrieve
    #Description: the function returns a full question:
    #             {question number} {question} {list of answers} {list of positions corresponding to the correct answer} 
    #Errors:      if wrong or unexisted id is passed - function returns None and prints a message
    #Assumptions: question id exists in a dictionary
    #--------------------------------------------------------------------------------------------------------------------


    #--------------------------------------------------------------------------------------------------------------------
    #Name:        retrieve_question_number_only(self,id):
    #Receives:    id (int) of a question desired to retrieve
    #Description: the function returns the question number portion of a question:
    #             {question number} 
    #Errors:      if wrong or unexisted id is passed - function returns None and prints a message
    #Assumptions: question id exists in a dictionary
    #--------------------------------------------------------------------------------------------------------------------  


    #--------------------------------------------------------------------------------------------------------------------
    #Name:        retrieve_question_only(self,id):
    #Receives:    id (int) of a question desired to retrieve
    #Description: the function returns the question portion of a question:
    #             {question}
    #Errors:      if wrong or unexisted id is passed - function returns None and prints a message 
    #Assumptions: question id exists in a dictionary
    #--------------------------------------------------------------------------------------------------------------------    


    #--------------------------------------------------------------------------------------------------------------------
    #Name:        retrieve_list_of_answers_only(self,id):
    #Receives:    id (int) of a question desired to retrieve
    #Description: the function returns the list of answers portion of a question:
    #             {list of answers} 
    #Errors:      if wrong or unexisted id is passed - function returns None and prints a message
    #Assumptions: question id exists in a dictionary
    #--------------------------------------------------------------------------------------------------------------------  


    #--------------------------------------------------------------------------------------------------------------------
    #Name:        retrieve_correct_answers_position_only(self,id):
    #Receives:    id (int) of a question desired to retrieve
    #Description: the function returns the list of correct answers positions portion of a question:
    #             {list of correct answers positions} 
    #Errors:      if wrong or unexisted id is passed - function returns None and prints a message
    #Assumptions: question id exists in a dictionary
    #--------------------------------------------------------------------------------------------------------------------  


Description of Question_Test.py:

contains 2 parts: No-verbose tests(Pass/Fail)
                  Verbose tests (prints content of dictionary, questions, separate question bits)

to run the test:
                  insert code from tests.py below in the class Question.py and run
