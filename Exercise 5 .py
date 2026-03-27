#Days of the month 

#storing key-value pair
months_day={
1:31, 
2:28,
3:31,
4:30,
5:31, 
6:30,
7:31, 
8:31, 
9:30, 
10:31, 
11:30,
12:31
}
month=int(input("Enter month_no : " ))
if month >=1 and month <=12 :
 print("no of days:"+str(months_day[month]))
else:
    print("Invalid month number")
#advance requirement
if month == 2 :
 leap =input("Is it a leap year ? (yes/no) ")
if leap.lower() =="yes":
 print("No of days in February: 29 ")
else:
 print("No of days in February: 28 ")

