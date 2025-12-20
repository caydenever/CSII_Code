'''
Author: Cayden Ever
Sources: Mr. Campbell, Titanic.Csv, W3schools for read/write
Description: Analyzes data from the Titanic crash dataset.
Date: 12.19.25
'''
import csv
import sys
import os

def read():
    '''
    Reads the file. 

    Args:
        None
    
    Returns:
        list: All rows from titanic.csv except the header row.
    '''
    try:
        with open("titanic.csv", newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            rows = list(reader)
            rows.remove(rows[0])  # # remove header row
            return rows
    except FileNotFoundError:
        current_directory = os.getcwd()
        print(f"Error: The file could not be found in the directory: {current_directory}")
        sys.exit()

def count_gender():
    '''
    Counts males and females in titanic.csv and writes results to write_gender.csv.

    Args:
        None

    Returns:
        None
    '''
    boys = 0
    girls = 0 
    with open('titanic.csv', 'r') as file:
        for line in file:
            row = line.strip().split(',')
            if row[5] == 'male':
                boys += 1
            elif row[5] == 'female':
                girls += 1
        
    with open('write_gender.csv', 'w', newline='') as csvfile:
        csvfile.write("males,females\n")
        data = str(girls) + ","  + str(boys)  # # girls then boys
        csvfile.write(data) 

def load_and_display(input):
    '''
    Writes the first 10 rows from input file to first_10_rows.csv.

    Args:
        input (file object): Open file object to read lines from

    Returns:
        None
    '''
    with open('first_10_rows.csv', 'w', newline='') as output:
        counter = 0
        for line in input:
            if counter >= 10:
                break
            else:
                output.write(line)
            counter = counter + 1

def calc_survival_rate(rows):
    '''
    Calculates overall survival rate and writes to survival_rate.csv.

    Args:
        rows (list): List of rows from titanic.csv

    Returns:
        None
    '''
    num_alive = 0
    total_people = 0
    out = open("survival_rate.csv", "w")
    for line in rows:
        if line[1] == "1":  # # "1" indicates survived
            num_alive += 1
        total_people += 1
    survival_rate = num_alive/total_people
    out.write("percent survived\n")
    data = str(survival_rate) 
    out.write(data)

def survival_by_gender(rows):
    '''
    Calculates survival rate by gender and writes to survival_rate_by_gender.csv.

    Args:
        rows (list): List of rows from titanic.csv

    Returns:
        None
    '''
    fem_alive = 0
    male_alive = 0
    total_male = 0 
    total_fem = 0 
    out = open("survival_rate_by_gender.csv", "w")
    for line in rows:
        if line[1] == "1" and line[4] == "male":
            male_alive += 1
            total_male += 1
        elif line[1] == "0" and line[4] == "male":
            total_male += 1
        if line[1] == "1" and line[4] == "female":
            fem_alive += 1
            total_fem += 1
        elif line[1] == "0" and line[4] == "female":
            total_fem += 1
    male_surv_rate = male_alive/total_male
    fem_surv_rate = fem_alive/total_fem
    out.write("male survival rate,female survival rate,higher survival rate\n")
    data = str(male_surv_rate) + "," + str(fem_surv_rate) + "," + ("females had a higher survival rate")
    out.write(data)

def age_analysis(rows):
    '''
    Analyzes passenger ages: averages, youngest, oldest, and survivor/non-survivor averages.

    Args:
        rows (list): List of rows from titanic.csv

    Returns:
        None
    '''
    total_age = 0
    total_people = 0
    out = open("age_analysis.csv", "w")
    for line in rows:
        if not line[5]:
            continue
        else:
            age = float(line[5])
            total_age += age
            total_people += 1
    average_age = total_age / total_people

    #average age of survivors and non-survivors
    alive = 0
    dead = 0
    total_dead_age = 0
    total_alive_age = 0
    for line in rows:
        if line[1] == "1":
            alive += 1
            if not line[5]:
                continue
            else:
                age = float(line[5])
                total_alive_age += age
        elif line[1] == "0":
            dead += 1
            if not line[5]:
                continue
            else:
                age = float(line[5])
                total_dead_age += age
    alive_age_average = total_alive_age/alive
    dead_age_average  = total_dead_age/dead
    
    youngest = 150
    oldest = 0
    
    for line in rows:
        age = 0
        age = line[5]
        if len(age) == 0:
            continue
        else:
            age = float(line[5])
        if age < youngest:
            youngest = age  # find youngest passenger
    for line in rows:
        age = 0
        age = line[5]
        if len(age) == 0:
            continue
        else:
            age = float(line[5])
        if age > oldest:
            oldest = age  # find oldest passenger
    
    out.write("average age,average age of survivors,average age of people who died, youngest passanger, oldest passengers\n")
    data = str(average_age) + ',' + str(alive_age_average) + ',' + str(dead_age_average) + ','  + str(youngest) + ',' + str(oldest)
    out.write(data)

def average_fares(rows):
    '''
    Calculates average fare for each passenger class.

    Args:
        rows (list): List of rows from titanic.csv

    Returns:
        tuple: (first_class_fare, second_class_fare, third_class_fare)
    '''
    total_first = 0 
    first_class_price = 0 
    total_second = 0
    second_class_price = 0
    total_third = 0
    third_class_price = 0
    for line in rows:
        if line[2] == "1":
            first_class_price += float(line[9])
            total_first +=1
        elif line[2] == "2":
            second_class_price += float(line[9])
            total_second += 1
        elif line[2] == "3":
            third_class_price += float(line[9])
            total_third += 1
    first_class_fare = first_class_price/total_first 
    second_class_fare = second_class_price/total_second
    third_class_fare = third_class_price/total_third
    return first_class_fare, second_class_fare, third_class_fare

def class_analysis(rows):
    '''
    Analyzes survival rate and average fare for each passenger class.

    Args:
        rows (list): List of rows from titanic.csv

    Returns:
        None
    '''
    rows = read()
    first_class_surv = 0
    total_first = 0
    for line in rows:
        if line[2] == "1" and line[1] == "1":
            first_class_surv +=1
            total_first +=1
        elif line[2]== "1" and line[1] == "0":
            total_first +=1
    first_surv_rate = first_class_surv/total_first

    second_class_surv = 0
    total_second = 0
    for line in rows:
        if line[2] == "2" and line[1] == "1":
            second_class_surv +=1
            total_second +=1
        elif line[2]== "2" and line[1] == "0":
            total_second +=1
    second_surv_rate = second_class_surv/total_second

    third_class_surv = 0
    total_third = 0
    for line in rows:
        if line[2] == "3" and line[1] == "1":
            third_class_surv +=1
            total_third +=1
        elif line[2]== "3" and line[1] == "0":
            total_third +=1
    third_surv_rate = third_class_surv/total_third

    fare1, fare2, fare3 = average_fares(rows)
    fare1_rounded = round(fare1, 2) #rounds to 2 decimal points using round function
    fare2_rounded = round(fare2, 2)
    fare3_rounded = round(fare3, 2)
    first_surv_rounded = round(first_surv_rate, 2)
    second_surv_rounded = round(second_surv_rate,2)
    third_surv_rounded = round(third_surv_rate, 2)
    
    out = open("class_analysis.csv", "w")
    out.write("First Class Survival Rate, First Class Average Fare, Second Class Survival Rate, Second Class Average Fare, Third Class Survival Rate, Third Class Average Fare \n")
    data = str(first_surv_rounded) + ',' + str(fare1_rounded) + ',' + str(second_surv_rounded) + ',' + str(fare2_rounded) + ',' + str(third_surv_rounded) + ',' + str(fare3_rounded) + ',' + ("First class passagners had the highest percent chance to surive, then second class, then third class.")
    out.write(data)

def family_survival_patterns(rows):
    '''
    Analyzes survival patterns based on family presence and writes to family_survival_patterns.csv.

    Args:
        rows (list): List of rows from titanic.csv

    Returns:
        None
    '''
    has_family = 0
    no_family = 0
    total = 0

    for line in rows[1:]:   # skip header
        sib = int(line[6])
        parch = int(line[7])

        if sib + parch > 0:
            has_family += 1
        else:
            no_family += 1

        total += 1

    no_fam_survival = no_family / total
    no_fam_surv_rounded = round(no_fam_survival, 2)
    has_fam_survival = has_family / total
    has_fam_surv_rounded = round (has_fam_survival, 2)

    out = open("family_survival_patterns.csv", "w")
    out.write("Has Family Survival Rate, No Family Survival Rate\n")
    data = str(has_fam_surv_rounded) + ',' + str(no_fam_surv_rounded) + ',' + ("People with no family had a higher chance to survive the titanic by 20%.")
    out.write(data)

def main():
    rows = read()
    while True:
        choice = input('''Menu:
                       1 = count gender count and dispay
                       2 = write the first ten rows of titanic
                       3 = calculate surival rate 
                       4 = calculate survival rate by gender
                       5 = calculate age analysis
                       6 = calculate class based analysis
                       7 = calculate family survival patterns
                       
                       Choice: ''')
        if choice == "1":
            file.seek(1)
            count_gender()
        elif choice == "2":
            file.seek(1)
            try:
                with open('titanic.csv', 'r') as file:
                    load_and_display(file)
            except FileNotFoundError:
                print("Error: 'titanic.csv' file not found.")
        elif choice == "3":
            calc_survival_rate(rows)
        elif choice == "4":
            survival_by_gender(rows)
        elif choice == "5":
            age_analysis(rows)
        elif choice == "6":
            class_analysis(rows)
        elif choice == "7": 
            family_survival_patterns(rows)

main()

