#Biography 

#step 1
#storing info in dict as key-value pairs
Bio_info={
    "name":"Hafsa",
    "hometown":"Sharjah",
    "age":21
}
#step 2
#to print values on different line 
for values in Bio_info:
    print(Bio_info[values])


#step 3
# use variables 
name="Hafsa"
hometown="Sharjah"
age=21

#storing data in dict with variables
Bio_info={"name":name,   
    "hometown": hometown, 
    "age": age           
}
for value in Bio_info.values():
    print(value)



# advance requirement
# create a dict storing key and empty value 
info= {"Name:":" ","Hometown:":" ","Age:":""} 
info ["Name:"] =input("Enter your name: " )
info ["Hometown:"] =input("Enter your place of birth: " )
info ["Age:"] =input("Enter your age: ")  # storing as string so twenty one can be entered
for key,value in info.items():
    print(key + value)

