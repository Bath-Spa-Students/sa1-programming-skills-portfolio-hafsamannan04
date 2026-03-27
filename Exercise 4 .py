# primitive quiz

# step 1
# asking question 
answer=input("What is the capital of France ? ")

# response using if & else
# step 2 & 3

if answer == "Paris" :
    print("answer is correct")
else:
 print("answer is incorrect")


# advance requirement
# ignoreing capitalization
answer=input("What is the capital of France ? ")
if answer.lower() == " paris " :
   print("answer is correct")
else:
   print("answer is incorrect")

# Multiple quiz questions
# using dictionary 
quiz_data={
   "Russia":"Moscow",
   "Belarus":"Minsk",
   "Italy":"Rome",
   "Germany":"Berlin",
   "Ukraine":"Kiev",
   "Spain":"Madrid",
   "Netherland":"Amsterdam",
   "United Kingdom":"London",
    " Ireland":"Dublin ",
   "Finland":"Helsinki ",
}
# control structure 
# string concatenation
for country in quiz_data:
   answer=input(" What is the capital of "+country+"? " )
   if answer.lower()== quiz_data[country].lower():
    print("Well done!","It is correct.")
   else:
    print("incorrect" )
