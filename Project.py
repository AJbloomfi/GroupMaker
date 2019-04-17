"""
430 Project
Matthew Karp
Jorge Contreras
Aaron Bloomfield 
"""

#imports
import pandas as pd 
import numpy as np 
import random
import string
import glob
import os
import time

#get users current directory
cwd = os.getcwd()
counter_for_something = 0
#loops the program if user wants to use it again
useprogram = True
while(useprogram):


    #%%
    #Open File
    
    #print all of the users csv files?
    print("Here are all of your csv files: ")
    print(glob.glob("*.csv"))
    
    #Loop until file is found 
    while True:
        # ask user for file 
        open_file = input("Enter the CSV file name: ")
        #Check if user put .csv
        if(open_file[-4:] != ".csv"):
        # concate filename with .csv
            open_file = open_file + ".csv"
        #tries to open the file then breaks out of loop if file is in 
        try:
            df = pd.read_csv(open_file)
            print()
            print(df)
            option = input("Is this the file you want to use(Y/N)? ")
            if(option == "Yes" or option == "yes" or option == "Y" or option== "y"):
                print("File Import Successful!")
                break
        #Prints error that file is not in directory
        except IOError as e:
            print(e.args)
        
    #End of Open File
    
    
    #%%
    
    #get number of rows of dataframe
    df_rows = len(df.index)
    half_class = int(df_rows/2)
    
    #Main stuff
    
    #Loop until user entered a number 
    while True:
        
        try:
            #ask user for the size of groups
            minNumGroups = input("Enter group size from 2-"+str(half_class) + ": ")
            minNumGroups = int(minNumGroups)
            if(minNumGroups > 1 and minNumGroups < half_class+1):
                break
            else:
                print("Error please enter group size from 2-"+str(half_class)+": ")
    
        #Prints error that user did not enter a number 
        except ValueError:
            print("Please enter a number! Try again!")
    
    
    #number of teams
    numTeams = int(df_rows / minNumGroups)
    
    #get col headers
    df = df.drop(columns=["Timestamp"])
   
    col_headers = list(df)
    print()
    
    #%%
    #WORK HERE
    csv_headers=[]
    
    #If the questions asked on the survey are going to be
    # What is your... (word) then get the last word to use as menu
    #below gets the last word in the string
    for i in range(len(col_headers)):  
        sting_head = col_headers[i]
        csv_headers.append(sting_head.split()[-1])
    #make col_headers = the fake list 
    col_headers = csv_headers
        
    sting_head_strip = []
    #need to strip punc 
    for i in range(len(col_headers)): 
        sting_head_strip.append(col_headers[i].translate(str.maketrans('', '', string.punctuation)))
    
    col_headers = sting_head_strip
    
    #captialize the words 
    new_headers = []
    for i in range(len(col_headers)): 
        new_headers.append(col_headers[i].capitalize())
    
    
    col_headers = new_headers
    
    
    df.columns = col_headers
    
    newFlag = False
    
    menuuuu = []    
    num = 0
    non_options = -1
    for i in col_headers:
        if(col_headers[num] == "Name" or col_headers[num] == "Blacklist" or col_headers[num] == "Timestamp"):
            num+=1
            non_options+=1
        else:
            menu_options = num-non_options
            menuuuu.append(col_headers[menu_options])
            num+=1

    
    
    #%%
    
    
    
    #ask for how many terms
    while True:
        try: 
            terms = input("How many different terms would you like to make (1-3)? ")
            terms = int(terms)
            if terms > 0 and terms < 4:
                break
            else:
                print("\nPlease enter a number that is between 1-3!")
                
                    #Prints error that user did not enter a number 
        except ValueError:
            print("Please enter a number! Try again!")
    
    print()
    
    
    menu=[]
    start_list = 1
    while True:
        end_list = 0
        try:
            if(terms == 1):
                while True:
                    number_choose = int(input("Would you like to sort by \n1) 1 Similarity \n2) Multiple Similarities \n3) Differences\n\n"))
                    if number_choose == 1 or number_choose == 2 or number_choose == 3:
                        break
                    else:
                        print("Error, please enter 1, 2, or 3! ")
                
                
                print()
                
                
##################################################################################################################


                #user wants only 1 option
                if(number_choose == 1):
                    counter=0
                    #make menu
                    print()
                    print("Choose one of the following options to sort by:")
                    num = 0
                    non_options = -1
                    for i in col_headers:
                        #might have to change
                        if(col_headers[num] == "Name" or col_headers[num] == "Blacklist" or col_headers[num] == "Timestamp"):
                            num+=1
                            non_options+=1
                        else:
                            menu_options = num-non_options
                            menu.append(menu_options)
                            print(str(menu_options) + ") Sort by", col_headers[num])
                            num+=1
                            end_list+=1
                    end_list+=1
                    print(str(menu_options+1) + ") Sort by Randomization")
                    print()
                    
                    while True:
                        try:
                            print("Enter your option: ", end = " ")
                            option = int(input())
                            if option >= start_list and option <= end_list:
                                break
                            else:
                                print()
                                print("Please enter a number from 1-" + str(end_list))
                                print()
                        except ValueError: 
                            print()
                            print("Please enter a number!")
                            print()
                            
                    if(option >= start_list and option <= end_list):
                         
                        #user selects anything but Randomization
                        if(option < menu_options+1):
                            #print("Would you like to sort by similarities or differences? (type similarity/difference)")
                            
                            
                            #Algorithms
                            
                            
                            #use modulus to check if teams are distrubted evenly 
                            #and no person is leftover
                            #use remainder to index in last column
                            remainder = df_rows % minNumGroups
                            
                            #print("Leftover students: " + str(remainder))
                            #print()
                            
                            if remainder == 0:
                                #list of teams
                                Teams = [[] for _ in range(numTeams)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams)]
                            else:
                                #list of teams
                                Teams = [[] for _ in range(numTeams+1)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams+1)]
                            
                            
                            #print random df
                            #print(df)
                            bigword = col_headers[option]
                            #variables
                            count=0         #to put x amount of students in the list
                            teamnum=0       # num for the team
                            nin = df.columns.get_loc("Name")   #name index number
                            bln = df.columns.get_loc("Blacklist")     # blacklist index number
                            df = df.sort_values(by=[bigword])
                            
                            
                            #loop through all df
                            for i in (range(df_rows)):
                            
                                #see group is 3 people
                                if count < minNumGroups:
                                    
                                    if i != df_rows:
                                    #append the blacklis names to the nested lists
                                        blacklist_list[teamnum].append(df.iloc[i, bln])     
                                        Teams[teamnum].append(df.iloc[i, nin]) 
                                        count += 1
                                        
                                #reset for next team, if count == maxsize of group
                                if count == minNumGroups:
                                    teamnum += 1         #go to the next team
                                    count = 0            #reset count to 0, to refill the next team
                                    
                            
                            
                            if(remainder != 0):
                                if(remainder == 1):
                                    Teams[teamnum-1].append(Teams[-1][0])
                                    blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                    
                                elif(remainder >= 2):
                                    while(len(Teams[-1]) != 0):
                                        for i in range(len(Teams)-1):
                                            if(remainder == 0):
                                                break
                                                           
                                            Teams[i].append(Teams[-1][remainder-1])
                                            blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                            del Teams[-1][remainder-1]
                                            remainder = remainder - 1
                                            #print(len(randomTeams[-1]))
                                            
                                del Teams[-1]
                                    
                            
                            
                            
                            #Blacklist
                            
                            #i= team num
                            #j=eachstudent in the team
                            #k=each student in bl
                            
                            #make bool true if teams are good, if there is a blacklist in the 
                            #team set bool to false
                            good_teams= True
                            
                            for i in range(teamnum):
                                lengthteamsize = len(Teams[i])
                                for j in range(lengthteamsize):
                                    for k in range(lengthteamsize):
                                        if(blacklist_list[i][k] == Teams[i][j]):
                            #                print(Teams[i][k],"HATES", Teams[i][j])
                                            good_teams = False
                            
                            counter+=1
                            
                            if counter == 50:   
                                break
                            
                            
                            #this is used for if there is a team that has a blacklist in it        
                            while(good_teams==False):
                                
                                #use modulus to check if teams are distrubted evenly 
                                #and no person is leftover
                                #use remainder to index in last column
                                remainder = df_rows % minNumGroups
                                
                                #print("Leftover students: " + str(remainder))
                                #print()
                                
                                
                                if remainder == 0:
                                    #list of teams
                                    Teams = [[] for _ in range(numTeams)]
                                    #list of blacklists
                                    blacklist_list = [[] for _ in range(numTeams)]
                                else:
                                    #list of teams
                                    Teams = [[] for _ in range(numTeams+1)]
                                    #list of blacklists
                                    blacklist_list = [[] for _ in range(numTeams+1)]
                                
                                #randomize the df
                                df = df.iloc[np.random.permutation(len(df))]
                                
                                #print random df
                                #print(df)
                                bigword = col_headers[option]
                                #variables
                                count=0         #to put x amount of students in the list
                                teamnum=0       # num for the team
                                nin = df.columns.get_loc("Name")   #name index number
                                bln = df.columns.get_loc("Blacklist")     # blacklist index number
                                
                                df = df.sort_values(by=[bigword])
                                
                                #loop through all df
                                for i in (range(df_rows)):
                                
                                    #see group is 3 people
                                    if count < minNumGroups:
                                        
                                        if i != df_rows:
                                        #append the blacklis names to the nested lists
                                            blacklist_list[teamnum].append(df.iloc[i, bln])     
                                            Teams[teamnum].append(df.iloc[i, nin]) 
                                            count += 1
                                            
                                    #reset for next team, if count == maxsize of group
                                    if count == minNumGroups:
                                        teamnum += 1         #go to the next team
                                        count = 0            #reset count to 0, to refill the next team
                                        
                                
                                
                                if(remainder != 0):
                                    
                                    if(remainder == 1):
                                        
                                        Teams[teamnum-1].append(Teams[-1][0])
                                        
                                        blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                        
                                        
                                        
                                    elif(remainder >= 2):
                                        while(len(Teams[-1]) != 0):
                                            for i in range(len(Teams)-1):
                                                if(remainder == 0):
                                                    break
                                                               
                                                Teams[i].append(Teams[-1][remainder-1])
                                                blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                                del Teams[-1][remainder-1]
                                                remainder = remainder - 1
                                                #print(len(randomTeams[-1]))
                                                
                                    del Teams[-1]
                                        
                                
                                #Blacklist
                                
                                #i= team num
                                #j=eachstudent in the team
                                #k=each student in bl
                                
                                #make bool true if teams are good, if there is a blacklist in the 
                                #team set bool to false
                                good_teams= True
                                
                                
                                for i in range(teamnum):
                                    lengthteamsize = len(Teams[i])
                                    for j in range(lengthteamsize):
                                        for k in range(lengthteamsize):
                                            if(blacklist_list[i][k] == Teams[i][j]):
                            #                   print(Teams[i][k],"HATES", Teams[i][j])
                                                good_teams = False
                            
                            
                                counter+=1
                                
                                if counter == 50:  
                                    break
                            
                            #End of 1 similarity algorithms
                            break
                        
    #                    if user selects Randomization
                        if(option == menu_options+1):
                            counter==0
    
            
                            #Algorithms
                            
                            
                            #use modulus to check if teams are distrubted evenly 
                            #and no person is leftover
                            #use remainder to index in last column
                            remainder = df_rows % minNumGroups
                            
                            #print("Leftover students: " + str(remainder))
                            #print()
                            
                            if remainder == 0:
                                #list of teams
                                Teams = [[] for _ in range(numTeams)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams)]
                            else:
                                #list of teams
                                Teams = [[] for _ in range(numTeams+1)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams+1)]
                            
                            #randomize the df
                            df = df.iloc[np.random.permutation(len(df))]
                            
                            #print random df
                            #print(df)
                            
                            #variables
                            count=0         #to put x amount of students in the list
                            teamnum=0       # num for the team
                            nin = df.columns.get_loc("Name")   #name index number
                            bln = df.columns.get_loc("Blacklist")     # blacklist index number
                            
                            
                            
                            #loop through all df
                            for i in (range(df_rows)):
                            
                                #see group is 3 people
                                if count < minNumGroups:
                                    
                                    if i != df_rows:
                                    #append the blacklis names to the nested lists
                                        blacklist_list[teamnum].append(df.iloc[i, bln])     
                                        Teams[teamnum].append(df.iloc[i, nin]) 
                                        count += 1
                                        
                                #reset for next team, if count == maxsize of group
                                if count == minNumGroups:
                                    teamnum += 1         #go to the next team
                                    count = 0            #reset count to 0, to refill the next team
                                    
                            
                            
                            if(remainder != 0):
                                if(remainder == 1):
                                    Teams[teamnum-1].append(Teams[-1][0])
                                    blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                    
                                elif(remainder >= 2):
                                    while(len(Teams[-1]) != 0):
                                        for i in range(len(Teams)-1):
                                            if(remainder == 0):
                                                break
                                                           
                                            Teams[i].append(Teams[-1][remainder-1])
                                            blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                            del Teams[-1][remainder-1]
                                            remainder = remainder - 1
                                            #print(len(randomTeams[-1]))
                                            
                                del Teams[-1]
                                    
                            
                            
                            
                            #Blacklist
                            
                            #i= team num
                            #j=eachstudent in the team
                            #k=each student in bl
                            
                            #make bool true if teams are good, if there is a blacklist in the 
                            #team set bool to false
                            good_teams= True
                            
                            for i in range(teamnum):
                                lengthteamsize = len(Teams[i])
                                for j in range(lengthteamsize):
                                    for k in range(lengthteamsize):
                                        if(blacklist_list[i][k] == Teams[i][j]):
                            #                print(Teams[i][k],"HATES", Teams[i][j])
                                            good_teams = False
                            
                            counter+=1
                            if counter == 50:  
                                break
                            
                            
                            #this is used for if there is a team that has a blacklist in it        
                            while(good_teams==False):
                                
                                #use modulus to check if teams are distrubted evenly 
                                #and no person is leftover
                                #use remainder to index in last column
                                remainder = df_rows % minNumGroups
                                
                                #print("Leftover students: " + str(remainder))
                                #print()
                                
                                
                                if remainder == 0:
                                    #list of teams
                                    Teams = [[] for _ in range(numTeams)]
                                    #list of blacklists
                                    blacklist_list = [[] for _ in range(numTeams)]
                                else:
                                    #list of teams
                                    Teams = [[] for _ in range(numTeams+1)]
                                    #list of blacklists
                                    blacklist_list = [[] for _ in range(numTeams+1)]
                                
                                #randomize the df
                                df = df.iloc[np.random.permutation(len(df))]
                                
                                #print random df
                                #print(df)
                                
                                #variables
                                count=0         #to put x amount of students in the list
                                teamnum=0       # num for the team
                                nin = df.columns.get_loc("Name")   #name index number
                                bln = df.columns.get_loc("Blacklist")     # blacklist index number
                                
                                
                                
                                #loop through all df
                                for i in (range(df_rows)):
                                
                                    #see group is 3 people
                                    if count < minNumGroups:
                                        
                                        if i != df_rows:
                                        #append the blacklis names to the nested lists
                                            blacklist_list[teamnum].append(df.iloc[i, bln])     
                                            Teams[teamnum].append(df.iloc[i, nin]) 
                                            count += 1
                                            
                                    #reset for next team, if count == maxsize of group
                                    if count == minNumGroups:
                                        teamnum += 1         #go to the next team
                                        count = 0            #reset count to 0, to refill the next team
                                        
                                
                                
                                if(remainder != 0):
                                    if(remainder == 1):
                                        Teams[teamnum-1].append(Teams[-1][0])
                                        blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                        
                                    elif(remainder >= 2):
                                        while(len(Teams[-1]) != 0):
                                            for i in range(len(Teams)-1):
                                                if(remainder == 0):
                                                    break
                                                               
                                                Teams[i].append(Teams[-1][remainder-1])
                                                blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                                del Teams[-1][remainder-1]
                                                remainder = remainder - 1
                                                #print(len(randomTeams[-1]))
                                                
                                    del Teams[-1]
                                        
                                
                                #Blacklist
                                
                                #i= team num
                                #j=eachstudent in the team
                                #k=each student in bl
                                
                                #make bool true if teams are good, if there is a blacklist in the 
                                #team set bool to false
                                good_teams= True
                                
                                for i in (range(teamnum)):
                                    lengthteamsize = len(Teams[i])
                                    for j in range(lengthteamsize):
                                        for k in range(lengthteamsize):
                                            if(blacklist_list[i][k] == Teams[i][j]):
                            #                   print(Teams[i][k],"HATES", Teams[i][j])
                                                good_teams = False
                            
                            
                                counter+=1
                                
    #                            print(counter)
                                if counter == 50: 
                                    break
                            
                            #End algorithms
                            break
