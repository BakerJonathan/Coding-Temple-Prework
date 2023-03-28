#Jonathan Baker
#Python Prework
#will assume inputs are valid

#Question 1
#Write a function that prints hello [username], [username] is the imput
def hello_name(user_name):
    print ("hello " + user_name)

#Question 2
#Write a function tat prints odds from 1 to 100
def first_odds():
    #will itterate throuth 1 to 100, printing when it's odd
        #in hindsight a while loop that goes up by two would've been a bit better
    for i in range(1,100):
        if i%2==1:
            print(i, end=" ")
            #worth noting that this only goes to 99 (doesn't check 100, tested with 99/101 as range num2)
            #in this case it doesn't matter, but it'll be useful
                #to remember for python iteration (+1 to 2nd range num)

#Question 3
#Write a function that returns the max number of a list
def max_num_in_list(a_list):
    #I'll itterate through the list, comparing curr_max
    curr_max=a_list[0]
    for i in range(1,len(a_list)): #1 not 0, cause 0 is curr_max, len should give 1 more than the last index, which should work, as range appears to exclude the largest num
        if a_list[i]>curr_max:
            curr_max=a_list[i]
    return curr_max

#Question 4
#Return (true) if a given year is a leap year
    #leap years are divisible by 4, not 100, unless 400
def is_leap_year(a_year):
    #a simple if else if starting at the most niche/exclusive case should do the trick
        #a case statement would do the trick too
    if a_year%400==0:
        return True
    elif a_year%100==0:
        return False
    elif a_year%4==0:
        return True
    else:
        return False

#Question 5
#Check if numbers in a list are consecutive
def is_consecutive(a_list):
    #going to modify off of question 3, as I'll be itterating a list again
    firstnum=a_list[0]
    for i in range(1,len(a_list)): 
        if a_list[i]!=firstnum+i:
            return False
    return True
#this code works with decimals, ie 1.5 and 2.5 are consecutive. For better or worse.






#test code (commented out)
#Q1
#hello_name("Jonathan")
#Q2
#first_odds()
#Q3
#list1=[5,12,66,99,14,56,78, 200] #Using 200 as the last number to ensure that it iterates through the whole list
#list2=[100.2, 7.5,78,-62,-300.9,55.5] #Check that negatives and floats work properly, check that front number is accounted for properly
#print(max_num_in_list(list1))
#print(max_num_in_list(list2))
#print(max_num_in_list([5,3,7,2,1,0,4]))#check that list made in call works fine (no reason it shouldn't)
#print(max_num_in_list([99]))#check list of 1
#Q4
#print(is_leap_year(2020)+is_leap_year(20)+is_leap_year(4)+is_leap_year(160)+is_leap_year(16000004)) #check basic 4's, should print 5, as there were 5 trues(1's)
#print(is_leap_year(100)+is_leap_year(200000300)+is_leap_year(700)+is_leap_year(300)+is_leap_year(1500)) #check 100's, not 400, should be 0
#print(is_leap_year(0)+is_leap_year(200000400)+is_leap_year(800)+is_leap_year(400)+is_leap_year(1600)) #check 400 centuries, should be 5
#print(is_leap_year(1)+is_leap_year(200000402)+is_leap_year(809)+is_leap_year(402)+is_leap_year(1607)) # check non 4's, should be 0
#Q5
#print(is_consecutive([1,2,3,4,5]))#basic success (true)
#print(is_consecutive([1,2,3,4,6]))#basic failure (false)
#print(is_consecutive([-2.0,-1,0.0,1,2,3.0,4,5]))#mixed and negative imputs (true)
#print(is_consecutive([1.6,2.6,3.6,4.6,5.6])) # a nuance allowed by how I set it up, not sure if this is what we care for exactly (true)
#print(is_consecutive([1,2,3,4.0000000001,5]))#failure to check that floats and small decimals usually won't cause issues (false)
#print(is_consecutive([1,2,3,4.00000000000000001,5]))#but they can since eventually rounding kicks in (true)
#print(is_consecutive([512.51234]))#check what happens with one number (true)
