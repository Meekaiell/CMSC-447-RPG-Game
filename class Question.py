#---------------------------------------------------------------------------------------------------------------------------------------
# Class Question: 
#                      receives a string of one/multiple questions in a specified format
#                      saves each question in the dictionary as a value with the coresponding question id as the key
#                      can return bits of the question, edit question when question id is passed
#                      can add a new question to the set of existing question
#                      can return full questions(all components) as one string or a list of bits when id is passed
# Format of the input: 
#                      {id - integer} {question_number - integer} {question - string}
#                      {list_of_answers - list of strings} {correct_answer_position - int or list of ints}

# Example:             '#4567: 3: What is orange? Answers: [color] [fruit] [vegetable] Correct: {1} {2} 
#                       #452: 9: Which of the following are caller saved registers? Answers: [RAX] [RDI] [RSI] [RDX] Correct: {2} {4}'
#---------------------------------------------------------------------------------------------------------------------------------------
import re
import collections

class Question:

    #--------------------------------------------------
    #Constructor
    #--------------------------------------------------
    def __init__(self,passed_list):      
        self.list = self.save_collection(passed_list)
        self.dict = self.create_dict(self.list)        

    
    #--------------------------------------------------------------------------------------------------------------------
    #Name:        save_collection(self,passed_list):
    #Receives:    a string of questions in expected format:
    #             {Question ID} {Question Number} {Question} {list of answers} {indexes of the correct answer positions}
    #             '#4567: 3: What is orange? Answers: [color] [fruit] [vegetable] Correct: {1} {2}'
    #Description: iterates throught the string and separates each question, stores in a list, returns a list
    #Assumptions: questions passed in a specified format
    #--------------------------------------------------------------------------------------------------------------------
    def save_collection(self, passed_list):        
       
        modified_list = passed_list.split('#')
        modified_list = list(filter(None, modified_list))

        return modified_list

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
    def create_dict(self, modified_list):
   
        new_list = []
        list_to_zip = []

        #EXTRACT ID:
        for m in modified_list:

            #Extracting id:
            id = [re.search('(.+?):', x).group(1) for x in modified_list]     #extract id from the question
            new_list = [re.sub('(.+?):', '', x, 1) for x in modified_list]    #removes id from question itself  
            new_list = [(x.strip()) for x in new_list]                        #removes any empty space before question

        #Extracting rest of the info:      
        for i in (new_list):                                  
             
                 extracted_list = []

                 #QUESTION NUMBER:
                 match = re.compile('(.+?):')                                 #extract question number from the question
                 question_number = match.search(i).group(1)                 
                 question_number = int(question_number)                       #convert question_number to int
                 i = re.sub('(.+?):', '', i, 1)                               #removes question number from the question
                 i = i.strip()                                                #removes any empty space before question
                 extracted_list.insert(0, question_number)                    #question number stored at [0]

                 #QUESTION:
                 match1 = re.compile('(.+?):')                                #extract question 
                 question = match1.search(i).group(1)                 
                 question = re.sub(r'\bAnswers\b', '', question, 1)
                 i = re.sub('(.+?):', '', i, 1)                               #removes question from the rest of the string
                 i = i.strip()                                                #removes any empty space before 
                 extracted_list.insert(1, question)                           #question number stored at [0]

                 #ANSWERS:
                 answers = i.split('Answers:')[0]                    
                 answers = re.sub(r'\bCorrect\b', '', answers, 1)             #extract answers in a separate string
                 list_of_answers = []                                         #insert each answer in a list of answers
                 pattern = re.compile(r'(?<=\[)(.*?)(?=\])')
                 for k in re.findall(pattern,answers):
                         list_of_answers.append(k)
                 extracted_list.insert(2, list_of_answers)                    #question number stored at [0]

                 #CORRECT ANSWER INDEX
                 correct_answer = i.split('Correct:')[1]
                 correct_answer = correct_answer.strip()
                 list_of_correct_answers_positions = []
                 pattern = re.compile(r'(?<=\{)(.*?)(?=\})')
                 for k in re.findall(pattern,correct_answer):
                         k = int(k)
                         list_of_correct_answers_positions.append(k)
                 extracted_list.insert(3, list_of_correct_answers_positions)  #question number stored at [0]
                 
                 list_to_zip.append(extracted_list)

        #creating dictionary
        dictionary = dict(zip(id, list_to_zip))                               #creates a dictionary: storing question id as key and rest as value
        d = {int(k):v for k,v in dictionary.items()}                          #convert keys to int from string

        return d
     
    #--------------------------------------------------------------------------------------------------------
    #Name:        print_dictionary(self):
    #Receives:    -
    #Description: the function prints content of a dictionary  
    #Assumptions: -
    #--------------------------------------------------------------------------------------------------------
    def print_dictionary(self):
        print(self.dict)

    #--------------------------------------------------------------------------------------------------------------------
    #Name:        retrieve_full_question(self, id):
    #Receives:    id (int) of a question desired to retrieve
    #Description: the function returns a full question as a list of bits:
    #             {question number} {question} {list of answers} {list of positions corresponding to the correct answer}
    #Errors:      if wrong or unexisted id is passed - function returns None and prints a message
    #Assumptions: question id exists in a dictionary
    #--------------------------------------------------------------------------------------------------------------------
    def retrieve_full_question(self, id):
        question = self.dict.get(id)
        if(question == None):
            print('Id is wrong or doesn\'t exist')
        return question

    #--------------------------------------------------------------------------------------------------------------------
    #Name:        retrieve_full_question_string(self, id):
    #Receives:    id (int) of a question to retrieve
    #Description: the function returns a full question in a form of a single string as:
    #             #question_number. question_itself ?/. answer1 answer2 answer3; correctPosition1 correctPosition2
    #Example:     
    #    input:   #4567: 3: What is orange? Answers: [color] [fruit] [vegetable] Correct: {1} {2} 
    #    output:  #3. What is orange? color fruit vegetable; 1 2
    #Errors:      if wrong or unexisted id is passed - function returns None and prints a message
    #Assumptions: question id exists in a dictionary
    #--------------------------------------------------------------------------------------------------------------------
    def retrieve_full_question_string(self, id):
        question = self.dict.get(id)
        if(question == None):
            print('Id is wrong or doesn\'t exist')
        else:
            my_string = '#' + str(question[0]) + '. ' + question[1] + ' '   #concatinate number and justion bits
            string = ' '
            temp_list_of_answers = [x + string for x in question[2]]        #add space for each item in asnwers list
            temp_string = ''.join(map(str,temp_list_of_answers))            #convert list of answers to a single string
            my_string = my_string + temp_string + ';'                       #add bits and separator between before positions

            temp_positions = [str(x) for x in question[3]]                  #convert each int in list to string
            temp_list_of_positions = [x + string for x in temp_positions]   #add spaces between correct positions
            temp_string1 = ''.join(map(str,temp_list_of_positions))         #convert positions to a string
            my_string = my_string + ' ' + temp_string1                      #add rest of the bits
            return my_string

    #--------------------------------------------------------------------------------------------------------------------
    #Name:        retrieve_question_number_only(self,id):
    #Receives:    id (int) of a question desired to retrieve
    #Description: the function returns the question number portion of a question:
    #             {question number} 
    #Errors:      if wrong or unexisted id is passed - function returns None and prints a message
    #Assumptions: question id exists in a dictionary
    #--------------------------------------------------------------------------------------------------------------------    
    def retrieve_question_number_only(self,id):
        full_question = self.dict.get(id)
        if(full_question == None):
            print('Id is wrong or doesn\'t exist')
            return None
        else:
            return full_question[0]

    #--------------------------------------------------------------------------------------------------------------------
    #Name:        retrieve_question_only(self,id):
    #Receives:    id (int) of a question desired to retrieve
    #Description: the function returns the question portion of a question:
    #             {question}
    #Errors:      if wrong or unexisted id is passed - function returns None and prints a message 
    #Assumptions: question id exists in a dictionary
    #--------------------------------------------------------------------------------------------------------------------    
    def retrieve_question_only(self,id):
        full_question = self.dict.get(id)
        if(full_question == None):
            print('Id is wrong or doesn\'t exist')  
            return None
        else:
            return full_question[1]

    #--------------------------------------------------------------------------------------------------------------------
    #Name:        retrieve_list_of_answers_only(self,id):
    #Receives:    id (int) of a question desired to retrieve
    #Description: the function returns the list of answers portion of a question:
    #             {list of answers} 
    #Errors:      if wrong or unexisted id is passed - function returns None and prints a message
    #Assumptions: question id exists in a dictionary
    #--------------------------------------------------------------------------------------------------------------------  
    def retrieve_list_of_answers_only(self,id):
        full_question = self.dict.get(id)
        if(full_question == None):
            print('Id is wrong or doesn\'t exist')
            return None
        else:
            return full_question[2]
    
    #--------------------------------------------------------------------------------------------------------------------
    #Name:        retrieve_correct_answers_position_only(self,id):
    #Receives:    id (int) of a question desired to retrieve
    #Description: the function returns the list of correct answers positions portion of a question:
    #             {list of correct answers positions} 
    #Errors:      if wrong or unexisted id is passed - function returns None and prints a message
    #Assumptions: question id exists in a dictionary
    #--------------------------------------------------------------------------------------------------------------------  
    def retrieve_correct_answers_position_only(self,id):
        full_question = self.dict.get(id)
        if(full_question == None):
            print('Id is wrong or doesn\'t exist')
            return None
        else:
            return full_question[3]

    #--------------------------------------------------------------------------------------------------------------------
    #Name:        edit_question_id(self,current_id,new_id):
    #Receives:    id (int) of a question to edit, new id number(int) to replace old id
    #Description: the function edits the question id: new id replaces the old id
    #Errors:      if wrong or unexisted id is passed - function returns None and prints a message
    #Assumptions: unique question id is passed
    #-------------------------------------------------------------------------------------------------------------------- 
    def edit_question_id(self,id,new_id):
        full_question = self.dict.get(id)
        if(full_question == None):
            print('Id is wrong or doesn\'t exist')
            return None
        else:
             self.dict[new_id] = self.dict.pop(id)

    #--------------------------------------------------------------------------------------------------------------------
    #Name:        edit_question_number(self,id,new_number):
    #Receives:    id (int) of a question to edit, new question number(int) to replace old question numbers
    #Description: the function edits the number of the question when passed a question id
    #Errors:      if wrong or unexisted id is passed - function returns None and prints a message
    #Assumptions: unique question id is passed
    #-------------------------------------------------------------------------------------------------------------------- 
    def edit_question_number(self,id,new_number):
        full_question = self.dict.get(id)
        if(full_question == None):
            print('Id is wrong or doesn\'t exist')
            return None
        else:
            full_question[0] = new_number
            self.dict[id] = full_question;


    #--------------------------------------------------------------------------------------------------------------------
    #Name:        edit_question_only(self,id,new_question):
    #Receives:    id (int) of a question to edit, new question only (string) to replace old question
    #Description: the function edits the question portion of the question when passed a question id
    #Errors:      if wrong or unexisted id is passed - function returns None and prints a message
    #Assumptions: unique question id is passed
    #-------------------------------------------------------------------------------------------------------------------- 
    def edit_question_only(self,id,new_question):
        full_question = self.dict.get(id)
        if(full_question == None):
            print('Id is wrong or doesn\'t exist')
            return None
        else:
            full_question[1] = new_question
            self.dict[id] = full_question;

    #--------------------------------------------------------------------------------------------------------------------
    #Name:        edit_answers_only(self,id,new_answers):
    #Receives:    id (int) of a question to edit, new answers only in expected format (string) to replace answers:
    #             input format: [answer1] [answer2] [answer3]...
    #Description: the function edits the answers portion of the question when passed a question id
    #Errors:      if wrong or unexisted id is passed - function returns None and prints a message
    #Assumptions: unique question id is passed, answers passed in expected format
    #-------------------------------------------------------------------------------------------------------------------- 
    def edit_answers_only(self,id,new_answers):
        full_question = self.dict.get(id)
        if(full_question == None):
            print('Id is wrong or doesn\'t exist')
            return None
        else:
            new_list_of_answers = []
            pattern = re.compile(r'(?<=\[)(.*?)(?=\])')
            for k in re.findall(pattern,new_answers):
                new_list_of_answers.append(k)

            full_question[2] = new_list_of_answers   #replace old list of answers with new
            self.dict[id] = full_question;

    #--------------------------------------------------------------------------------------------------------------------
    #Name:        edit_correct_answers(self,id,new_positions):
    #Receives:    id (int) of a question to edit, new correct answers positions only in expected format (string):
    #             input format: {2} {4} ...
    #Description: the function edits the answers portion of the question when passed a question id
    #Errors:      if wrong or unexisted id is passed - function returns None and prints a message
    #Assumptions: unique question id is passed, answers passed in expected format
    #-------------------------------------------------------------------------------------------------------------------- 
    def edit_correct_answers(self,id,new_positions):
        full_question = self.dict.get(id)
        if(full_question == None):
            print('Id is wrong or doesn\'t exist')
            return None
        else:
            new_list_of_positions = []
            pattern = re.compile(r'(?<=\{)(.*?)(?=\})')
            for k in re.findall(pattern,new_positions):
                k = int(k)
                new_list_of_positions.append(k)

            full_question[3] = new_list_of_positions   #replace old list of answers with new
            self.dict[id] = full_question;

    
    #--------------------------------------------------------------------------------------------------------------------
    #Name:        add_new_question(self,id):
    #Receives:    id (int) of a new question to add
    #Description: the function adds a new question to the dictionary,
    #             the function receives an id and fills with blanks a corresonding question bits
    #Errors:      if duplicate id passed - 
    #Assumptions: unique question id is passed
    #-------------------------------------------------------------------------------------------------------------------- 
    def add_new_question(self,id):
        list = [0, '', '', 0]
        self.dict[id] = list




