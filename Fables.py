#create madlib program

#https://www.eduplace.com/tales/

#noun: person, place or thing
#singualr and plural

#adjectives: a words that describes a noun; can also tell what kind or how many

#verb: action word
#present, past and future tense

#adverbs: word that descibes a verb (high, loudly, truly)
#can tell how (quickly), when (often) or where (here)

print("Create your own fable.")

#prompt user for corresponging variable input
place = input("place: ").capitalize()
holiday = input("holiday: ").capitalize()
creature = input("mythical creature: ")
name = input("name: ").capitalize()
past_tense_verb = input("past tense verb: ")
character = input("type of job: ")
first_verb = input("first verb: ")
noun = input("plural noun: ")
adjective = input("adjective: ")
friend = input("friend: ").capitalize()
second_verb = input("second verb: ")
exclaimation = input("exlaimation: ").upper()
adverb = input("adverb: ")

#try funtion used to ensure user submits an integer
def numbers():
    while True:
        try:
            number = int(input("number: "))
            return number
            break
        except ValueError:
            print("Oops! That was not a valid number. Please enter your number in numerical form.")
                
user_number = numbers()

print()
print(f"There was once a {creature} named {name} who lived in {place}.")
print(f"Every year, the people of {place} gather round to celebrate a holiday called {holiday}.")
print(f"{name}, the {creature}, often {past_tense_verb} through town during this time.")
print(f"The {character} waits every year for {name} to gather ingredients for the town feast.")
print(f"But in order to do this, {name} has to complete a mission from the {character}.")
print(f"This year, {name} has been given the task to {first_verb} {user_number} {adjective} {noun}.")
print()
print(f"{name} set out the next morning with their friend, {friend}.")
print(f"As {name}, the {creature} {past_tense_verb} with {friend}, they discovered the {noun}!")
print(f"'{exclaimation}!!! WE FOUND IT {friend.upper()}!!'")
print(f"{name} and {friend} {second_verb} as {adverb} as they {past_tense_verb} to the town, delivering the goods.")
