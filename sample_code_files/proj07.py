########################################################
#   CSE 231 Project 5
#   
#   Program
#       Prompt for file
#       Organize country infromation from files into 2 lists
#       Prompt for 4 options
#           1) Show which regime has lasted longest for specific country
#           2) List all countries which had lonest specified government
#           3) List all countries to specified length that have had the most regime changes
#           4) Prompt to quit
#
########################################################

import csv
from operator import itemgetter

REGIME=["Closed autocracy","Electoral autocracy","Electoral democracy","Liberal democracy"]
MENU='''\nRegime Options:
            (1) Display regime history
            (2) Display allies
            (3) Display chaotic regimes        
    '''
    
def open_file():
    """
    Opens specified file without crashing the program

    Returns
    -------
    File Pointer
        File pointer of specified file

    """
    #Loops until a valid file is opened
    while True:
        #Gets file name input
        user_input = input("Enter a file: ")
        
        #Opens file wth name of input
        try:
            open(user_input, "r")
            break
        
        #If file name does not exist display error message
        except FileNotFoundError:
            print("File not found. Please try again.")
            
    #Returns opened file pointer
    return open(user_input, "r")


#DONE
def read_file(fp):
    """
    Converts information from files into 2 lists

    Parameters
    ----------
    File Pointer
        File Pointer from previously descirbed funciton

    Returns
    -------
    country_names : List
        list of every country from a file
    list_of_regime_lists : List of Lists
        List of every countries regime over a time period that exists in file

    """
    
    reader = csv.reader(fp)
    
    #Skips first line
    next(fp, None)

    country_names = []
    list_of_regime_lists = [] #Master list of regimes
    local_regime_list = [] #List of regimes for specific country
    
    previous_country = None
    
    #Counter variable
    country_index = 0

    #Loops through every line in the file
    for line_lst in reader:
        country = line_lst[1]
        regime = line_lst[4]
        
        
        
        if country != previous_country:
            previous_country = country
            country_names.append(country) #Append country to list
            
            #Append regime list to master regime list
            if country_index < 1:
                pass
            else:
                list_of_regime_lists.append(local_regime_list)
             
            #Reset local list of regimes
            local_regime_list = []
            country_index += 1      
            
            
        local_regime_list.append(int(regime))
    
    #Append last regime onto master list
    list_of_regime_lists.append(local_regime_list)
    
    return country_names, list_of_regime_lists
    

 #DONE   
def history_of_country(country,country_names,list_of_regime_lists):
    '''
    Finds which regime has existed the longest in a specified country
    Parameters
    ----------
    country : str
        Name of country in country_name list
    country_names : List
        List of every country in file
    list_of_regime_lists : List of lists
        List of every countries regime over a time period that exists in file

    Returns
    -------
    str
        Names of regime

    '''
    #Number of times each country has had a specific government
    count_0 = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    max = 0
    
    #Finds position of country in list of countries
    index = country_names.index(country)
    
    #Creates list of every regime held of specified country
    regime_history_list = list_of_regime_lists[index]
    
    #Finds total years that regimes have existed
    for item in regime_history_list:
        if item == 0:
            count_0 += 1
        elif item == 1:
            count_1 += 1
        elif item == 2:
            count_2 += 1
        elif item == 3:
            count_3 += 1
    
    #Finds which regime was in power the longest
    if count_0 > max:
        max = count_0
    if count_1 > max:
        max = count_1
    if count_2 > max:
        max = count_2
    if count_3 > max:
        max = count_3
    
    #Returns longest lasting regime
    if max == count_0:
        return "Closed autocracy"
    if max == count_1:
        return "Electoral autocracy"
    if max == count_2:
        return "Electoral democracy"
    if max == count_3:
        return "Liberal democracy"



