<<<<<<< HEAD:Client-side/Question_Test.py
test1 = Question("""#5467: 1: How many bits in a Quad Word on Intel x86? Answers: [64 bits] [32 bits] [4 bits] [8 bits] [16 bits] Correct: {3} #29876: 2: What is -o in 8 bits Two's complemet? Answers: [Does not exist] [1000] [00000] [1111111] [0] [1000000] Correct: {1} {4} #1058: 7: The edges of K-Map must maintain a 1 bit change between the values? Answers: [True] [False] Correct: {2}""")
print('Retrieve question number:')
if(test1.retrieve_question_number_only(5467) == 1):
    print('Passed.')
else:
    print('Failed')

print('Retrieve question only:')
string1 = test1.retrieve_question_only(5467)
string2 = 'How many bits in a Quad Word on Intel x86? '
if(string1 == string2 ):
    print('Passed.')
else:
    print('Failed')

print('Retrieve list of answer choices:')
correct = ['64 bits', '32 bits', '4 bits', '8 bits', '16 bits']
if(collections.Counter(test1.retrieve_list_of_answers_only(5467)) == collections.Counter(correct)):
    print('Passed.')
else:
    print('Failed')

print('Retrieve list of correct answers positions:')
correct1 = [3]
if(collections.Counter(test1.retrieve_correct_answers_position_only(5467)) == collections.Counter(correct1)):
    print('Passed.')
else:
    print('Failed')

print('Retrieve non-existing ids for q#:')
if(test1.retrieve_question_number_only(5) == None):
    print('Passed.')
else:
    print('Failed')

print('Retrieve non-existing ids for q:')
if(test1.retrieve_question_only(5) == None):
    print('Passed.')
else:
    print('Failed')

print('Retrieve non-existing ids for answer choices:')
if(test1.retrieve_list_of_answers_only(5) == None):
    print('Passed.')
else:
    print('Failed')
print('\n')

print('Retrieve non-existing ids for correct answers:')
if(test1.retrieve_correct_answers_position_only(5) == None):
    print('Passed.')
else:
    print('Failed')
print('\n')

print('Retrieve non-existing ids for whole q:')
if(test1.retrieve_full_question(5) == None):
    print('Passed.')
else:
    print('Failed')
print('\n')

#Test case: Some questions from the CMSC 313 quizes and hw:
print('Verbose tests: \n\n')
test2 = Question("""#5467: 1: How many bits in a Quad Word on Intel x86? Answers: [64 bits] [32 bits] [4 bits] [8 bits] [16 bits] Correct: {3} #29876: 2: What is -o in 8 bits Two's complemet? Answers: [Does not exist] [1000] [00000] [1111111] [0] [1000000] Correct: {1} {4} #1058: 7: The edges of K-Map must maintain a 1 bit change between the values? Answers: [True] [False] Correct: {2}""")
print('Printing content of a dictionary: \n')
test2.print_dictionary()
print('\n')
print('Retrieveing full questions: \n')
print(test2.retrieve_full_question(29876))
print(test2.retrieve_full_question(5467))
print(test2.retrieve_full_question(1058))
print('\n')
print('Retrieveing question numbers only: \n')
print(test2.retrieve_question_number_only(29876))
print(test2.retrieve_question_number_only(5467))
print(test2.retrieve_question_number_only(1058))
print('\n')
print('Retrieveing questions only: \n')
print(test2.retrieve_question_only(29876))
print(test2.retrieve_question_only(5467))
print(test2.retrieve_question_only(1058))
print('\n')
print('Retrieveing list of answer choices only: \n')
print(test2.retrieve_list_of_answers_only(29876))
print(test2.retrieve_list_of_answers_only(5467))
print(test2.retrieve_list_of_answers_only(1058))
print('\n')
print('Retrieveing list of correct answer positions only: \n')
print(test2.retrieve_correct_answers_position_only(29876))
print(test2.retrieve_correct_answers_position_only(5467))
print(test2.retrieve_correct_answers_position_only(1058))
print('\n')

#Test case: only one question passed:
test3 = Question("""#452: 9: Which of the following are caller saved registers? Answers: [RAX] [RDI] [RSI] [RDX] [RCX] [R8] [R9] [R10] [R11] Correct: {2} {6}""")

print(test3.retrieve_full_question(452))
print(test3.retrieve_question_number_only(452))
print(test3.retrieve_question_only(452))
print(test3.retrieve_list_of_answers_only(452))
print(test3.retrieve_correct_answers_position_only(452))

#Test case: retrieving id that does not exist:
print(test3.retrieve_full_question(81))
#Test case: retrieving id that does not exist:
print(test3.retrieve_correct_answers_position_only(81))
print(test3.retrieve_list_of_answers_only(81))
print(test3.retrieve_question_number_only(81))
print(test3.retrieve_question_only(81))

