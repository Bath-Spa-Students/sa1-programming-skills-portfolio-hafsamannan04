#simple search
#to search sam in list 
#step1 : create list

name_list = ["Jake","Zac", "Ian", "Ron", "Sam", "Dave"]

#step2: search input
search_box = input("Enter name to search: ")

#step3 : search for sam
if search_box.lower() in [ name.lower() for name in name_list]:
    print ("yes," + search_box +" "+ "is in the list")
else :
 print("not found")