def historical_allies(regime,country_names,list_of_regime_lists):
    '''
    Finds all countries that have had specified regime the longest

    Parameters
    ----------
    regime : string
        Name of regime in string form
    country_names : List
        List of every country in file
    list_of_regime_lists : List of lists
        List of every countries regime over a time period that exists in file

    Returns
    -------
    list_of_allies : List
        list of every country that has had the longest specified regime
    '''
    list_of_allies = []
    
    #Loops through list of countries
    for country in country_names:
        #Calls history_of_country() function to longest regimes
        regime_name = history_of_country(country, country_names, list_of_regime_lists)
        
        #Checks if current country was most often the specified regime
        if regime_name == regime:
            #Adds country to list of countries with same longest regime
            list_of_allies.append(country)
    
    
    return list_of_allies
    
    

def top_coup_detat_count(top, country_names,list_of_regime_lists):          
    '''
    Creates a list of countries that have had the most regime change 

    Parameters
    ----------
    top : int
        Number of countries that are going to be listed in final list
    country_names : List
        List of every country in file
    list_of_regime_lists : List of lists
        List of every countries regime over a time period that exists in file

    Returns
    -------
    List of Tuples
        List of tuples that contain the country and the amount of regime changes it has had
    '''
    
    num_of_coup = 0
    #index variable
    i = 0
    
    #List of countries and amount of coups   
    coup_list = []
    
    #Loops through list of lists that contain regime
    for item in list_of_regime_lists:
        #Counter variable
        counter = -1
        
        prev_gov = None
        #Loops through individual regime changes
        for gov in item:
            #Counts regime changes
            if gov != prev_gov:
                prev_gov = gov
                counter += 1
        
        coup_list.append((country_names[i], counter))
        i += 1
     
    #Sorts countries by number of regime changes           
    coup_list.sort(key=itemgetter(1), reverse = True)
    
    return coup_list[:top]


    
def main():
    fp = open_file()
    country_names, list_of_regime_lists = read_file(fp)
    
    #Output
    while True:
        print(MENU)
        user_input = input("Input an option (Q to quit): ")
        
        #Quit Function
        if user_input == 'q' or user_input == 'Q':
            break
        
        #Option 1
        if user_input == '1':
            while True:
                try:
                    country_input = input("Enter a country: ")
                    history = history_of_country(country_input, country_names, list_of_regime_lists)
                    break
                except:
                    print("Invalid country. Please try again.")
            
            
            print()
            if history[0] == "C" or history[0] == "L":
                print("Historically " + country_input + " has mostly been a " + history)
            else:
                print("Historically " + country_input + " has mostly been an " + history)
            
        #Option 2
        if user_input == '2':
            while True:
                try:
                    regime_input = input("Enter a regime: ")
                    allies = historical_allies(regime_input, country_names, list_of_regime_lists)
                    allies_list = []
                    for country in allies:
                        country_format = (country + ",")
                        allies_list.append(country_format)
                    allies_string = (' '.join(allies_list))
                    allies_string.rstrip(allies_string[-1])
                    break
                except:
                    print("Invalid regime. Please try again.")
                    
            print()
            print("Historically these countries are allies of type: " + regime_input)
            print()
            allies_list = []
            for country in allies:
                country_format = (country + ",")
                allies_list.append(country_format)
            allies_string = (' '.join(allies_list))
            print(allies_string.rstrip(allies_string[-1]))
        
        #Option 3
        if user_input == '3':
            while True:
                try:
                    top_input = input("Enter how many to display: ")
                    top_list = top_coup_detat_count(int(top_input), country_names, list_of_regime_lists)
                    break
                except:
                    print("Invalid number. Please try again.")
            
            
            print("\n{: >25} {: >8}".format("Country", "Changes"))
                  
                  
            #"{: >25} {: >8}"
            print()
            for items in top_list:
                print("{: >25} {: >8}".format(items[0], items[1]))
            
        
        
        else:
            pass
        
    
    print("The end.")

# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.  
if __name__ == "__main__": 
    main() 
