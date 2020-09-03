import random

#create student data list
student_data = [
      {"name": "Jacy Yang",
       "student id": 123456,
       "email": "jyang456@gmail.com"},
      {"name": "Jolly Ranger",
       "student id": 456789,
       "email": "jranger789@gmail.com"}
]

#generate student id and email
def generate_student_data(name):
    #generates randomized student id 
    student_id = random.randint(111111,999999)
    
    seperate_name = name.split()
    first = seperate_name[0]
    last = seperate_name[1]
  
    email_number_id = str(student_id)
    email = first[0] + last + email_number_id[-3:] + "@gmail.com"

    student_data.append(
        {"name": name,
         "student id": student_id,
         "email": email}
    )


def add_name_again():
    add = True
    while add == True:
      add_again = input("Would you like to add another name? ")
      if "y" in add_again or "Y" in add_again:
        names()
      elif "N" in add_again or "n" in add_again:
        print(add_again[0])
        print("You have added all your names.")
        print(student_data)
        add = False
      else:
        print("Please type Yes or No.")

#name function to add student data or to print user student-selected data
def names():
  #prompts user for student name
  name = input("Please enter student name: ")
  #checks for dictionary with name-key that has the name-value inputted from user
  if not any(d["name"] == name for d in student_data):
    generate_student_data(name)
    print(name + " has been added to the student registry.")
    
    add_name_again()

  else:
     print("There is already a student with that name.")
     print(student_data)

names()