#######################End of 1 similarity##############################



############################Option 2 multiple similarities##############
                        
                if(number_choose == 2):
                    while True:
                        
                        menops = len(menuuuu)
                        
                        if menops == 2: 
                            try: 
                                sim_num = int(input("You can choose 2-"+ str(menops)+ " similarities: "))
                                if sim_num == 2 :
                                    break
                                else:
                                    print()
                                    print("Error, please enter 2!")
                                    print()
                            except ValueError: 
                                    print()
                                    print("Please enter a number!")
                                    print()
                           
                        if menops == 3: 
                            try: 
                                sim_num = int(input("You can choose 2-"+ str(menops)+ " similarities: "))
                                if sim_num >1 and sim_num < 4 :
                                    break
                                else:
                                    print()
                                    print("Error, please enter a number from 2-3! ")
                                    print()
                            except ValueError: 
                                    print()
                                    print("Please enter a number!")  
                                    print()
                                    
                                    
                        if menops == 4: 
                            try: 
                                sim_num = int(input("You can choose 2-"+ str(menops)+ " similarities: "))
                                if sim_num >1 and sim_num < 5 :
                                    break
                                else:
                                    print()
                                    print("Error, please enter a number from 2-4! ")
                                    print()
                            except ValueError: 
                                    print()
                                    print("Please enter a number!")
                                    print()
                                    
                        if menops > 4: 
                            try: 
                                sim_num = int(input("You can choose 2-5 similarities: "))
                                if sim_num >1 and sim_num < 6:
                                    break
                                else:
                                    print()
                                    print("Error, please enter a number from 2-5! ")
                                    print()
                            except ValueError: 
                                    print()
                                    print("Please enter a number!")
                                    print()
                                    
                                    
                    if(sim_num == 2):
                        counter=0
                        print()
                        print("Choose one of the following options to sort by:")
                        num = 0
                        non_options = -1
                        for i in col_headers:
                            if(col_headers[num] == "Name" or col_headers[num] == "Blacklist" or col_headers[num] == "Timestamp"):
                                num+=1
                                non_options+=1
                            else:
                                menu_options = num-non_options
                                menu.append(menu_options)
                                print(str(menu_options) + ") Sort by", col_headers[num])
                                num+=1
                                end_list+=1
                        print()
                        while True:
                            try:
                                print("Enter option 1: ", end = " ")
                                option1 = int(input())
                                if option1 > 0 and option1 <= end_list:
                                    break
                                else:
                                    print()
                                    print("Error, please enter a number from the list \nOr do not select the same option!")
                                    print()
                            except ValueError: 
                                print()
                                print("Please enter a number!")
                                print()
                            
                        print()
                        while True:
                            try:
                                print("Enter option 2: ", end = " ")
                                option2 = int(input())
                                if option2 != option1 and option2 > 0 and option2 <= end_list:
                                    break
                                else:
                                    print()
                                    print("Error, please enter a number from the list \nOr do not select the same option!")
                                    print()
                            except ValueError: 
                                print()
                                print("Please enter a number!")
                                print()
                                    
                        print()
                        if(option1 >= start_list and option1 <= end_list and option2 >= start_list and option2 <= end_list):
                            remainder = df_rows % minNumGroups
                                
                                #print("Leftover students: " + str(remainder))
                                #print()
                                
                            if remainder == 0:
                                #list of teams
                                Teams = [[] for _ in range(numTeams)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams)]
                            else:
                                #list of teams
                                Teams = [[] for _ in range(numTeams+1)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams+1)]
                            
                            
                            #print random df
                            #print(df)
                            bigword1 = col_headers[option1]
                            bigword2 = col_headers[option2]
                            #variables
                            count=0         #to put x amount of students in the list
                            teamnum=0       # num for the team
                            nin = df.columns.get_loc("Name")   #name index number
                            bln = df.columns.get_loc("Blacklist")     # blacklist index number
                            df = df.sort_values(by=[bigword1, bigword2])
                            
                            for i in (range(df_rows)):
                                
                                    #see group is 3 people
                                if count < minNumGroups:
                                    
                                    if i != df_rows:
                                    #append the blacklis names to the nested lists
                                        blacklist_list[teamnum].append(df.iloc[i, bln])     
                                        Teams[teamnum].append(df.iloc[i, nin]) 
                                        count += 1
                                        
                                #reset for next team, if count == maxsize of group
                                if count == minNumGroups:
                                    teamnum += 1         #go to the next team
                                    count = 0            #reset count to 0, to refill the next team
                                
                                
                            if(remainder != 0):
                                if(remainder == 1):
                                    Teams[teamnum-1].append(Teams[-1][0])
                                    blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                    
                                elif(remainder >= 2):
                                    while(len(Teams[-1]) != 0):
                                        for i in range(len(Teams)-1):
                                            if(remainder == 0):
                                                break
                                                           
                                            Teams[i].append(Teams[-1][remainder-1])
                                            blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                            del Teams[-1][remainder-1]
                                            remainder = remainder - 1
                                            #print(len(randomTeams[-1]))
                                            
                                del Teams[-1]
                                
                             #Blacklist
                                
                            #i= team num
                            #j=eachstudent in the team
                            #k=each student in bl
                            
                            #make bool true if teams are good, if there is a blacklist in the 
                            #team set bool to false
                            good_teams= True
                            
                            for i in range(teamnum):
                                lengthteamsize = len(Teams[i])
                                for j in range(lengthteamsize):
                                    for k in range(lengthteamsize):
                                        if(blacklist_list[i][k] == Teams[i][j]):
                            #                print(Teams[i][k],"HATES", Teams[i][j])
                                            good_teams = False
                                            
                            counter+=1
                         
                            if counter == 50:
                                break
                            
                            #this is used for if there is a team that has a blacklist in it        
                            while(good_teams==False):
                                
                                #use modulus to check if teams are distrubted evenly 
                                #and no person is leftover
                                #use remainder to index in last column
                                remainder = df_rows % minNumGroups
                                
                                #print("Leftover students: " + str(remainder))
                                #print()
                                
                                
                                if remainder == 0:
                                    #list of teams
                                    Teams = [[] for _ in range(numTeams)]
                                    #list of blacklists
                                    blacklist_list = [[] for _ in range(numTeams)]
                                else:
                                    #list of teams
                                    Teams = [[] for _ in range(numTeams+1)]
                                    #list of blacklists
                                    blacklist_list = [[] for _ in range(numTeams+1)]
                                
                                #randomize the df
                                df = df.iloc[np.random.permutation(len(df))]
                                
                                #print random df
                                #print(df)
                                bigword1 = col_headers[option1]
                                bigword2 = col_headers[option2]
                                #variables
                                count=0         #to put x amount of students in the list
                                teamnum=0       # num for the team
                                nin = df.columns.get_loc("Name")   #name index number
                                bln = df.columns.get_loc("Blacklist")     # blacklist index number
                                
                                df = df.sort_values(by=[bigword1, bigword2])
                                
                                #loop through all df
                                for i in (range(df_rows)):
                                
                                    #see group is 3 people
                                    if count < minNumGroups:
                                        
                                        if i != df_rows:
                                        #append the blacklis names to the nested lists
                                            blacklist_list[teamnum].append(df.iloc[i, bln])     
                                            Teams[teamnum].append(df.iloc[i, nin]) 
                                            count += 1
                                            
                                    #reset for next team, if count == maxsize of group
                                    if count == minNumGroups:
                                        teamnum += 1         #go to the next team
                                        count = 0            #reset count to 0, to refill the next team
                                        
                                
                                
                                if(remainder != 0):
                                    
                                    if(remainder == 1):
                                        
                                        Teams[teamnum-1].append(Teams[-1][0])
                                        
                                        blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                        
                                        
                                        
                                    elif(remainder >= 2):
                                        while(len(Teams[-1]) != 0):
                                            for i in range(len(Teams)-1):
                                                if(remainder == 0):
                                                    break
                                                               
                                                Teams[i].append(Teams[-1][remainder-1])
                                                blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                                del Teams[-1][remainder-1]
                                                remainder = remainder - 1
                                                #print(len(randomTeams[-1]))
                                                
                                    del Teams[-1]
                                        
                                
                                #Blacklist
                                
                                #i= team num
                                #j=eachstudent in the team
                                #k=each student in bl
                                
                                #make bool true if teams are good, if there is a blacklist in the 
                                #team set bool to false
                                good_teams= True
                                
                                for i in range(teamnum):
                                    lengthteamsize = len(Teams[i])
                                    for j in range(lengthteamsize):
                                        for k in range(lengthteamsize):
                                            if(blacklist_list[i][k] == Teams[i][j]):
                            #                   print(Teams[i][k],"HATES", Teams[i][j])
                                                good_teams = False
                        
                                counter+=1
    #                            print(counter)
                               
                                if(counter == 50):   
                                    break
                        
                        
                        
                        #End algorithms
                        break
                        
                    #user wants 3 options sorted similarity ==============================================================
                    if(sim_num == 3): 
                        counter = 0
                        print()
                        print("Choose one of the following options to sort by:")
                        num = 0
                        non_options = -1
                        for i in col_headers:
                            if(col_headers[num] == "Name" or col_headers[num] == "Blacklist" or col_headers[num] == "Timestamp"):
                                num+=1
                                non_options+=1
                            else:
                                menu_options = num-non_options
                                menu.append(menu_options)
                                print(str(menu_options) + ") Sort by", col_headers[num])
                                num+=1
                                end_list+=1
                        
                        print()
                        while True:
                            try:
                                print("Enter option 1: ", end = " ")
                                option1 = int(input())
                                if option1 > 0 and option1 <= end_list:
                                    break
                                else:
                                    print()
                                    print("Error, please enter a number from the list \nOr do not select the same option!")
                                    print()
                            except ValueError: 
                                print()
                                print("Please enter a number!")
                                print()
                            
                        print()
                        while True:
                            try:
                                print("Enter option 2: ", end = " ")
                                option2 = int(input())
                                if option2 != option1 and option2 > 0 and option2 <= end_list:
                                    break
                                else:
                                    print()
                                    print("Error, please enter a number from the list \nOr do not select the same option!")
                                    print()
                            except ValueError: 
                                print()
                                print("Please enter a number!")
                                print()
                        print()
                        while True:
                            try:
                                print("Enter option 3: ", end = " ")
                                option3 = int(input())
                                if option3 != option1 and option3 != option2 and option3 > 0 and option3 <= end_list:
                                    break
                                else:
                                    print()
                                    print("Error, please enter a number from the list \nOr do not select the same option!")
                                    print()
                            except ValueError: 
                                print()
                                print("Please enter a number!")   
                                print()
                                
                        print()
                        if(option1 >= start_list and option1 <= end_list and option2 >= start_list and option2 <= end_list and option3 >= start_list and option3 <= end_list):
                            remainder = df_rows % minNumGroups
                                
                                #print("Leftover students: " + str(remainder))
                                #print()
                                
                            if remainder == 0:
                                #list of teams
                                Teams = [[] for _ in range(numTeams)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams)]
                            else:
                                #list of teams
                                Teams = [[] for _ in range(numTeams+1)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams+1)]
                            
                            
                            #print random df
                            #print(df)
                            bigword1 = col_headers[option1]
                            bigword2 = col_headers[option2]
                            bigword3 = col_headers[option3]
                            
                            #variables
                            count=0         #to put x amount of students in the list
                            teamnum=0       # num for the team
                            nin = df.columns.get_loc("Name")   #name index number
                            bln = df.columns.get_loc("Blacklist")     # blacklist index number
                            df = df.sort_values(by=[bigword1, bigword2, bigword3])
                            
                            for i in (range(df_rows)):
                                
                                    #see group is 3 people
                                if count < minNumGroups:
                                    
                                    if i != df_rows:
                                    #append the blacklis names to the nested lists
                                        blacklist_list[teamnum].append(df.iloc[i, bln])     
                                        Teams[teamnum].append(df.iloc[i, nin]) 
                                        count += 1
                                        
                                #reset for next team, if count == maxsize of group
                                if count == minNumGroups:
                                    teamnum += 1         #go to the next team
                                    count = 0            #reset count to 0, to refill the next team
                                
                                
                            if(remainder != 0):
                                if(remainder == 1):
                                    Teams[teamnum-1].append(Teams[-1][0])
                                    blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                    
                                elif(remainder >= 2):
                                    while(len(Teams[-1]) != 0):
                                        for i in range(len(Teams)-1):
                                            if(remainder == 0):
                                                break
                                                           
                                            Teams[i].append(Teams[-1][remainder-1])
                                            blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                            del Teams[-1][remainder-1]
                                            remainder = remainder - 1
                                            #print(len(randomTeams[-1]))
                                            
                                del Teams[-1]
                                
                             #Blacklist
                                
                            #i= team num
                            #j=eachstudent in the team
                            #k=each student in bl
                            
                            #make bool true if teams are good, if there is a blacklist in the 
                            #team set bool to false
                            good_teams= True
                            
                            for i in range(teamnum):
                                lengthteamsize = len(Teams[i])
                                for j in range(lengthteamsize):
                                    for k in range(lengthteamsize):
                                        if(blacklist_list[i][k] == Teams[i][j]):
                            #                print(Teams[i][k],"HATES", Teams[i][j])
                                            good_teams = False
                                            
                            counter+=1
                       
                            if counter == 50:  
                                break
                            
                            #this is used for if there is a team that has a blacklist in it        
                            while(good_teams==False):
                                
                                #use modulus to check if teams are distrubted evenly 
                                #and no person is leftover
                                #use remainder to index in last column
                                remainder = df_rows % minNumGroups
                                
                                #print("Leftover students: " + str(remainder))
                                #print()
                                
                                
                                if remainder == 0:
                                    #list of teams
                                    Teams = [[] for _ in range(numTeams)]
                                    #list of blacklists
                                    blacklist_list = [[] for _ in range(numTeams)]
                                else:
                                    #list of teams
                                    Teams = [[] for _ in range(numTeams+1)]
                                    #list of blacklists
                                    blacklist_list = [[] for _ in range(numTeams+1)]
                                
                                #randomize the df
                                df = df.iloc[np.random.permutation(len(df))]
                                
                                #print random df
                                #print(df)
                                bigword1 = col_headers[option1]
                                bigword2 = col_headers[option2]
                                bigword3 = col_headers[option3]
                                #variables
                                count=0         #to put x amount of students in the list
                                teamnum=0       # num for the team
                                nin = df.columns.get_loc("Name")   #name index number
                                bln = df.columns.get_loc("Blacklist")     # blacklist index number
                                
                                df = df.sort_values(by=[bigword1, bigword2, bigword3])
                                
                                #loop through all df
                                for i in (range(df_rows)):
                                
                                    #see group is 3 people
                                    if count < minNumGroups:
                                        
                                        if i != df_rows:
                                        #append the blacklis names to the nested lists
                                            blacklist_list[teamnum].append(df.iloc[i, bln])     
                                            Teams[teamnum].append(df.iloc[i, nin]) 
                                            count += 1
                                            
                                    #reset for next team, if count == maxsize of group
                                    if count == minNumGroups:
                                        teamnum += 1         #go to the next team
                                        count = 0            #reset count to 0, to refill the next team
                                        
                                
                                
                                if(remainder != 0):
                                    
                                    if(remainder == 1):
                                        
                                        Teams[teamnum-1].append(Teams[-1][0])
                                        
                                        blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                        
                                        
                                        
                                    elif(remainder >= 2):
                                        while(len(Teams[-1]) != 0):
                                            for i in range(len(Teams)-1):
                                                if(remainder == 0):
                                                    break
                                                               
                                                Teams[i].append(Teams[-1][remainder-1])
                                                blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                                del Teams[-1][remainder-1]
                                                remainder = remainder - 1
                                                #print(len(randomTeams[-1]))
                                                
                                    del Teams[-1]
                                        
                                
                                #Blacklist
                                
                                #i= team num
                                #j=eachstudent in the team
                                #k=each student in bl
                                
                                #make bool true if teams are good, if there is a blacklist in the 
                                #team set bool to false
                                good_teams= True
                                
                                
                                if counter_for_something == 0 :
                                 
                                    counter_for_something+=1
                                    
                                for i in (range(teamnum)):
                                    lengthteamsize = len(Teams[i])
                                    for j in range(lengthteamsize):
                                        for k in range(lengthteamsize):
                                            if(blacklist_list[i][k] == Teams[i][j]):
                            #                   print(Teams[i][k],"HATES", Teams[i][j])
                                                good_teams = False
                                                
                        
                        
                                counter+=1
    #                            print(counter)
                       
                                if(counter == 50):
                                    break
                            
                        
    
                        
                        #End algorithms
                        break
                        
                    
                    #user wants 4 selections ##########################################################################
                    if(sim_num == 4):
                        counter = 0
                        print()
                        print("Choose one of the following options to sort by:")
                        num = 0
                        non_options = -1
                        for i in col_headers:
                            if(col_headers[num] == "Name" or col_headers[num] == "Blacklist" or col_headers[num] == "Timestamp"):
                                num+=1
                                non_options+=1
                            else:
                                menu_options = num-non_options
                                menu.append(menu_options)
                                print(str(menu_options) + ") Sort by", col_headers[num])
                                num+=1
                                end_list+=1
                        
    
                        print()
                        while True:
                            try:
                                print("Enter option 1: ", end = " ")
                                option1 = int(input())
                                if option1 > 0 and option1 <= end_list:
                                    break
                                else:
                                    print()
                                    print("Error, please enter a number from the list \nOr do not select the same option!")
                                    print()
                            except ValueError: 
                                print()
                                print("Please enter a number!")
                                print()
                            
                        print()
                        while True:
                            try:
                                print("Enter option 2: ", end = " ")
                                option2 = int(input())
                                if option2 != option1 and option2 > 0 and option2 <= end_list:
                                    break
                                else:
                                    print()
                                    print("Error, please enter a number from the list \nOr do not select the same option!")
                                    print()
                            except ValueError: 
                                print()
                                print("Please enter a number!")
                        print()
                        while True:
                            try:
                                print("Enter option 3: ", end = " ")
                                option3 = int(input())
                                if option3 != option1 and option3 != option2 and option3 > 0 and option3 <= end_list:
                                    break
                                else:
                                    print()
                                    print("Error, please enter a number from the list \nOr do not select the same option!")
                                    print()
                            except ValueError: 
                                print()
                                print("Please enter a number!") 
                        print()
                        while True:
                            try:
                                print("Enter option 4: ", end = " ")
                                option4 = int(input())
                                if option4 != option1 and option4 != option2 and option4 != option3 and option4 > 0 and option4 <= end_list:
                                    break
                                else:
                                    print()
                                    print("Error, please enter a number from the list \nOr do not select the same option!")
                                    print()
                            except ValueError: 
                                print()
                                print("Please enter a number!") 
                                print()
                        
                                
                        if(option1 >= start_list and option1 <= end_list and option2 >= start_list and option2 <= end_list and option3 >= start_list and option3 <= end_list and option4 >= start_list and option4 <= end_list):
                            remainder = df_rows % minNumGroups
                                
                                #print("Leftover students: " + str(remainder))
                                #print()
                                
                            if remainder == 0:
                                #list of teams
                                Teams = [[] for _ in range(numTeams)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams)]
                            else:
                                #list of teams
                                Teams = [[] for _ in range(numTeams+1)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams+1)]
                            
                            
                            #print random df
                            #print(df)
                            bigword1 = col_headers[option1]
                            bigword2 = col_headers[option2]
                            bigword3 = col_headers[option3]
                            bigword4 = col_headers[option4]
                            #variables
                            count=0         #to put x amount of students in the list
                            teamnum=0       # num for the team
                            nin = df.columns.get_loc("Name")   #name index number
                            bln = df.columns.get_loc("Blacklist")     # blacklist index number
                            df = df.sort_values(by=[bigword1, bigword2, bigword3, bigword4])
                            
                            for i in (range(df_rows)):
                                
                                    #see group is 3 people
                                if count < minNumGroups:
                                    
                                    if i != df_rows:
                                    #append the blacklis names to the nested lists
                                        blacklist_list[teamnum].append(df.iloc[i, bln])     
                                        Teams[teamnum].append(df.iloc[i, nin]) 
                                        count += 1
                                        
                                #reset for next team, if count == maxsize of group
                                if count == minNumGroups:
                                    teamnum += 1         #go to the next team
                                    count = 0            #reset count to 0, to refill the next team
                                
                                
                            if(remainder != 0):
                                if(remainder == 1):
                                    Teams[teamnum-1].append(Teams[-1][0])
                                    blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                    
                                elif(remainder >= 2):
                                    while(len(Teams[-1]) != 0):
                                        for i in range(len(Teams)-1):
                                            if(remainder == 0):
                                                break
                                                           
                                            Teams[i].append(Teams[-1][remainder-1])
                                            blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                            del Teams[-1][remainder-1]
                                            remainder = remainder - 1
                                            #print(len(randomTeams[-1]))
                                            
                                del Teams[-1]
                                
                             #Blacklist
                                
                            #i= team num
                            #j=eachstudent in the team
                            #k=each student in bl
                            
                            #make bool true if teams are good, if there is a blacklist in the 
                            #team set bool to false
                            good_teams= True
                            
                            for i in range(teamnum):
                                lengthteamsize = len(Teams[i])
                                for j in range(lengthteamsize):
                                    for k in range(lengthteamsize):
                                        if(blacklist_list[i][k] == Teams[i][j]):
                            #                print(Teams[i][k],"HATES", Teams[i][j])
                                            good_teams = False
                                            
                            counter+=1
                        
                            if counter == 50:    
                                break
                            
                            #this is used for if there is a team that has a blacklist in it        
                            while(good_teams==False):
                                
                                #use modulus to check if teams are distrubted evenly 
                                #and no person is leftover
                                #use remainder to index in last column
                                remainder = df_rows % minNumGroups
                                
                                #print("Leftover students: " + str(remainder))
                                #print()
                                
                                
                                if remainder == 0:
                                    #list of teams
                                    Teams = [[] for _ in range(numTeams)]
                                    #list of blacklists
                                    blacklist_list = [[] for _ in range(numTeams)]
                                else:
                                    #list of teams
                                    Teams = [[] for _ in range(numTeams+1)]
                                    #list of blacklists
                                    blacklist_list = [[] for _ in range(numTeams+1)]
                                
                                #randomize the df
                                df = df.iloc[np.random.permutation(len(df))]
                                
                                #print random df
                                #print(df)
                                bigword1 = col_headers[option1]
                                bigword2 = col_headers[option2]
                                bigword3 = col_headers[option3]
                                bigword4 = col_headers[option4]
                                #variables
                                count=0         #to put x amount of students in the list
                                teamnum=0       # num for the team
                                nin = df.columns.get_loc("Name")   #name index number
                                bln = df.columns.get_loc("Blacklist")     # blacklist index number
                                
                                df = df.sort_values(by=[bigword1, bigword2, bigword3, bigword4])
                                
                                #loop through all df
                                for i in (range(df_rows)):
                                
                                    #see group is 3 people
                                    if count < minNumGroups:
                                        
                                        if i != df_rows:
                                        #append the blacklis names to the nested lists
                                            blacklist_list[teamnum].append(df.iloc[i, bln])     
                                            Teams[teamnum].append(df.iloc[i, nin]) 
                                            count += 1
                                            
                                    #reset for next team, if count == maxsize of group
                                    if count == minNumGroups:
                                        teamnum += 1         #go to the next team
                                        count = 0            #reset count to 0, to refill the next team
                                        
                                
                                
                                if(remainder != 0):
                                    
                                    if(remainder == 1):
                                        
                                        Teams[teamnum-1].append(Teams[-1][0])
                                        
                                        blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                        
                                        
                                        
                                    elif(remainder >= 2):
                                        while(len(Teams[-1]) != 0):
                                            for i in range(len(Teams)-1):
                                                if(remainder == 0):
                                                    break
                                                               
                                                Teams[i].append(Teams[-1][remainder-1])
                                                blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                                del Teams[-1][remainder-1]
                                                remainder = remainder - 1
                                                #print(len(randomTeams[-1]))
                                                
                                    del Teams[-1]
                                        
                                
                                #Blacklist
                                
                                #i= team num
                                #j=eachstudent in the team
                                #k=each student in bl
                                
                                #make bool true if teams are good, if there is a blacklist in the 
                                #team set bool to false
                                good_teams= True
                                
                                for i in range(teamnum):
                                    lengthteamsize = len(Teams[i])
                                    for j in range(lengthteamsize):
                                        for k in range(lengthteamsize):
                                            if(blacklist_list[i][k] == Teams[i][j]):
                            #                   print(Teams[i][k],"HATES", Teams[i][j])
                                                good_teams = False
                        
                        
                                counter+=1
                              
                                if(counter == 50):  
                                    break
                            
                        
    
                        
                        #End algorithms
                        break
                        # 5 options ++++++++))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
                    if(sim_num == 5):
                        counter = 0
                        print()
                        print("Choose one of the following options to sort by:")
                        num = 0
                        non_options = -1
                        for i in col_headers:
                            if(col_headers[num] == "Name" or col_headers[num] == "Blacklist" or col_headers[num] == "Timestamp"):
                                num+=1
                                non_options+=1
                            else:
                                menu_options = num-non_options
                                menu.append(menu_options)
                                print(str(menu_options) + ") Sort by", col_headers[num])
                                num+=1
                                end_list+=1
                        
    
                        print()
                        while True:
                            try:
                                print("Enter option 1: ", end = " ")
                                option1 = int(input())
                                if option1 > 0 and option1 <= end_list:
                                    break
                                else:
                                    print()
                                    print("Error, please enter a number from the list \nOr do not select the same option!")
                                    print()
                            except ValueError: 
                                print()
                                print("Please enter a number!")
                                print()
                            
                        print()
                        while True:
                            try:
                                print("Enter option 2: ", end = " ")
                                option2 = int(input())
                                if option2 != option1 and option2 > 0 and option2 <= end_list:
                                    break
                                else:
                                    print()
                                    print("Error, please enter a number from the list \nOr do not select the same option!")
                                    print()
                            except ValueError: 
                                print()
                                print("Please enter a number!")
                                print()
                        print()
                        while True:
                            try:
                                print("Enter option 3: ", end = " ")
                                option3 = int(input())
                                if option3 != option1 and option3 != option2 and option3 > 0 and option3 <= end_list:
                                    break
                                else:
                                    print()
                                    print("Error, please enter a number from the list \nOr do not select the same option!")
                                    print()
                            except ValueError: 
                                print()
                                print("Please enter a number!") 
                                print()
                        print()
                        while True:
                            try:
                                print("Enter option 4: ", end = " ")
                                option4 = int(input())
                                if option4 != option1 and option4 != option2 and option4 != option3 and option4 > 0 and option4 <= end_list:
                                    break
                                else:
                                    print()
                                    print("Error, please enter a number from the list \nOr do not select the same option!")
                                    print()
                            except ValueError: 
                                print()
                                print("Please enter a number!") 
                                print()
                        print()
                        while True:
                            try:
                                print("Enter option 5: ", end = " ")
                                option5 = int(input())
                                if option5 != option1 and option5 != option2 and option5 != option3 and option5 != option4 and option5 > 0 and option5 <= end_list:
                                    break
                                else:
                                    print()
                                    print("Error, please enter a number from the list \nOr do not select the same option!")
                                    print()
                            except ValueError: 
                                print()
                                print("Please enter a number!") 
                                print()
                                
                        print()
                        if(option1 >= start_list and option1 <= end_list and option2 >= start_list and option2 <= end_list and option3 >= start_list and option3 <= end_list and option4 >= start_list and option4 <= end_list and option5 >= start_list and option5 <= end_list):
                            remainder = df_rows % minNumGroups
                                
                                #print("Leftover students: " + str(remainder))
                                #print()
                                
                            if remainder == 0:
                                #list of teams
                                Teams = [[] for _ in range(numTeams)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams)]
                            else:
                                #list of teams
                                Teams = [[] for _ in range(numTeams+1)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams+1)]
                            
                            
                            #print random df
                            #print(df)
                            bigword1 = col_headers[option1]
                            bigword2 = col_headers[option2]
                            bigword3 = col_headers[option3]
                            bigword4 = col_headers[option4]
                            bigword5 = col_headers[option5]
                            #variables
                            count=0         #to put x amount of students in the list
                            teamnum=0       # num for the team
                            nin = df.columns.get_loc("Name")   #name index number
                            bln = df.columns.get_loc("Blacklist")     # blacklist index number
                            df = df.sort_values(by=[bigword1, bigword2, bigword3, bigword4, bigword5])
                            
                            for i in (range(df_rows)):
                                
                                    #see group is 3 people
                                if count < minNumGroups:
                                    
                                    if i != df_rows:
                                    #append the blacklis names to the nested lists
                                        blacklist_list[teamnum].append(df.iloc[i, bln])     
                                        Teams[teamnum].append(df.iloc[i, nin]) 
                                        count += 1
                                        
                                #reset for next team, if count == maxsize of group
                                if count == minNumGroups:
                                    teamnum += 1         #go to the next team
                                    count = 0            #reset count to 0, to refill the next team
                                
                                
                            if(remainder != 0):
                                if(remainder == 1):
                                    Teams[teamnum-1].append(Teams[-1][0])
                                    blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                    
                                elif(remainder >= 2):
                                    while(len(Teams[-1]) != 0):
                                        for i in range(len(Teams)-1):
                                            if(remainder == 0):
                                                break
                                                           
                                            Teams[i].append(Teams[-1][remainder-1])
                                            blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                            del Teams[-1][remainder-1]
                                            remainder = remainder - 1
                                            #print(len(randomTeams[-1]))
                                            
                                del Teams[-1]
                                
                             #Blacklist
                                
                            #i= team num
                            #j=eachstudent in the team
                            #k=each student in bl
                            
                            #make bool true if teams are good, if there is a blacklist in the 
                            #team set bool to false
                            good_teams= True
                            
                            for i in range(teamnum):
                                lengthteamsize = len(Teams[i])
                                for j in range(lengthteamsize):
                                    for k in range(lengthteamsize):
                                        if(blacklist_list[i][k] == Teams[i][j]):
                            #                print(Teams[i][k],"HATES", Teams[i][j])
                                            good_teams = False
                                            
                                            
                            counter+=1
                            
                            if counter == 50:   
                                break
                            
                            #this is used for if there is a team that has a blacklist in it        
                            while(good_teams==False):
                                
                                #use modulus to check if teams are distrubted evenly 
                                #and no person is leftover
                                #use remainder to index in last column
                                remainder = df_rows % minNumGroups
                                
                                #print("Leftover students: " + str(remainder))
                                #print()
                                
                                
                                if remainder == 0:
                                    #list of teams
                                    Teams = [[] for _ in range(numTeams)]
                                    #list of blacklists
                                    blacklist_list = [[] for _ in range(numTeams)]
                                else:
                                    #list of teams
                                    Teams = [[] for _ in range(numTeams+1)]
                                    #list of blacklists
                                    blacklist_list = [[] for _ in range(numTeams+1)]
                                
                                #randomize the df
                                df = df.iloc[np.random.permutation(len(df))]
                                
                                #print random df
                                #print(df)
                                
                                bigword1 = col_headers[option1]
                                bigword2 = col_headers[option2]
                                bigword3 = col_headers[option3]
                                bigword4 = col_headers[option4]
                                bigword5 = col_headers[option5]
                                #variables
                                count=0         #to put x amount of students in the list
                                teamnum=0       # num for the team
                                nin = df.columns.get_loc("Name")   #name index number
                                bln = df.columns.get_loc("Blacklist")     # blacklist index number
                                
                                df = df.sort_values(by=[bigword1, bigword2, bigword3, bigword4, bigword5])
                                
                                #loop through all df
                                for i in (range(df_rows)):
                                
                                    #see group is 3 people
                                    if count < minNumGroups:
                                        
                                        if i != df_rows:
                                        #append the blacklis names to the nested lists
                                            blacklist_list[teamnum].append(df.iloc[i, bln])     
                                            Teams[teamnum].append(df.iloc[i, nin]) 
                                            count += 1
                                            
                                    #reset for next team, if count == maxsize of group
                                    if count == minNumGroups:
                                        teamnum += 1         #go to the next team
                                        count = 0            #reset count to 0, to refill the next team
                                        
                                
                                
                                if(remainder != 0):
                                    
                                    if(remainder == 1):
                                        
                                        Teams[teamnum-1].append(Teams[-1][0])
                                        
                                        blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                        
                                        
                                        
                                    elif(remainder >= 2):
                                        while(len(Teams[-1]) != 0):
                                            for i in range(len(Teams)-1):
                                                if(remainder == 0):
                                                    break
                                                               
                                                Teams[i].append(Teams[-1][remainder-1])
                                                blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                                del Teams[-1][remainder-1]
                                                remainder = remainder - 1
                                                #print(len(randomTeams[-1]))
                                                
                                    del Teams[-1]
                                        
                                
                                #Blacklist
                                
                                #i= team num
                                #j=eachstudent in the team
                                #k=each student in bl
                                
                                #make bool true if teams are good, if there is a blacklist in the 
                                #team set bool to false
                                good_teams= True
                                
                                for i in range(teamnum):
                                    lengthteamsize = len(Teams[i])
                                    for j in range(lengthteamsize):
                                        for k in range(lengthteamsize):
                                            if(blacklist_list[i][k] == Teams[i][j]):
                            #                   print(Teams[i][k],"HATES", Teams[i][j])
                                                good_teams = False
                        
                        
                                counter+=1
                                
                                if(counter == 50):  
                                    break
                            
                        
    
                        
                        #End algorithms
                        break
                        
                    break
