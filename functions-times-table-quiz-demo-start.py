''' learning about functions - times tables quiz demo - Raspberry Pi Foundation - adapted by Ms Lee 28/2/2022'''

''' this code runs a basic times tables quiz, asks user which times table, then which value to go up to.
Then asks user to answer questions for chosen times table. '''

def check_integer():
  not_validated = True
  
  while not_validated:
    try:
      num1 = int(input())
      not_validated = False
    except ValueError:
      print("You must enter a whole number: ")
      
    return num1

## - main program
print("Welcome to the times table quiz")

# get choice of times table
print("Enter a times table that you would like to be tested on:")
times_table = check_integer()


# get maximum value for chosen times table    

print("Enter the maximum value for your times table: ")

max_value = check_integer()
 
# add 1 so that max value is included in quiz    
max_value = max_value + 1
answer = 0

# display the quiz
print(f"Here is your quiz on the {times_table} times table")

# ask each question (start with 1, end with max value chosen by user)
for x in range(1,max_value):
  
  # calc answer
    answer = x * times_table
    # print question
    print(f"{x} times {times_table} is ...")
    
    # get answer
    not_validated = True
    while not_validated:
      try:
        print("Answer:")
        user_answer = int(input())
        not_validated = False
      except ValueError:
        print("You must enter a whole number")
    
    # say if answer is correct or incorrect    
    if user_answer == answer:
      print("Correct")
    else:
      print("Incorrect")