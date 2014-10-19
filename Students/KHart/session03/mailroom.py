#!/usr/bin/env python
import sys  #so I can call sys.exit to quit completely

donor_list = [["Jonny Hart", ["5"]], ["Kyle Hart", ["50", "100"]], ["Isaac Hart", ["25", "30"]], ["Nathan Hart", ["20"]], ["Thad Hart", ["1"]]]

#first prompt of program
def prompt():
    input1 = raw_input("\nPlease type the corresponding number below: \n1: Send a Thank You \n2: Create a Report\n:  ")
    check_quit(input1, q=True)
    retry_input = True
    while retry_input:
        if input1 == "1":
            retry_input = False
            thankyou()
        elif input1 == "2":
            retry_input = False
            report()
        else:
            input1 = check_input(input1, ["1", "2"])
            

            
#Can call this function any time an invalid input is received.  It will loop until correct input recieved
def check_input(input, valid_options_list):
    while input not in valid_options_list:
        print "\n'%s' is not a valid option" % input
        print "Please choose one of the following: "
        input = raw_input(valid_options_list)
        check_quit(input)
    return input

def check_quit(input, q=False):
    if q and input.lower() == "quit":  #this allows program quit from main prompt
        sys.exit(0)
    elif input.lower() == "quit":   #all other quits will return to prompt
        prompt()

def check_int(value):
    return_int = False
    while return_int == False:    #can I replace these two lines with 'while True' ? just to create loop
        try:
            if type(int(value)) == int:
                return int(value)
        except ValueError:
            value = raw_input("That's not a valid number, please try again:  ")
            check_quit(value)


def thankyou():
    global donor_list

    # asks for name, can be called in loop if list is called multiple times
    def enter_name():
        input2 = raw_input("Please enter Donor's Full Name: ")
        check_quit(input2)
        return input2

    def print_letter(name, amount):
        print """
        Dear %s, 

        Thank you kindly for your donation of $%s.

        Sincerely, 
        The Foundation
        """ % (name, amount)


    # calls initial prompt
    input2 = enter_name()

    # if user types 'list' then donor_list displayed and asks for user name again; allows for list to be called again
    while input2.lower() == "list":
        for name in donor_list:
            print name[0]
        input2 = enter_name()


    # checks if input is in donor list or not, acts accordingly
    active_record = None
    match = False
    for index, name in enumerate(donor_list):
        if input2.lower() == name[0].lower():
            active_record = index
            amount1 = raw_input("How much did %s donate?: " % name[0])
            check_quit(amount1)
            amount1 = check_int(amount1)
            donor_list[index][1].append(amount1)
            #print donor_list  #test displays that donor list was updated
            print_letter(donor_list[index][0], amount1)
            match = True
            prompt()
        
    if match == False:
        print "\nWe'll add '%s' to our donor list" % input2
        amount2 = raw_input("How much did %s donate?: " % input2)
        check_quit(amount2)
        amount2 = check_int(amount2)
        donor_list.append([input2, [amount2]])
        #print donor_list  #this line confirms list was updated with  new amount and name
        print_letter(input2, amount2)
        prompt()



def report():
    print ""
    print "DONOR NAME \tTOTAL DONATED \t# OF DONATIONS \tAVERAGE DONATION"
    for donor in donor_list:
        name = donor[0]
        total = 0
        for number in donor[1]:    #this turns the raw_input strings of amounts into ints and sums them
            total += int(number)
        number = len(donor[1])
        average = total / number #turn this into a float number??
        print "%s\t%s\t\t%s\t\t%s\t\t" % (name, total, number, average)
    print ""
    prompt()

if __name__ == '__main__':
    prompt()