########Start of differences##########

#                #user wants only 3 option
#                if(number_choose == 3):
#                    counter=0
#                    #make menu
#                    print()
#                    print("Choose one of the following options to sort by:")
#                    num = 0
#                    non_options = -1
#                    for i in col_headers:
#                        #might have to change
#                        if(col_headers[num] == "Name" or col_headers[num] == "Age" or col_headers[num] == "Blacklist" or col_headers[num] == "Timestamp"):
#                            num+=1
#                            non_options+=1
#                        else:
#                            menu_options = num-non_options
#                            menu.append(menu_options)
#                            print(str(menu_options) + ") Sort by", col_headers[num])
#                            num+=1
#                            end_list+=1
#                    end_list+=1
#                    print(str(menu_options+1) + ") Sort by Randomization")
#                    print()
#                    
#                    while True:
#                        try:
#                            print("Enter your option: ", end = " ")
#                            option = int(input())
#                            if option >= start_list and option <= end_list:
#                                break
#                            else:
#                                print("Error")
#                        except ValueError: 
#                            print("Please enter a number!")
#                            
#                    if(option >= start_list and option <= end_list):
#                         
#                        #user selects anything but Randomization
#                        if(option < menu_options+1):
#                            #print("Would you like to sort by similarities or differences? (type similarity/difference)")
#                            
#                            
#                            #Algorithms
#                            
#                            
#                            #use modulus to check if teams are distrubted evenly 
#                            #and no person is leftover
#                            #use remainder to index in last column
#                            remainder = df_rows % minNumGroups
#                            
#                            #print("Leftover students: " + str(remainder))
#                            #print()
#                            
#                            if remainder == 0:
#                                #list of teams
#                                Teams = [[] for _ in range(numTeams)]
#                                #list of blacklists
#                                blacklist_list = [[] for _ in range(numTeams)]
#                            else:
#                                #list of teams
#                                Teams = [[] for _ in range(numTeams+1)]
#                                #list of blacklists
#                                blacklist_list = [[] for _ in range(numTeams+1)]
#                            
#                            
#                            #print random df
#                            #print(df)
#                            bigword = col_headers[option]
#                            #variables
#                            count=0         #to put x amount of students in the list
#                            teamnum=0       # num for the team
#                            nin = df.columns.get_loc("Name")   #name index number
#                            bln = df.columns.get_loc("Blacklist")     # blacklist index number
#                            df = df.sort_values(by=[bigword])
#                            
#                            
#                            #loop through all df
#                            for i in (range(df_rows)):
#                            
#                                #see group is 3 people
#                                if count < minNumGroups:
#                                    
#                                    if i != df_rows:
#                                    #append the blacklis names to the nested lists
#                                        blacklist_list[teamnum].append(df.iloc[i, bln])     
#                                        Teams[teamnum].append(df.iloc[i, nin]) 
#                                        count += 1
#                                        
#                                #reset for next team, if count == maxsize of group
#                                if count == minNumGroups:
#                                    teamnum += 1         #go to the next team
#                                    count = 0            #reset count to 0, to refill the next team
#                                    
#                            
#                            
#                            if(remainder != 0):
#                                if(remainder == 1):
#                                    Teams[teamnum-1].append(Teams[-1][0])
#                                    blacklist_list[teamnum-1].append(blacklist_list[-1][0])
#                                    
#                                elif(remainder >= 2):
#                                    while(len(Teams[-1]) != 0):
#                                        for i in range(len(Teams)-1):
#                                            if(remainder == 0):
#                                                break
#                                                           
#                                            Teams[i].append(Teams[-1][remainder-1])
#                                            blacklist_list[i].append(blacklist_list[-1][remainder-1])
#                                            del Teams[-1][remainder-1]
#                                            remainder = remainder - 1
#                                            #print(len(randomTeams[-1]))
#                                            
#                                del Teams[-1]
#                                    
#                            
#                            
#                            
#                            #Blacklist
#                            
#                            #i= team num
#                            #j=eachstudent in the team
#                            #k=each student in bl
#                            
#                            #make bool true if teams are good, if there is a blacklist in the 
#                            #team set bool to false
#                            good_teams= True
#                            
#                            for i in range(teamnum):
#                                lengthteamsize = len(Teams[i])
#                                for j in range(lengthteamsize):
#                                    for k in range(lengthteamsize):
#                                        if(blacklist_list[i][k] == Teams[i][j]):
#                            #                print(Teams[i][k],"HATES", Teams[i][j])
#                                            good_teams = False
#                            
#                            counter+=1
#                            
#                            if counter == 50:   
#                                break
#                            
#                            
#                            #this is used for if there is a team that has a blacklist in it        
#                            while(good_teams==False):
#                                
#                                #use modulus to check if teams are distrubted evenly 
#                                #and no person is leftover
#                                #use remainder to index in last column
#                                remainder = df_rows % minNumGroups
#                                
#                                #print("Leftover students: " + str(remainder))
#                                #print()
#                                
#                                
#                                if remainder == 0:
#                                    #list of teams
#                                    Teams = [[] for _ in range(numTeams)]
#                                    #list of blacklists
#                                    blacklist_list = [[] for _ in range(numTeams)]
#                                else:
#                                    #list of teams
#                                    Teams = [[] for _ in range(numTeams+1)]
#                                    #list of blacklists
#                                    blacklist_list = [[] for _ in range(numTeams+1)]
#                                
#                                #randomize the df
#                                df = df.iloc[np.random.permutation(len(df))]
#                                
#                                #print random df
#                                #print(df)
#                                bigword = col_headers[option]
#                                #variables
#                                count=0         #to put x amount of students in the list
#                                teamnum=0       # num for the team
#                                nin = df.columns.get_loc("Name")   #name index number
#                                bln = df.columns.get_loc("Blacklist")     # blacklist index number
#                                
#########################Sorts column in dataframe##########
#                                df = df.sort_values(by=[bigword])
#                                
#                                #loop through all df
#                                for i in (range(df_rows)):
#                                
#                                    #see group is 3 people
#                                    if count < minNumGroups:
#                                        
#                                        if i != df_rows:
#                                        #append the blacklis names to the nested lists
#                                            blacklist_list[teamnum].append(df.iloc[i, bln])     
#                                            Teams[teamnum].append(df.iloc[i, nin]) 
#                                            count += 1
#                                            
#                                    #reset for next team, if count == maxsize of group
#                                    if count == minNumGroups:
#                                        teamnum += 1         #go to the next team
#                                        count = 0            #reset count to 0, to refill the next team
#                                        
#                                
#                                
#                                if(remainder != 0):
#                                    
#                                    if(remainder == 1):
#                                        
#                                        Teams[0].append(Teams[-1][0])
#                                        
#                                        blacklist_list[0].append(blacklist_list[-1][0])
#                                        
#                                        
#                                        
#                                    elif(remainder >= 2):
#                                        while(len(Teams[-1]) != 0):
#                                            for i in range(len(Teams)-1):
#                                                if(remainder == 0):
#                                                    break
#                                                               
#                                                Teams[i].append(Teams[-1][remainder-1])
#                                                blacklist_list[i].append(blacklist_list[-1][remainder-1])
#                                                del Teams[-1][remainder-1]
#                                                remainder = remainder - 1
#                                                #print(len(randomTeams[-1]))
#                                                
#                                    del Teams[-1]
#                                        
#                                
#                                #Blacklist
#                                
#                                #i= team num
#                                #j=eachstudent in the team
#                                #k=each student in bl
#                                
#                                #make bool true if teams are good, if there is a blacklist in the 
#                                #team set bool to false
#                                good_teams= True
#                                
#                                
#                                for i in range(teamnum):
#                                    lengthteamsize = len(Teams[i])
#                                    for j in range(lengthteamsize):
#                                        for k in range(lengthteamsize):
#                                            if(blacklist_list[i][k] == Teams[i][j]):
#                            #                   print(Teams[i][k],"HATES", Teams[i][j])
#                                                good_teams = False
#                            
#                            
#                                counter+=1
#                                
#                                if counter == 50:   
#                                    break
#                            
#                            #End of 1 similarity algorithms
#                            break
#                        
#    #                    if user selects Randomization
#                        if(option == menu_options+1):
#                            counter==0
#    
#            
#                            #Algorithms
#                            
#                            
#                            #use modulus to check if teams are distrubted evenly 
#                            #and no person is leftover
#                            #use remainder to index in last column
#                            remainder = df_rows % minNumGroups
#                            
#                            #print("Leftover students: " + str(remainder))
#                            #print()
#                            
#                            if remainder == 0:
#                                #list of teams
#                                Teams = [[] for _ in range(numTeams)]
#                                #list of blacklists
#                                blacklist_list = [[] for _ in range(numTeams)]
#                            else:
#                                #list of teams
#                                Teams = [[] for _ in range(numTeams+1)]
#                                #list of blacklists
#                                blacklist_list = [[] for _ in range(numTeams+1)]
#                            
#                            #randomize the df
#                            df = df.iloc[np.random.permutation(len(df))]
#                            
#                            #print random df
#                            #print(df)
#                            
#                            #variables
#                            count=0         #to put x amount of students in the list
#                            teamnum=0       # num for the team
#                            nin = df.columns.get_loc("Name")   #name index number
#                            bln = df.columns.get_loc("Blacklist")     # blacklist index number
#                            
#                            
#                            
#                            #loop through all df
#                            for i in (range(df_rows)):
#                            
#                                #see group is 3 people
#                                if count < minNumGroups:
#                                    
#                                    if i != df_rows:
#                                    #append the blacklis names to the nested lists
#                                        blacklist_list[teamnum].append(df.iloc[i, bln])     
#                                        Teams[teamnum].append(df.iloc[i, nin]) 
#                                        count += 1
#                                        
#                                #reset for next team, if count == maxsize of group
#                                if count == minNumGroups:
#                                    teamnum += 1         #go to the next team
#                                    count = 0            #reset count to 0, to refill the next team
#                                    
#                            
#                            
#                            if(remainder != 0):
#                                if(remainder == 1):
#                                    Teams[teamnum-1].append(Teams[-1][0])
#                                    blacklist_list[teamnum-1].append(blacklist_list[-1][0])
#                                    
#                                elif(remainder >= 2):
#                                    while(len(Teams[-1]) != 0):
#                                        for i in range(len(Teams)-1):
#                                            if(remainder == 0):
#                                                break
#                                                           
#                                            Teams[i].append(Teams[-1][remainder-1])
#                                            blacklist_list[i].append(blacklist_list[-1][remainder-1])
#                                            del Teams[-1][remainder-1]
#                                            remainder = remainder - 1
#                                            #print(len(randomTeams[-1]))
#                                            
#                                del Teams[-1]
#                                    
#                            
#                            
#                            
#                            #Blacklist
#                            
#                            #i= team num
#                            #j=eachstudent in the team
#                            #k=each student in bl
#                            
#                            #make bool true if teams are good, if there is a blacklist in the 
#                            #team set bool to false
#                            good_teams= True
#                            
#                            for i in range(teamnum):
#                                lengthteamsize = len(Teams[i])
#                                for j in range(lengthteamsize):
#                                    for k in range(lengthteamsize):
#                                        if(blacklist_list[i][k] == Teams[i][j]):
#                            #                print(Teams[i][k],"HATES", Teams[i][j])
#                                            good_teams = False
#                            
#                            counter+=1
#                            if counter == 50:  
#                                break
#                            
#                            
#                            #this is used for if there is a team that has a blacklist in it        
#                            while(good_teams==False):
#                                
#                                #use modulus to check if teams are distrubted evenly 
#                                #and no person is leftover
#                                #use remainder to index in last column
#                                remainder = df_rows % minNumGroups
#                                
#                                #print("Leftover students: " + str(remainder))
#                                #print()
#                                
#                                
#                                if remainder == 0:
#                                    #list of teams
#                                    Teams = [[] for _ in range(numTeams)]
#                                    #list of blacklists
#                                    blacklist_list = [[] for _ in range(numTeams)]
#                                else:
#                                    #list of teams
#                                    Teams = [[] for _ in range(numTeams+1)]
#                                    #list of blacklists
#                                    blacklist_list = [[] for _ in range(numTeams+1)]
#                                
#                                #randomize the df
#                                df = df.iloc[np.random.permutation(len(df))]
#                                
#                                #print random df
#                                #print(df)
#                                
#                                #variables
#                                count=0         #to put x amount of students in the list
#                                teamnum=0       # num for the team
#                                nin = df.columns.get_loc("Name")   #name index number
#                                bln = df.columns.get_loc("Blacklist")     # blacklist index number
#                                
#                                
#                                
#                                #loop through all df
#                                for i in (range(df_rows)):
#                                
#                                    #see group is 3 people
#                                    if count < minNumGroups:
#                                        
#                                        if i != df_rows:
#                                        #append the blacklis names to the nested lists
#                                            blacklist_list[teamnum].append(df.iloc[i, bln])     
#                                            Teams[teamnum].append(df.iloc[i, nin]) 
#                                            count += 1
#                                            
#                                    #reset for next team, if count == maxsize of group
#                                    if count == minNumGroups:
#                                        teamnum += 1         #go to the next team
#                                        count = 0            #reset count to 0, to refill the next team
#                                        
#                                
#                                
#                                if(remainder != 0):
#                                    if(remainder == 1):
#                                        Teams[teamnum-1].append(Teams[-1][0])
#                                        blacklist_list[teamnum-1].append(blacklist_list[-1][0])
#                                        
#                                    elif(remainder >= 2):
#                                        while(len(Teams[-1]) != 0):
#                                            for i in range(len(Teams)-1):
#                                                if(remainder == 0):
#                                                    break
#                                                               
#                                                Teams[i].append(Teams[-1][remainder-1])
#                                                blacklist_list[i].append(blacklist_list[-1][remainder-1])
#                                                del Teams[-1][remainder-1]
#                                                remainder = remainder - 1
#                                                #print(len(randomTeams[-1]))
#                                                
#                                    del Teams[-1]
#                                        
#                                
#                                #Blacklist
#                                
#                                #i= team num
#                                #j=eachstudent in the team
#                                #k=each student in bl
#                                
#                                #make bool true if teams are good, if there is a blacklist in the 
#                                #team set bool to false
#                                good_teams= True
#                                
#                                for i in (range(teamnum)):
#                                    lengthteamsize = len(Teams[i])
#                                    for j in range(lengthteamsize):
#                                        for k in range(lengthteamsize):
#                                            if(blacklist_list[i][k] == Teams[i][j]):
#                            #                   print(Teams[i][k],"HATES", Teams[i][j])
#                                                good_teams = False
#                            
#                            
#                                counter+=1
#                                
#    #                            print(counter)
#                                if counter == 50:  
#                                    break
#                            
#                            #End algorithms
#                            break


