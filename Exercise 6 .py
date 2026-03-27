#Brute Force Attack 
#assigning a password
my_password= 12345
password = 0 # intial 
while password != my_password:
 password = int(input("Enter the password: " ))
 if password != my_password:
    print("Try again")
if password == my_password:
    print("Access granted")

#optional requirement 
my_password = 12345
# declaring max attempt 
total_attempt = 5
attempt = 0

while attempt < total_attempt:
    remaining = total_attempt - attempt
    print(" remaining attempts left: " + str(remaining))
    password_input = int(input( " Enter the password: " ))
    attempt += 1
    if password_input == my_password:
        print("Access granted")
        break  # attempt
else :
#if attempt >= total_attempt:  
    print("Authorities have been alerted")



