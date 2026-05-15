def factorial(n):
    '''
    calculates the factorial of n
    paramaters: n(int): the number to calculate the factorial of
    returns: int: the factorial of n
    '''
    if n == 0:  #if n reaches zero
        return 1 #return 1
    return n * factorial(n - 1) #keep multiplying the n by n-1 until it reaches 0

def summation(n):
    '''
    calculates the summation of n
    paramaters: n(int): the number to calculate the summation of
    returns: int: the summation of n
    '''
    if n == 0: #if n reaches 0
        return 0 #end and return 0
    return n + summation(n - 1)  #add n - 1 to n until it reaches 0

def powers(p, n):
    '''
    calculates n to the power of p
    paramaters: n(int): the number to calulate the power of
    returns: int: n to the power of p

    '''
    if n == 0:   #if n reaches 0
        return 1 #end and return 0
    return p * powers(p, n - 1)  #multiply n by itself until it reaches 0

def sum_of_numbers_digits(n):
    '''
    calculates the sum of the digits of n
    paramaters: n(int): the number to calculate the sum of the digits of
    returns: int: the sum of the digits of n
    '''
    if n < 10:  #if n is smaller than 10
        return n #return n
    return sum_of_numbers_digits(n // 10) + n % 10 #add sum digits

def fibonacci(n):
    '''
    calculates the fibonacci of n
    paramaters: n(int) the number to calculate the fibonacci of
    returns: the fibonacci of n'''
    if n == 0: #if n reaches 0
        return 0 #return 0
    if n == 1:   #if n is 1
        return 1 #return 1
    return fibonacci(n - 1) + fibonacci(n - 2) #calculate fibonacci of n

def gcd(x, y):
    '''
    calculates the greatest common denominator of x and y
    paramaters: x,y the numbers to find the common denominator of
    returns: int: the greatest common denominator of x and y
    '''
    if y <= x and x % y == 0: #if y is bigger than or = to x and x mod y = 0
        return y #return y
    return gcd(y, x % y) #calculate greadest common denominator

def compound_interest(p, r, t):
    '''
    calculates the compound interest by taking in the principal, rate and time (years)
    paramaters p: principal amount r: rate of return t: time in years
    returns: float: the compound interest from principal, rate, and time
    '''
    if t == 0: #when time reaches 0
        return p #return principal
    return (1 + r) * compound_interest(p, r, t - 1) #calculate rate per year and - 1 from years

def product_two_num(a, b):
    '''
    calculates the product of two numbers
    paramaters: a(int),b (int) numbers to multiply
    returns: the product of a and b
    '''
    if b == 0: #if int b reaches 0
        return 0 # return 0
    return a + product_two_num(a, b - 1) #return a + b and subtract 1 from b


def main():
    while True:
        try:
            print("enter the number 1-8 corresponding to the operation you want to execute. ('q' to quit)") #give user directions
            #print options and get user choice
            choice = input("1.factorial \n" \
            "2.summation \n" \
            "3.powers \n" \
            "4.digitsum \n" \
            "5.fibonacci \n" \
            "6.gcd \n" \
            "7.compound \n" \
            "8.product\n" \
            ": ")
            #call functions for each input
            if choice == "1":
                n = int(input("enter number: "))
                print(factorial(n))
            elif choice == "2":
                n = int(input("enter number: "))
                print(summation(n))
            elif choice == "3":
                n = int(input("enter number: "))
                print(powers(n, int(input("enter exponent: "))))
            elif choice == "4":
                n = int(input("enter number: "))
                print(sum_of_numbers_digits(n))
            elif choice == "5":
                n = int(input("enter number: "))
                print(fibonacci(n))
            elif choice == "6":
                n = int(input("enter number: "))
                print(gcd(n, int(input("enter second number: "))))
            elif choice == "7":
                n = int(input("enter number: "))
                print(compound_interest(n, int(input("enter rate: ")), int(input("enter time: "))))
            elif choice == "8":
                n = int(input("enter number: "))
                print(product_two_num(n, int(input("enter second number: "))))
            elif choice == "q":
                quit()
            else:
                print("invalid")

        except ValueError:
            print("error: please enter a valid integer")
        except RecursionError:
            print("error: number too large")
        except ZeroDivisionError:
            print("error: cannot divide by zero")
        except Exception as e:
            print(f"error: {e}")

main()