######End of Difference algorithm#######
                
                
                
                
                

                        
                                                 #%%

            #if the user wants 2 terms
            if(terms == 2):
                newFlag = True
                counter=0
                #make menu
                print()
                print("Choose one of the following options to sort by:")
                num = 0
                non_options = -1
                for i in col_headers:
                    #might have to change
                    if(col_headers[num] == "Name" or col_headers[num] == "Blacklist" or col_headers[num] == "Timestamp"):
                        num+=1
                        non_options+=1
                    else:
                        menu_options = num-non_options
                        menu.append(menu_options)
                        print(str(menu_options) + ") Sort by", col_headers[num])
                        num+=1
                        end_list+=1
                end_list+=1
                print(str(menu_options+1) + ") Sort by Randomization")
                print()
                print("Enter your option for the first term: ", end = " ")
                option = int(input())
                while True: 
                    print("Enter your option for the second term: ", end = " ")
                    option2 = int(input())
                    if option2 != option:
                        break
                    else:
                        print()
                        print("Do not enter the same option!")
                        print()
                if(option >= start_list and option <= end_list and option2 >= start_list and option2 <= end_list):
                     
                    #user selects anything but Randomization
                    if(option < menu_options+1):
                        #print("Would you like to sort by similarities or differences? (type similarity/difference)")
                        
                        
                        #Algorithms
                        
                        
                        #use modulus to check if teams are distrubted evenly 
                        #and no person is leftover
                        #use remainder to index in last column
                        remainder = df_rows % minNumGroups
                        
                        #print("Leftover students: " + str(remainder))
                        #print()
                        
                        if remainder == 0:
                            #list of teams
                            Teams = [[] for _ in range(numTeams)]
                            #list of blacklists
                            blacklist_list = [[] for _ in range(numTeams)]
                            
                            Teams2 = [[] for _ in range(numTeams)]
                            #list of blacklists
                            blacklist_list2 = [[] for _ in range(numTeams)]
                        else:
                            #list of teams
                            Teams = [[] for _ in range(numTeams+1)]
                            #list of blacklists
                            blacklist_list = [[] for _ in range(numTeams+1)]
                            
                            Teams2 = [[] for _ in range(numTeams+1)]
                            #list of blacklists
                            blacklist_list2 = [[] for _ in range(numTeams+1)]
                        
                        
                        #print random df
                        #print(df)
                        bigword = col_headers[option]
                        bigword2 = col_headers[option2]
                        #variables
                        count=0         #to put x amount of students in the list
                        teamnum=0       # num for the team
                        nin = df.columns.get_loc("Name")   #name index number
                        bln = df.columns.get_loc("Blacklist")     # blacklist index number
                        
                        df = df.sort_values(by=[bigword])
                        df2 = df.sort_values(by=[bigword2])
                        
                        
                        
                        #loop through all df
                        for i in (range(df_rows)):
                        
                            #see group is 3 people
                            if count < minNumGroups:
                                
                                if i != df_rows:
                                #append the blacklis names to the nested lists
                                    blacklist_list[teamnum].append(df.iloc[i, bln])     
                                    Teams[teamnum].append(df.iloc[i, nin]) 
                                    blacklist_list2[teamnum].append(df2.iloc[i, bln])     
                                    Teams2[teamnum].append(df2.iloc[i, nin]) 
                                    count += 1
                                    
                            #reset for next team, if count == maxsize of group
                            if count == minNumGroups:
                                teamnum += 1         #go to the next team
                                count = 0            #reset count to 0, to refill the next team
                                
                        
                        
                        if(remainder != 0):
                            if(remainder == 1):
                                Teams[teamnum-1].append(Teams[-1][0])
                                blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                Teams2[teamnum-1].append(Teams2[-1][0])
                                blacklist_list2[teamnum-1].append(blacklist_list2[-1][0])
                                
                            elif(remainder >= 2):
                                while(len(Teams[-1]) != 0):
                                    for i in range(len(Teams)-1):
                                        if(remainder == 0):
                                            break
                                                       
                                        Teams[i].append(Teams[-1][remainder-1])
                                        blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                        del Teams[-1][remainder-1]
                                        
                                        Teams2[i].append(Teams2[-1][remainder-1])
                                        blacklist_list2[i].append(blacklist_list2[-1][remainder-1])
                                        del Teams2[-1][remainder-1]
                                        remainder = remainder - 1
                                        #print(len(randomTeams[-1]))
                                        
                            del Teams[-1]
                            del Teams2[-1]
                                
                        
                        
                        
                        #Blacklist
                        
                        #i= team num
                        #j=eachstudent in the team
                        #k=each student in bl
                        
                        #make bool true if teams are good, if there is a blacklist in the 
                        #team set bool to false
                        good_teams= True
                        
                        for i in range(teamnum):
                            lengthteamsize = len(Teams[i])
                            for j in range(lengthteamsize):
                                for k in range(lengthteamsize):
                                    if(blacklist_list[i][k] == Teams[i][j]):
                        #                print(Teams[i][k],"HATES", Teams[i][j])
                                        good_teams = False
                                    if(blacklist_list2[i][k] == Teams2[i][j]):
                        #                print(Teams[i][k],"HATES", Teams[i][j])
                                        good_teams = False
                        
                        counter+=1
                        
                        if counter == 50:  
                            break
                        
                        
                        #this is used for if there is a team that has a blacklist in it        
                        while(good_teams==False):
                            
                            #use modulus to check if teams are distrubted evenly 
                            #and no person is leftover
                            #use remainder to index in last column
                            remainder = df_rows % minNumGroups
                            
                            #print("Leftover students: " + str(remainder))
                            #print()
                            
                            
                            if remainder == 0:
                                #list of teams
                                Teams = [[] for _ in range(numTeams)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams)]
                                Teams2 = [[] for _ in range(numTeams)]
                                #list of blacklists
                                blacklist_list2 = [[] for _ in range(numTeams)]
                            else:
                                #list of teams
                                Teams = [[] for _ in range(numTeams+1)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams+1)]
                                Teams2 = [[] for _ in range(numTeams+1)]
                                #list of blacklists
                                blacklist_list2 = [[] for _ in range(numTeams+1)]
                            
                            #randomize the df
                            df = df.iloc[np.random.permutation(len(df))]
                            
                            #print random df
                            #print(df)
                            bigword = col_headers[option]
                            bigword2 = col_headers[option2]
                            #variables
                            count=0         #to put x amount of students in the list
                            teamnum=0       # num for the team
                            nin = df.columns.get_loc("Name")   #name index number
                            bln = df.columns.get_loc("Blacklist")     # blacklist index number
                            
                            df = df.sort_values(by=[bigword])
                            df2 = df.sort_values(by=[bigword2])
                            
                            #loop through all df
                            for i in (range(df_rows)):
                            
                                #see group is 3 people
                                if count < minNumGroups:
                                    
                                    if i != df_rows:
                                    #append the blacklis names to the nested lists
                                        blacklist_list[teamnum].append(df.iloc[i, bln])     
                                        Teams[teamnum].append(df.iloc[i, nin]) 
                                        blacklist_list2[teamnum].append(df2.iloc[i, bln])     
                                        Teams2[teamnum].append(df2.iloc[i, nin])
                                        count += 1
                                        
                                #reset for next team, if count == maxsize of group
                                if count == minNumGroups:
                                    teamnum += 1         #go to the next team
                                    count = 0            #reset count to 0, to refill the next team
                                    
                            
                            
                            if(remainder != 0):
                                
                                if(remainder == 1):
                                    
                                    Teams[teamnum-1].append(Teams[-1][0])
                                    
                                    blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                    Teams2[teamnum-1].append(Teams2[-1][0])
                                    
                                    blacklist_list2[teamnum-1].append(blacklist_list2[-1][0])
                                    
                                    
                                    
                                elif(remainder >= 2):
                                    while(len(Teams[-1]) != 0):
                                        for i in range(len(Teams)-1):
                                            if(remainder == 0):
                                                break
                                                           
                                            Teams[i].append(Teams[-1][remainder-1])
                                            blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                            del Teams[-1][remainder-1]
                                            Teams2[i].append(Teams2[-1][remainder-1])
                                            blacklist_list2[i].append(blacklist_list2[-1][remainder-1])
                                            del Teams2[-1][remainder-1]
                                            remainder = remainder - 1
                                            #print(len(randomTeams[-1]))
                                            
                                del Teams[-1]
                                del Teams2[-1]
                                    
                            
                            #Blacklist
                            
                            #i= team num
                            #j=eachstudent in the team
                            #k=each student in bl
                            
                            #make bool true if teams are good, if there is a blacklist in the 
                            #team set bool to false
                            good_teams= True
                            
                            
                            for i in range(teamnum):
                                lengthteamsize = len(Teams[i])
                                for j in range(lengthteamsize):
                                    for k in range(lengthteamsize):
                                        if(blacklist_list[i][k] == Teams[i][j]):
                        #                   print(Teams[i][k],"HATES", Teams[i][j])
                                            good_teams = False
                                        if(blacklist_list2[i][k] == Teams2[i][j]):
                        #                   print(Teams[i][k],"HATES", Teams[i][j])
                                            good_teams = False
                        
                        
                            counter+=1
                            
                            if counter == 50:  
                                break
                        
                        #End algorithms
                        break
                    
                                             #%%
