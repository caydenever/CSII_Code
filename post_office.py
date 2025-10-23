'''
Author: Cayden Ever
Sources: Mr. Campbell, Post Office instruction Sheet
Description: Returns the price it takes to ship item at the post office based on package type and zipcode. 
Date: 10.31.25
'''


def get_size(l,h,w):
    '''
    Gets the type of package based on dimensions
    
    Args:
        l(float)
        w(float)
        h(float)
    Returns:
        type(int) based on what the l,w,h fits in.
    '''
    type = 0
    # 1 = regular postcard 
    # 2 = large poster card 
    # 3 = envelope
    # 4 = large envelope 
    # 5 = package 
    # 6 = large package 
    # 0 = unmailable
    if 3.5 <= l <= 4.25 and 3.5 <= h <= 6 and 0.007 <= w <= 0.016:
        type = 1
    elif 4.25 <= l <= 6 and 6 <= h <= 11.5 and 0.007 <= w <= 0.015:
        type = 2
    elif 3.5 <= l <= 6.125 and 5 <= h <= 11.5 and 0.016 <= w <= 0.25:
        type = 3 
    elif 6.125 <= l <= 24 and 11 <= h <= 18 and 0.25 <= w <= 0.5:
        type = 4
    elif l > 24 and h > 18 and w > .5 and l + h + h + w + w <= 84:
        type = 5
    elif l + h + h + w + w > 84 <= 130:
        type = 6
    else:
        type = 0
    return type

def get_zip(zip):
    '''
    Gets the type of the zip code and returns type.
    
    Args:
        zip(int)
    Returns:
        type(int)
    '''

    if zip > 1 and zip < 6999:
        return 1
    elif zip > 7000 and zip < 19999:
        return 2 
    elif zip > 20000 and zip < 35999:
        return 3
    elif zip > 36000 and zip < 62999:
        return 4
    elif zip > 63000 and zip < 84999:
        return 5
    elif zip > 85000 and zip < 99999: 
        return 6
    else:  
        return 0
    
def calculate_cost(distance,package_type):
    '''
    Calculates cost based on distance and package_type.

    Args:
        distance(int)
        package type(int)
    Returns:
        cost(int)
    '''
    cost = 0
   
    #if package is a regular post card
    if package_type == 1:
        cost +=.20
        cost+= distance*.03
    #if package is a large post card
    elif package_type == 2:
        cost +=.37
        cost += distance*.03
    #if package is an envelope
    elif package_type == 3:
        cost += .37
        cost += distance*.04
    #if package is a large envelope
    elif package_type == 4:
        cost += .60
        cost += distance*.05
    #if package is a package
    elif package_type == 5:
        cost += 2.95
        cost += distance*.25
    #if package is a large package
    elif package_type == 6:
        cost += 3.95 
        cost += distance*.35
    #if it fits none of the types
    else:
        return ("UNMAILABLE")
    return cost

def main ():
    tries = 5
    #give the user 5 tries
    while tries > 0:
        #get data from the user in floats for dimensions, and int for zipcodes
        data = input("enter the length, height, width, start zicode, end zicode. Seperated all data by commas:").split(",")
        l = float(data[0])
        h = float(data[1])
        w = float(data[2])
        your_zip = int(data[3])
        delivery_zip = int(data[4])

        #convert zips into their zones
        zip1 = get_zip(your_zip)
        zip2 = get_zip(delivery_zip)
        #get total distance by finding the difference of the zips
        total_distance = abs(zip2 - zip1)
        #get package type
        package_type = get_size(l,h,w)
        #calculate the cost by putting distance and package type into the function
        cost = calculate_cost(total_distance, package_type)
        #print the cost without the zero and only 2 integers
        if cost == "UNMAILABLE":
            print (f"{cost}")
        else:
            print(f"{cost:.2f}".lstrip("0")) 
        tries -=1
main()
