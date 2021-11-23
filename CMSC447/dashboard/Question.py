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
    #Description: the function returns a full question:
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