#                    if user selects Randomization
                    if(option == menu_options+1):
                        counter==0

        
                        #Algorithms
                        
                        
                        #use modulus to check if teams are distrubted evenly 
                        #and no person is leftover
                        #use remainder to index in last column
                        remainder = df_rows % minNumGroups
                        
                        #print("Leftover students: " + str(remainder))
                        #print()
                        
                        if remainder == 0:
                            #list of teams
                            Teams = [[] for _ in range(numTeams)]
                            #list of blacklists
                            blacklist_list = [[] for _ in range(numTeams)]
                            Teams2 = [[] for _ in range(numTeams)]
                            #list of blacklists
                            blacklist_list2 = [[] for _ in range(numTeams)]
                        else:
                            #list of teams
                            Teams = [[] for _ in range(numTeams+1)]
                            #list of blacklists
                            blacklist_list = [[] for _ in range(numTeams+1)]
                            Teams2 = [[] for _ in range(numTeams+1)]
                            #list of blacklists
                            blacklist_list2 = [[] for _ in range(numTeams+1)]
                        
                        #randomize the df
                        
                        df2 = df.iloc[np.random.permutation(len(df))]
                        df = df.iloc[np.random.RandomState(seed=1000).permutation(len(df))]
                        
                        
                        #print random df
                        #print(df)
                        
                        #variables
                        count=0         #to put x amount of students in the list
                        teamnum=0       # num for the team
                        nin = df.columns.get_loc("Name")   #name index number
                        bln = df.columns.get_loc("Blacklist")     # blacklist index number
                        
                        
                        
                        #loop through all df
                        for i in (range(df_rows)):
                        
                            #see group is 3 people
                            if count < minNumGroups:
                                
                                if i != df_rows:
                                #append the blacklis names to the nested lists
                                    blacklist_list[teamnum].append(df.iloc[i, bln])     
                                    Teams[teamnum].append(df.iloc[i, nin]) 
                                    blacklist_list2[teamnum].append(df2.iloc[i, bln])     
                                    Teams2[teamnum].append(df2.iloc[i, nin])
                                    count += 1
                                    
                            #reset for next team, if count == maxsize of group
                            if count == minNumGroups:
                                teamnum += 1         #go to the next team
                                count = 0            #reset count to 0, to refill the next team
                                
                        
                        
                        if(remainder != 0):
                            if(remainder == 1):
                                Teams[teamnum-1].append(Teams[-1][0])
                                blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                Teams2[teamnum-1].append(Teams2[-1][0])
                                blacklist_list2[teamnum-1].append(blacklist_list2[-1][0])
                                
                            elif(remainder >= 2):
                                while(len(Teams[-1]) != 0):
                                    for i in range(len(Teams)-1):
                                        if(remainder == 0):
                                            break
                                                       
                                        Teams[i].append(Teams[-1][remainder-1])
                                        blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                        Teams2[i].append(Teams2[-1][remainder-1])
                                        blacklist_list2[i].append(blacklist_list2[-1][remainder-1])
                                        del Teams[-1][remainder-1]
                                        del Teams2[-1][remainder-1]
                                        remainder = remainder - 1
                                        #print(len(randomTeams[-1]))
                                        
                            del Teams[-1]
                            del Teams2[-1]
                                
                        
                        
                        
                        #Blacklist
                        
                        #i= team num
                        #j=eachstudent in the team
                        #k=each student in bl
                        
                        #make bool true if teams are good, if there is a blacklist in the 
                        #team set bool to false
                        good_teams= True
                        
                        for i in range(teamnum):
                            lengthteamsize = len(Teams[i])
                            for j in range(lengthteamsize):
                                for k in range(lengthteamsize):
                                    if(blacklist_list[i][k] == Teams[i][j]):
                        #                print(Teams[i][k],"HATES", Teams[i][j])
                                        good_teams = False
                                    if(blacklist_list2[i][k] == Teams2[i][j]):
                                        good_teams = False
                        counter+=1
                        if counter == 50:   
                            break
                        
                        
                        #this is used for if there is a team that has a blacklist in it        
                        while(good_teams==False):
                            
                            #use modulus to check if teams are distrubted evenly 
                            #and no person is leftover
                            #use remainder to index in last column
                            remainder = df_rows % minNumGroups
                            
                            #print("Leftover students: " + str(remainder))
                            #print()
                            
                            
                            if remainder == 0:
                                #list of teams
                                Teams = [[] for _ in range(numTeams)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams)]
                                Teams2 = [[] for _ in range(numTeams)]
                                #list of blacklists
                                blacklist_list2 = [[] for _ in range(numTeams)]
                            else:
                                #list of teams
                                Teams = [[] for _ in range(numTeams+1)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams+1)]
                                Teams2 = [[] for _ in range(numTeams+1)]
                                #list of blacklists
                                blacklist_list2 = [[] for _ in range(numTeams+1)]
                            
                            #randomize the df
                            
                            df2 = df.iloc[np.random.permutation(len(df))]
                            
                            df = df.iloc[np.random.RandomState(seed=42).permutation(len(df))]
                            
                            
                            #print random df
                            #print(df)
                            
                            #variables
                            count=0         #to put x amount of students in the list
                            teamnum=0       # num for the team
                            nin = df.columns.get_loc("Name")   #name index number
                            bln = df.columns.get_loc("Blacklist")     # blacklist index number
                            
                            
                            
                            #loop through all df
                            for i in (range(df_rows)):
                            
                                #see group is 3 people
                                if count < minNumGroups:
                                    
                                    if i != df_rows:
                                    #append the blacklis names to the nested lists
                                        blacklist_list[teamnum].append(df.iloc[i, bln])     
                                        Teams[teamnum].append(df.iloc[i, nin]) 
                                        blacklist_list2[teamnum].append(df2.iloc[i, bln])     
                                        Teams2[teamnum].append(df2.iloc[i, nin])
                                        count += 1
                                        
                                #reset for next team, if count == maxsize of group
                                if count == minNumGroups:
                                    teamnum += 1         #go to the next team
                                    count = 0            #reset count to 0, to refill the next team
                                    
                            
                            
                            if(remainder != 0):
                                if(remainder == 1):
                                    Teams[teamnum-1].append(Teams[-1][0])
                                    blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                    Teams2[teamnum-1].append(Teams2[-1][0])
                                    blacklist_list2[teamnum-1].append(blacklist_list2[-1][0])
                                    
                                elif(remainder >= 2):
                                    while(len(Teams[-1]) != 0):
                                        for i in range(len(Teams)-1):
                                            if(remainder == 0):
                                                break
                                                           
                                            Teams[i].append(Teams[-1][remainder-1])
                                            blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                            del Teams[-1][remainder-1]
                                            Teams2[i].append(Teams2[-1][remainder-1])
                                            blacklist_list2[i].append(blacklist_list2[-1][remainder-1])
                                            del Teams2[-1][remainder-1]
                                            remainder = remainder - 1
                                            #print(len(randomTeams[-1]))
                                            
                                del Teams[-1]
                                del Teams2[-1]
                                
                            
                            #Blacklist
                            
                            #i= team num
                            #j=eachstudent in the team
                            #k=each student in bl
                            
                            #make bool true if teams are good, if there is a blacklist in the 
                            #team set bool to false
                            good_teams= True
                            
                            for i in (range(teamnum)):
                                lengthteamsize = len(Teams[i])
                                for j in range(lengthteamsize):
                                    for k in range(lengthteamsize):
                                        if(blacklist_list[i][k] == Teams[i][j]):
                        #                   print(Teams[i][k],"HATES", Teams[i][j])
                                            good_teams = False
                                        if(blacklist_list2[i][k] == Teams2[i][j]):
                        #                   print(Teams[i][k],"HATES", Teams[i][j])
                                            good_teams = False
                        
                            counter+=1
                            