=======
test1 = Question("""#5467: 1: How many bits in a Quad Word on Intel x86? Answers: [64 bits] [32 bits] [4 bits] [8 bits] [16 bits] Correct: {3} #29876: 2: What is -o in 8 bits Two's complemet? Answers: [Does not exist] [1000] [00000] [1111111] [0] [1000000] Correct: {1} {4} #1058: 7: The edges of K-Map must maintain a 1 bit change between the values? Answers: [True] [False] Correct: {2}""")
print('Retrieve question number:')
if(test1.retrieve_question_number_only(5467) == 1):
    print('Passed.')
else:
    print('Failed')

print('Retrieve question only:')
string1 = test1.retrieve_question_only(5467)
string2 = 'How many bits in a Quad Word on Intel x86? '
if(string1 == string2 ):
    print('Passed.')
else:
    print('Failed')

print('Retrieve list of answer choices:')
correct = ['64 bits', '32 bits', '4 bits', '8 bits', '16 bits']
if(collections.Counter(test1.retrieve_list_of_answers_only(5467)) == collections.Counter(correct)):
    print('Passed.')
else:
    print('Failed')

print('Retrieve list of correct answers positions:')
correct1 = [3]
if(collections.Counter(test1.retrieve_correct_answers_position_only(5467)) == collections.Counter(correct1)):
    print('Passed.')
else:
    print('Failed')

print('Retrieve non-existing ids for q#:')
if(test1.retrieve_question_number_only(5) == None):
    print('Passed.')
else:
    print('Failed')

print('Retrieve non-existing ids for q:')
if(test1.retrieve_question_only(5) == None):
    print('Passed.')
else:
    print('Failed')

print('Retrieve non-existing ids for answer choices:')
if(test1.retrieve_list_of_answers_only(5) == None):
    print('Passed.')
else:
    print('Failed')
print('\n')

print('Retrieve non-existing ids for correct answers:')
if(test1.retrieve_correct_answers_position_only(5) == None):
    print('Passed.')
else:
    print('Failed')
print('\n')

print('Retrieve non-existing ids for whole q:')
if(test1.retrieve_full_question(5) == None):
    print('Passed.')
else:
    print('Failed')
print('\n')

#Test case: Some questions from the CMSC 313 quizes and hw:
print('Verbose tests: \n\n')
test2 = Question("""#5467: 1: How many bits in a Quad Word on Intel x86? Answers: [64 bits] [32 bits] [4 bits] [8 bits] [16 bits] Correct: {3} #29876: 2: What is -o in 8 bits Two's complemet? Answers: [Does not exist] [1000] [00000] [1111111] [0] [1000000] Correct: {1} {4} #1058: 7: The edges of K-Map must maintain a 1 bit change between the values? Answers: [True] [False] Correct: {2}""")
print('Printing content of a dictionary: \n')
test2.print_dictionary()
print('\n')
print('Retrieveing full questions: \n')
print(test2.retrieve_full_question(29876))
print(test2.retrieve_full_question(5467))
print(test2.retrieve_full_question(1058))
print('\n')
print('Retrieveing full questions as strings: \n')
print(test2.retrieve_full_question_string(29876))
print(test2.retrieve_full_question_string(5467))
print(test2.retrieve_full_question_string(1058))
print('\n')
print('Editing bits of the question: \n')

test2.edit_question_number(1058, 11)
test2.edit_question_only(1058, 'this is the new question.')
test2.edit_answers_only(1058, '[new1] [new2] [new3] [new4]')
test2.edit_correct_answers(1058, '{2} {4}')
test2.edit_question_id(1058, 990)
print(test2.retrieve_full_question(1058))  #should return none and print doesn't exist
print(test2.retrieve_full_question(990))
print(test2.retrieve_full_question_string(990))

print('\nPrinting content of a dictionary with one question fully changed: \n')
test2.print_dictionary()

print('\nRETRIEVING BITS OF THE QUESTIONS:')
print('Retrieveing question numbers only: \n')
print(test2.retrieve_question_number_only(29876))
print(test2.retrieve_question_number_only(5467))
print(test2.retrieve_question_number_only(990))
print('\n')
print('Retrieveing questions only: \n')
print(test2.retrieve_question_only(29876))
print(test2.retrieve_question_only(5467))
print(test2.retrieve_question_only(990))
print('\n')
print('Retrieveing list of answer choices only: \n')
print(test2.retrieve_list_of_answers_only(29876))
print(test2.retrieve_list_of_answers_only(5467))
print(test2.retrieve_list_of_answers_only(990))
print('\n')
print('Retrieveing list of correct answer positions only: \n')
print(test2.retrieve_correct_answers_position_only(29876))
print(test2.retrieve_correct_answers_position_only(5467))
print(test2.retrieve_correct_answers_position_only(990))
print('\n')

print('\nADDING NEW QUESTION TO THE EXISTING SET:')
test2.add_new_question(5555)
print(test2.retrieve_full_question(5555))
test2.edit_question_number(5555, 12)
test2.edit_question_only(5555, 'is this a new question I just added?')
test2.edit_answers_only(5555, '[True] [False] [Both]')
test2.edit_correct_answers(5555, '{1} {3}')
print(test2.retrieve_full_question(5555))
print(test2.retrieve_full_question_string(5555))

print('Print final dictionaty with all questions:')
test2.print_dictionary()
>>>>>>> main:Question_Test.py
