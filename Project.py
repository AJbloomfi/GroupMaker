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

#get users current directory
cwd = os.getcwd()
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
col_headers = list(df)
print()

#%%
#WORK HERE
reee=[]

#If the questions asked on the survey are going to be
# What is your... (word) then get the last word to use as menu
#below gets the last word in the string
for i in range(len(col_headers)):  
    s = col_headers[i]
    reee.append(s.split()[-1])
#make col_headers = the fake list 
col_headers = reee
    
r = []
#need to strip punc 
for i in range(len(col_headers)): 
    r.append(col_headers[i].translate(str.maketrans('', '', string.punctuation)))

col_headers = r

#captialize the words 
new = []
for i in range(len(col_headers)): 
    new.append(col_headers[i].capitalize())


col_headers = new

df.columns = col_headers

#%%



menu=[]
start_list = 1
while True:
    end_list = 0
    try:
        #make menu
        print("Choose one of the following options to sort by:")
        num = 0
        non_options = -1
        for i in col_headers:
            #might have to change
            if(col_headers[num] == "Name" or col_headers[num] == "Age" or col_headers[num] == "Blacklist" or col_headers[num] == "Timestamp"):
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
        option = int(input())
        if(option >= start_list and option <= end_list):
            break
        
    #Prints error that file is not in directory
    except ValueError:
        print("\nPlease enter a number! Try again!\n")

print()


#%%

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
    b = [[] for _ in range(numTeams)]
else:
    #list of teams
    Teams = [[] for _ in range(numTeams+1)]
    #list of blacklists
    b = [[] for _ in range(numTeams+1)]

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
            b[teamnum].append(df.iloc[i, bln])     
            Teams[teamnum].append(df.iloc[i, nin]) 
            count += 1
            
    #reset for next team, if count == maxsize of group
    if count == minNumGroups:
        teamnum += 1         #go to the next team
        count = 0            #reset count to 0, to refill the next team
        


if(remainder != 0):
    if(remainder == 1):
        Teams[0].append(Teams[-1][0])
        
    elif(remainder >= 2):
        while(len(Teams[-1]) != 0):
            for i in range(len(Teams)-1):
                if(remainder == 0):
                    break
                               
                Teams[i].append(Teams[-1][remainder-1])
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
    for j in range(minNumGroups):
        for k in range(minNumGroups):
            if(b[i][k] == Teams[i][j]):
#                print(Teams[i][k],"HATES", Teams[i][j])
                good_teams = False



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
        b = [[] for _ in range(numTeams)]
    else:
        #list of teams
        Teams = [[] for _ in range(numTeams+1)]
        #list of blacklists
        b = [[] for _ in range(numTeams+1)]
    
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
                b[teamnum].append(df.iloc[i, bln])     
                Teams[teamnum].append(df.iloc[i, nin]) 
                count += 1
                
        #reset for next team, if count == maxsize of group
        if count == minNumGroups:
            teamnum += 1         #go to the next team
            count = 0            #reset count to 0, to refill the next team
            
    
    
    if(remainder != 0):
        if(remainder == 1):
            Teams[0].append(Teams[-1][0])
            
        elif(remainder >= 2):
            while(len(Teams[-1]) != 0):
                for i in range(len(Teams)-1):
                    if(remainder == 0):
                        break
                                   
                    Teams[i].append(Teams[-1][remainder-1])
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
        for j in range(minNumGroups):
            for k in range(minNumGroups):
                if(b[i][k] == Teams[i][j]):
    #                print(Teams[i][k],"HATES", Teams[i][j])
                    good_teams = False




#End algorithms





#%%

#make a dataframe ofthe new teams
grouped = pd.DataFrame(Teams)
#transpose the teams,,  teams were going left to right,, now lists vertically
regrouped = grouped.transpose()
#make the col headers for new df
new_col = []
#loop through to make the groups needed 
for i in range(numTeams):
    new_col.append("Group " + str(i+1))

#put the groups headers above the member of the team 
regrouped.columns = new_col

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


    #ask if user really wants to save this file 
    print("Are you sure you want to save the file as", save_file,"? (Y/N)")
    save = input()

    if(save == "Yes" or save == "yes" or save == "Y" or save == "y"):
        #save the new df as csv on users directory
        regrouped.to_csv(save_file, encoding='utf-8', index=False)
        print()
        print(save_file,"has been saved in your current directory.")
        break

    
#print something to it the end of the program
print("\nThank you for using the program!")

#%%



#Extra





