#                            print(counter)
                            if counter == 50:   
                                break
                        
                        #End algorithms
                        
                
                    
                    
            if(terms == 3):
                newFlag = True
                counter=0
                #make menu
                print()
                print("Choose one of the following options to sort by:")
                num = 0
                non_options = -1
                for i in col_headers:
                    #might have to change
                    if(col_headers[num] == "Name" or col_headers[num] == "Blacklist" or col_headers[num] == "Timestamp"):
                        num+=1
                        non_options+=1
                    else:
                        menu_options = num-non_options
                        menu.append(menu_options)
                        print(str(menu_options) + ") Sort by", col_headers[num])
                        num+=1
                        end_list+=1
                end_list+=1
                print(str(menu_options+1) + ") Sort by Randomization")
                print()
                print("Enter your option for the first term: ", end = " ")
                option = int(input())
                while True:
                    print("Enter your option for the second term: ", end = " ")
                    option2 = int(input())
                    if option2 != option:
                        break
                    else:
                        print()
                        print("Do not enter the same option!")
                        print()
                while True:
                    print("Enter your option for the three term: ", end = " ")
                    option3 = int(input())
                    if option3 != option2 and option3 != option:
                        break
                    else:
                        print()
                        print("Do not enter the same option!")
                        print()
                if((option >= start_list and option <= end_list and option2 >= start_list and option2 <= end_list and option3 >= start_list and option3 <= end_list)):
                     
                    #user selects anything but Randomization
                    if(option < menu_options+1):
                        #print("Would you like to sort by similarities or differences? (type similarity/difference)")
                        
                        
                        #Algorithms
                        
                        
                        #use modulus to check if teams are distrubted evenly 
                        #and no person is leftover
                        #use remainder to index in last column
                        remainder = df_rows % minNumGroups
                        
                        #print("Leftover students: " + str(remainder))
                        #print()
                        
                        if remainder == 0:
                            #list of teams
                            Teams = [[] for _ in range(numTeams)]
                            #list of blacklists
                            blacklist_list = [[] for _ in range(numTeams)]
                            
                            Teams2 = [[] for _ in range(numTeams)]
                            #list of blacklists
                            blacklist_list2 = [[] for _ in range(numTeams)]
                            
                            Teams3 = [[] for _ in range(numTeams)]
                            #list of blacklists
                            blacklist_list3 = [[] for _ in range(numTeams)]
                        else:
                            #list of teams
                            Teams = [[] for _ in range(numTeams+1)]
                            #list of blacklists
                            blacklist_list = [[] for _ in range(numTeams+1)]
                            
                            Teams2 = [[] for _ in range(numTeams+1)]
                            #list of blacklists
                            blacklist_list2 = [[] for _ in range(numTeams+1)]
                            
                            Teams3 = [[] for _ in range(numTeams+1)]
                            #list of blacklists
                            blacklist_list3 = [[] for _ in range(numTeams+1)]
                        
                        
                        #print random df
                        #print(df)
                        bigword = col_headers[option]
                        bigword2 = col_headers[option2]
                        bigword3 = col_headers[option3]
                        #variables
                        count=0         #to put x amount of students in the list
                        teamnum=0       # num for the team
                        nin = df.columns.get_loc("Name")   #name index number
                        bln = df.columns.get_loc("Blacklist")     # blacklist index number
                        
                        df = df.sort_values(by=[bigword])
                        df2 = df.sort_values(by=[bigword2])
                        df3 = df.sort_values(by=[bigword3])
                        
                        
                        
                        #loop through all df
                        for i in (range(df_rows)):
                        
                            #see group is 3 people
                            if count < minNumGroups:
                                
                                if i != df_rows:
                                #append the blacklis names to the nested lists
                                    blacklist_list[teamnum].append(df.iloc[i, bln])     
                                    Teams[teamnum].append(df.iloc[i, nin]) 
                                    blacklist_list2[teamnum].append(df2.iloc[i, bln])     
                                    Teams2[teamnum].append(df2.iloc[i, nin]) 
                                    blacklist_list3[teamnum].append(df3.iloc[i, bln])     
                                    Teams3[teamnum].append(df3.iloc[i, nin])
                                    count += 1
                                    
                            #reset for next team, if count == maxsize of group
                            if count == minNumGroups:
                                teamnum += 1         #go to the next team
                                count = 0            #reset count to 0, to refill the next team
                                
                        
                        
                        if(remainder != 0):
                            if(remainder == 1):
                                Teams[teamnum-1].append(Teams[-1][0])
                                blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                Teams2[teamnum-1].append(Teams2[-1][0])
                                blacklist_list2[teamnum-1].append(blacklist_list2[-1][0])
                                Teams3[teamnum-1].append(Teams3[-1][0])
                                blacklist_list3[teamnum-1].append(blacklist_list3[-1][0])
                                
                            elif(remainder >= 2):
                                while(len(Teams[-1]) != 0):
                                    for i in range(len(Teams)-1):
                                        if(remainder == 0):
                                            break
                                                       
                                        Teams[i].append(Teams[-1][remainder-1])
                                        blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                        del Teams[-1][remainder-1]
                                        
                                        Teams2[i].append(Teams2[-1][remainder-1])
                                        blacklist_list2[i].append(blacklist_list2[-1][remainder-1])
                                        
                                        Teams3[i].append(Teams3[-1][remainder-1])
                                        blacklist_list3[i].append(blacklist_list3[-1][remainder-1])
                                        del Teams3[-1][remainder-1]
                                        
                                        del Teams2[-1][remainder-1]
                                        remainder = remainder - 1
                                        #print(len(randomTeams[-1]))
                                        
                            del Teams[-1]
                            del Teams2[-1]
                            del Teams3[-1]
                                
                        
                        
                        
                        #Blacklist
                        
                        #i= team num
                        #j=eachstudent in the team
                        #k=each student in bl
                        
                        #make bool true if teams are good, if there is a blacklist in the 
                        #team set bool to false
                        good_teams= True
                        
                        for i in range(teamnum):
                            lengthteamsize = len(Teams[i])
                            for j in range(lengthteamsize):
                                for k in range(lengthteamsize):
                                    if(blacklist_list[i][k] == Teams[i][j]):
                        #                print(Teams[i][k],"HATES", Teams[i][j])
                                        good_teams = False
                                    if(blacklist_list2[i][k] == Teams2[i][j]):
                        #                print(Teams[i][k],"HATES", Teams[i][j])
                                        good_teams = False
                                    if(blacklist_list3[i][k] == Teams3[i][j]):
                        #                print(Teams[i][k],"HATES", Teams[i][j])
                                        good_teams = False
                        
                        counter+=1
                        
                        if counter == 50:  
                            break
                        
                        
                        #this is used for if there is a team that has a blacklist in it        
                        while(good_teams==False):
                            
                            #use modulus to check if teams are distrubted evenly 
                            #and no person is leftover
                            #use remainder to index in last column
                            remainder = df_rows % minNumGroups
                            
                            #print("Leftover students: " + str(remainder))
                            #print()
                            
                            
                            if remainder == 0:
                                #list of teams
                                Teams = [[] for _ in range(numTeams)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams)]
                                Teams2 = [[] for _ in range(numTeams)]
                                #list of blacklists
                                blacklist_list2 = [[] for _ in range(numTeams)]
                                Teams3 = [[] for _ in range(numTeams)]
                                #list of blacklists
                                blacklist_list3 = [[] for _ in range(numTeams)]
                            else:
                                #list of teams
                                Teams = [[] for _ in range(numTeams+1)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams+1)]
                                Teams2 = [[] for _ in range(numTeams+1)]
                                #list of blacklists
                                blacklist_list2 = [[] for _ in range(numTeams+1)]
                                Teams3 = [[] for _ in range(numTeams+1)]
                                #list of blacklists
                                blacklist_list3 = [[] for _ in range(numTeams+1)]
                            
                            #randomize the df
                            df = df.iloc[np.random.permutation(len(df))]
                            
                            #print random df
                            #print(df)
                            bigword = col_headers[option]
                            bigword2 = col_headers[option2]
                            bigword3 = col_headers[option3]
                            #variables
                            count=0         #to put x amount of students in the list
                            teamnum=0       # num for the team
                            nin = df.columns.get_loc("Name")   #name index number
                            bln = df.columns.get_loc("Blacklist")     # blacklist index number
                            
                            df = df.sort_values(by=[bigword])
                            df2 = df.sort_values(by=[bigword2])
                            df3 = df.sort_values(by=[bigword3])
                            
                            #loop through all df
                            for i in (range(df_rows)):
                            
                                #see group is 3 people
                                if count < minNumGroups:
                                    
                                    if i != df_rows:
                                    #append the blacklis names to the nested lists
                                        blacklist_list[teamnum].append(df.iloc[i, bln])     
                                        Teams[teamnum].append(df.iloc[i, nin]) 
                                        blacklist_list2[teamnum].append(df2.iloc[i, bln])     
                                        Teams2[teamnum].append(df2.iloc[i, nin])
                                        blacklist_list3[teamnum].append(df3.iloc[i, bln])     
                                        Teams3[teamnum].append(df3.iloc[i, nin])
                                        count += 1
                                        
                                #reset for next team, if count == maxsize of group
                                if count == minNumGroups:
                                    teamnum += 1         #go to the next team
                                    count = 0            #reset count to 0, to refill the next team
                                    
                            
                            
                            if(remainder != 0):
                                
                                if(remainder == 1):
                                    
                                    Teams[teamnum-1].append(Teams[-1][0])
                                    
                                    blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                    
                                    Teams2[teamnum-1].append(Teams2[-1][0])
                                    
                                    blacklist_list2[teamnum-1].append(blacklist_list2[-1][0])
                                    
                                    Teams3[teamnum-1].append(Teams3[-1][0])
                                    
                                    blacklist_list3[teamnum-1].append(blacklist_list3[-1][0])
                                    
                                    
                                    
                                elif(remainder >= 2):
                                    while(len(Teams[-1]) != 0):
                                        for i in range(len(Teams)-1):
                                            if(remainder == 0):
                                                break
                                                           
                                            Teams[i].append(Teams[-1][remainder-1])
                                            blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                            del Teams[-1][remainder-1]
                                            
                                            Teams2[i].append(Teams2[-1][remainder-1])
                                            blacklist_list2[i].append(blacklist_list2[-1][remainder-1])
                                            del Teams2[-1][remainder-1]
                                            
                                            Teams3[i].append(Teams3[-1][remainder-1])
                                            blacklist_list3[i].append(blacklist_list3[-1][remainder-1])
                                            del Teams3[-1][remainder-1]
                                            
                                            remainder = remainder - 1
                                            #print(len(randomTeams[-1]))
                                            
                                del Teams[-1]
                                del Teams2[-1]
                                del Teams3[-1]
                                    
                            
                            #Blacklist
                            
                            #i= team num
                            #j=eachstudent in the team
                            #k=each student in bl
                            
                            #make bool true if teams are good, if there is a blacklist in the 
                            #team set bool to false
                            good_teams= True
                            
                            
                            for i in range(teamnum):
                                lengthteamsize = len(Teams[i])
                                for j in range(lengthteamsize):
                                    for k in range(lengthteamsize):
                                        if(blacklist_list[i][k] == Teams[i][j]):
                        #                   print(Teams[i][k],"HATES", Teams[i][j])
                                            good_teams = False
                                        if(blacklist_list2[i][k] == Teams2[i][j]):
                        #                   print(Teams[i][k],"HATES", Teams[i][j])
                                            good_teams = False
                                        if(blacklist_list3[i][k] == Teams3[i][j]):
                        #                   print(Teams[i][k],"HATES", Teams[i][j])
                                            good_teams = False
                        
                        
                            counter+=1
                            
                            if counter == 50:   
                                break
                        
                        #End algorithms
                        break
                    
                                             #%%
