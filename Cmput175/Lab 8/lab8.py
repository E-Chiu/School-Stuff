def main():
    # exercise 1
    alist = [43, 76, 97, 86]
    print(mylen(alist))
    # exercise 2
    n = int(input('Enter an integer dividend: '))
    m = int(input('Enter an integer divisor: '))
    print('Integer division', n, '//', m, '=', intDivision(n,m)) 
    # exercise 3
    number = int(input('Enter a number:'))
    print(sumdigits(number)) 
    # exercise 4
    number = int(input('Enter a number:'))
    print(reverseDisplay(number))
    # exercise 5
    some_list = [-8,-2,1,3,5,7,9]
    print(binarySearch2(9,some_list,0,len(some_list)-1))
    print(binarySearch2(-8,some_list,0,len(some_list)-1))
    print(binarySearch2(4,some_list,0,len(some_list)-1)) 



# exercise 1
def mylen(someList):
    '''
    This function points to a smaller list each time until the list is empty
    inputs: list
    output: list size
    '''
    if someList == []:
        return 0
    return mylen(someList[1:]) + 1

# exercise 2
def intDivision(n, m):
    '''
    subtracts denominator from numerator to mimic division
    inputs: numerator, denominator
    outputs: quotient
    '''
    assert n >= 0 and m > 0, "invalid input"
    if n - m < 0:
        return 0
    return intDivision(n - m, m) + 1

# exercise 3
def sumdigits(number):
    '''
    adds the digits of a number together
    input: number
    output: sum of digits
    '''
    if number % 10 == number:
        return number
    assert number > 0, "invalid input"
    # convert to string for cutting then back to int for summing
    digit = int(str(number)[0])
    newNum = int(str(number)[1:])
    return sumdigits(newNum) + digit

# exercise 4
def reverseDisplay(number):
    '''
    reverses order of number
    input: number
    output: reversed number
    '''
    if number == '':
        return number
    # convert to string for cutting
    digit = str(number)[0]
    newNum = str(number)[1:]
    return reverseDisplay(newNum) + digit

# exercise 5
def binarySearch2(key, alist, low, high):
    '''
    returns location of key, or lack therof
    inputs: key
    outputs: location
    '''
    # split list into two
    middle = (high + low) // 2
    # check if the key is higher or lower than the current position
    if key == alist[middle]:
        return middle
    elif high == low:
        return 'Item is not in the list'
    elif alist[middle] < key:
        # if key is higher check the top half of current list
        return binarySearch2(key, alist, low + 1, high)
    elif alist[middle] > key:
        # if key is lower check the bottom half of the current list
        return binarySearch2(key, alist, low, high - 1)
    
main()