#get size (l,w h)
#Get zip (from,to)
#get Cost ()

def get_size(l,w,h):
    #Key 1 = regular postcard 2 = large poster card 3 = Envelope = 4 
    if 4.25 > l > 3.5 and 6 > h > 3.5 and .016 > w > 0.007:
        type = 1
    elif 6 > l > 4.25 and 11.5 > h > 6 and .015 > w > 0.007:
        type = 2
    elif 6.125 > l > 3.5 and 11.5 > h > 5 and .025 > w > .016:
        type = 3 
    elif 24 > l > 6.125 and 18 > h > 11 and .5 > w > .25:
        type = 4
    elif l > 24 and h > 18 and w > .5 and l + h + h + w + w <= 84:
        type = 5
    elif l + h + h + w + w > 84 <= 130:
        type = 6
    return type

def get_zip(zip):
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


def main ():

    data = input("please enter the length, width, height, start zicode, end zicode. Seperated all data by commas:").split(",")
    l = float(data[0])
    w = float(data[1])
    h = float(data[2])
    your_zip = int(data[3])
    delivery_zip = int(data[4])
    package_type = get_size(l,w,h)
    print (f"{package_type}")
    print(f"{l},{w},{h},{your_zip},{delivery_zip}")

main()


