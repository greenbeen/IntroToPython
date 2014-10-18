#!/usr/bin/env python

#first prompt of program
def prompt():
    input1 = raw_input("\nPlease type the corresponding number below: \n1: Send a Thank You \n2: Create a Report\n:  ")
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
    return input



def thankyou():
    print "need to define 'thankyou' function"
    

def report():
    print "need to define 'report' function"


prompt()