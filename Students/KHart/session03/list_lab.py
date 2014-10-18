#!/usr/bin/env python



#Create list
fruit_list = ["Apples", "Pears", "Oranges", "Peaches"]
#Display list
print fruit_list

# for formatting output in terminal
def re():
    print "\nRevised fruit list:"
    print fruit_list
    
# ask for fruit, add to end of list
input1 = raw_input("Type a fruit to add: ")
fruit_list.append(input1)
#display list, now using re() to simplify and create formatting lines
re()

# ask for number to display that fruit index from list (using starting index at 1)
input2 = raw_input("Choose a number between 1 and %r: " % len(fruit_list))
#display corresponding fruit back
print str(fruit_list[int(input2) - 1]) + " is number %r in the list." % int(input2)

# add a fruit using '+'
fruit_list = ["Banana"] + fruit_list
re()

# add fruit using "insert()"
fruit_list.insert(0, "Mango")
re()

# display all fruits beginning with "P"
#check 1st position of each item in list to see if equals P
temp_list = []
for fruit in fruit_list:
    if fruit[0].upper() == "P": 
        temp_list += [fruit]
print temp_list


print fruit_list

#remove last fruit
del fruit_list[-1]
re()

#Delete user typed fruit, loops if type invalid fruit
def delete_fruit():
    input3 = raw_input("Which fruit would you like to delete?  ")
    original_length = len(fruit_list)
    for idx, fruit in enumerate(fruit_list):
        if input3.upper() == fruit.upper():
            del fruit_list[idx]  
    if original_length == len(fruit_list):
        print "That's not an option, please try again"
        delete_fruit()

delete_fruit()
re()

# ask if user likes each fruit - delete if no
last_list = []
for fruit in fruit_list:
    input4 = raw_input("Do you like %s: " % fruit)
    if input4.lower() == "yes":
        last_list += [fruit]
    elif input4.lower() == "no":
        continue
    else:
        while input4.lower() != "yes" and input4.lower() != "no":
            print "\nThat's not a valid option"
            print "Do you like %s " % fruit
            input4 = raw_input("Type 'yes' or 'no': ")
            if input4.lower() == "yes":
                last_list += [fruit]

fruit_list = last_list
re()