#                    if user selects Randomization
                    if(option == menu_options+1):
                        counter==0

        
                        #Algorithms
                        
                        
                        #use modulus to check if teams are distrubted evenly 
                        #and no person is leftover
                        #use remainder to index in last column
                        remainder = df_rows % minNumGroups
                        
                        #print("Leftover students: " + str(remainder))
                        #print()
                        
                        if remainder == 0:
                            #list of teams
                            Teams = [[] for _ in range(numTeams)]
                            #list of blacklists
                            blacklist_list = [[] for _ in range(numTeams)]
                            Teams2 = [[] for _ in range(numTeams)]
                            #list of blacklists
                            blacklist_list2 = [[] for _ in range(numTeams)]
                            Teams3 = [[] for _ in range(numTeams)]
                            #list of blacklists
                            blacklist_list3 = [[] for _ in range(numTeams)]
                        else:
                            #list of teams
                            Teams = [[] for _ in range(numTeams+1)]
                            #list of blacklists
                            blacklist_list = [[] for _ in range(numTeams+1)]
                            Teams2 = [[] for _ in range(numTeams+1)]
                            #list of blacklists
                            blacklist_list2 = [[] for _ in range(numTeams+1)]
                            Teams3 = [[] for _ in range(numTeams+1)]
                            #list of blacklists
                            blacklist_list3 = [[] for _ in range(numTeams+1)]
                        
                        #randomize the df
                        df3 = df.iloc[np.random.RandomState(seed=42).permutation(len(df))]
                        df2 = df.iloc[np.random.permutation(len(df))]
                        df = df.iloc[np.random.RandomState(seed=1000).permutation(len(df))]
                        
                        
                        #print random df
                        #print(df)
                        
                        #variables
                        count=0         #to put x amount of students in the list
                        teamnum=0       # num for the team
                        nin = df.columns.get_loc("Name")   #name index number
                        bln = df.columns.get_loc("Blacklist")     # blacklist index number
                        
                        
                        
                        #loop through all df
                        for i in (range(df_rows)):
                        
                            #see group is 3 people
                            if count < minNumGroups:
                                
                                if i != df_rows:
                                #append the blacklis names to the nested lists
                                    blacklist_list[teamnum].append(df.iloc[i, bln])     
                                    Teams[teamnum].append(df.iloc[i, nin]) 
                                    blacklist_list2[teamnum].append(df2.iloc[i, bln])     
                                    Teams2[teamnum].append(df2.iloc[i, nin])
                                    blacklist_list3[teamnum].append(df3.iloc[i, bln])     
                                    Teams3[teamnum].append(df3.iloc[i, nin])
                                    count += 1
                                    
                            #reset for next team, if count == maxsize of group
                            if count == minNumGroups:
                                teamnum += 1         #go to the next team
                                count = 0            #reset count to 0, to refill the next team
                                
                        
                        
                        if(remainder != 0):
                            if(remainder == 1):
                                Teams[teamnum-1].append(Teams[-1][0])
                                blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                Teams2[teamnum-1].append(Teams2[-1][0])
                                blacklist_list2[teamnum-1].append(blacklist_list2[-1][0])
                                Teams3[teamnum-1].append(Teams3[-1][0])
                                blacklist_list3[teamnum-1].append(blacklist_list3[-1][0])
                                
                            elif(remainder >= 2):
                                while(len(Teams[-1]) != 0):
                                    for i in range(len(Teams)-1):
                                        if(remainder == 0):
                                            break
                                                       
                                        Teams[i].append(Teams[-1][remainder-1])
                                        blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                        Teams2[i].append(Teams2[-1][remainder-1])
                                        blacklist_list2[i].append(blacklist_list2[-1][remainder-1])
                                        Teams3[i].append(Teams3[-1][remainder-1])
                                        blacklist_list3[i].append(blacklist_list3[-1][remainder-1])
                                        del Teams[-1][remainder-1]
                                        del Teams2[-1][remainder-1]
                                        del Teams3[-1][remainder-1]
                                        remainder = remainder - 1
                                        #print(len(randomTeams[-1]))
                                        
                            del Teams[-1]
                            del Teams2[-1]
                            del Teams2[-1]
                                
                        
                        
                        
                        #Blacklist
                        
                        #i= team num
                        #j=eachstudent in the team
                        #k=each student in bl
                        
                        #make bool true if teams are good, if there is a blacklist in the 
                        #team set bool to false
                        good_teams= True
                        
                        for i in range(teamnum):
                            lengthteamsize = len(Teams[i])
                            for j in range(lengthteamsize):
                                for k in range(lengthteamsize):
                                    if(blacklist_list[i][k] == Teams[i][j]):
                        #                print(Teams[i][k],"HATES", Teams[i][j])
                                        good_teams = False
                                    if(blacklist_list2[i][k] == Teams2[i][j]):
                                        good_teams = False
                                    if(blacklist_list3[i][k] == Teams3[i][j]):
                                        good_teams = False
                        counter+=1
                        if counter == 50:  
                            break
                        
                        
                        #this is used for if there is a team that has a blacklist in it        
                        while(good_teams==False):
                            
                            #use modulus to check if teams are distrubted evenly 
                            #and no person is leftover
                            #use remainder to index in last column
                            remainder = df_rows % minNumGroups
                            
                            #print("Leftover students: " + str(remainder))
                            #print()
                            
                            
                            if remainder == 0:
                                #list of teams
                                Teams = [[] for _ in range(numTeams)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams)]
                                Teams2 = [[] for _ in range(numTeams)]
                                #list of blacklists
                                blacklist_list2 = [[] for _ in range(numTeams)]
                                Teams3 = [[] for _ in range(numTeams)]
                                #list of blacklists
                                blacklist_list3 = [[] for _ in range(numTeams)]
                            else:
                                #list of teams
                                Teams = [[] for _ in range(numTeams+1)]
                                #list of blacklists
                                blacklist_list = [[] for _ in range(numTeams+1)]
                                Teams2 = [[] for _ in range(numTeams+1)]
                                #list of blacklists
                                blacklist_list2 = [[] for _ in range(numTeams+1)]
                                Teams3 = [[] for _ in range(numTeams+1)]
                                #list of blacklists
                                blacklist_list3 = [[] for _ in range(numTeams+1)]
                            
                            #randomize the df
                            df3 = df.iloc[np.random.RandomState(seed=1000).permutation(len(df))]
                            df2 = df.iloc[np.random.permutation(len(df))]
                            
                            df = df.iloc[np.random.RandomState(seed=42).permutation(len(df))]
                            
                            
                            #print random df
                            #print(df)
                            
                            #variables
                            count=0         #to put x amount of students in the list
                            teamnum=0       # num for the team
                            nin = df.columns.get_loc("Name")   #name index number
                            bln = df.columns.get_loc("Blacklist")     # blacklist index number
                            
                            
                            
                            #loop through all df
                            for i in (range(df_rows)):
                            
                                #see group is 3 people
                                if count < minNumGroups:
                                    
                                    if i != df_rows:
                                    #append the blacklis names to the nested lists
                                        blacklist_list[teamnum].append(df.iloc[i, bln])     
                                        Teams[teamnum].append(df.iloc[i, nin]) 
                                        blacklist_list2[teamnum].append(df2.iloc[i, bln])     
                                        Teams2[teamnum].append(df2.iloc[i, nin])
                                        blacklist_list3[teamnum].append(df3.iloc[i, bln])     
                                        Teams3[teamnum].append(df3.iloc[i, nin])
                                        count += 1
                                        
                                #reset for next team, if count == maxsize of group
                                if count == minNumGroups:
                                    teamnum += 1         #go to the next team
                                    count = 0            #reset count to 0, to refill the next team
                                    
                            
                            
                            if(remainder != 0):
                                if(remainder == 1):
                                    Teams[teamnum-1].append(Teams[-1][0])
                                    blacklist_list[teamnum-1].append(blacklist_list[-1][0])
                                    Teams2[teamnum-1].append(Teams2[-1][0])
                                    blacklist_list2[teamnum-1].append(blacklist_list2[-1][0])
                                    Teams3[teamnum-1].append(Teams3[-1][0])
                                    blacklist_list3[teamnum-1].append(blacklist_list3[-1][0])
                                    
                                elif(remainder >= 2):
                                    while(len(Teams[-1]) != 0):
                                        for i in range(len(Teams)-1):
                                            if(remainder == 0):
                                                break
                                                           
                                            Teams[i].append(Teams[-1][remainder-1])
                                            blacklist_list[i].append(blacklist_list[-1][remainder-1])
                                            del Teams[-1][remainder-1]
                                            Teams2[i].append(Teams2[-1][remainder-1])
                                            blacklist_list2[i].append(blacklist_list2[-1][remainder-1])
                                            del Teams2[-1][remainder-1]
                                            Teams3[i].append(Teams3[-1][remainder-1])
                                            blacklist_list3[i].append(blacklist_list3[-1][remainder-1])
                                            del Teams3[-1][remainder-1]
                                            remainder = remainder - 1
                                            #print(len(randomTeams[-1]))
                                            
                                del Teams[-1]
                                del Teams2[-1]
                                del Teams3[-1]
                                
                            
                            #Blacklist
                            
                            #i= team num
                            #j=eachstudent in the team
                            #k=each student in bl
                            
                            #make bool true if teams are good, if there is a blacklist in the 
                            #team set bool to false
                            good_teams= True
                            
                            for i in (range(teamnum)):
                                lengthteamsize = len(Teams[i])
                                for j in range(lengthteamsize):
                                    for k in range(lengthteamsize):
                                        if(blacklist_list[i][k] == Teams[i][j]):
                        #                   print(Teams[i][k],"HATES", Teams[i][j])
                                            good_teams = False
                                        if(blacklist_list2[i][k] == Teams2[i][j]):
                        #                   print(Teams[i][k],"HATES", Teams[i][j])
                                            good_teams = False
                                            
                                        if(blacklist_list3[i][k] == Teams3[i][j]):
                        #                   print(Teams[i][k],"HATES", Teams[i][j])
                                            good_teams = False
                        
                            counter+=1
                            
