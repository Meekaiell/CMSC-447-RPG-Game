Files:

class Question.py  - contains the the code for the question container
Question_Test.py           - contains tests for class Question



							Description of class Question.py:

Class receives questions as one large string. Each question must be inputed in the following format:

{id - integer} {question_number - integer} {question - string}{list_of_answers - list of strings} {correct_answer_position - int or list of ints}

'#4567: 3: What is orange? Answers: [color] [fruit] [vegetable] Correct: {1} {2} #452: 9: Which of the following are caller saved registers? Answers: [RAX] [RDI] [RSI] [RDX] Correct: {2} {4}'

Supported functionality:

1) add a question to the existing list of questions: USE 
    
    add_new_question(self,id):                 - the function will add the question to the dictionary of existing question with id passed to the function as the key, 
                                                 and an EMPTY list.
2) to edit existing question (including EMPTY list for add_new_question(self,id)) use functions:
   
   edit_question_number(self,id,new_number)    - pass an id and the old question number will be replaced by the new_number(int)
   edit_question_only(self,id,new_question)    - pass an id and the old question portion of the question will be replaced with the new_question(string)
   edit_answers_only(self,id,new_answers)      - pass an id and the list of answer options will be replaced with the new_answers(string)
                                                 new_answers (string) must be formated as : '[answer1] [answer2] [answer3]...'
   edit_correct_answers(self,id,new_positions) - pass an id and the list of correct positions will be replaced with the new_positions(string)
                                                 new_apositions (string) must be formated as : '{position1} {position2}...'
   edit_question_id(self,id,new_id)            - pass an id and the new id and current id will be replaced by the new_id(int)
                                                 id is a unique key that used to retrieve/edit questions in the class

3) print all questions (id-questions pair) (format of python dictionary): USE
   
   print_dictionary(self)                      - prints all questions in the format of key - list of bits of questions

4) retrieve question by id: USE

   retrieve_full_question(self, id)            - pass an id of the question to retrieve
                                                 returned as a LIST of BITS of the question
                                                 example: 
                                                 [2, "What is -o in 8 bits Two's complemet? ", ['Does not exist', '1000', '00000', '1111111', '0', '1000000'], [1, 4]]
                                                 [questionNumber(int), "question"(string), list of answer choices(list of strings), list of correct answer positions(list of ints)]
  
  retrieve_full_question_string(self, id)      - pass an id of the question to retrieve
                                                 returns a STRING of all bits of the question
                                                 example:
                                                 '#2. What is -o in 8 bits Two's complemet?  Does not exist 1000 00000 1111111 0 1000000 ; 1 4'
5) retrieve separate bits of the question: USE


   retrieve_question_number_only(self,id)      - pass an id of the question to work with
                                                 returns a question number(int) corresponding to the passed id
   
   retrieve_question_only(self,id)             - pass an id of the question to work with
                                                 returns a question portion of the question (string) corresponding to the passed id
   
   retrieve_list_of_answers_only(self,id)      - pass an id of the question to work with
                                                 returns a LIST of strings of answer choices

   retrieve_correct_answers_position_only(self,id) - pass an id of the question to work with
                                                     returns a LIST of ints of correct positions in a LIST of answer choices OR an int if the only one choice is correct





							Description of Question_Test.py:

contains 2 parts: No-verbose tests(Pass/Fail)
                  Verbose tests (prints content of dictionary, questions, separate question bits)

to run the test:
                  insert code from tests.py below in the class Question.py and run