#                            print(counter)
                            if counter == 50:   
                                break
                        
                        #End algorithms
                        break
        #Prints error that file is not in directory
        except ValueError:
            print("\nPlease enter a number! Try again!\n")
    
    
    
    
    
    
    
    
    
    
    #%%
    if(newFlag == True):
        if(terms == 2):
            grouped = pd.DataFrame(Teams)
            grouped2 = pd.DataFrame(Teams2)
            #transpose the teams,,  teams were going left to right,, now lists vertically
            regrouped = grouped.transpose()
            regrouped2 = grouped2.transpose()
            #make the col headers for new_headers df
            new_col = []
            new_col2 = []
            #loop through to make the groups needed 
            for i in range(numTeams):
                new_col.append("Group " + str(i+1))
                new_col2.append("Group " + str(i+1))
            
            #put the groups headers above the member of the team 
            regrouped.columns = new_col
            regrouped2.columns = new_col2
            
            frames = [regrouped, regrouped2]
            
            result = pd.concat(frames)
            
            print()
            print("This is the generated groups")
            print(result)
            
            #Saving the new csv file
            
            while True:
            
                #ask user to enter name of formed csv
                save_file = input("Please enter the name of the new csv: ")
                #check if the sting has .csv
                if(save_file[-4:] != ".csv"):
                    # concate filename with .csv
                    save_file = save_file + ".csv"
            
                print()
                #ask if user really wants to save this file 
                print("Are you sure you want to save the file as", save_file,"? (Y/N)", end=" ")
                save = input()
            
                if(save == "Yes" or save == "yes" or save == "Y" or save == "y"):
                    #save the new df as csv on users directory
                    result.to_csv(save_file, encoding='utf-8', index=False)
                    print()
                    print(save_file,"has been saved in your current directory.")
                    break
            
                
            #ask user if they want to use th eprogram again 
            while True:
                useprogram = input("Would you like to use the program again?(Y/N) ")
                if(useprogram == "No" or useprogram == "N" or useprogram == "n" or useprogram == "no"):
                    useprogram=False
                    break
                elif useprogram == "Yes" or useprogram == "Y" or useprogram == "y" or useprogram == "yes":
                    useprogram=True
                    break
        if(terms == 3):
            grouped = pd.DataFrame(Teams)
            grouped2 = pd.DataFrame(Teams2)
            grouped3 = pd.DataFrame(Teams3)
            #transpose the teams,,  teams were going left to right,, now lists vertically
            regrouped = grouped.transpose()
            regrouped2 = grouped2.transpose()
            regrouped3 = grouped3.transpose()
            #make the col headers for new_headers df
            new_col = []
            new_col2 = []
            new_col3 = []
            #loop through to make the groups needed 
            for i in range(numTeams):
                new_col.append("Group " + str(i+1))
                new_col2.append("Group " + str(i+1))
                new_col3.append("Group " + str(i+1))
            
            #put the groups headers above the member of the team 
            regrouped.columns = new_col
            regrouped2.columns = new_col2
            regrouped3.columns = new_col3
            
            frames = [regrouped, regrouped2, regrouped3]
            
            result = pd.concat(frames)
            
            print()
            print("This is the generated groups")
            print(result)
            
            #Saving the new csv file
            
            while True:
            
                #ask user to enter name of formed csv
                save_file = input("Please enter the name of the new csv: ")
                #check if the sting has .csv
                if(save_file[-4:] != ".csv"):
                    # concate filename with .csv
                    save_file = save_file + ".csv"
            
                print()
                #ask if user really wants to save this file 
                print("Are you sure you want to save the file as", save_file,"? (Y/N)", end=" ")
                save = input()
            
                if(save == "Yes" or save == "yes" or save == "Y" or save == "y"):
                    #save the new df as csv on users directory
                    result.to_csv(save_file, encoding='utf-8', index=False)
                    print()
                    print(save_file,"has been saved in your current directory.")
                    break
            
                
            #ask user if they want to use th eprogram again 
            while True:
                useprogram = input("Would you like to use the program again?(Y/N) ")
                if(useprogram == "No" or useprogram == "N" or useprogram == "n" or useprogram == "no"):
                    useprogram=False
                    break
                elif useprogram == "Yes" or useprogram == "Y" or useprogram == "y" or useprogram == "yes":
                    useprogram=True
                    break
    else:
        
        #make a dataframe ofthe new_headers teams
        grouped = pd.DataFrame(Teams)
        
        #transpose the teams,,  teams were going left to right,, now lists vertically
        regrouped = grouped.transpose()
        
        #make the col headers for new_headers df
        new_col = []
        
        #loop through to make the groups needed 
        for i in range(numTeams):
            new_col.append("Group " + str(i+1))
            
        
        #put the groups headers above the member of the team 
        regrouped.columns = new_col
        
        
        print()
        print("This is the generated groups")
        print(regrouped)
        
        #Saving the new csv file
        
        while True:
        
            #ask user to enter name of formed csv
            save_file = input("Please enter the name of the new csv: ")
            #check if the sting has .csv
            if(save_file[-4:] != ".csv"):
                # concate filename with .csv
                save_file = save_file + ".csv"
        
            print()
            #ask if user really wants to save this file 
            print("Are you sure you want to save the file as", save_file,"? (Y/N)", end=" ")
            save = input()
        
            if(save == "Yes" or save == "yes" or save == "Y" or save == "y"):
                #save the new df as csv on users directory
                regrouped.to_csv(save_file, encoding='utf-8', index=False)
                print()
                print(save_file,"has been saved in your current directory.")
                break
        
            
        #ask user if they want to use th eprogram again 
        while True:
            useprogram = input("Would you like to use the program again?(Y/N) ")
            if(useprogram == "No" or useprogram == "N" or useprogram == "n" or useprogram == "no"):
                useprogram=False
                break
            elif useprogram == "Yes" or useprogram == "Y" or useprogram == "y" or useprogram == "yes":
                useprogram=True
                break


#print something to it the end of the program
print("\nThank you for using the program!")

#%%



#Extra





















