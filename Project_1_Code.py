# Definition of Decimal NFA. Will be called if the input string is Decimal.
def decq0(n):
    if(len(n)==0):
        print("This is not a valid integer.")

    else:
        if(n[0]in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
            decq1(n[1:])

        elif(n[0]=='0'):
            decq4(n[1:])

def decq1(n):
    if(len(n)==0):
        print("This is a valid integer.")

    else:
        if(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            decq1(n[1:])

        elif(n[0]=='_'):
            decq3(n[1:])

def decq2(n):
    if(len(n)==0):
        print("This is a valid integer.")

    else:
        if(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            decq2(n[1:])

        elif(n[0]=='_'):
            decq3(n[1:])

def decq3(n):
    if(len(n)==0):
        print("This is not a valid integer.")

    else:
        if(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            decq2(n[1:])

def decq4(n):
    if(len(n)==0):
        print("This is a valid integer.")

    else:
        if(n[0]=='0'):
            decq4(n[1:])

        elif(n[0]=='_'):
            decq5(n[1:])

        elif(n[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
            print("This is not a valid integer.")

def decq5(n):
    if(len(n)==0):
        print("This is a valid integer.")

    else:
        if(n[0]=='0'):
            decq4(n[1:])

        elif(n[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
            print("This is not a valid integer.")

#-------------------------------------------------------------------------------
# Definition of Octal NFA. Will be called if the input string is Octal.
def octq0(n):
    if(len(n)==0):
        print("This is not a valid integer.")

    else:
        if(n[0]=='0'):
            octq1(n[1:])

def octq1(n):
    if(len(n)==0):
        print("This is not a valid integer.")

    else:
        if(n[0] in ['o', 'O']):
            octq2(n[1:])

def octq2(n):
    if(len(n)==0):
        print("This is not a valid integer.")

    else:
        if(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7']):
            octq3(n[1:])

        elif(n[0]=='_'):
            octq4(n[1:])

def octq3(n):
    if(len(n)==0):
        print("This is a valid integer.")

    else:
        if(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7']):
            octq3(n[1:])

        elif(n[0]=='_'):
            octq4(n[1:])

def octq4(n):
    if(len(n)==0):
        print("This is not a valid integer.")

    else:
        if(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7']):
            octq3(n[1:])

#-------------------------------------------------------------------------------
# Definition of Hexadecimal NFA. Will be called if the input string is Hexadecimal.
def hexq0(n):
    if(len(n)==0):
        print("This is not a valid integer.")

    else:
        if(n[0]=='0'):
            hexq1(n[1:])

def hexq1(n):
    if(len(n)==0):
        print("This is not a valid integer.")

    else:
        if(n[0] in ['x', 'X']):
            hexq2(n[1:])

def hexq2(n):
    if(len(n)==0):
        print("This is not a valid integer.")

    else:
        if(n[0]=='_'):
            hexq3(n[1:])

        elif(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F']):
            hexq4(n[1:])

def hexq3(n):
    if(len(n)==0):
        print("This is not a valid integer.")

    else:
        if(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F']):
            hexq4(n[1:])

def hexq4(n):
    if(len(n)==0):
        print("This is a valid integer.")

    else:
        if(n[0]=='_'):
            hexq3(n[1:])

        elif(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F']):
            hexq4(n[1:])

#-------------------------------------------------------------------------------
# Definition of Floating Point NFA. Will be called if the input string is Floating Point.
def floatq0(n):
    if(len(n)==0):
        print("This is not a valid integer.")

    else:
        if(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            floatq1(n[1:])

        elif(n[0]=='.'):
            floatq3(n[1:])

def floatq1(n):
    if(len(n)==0):
        print("This is not a valid integer.")

    else:
        if(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            floatq1(n[1:])

        elif(n[0]=='.'):
            floatq2(n[1:])

        elif(n[0] in ['e', 'E']):
            floatq5(n[1:])

        elif(n[0]=='_'):
            floatq0(n[1:])

def floatq2(n):
    if(len(n)==0):
        print("This is a valid integer.")

    else:
        if(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            floatq2(n[1:])

        elif(n[0]=='_'):
            floatq8(n[1:])

        elif(n[0] in ['e', 'E']):
            floatq5(n[1:])

def floatq3(n):
    if(len(n)==0):
        print("This is not a valid integer.")

    else:
        if(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            floatq4(n[1:])

def floatq4(n):
    if(len(n)==0):
        print("This is a valid integer.")

    else:
        if(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            floatq4(n[1:])

        elif(n[0]=='_'):
            floatq7(n[1:])

def floatq5(n):
    if(len(n)==0):
        print("This is not a valid integer.")

    else:
        if(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            floatq2(n[1:])

        elif(n[0] in ['+', '-']):
            floatq6(n[1:])

def floatq6(n):
    if(len(n)==0):
        print("This is not a valid integer.")

    else:
        if(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            floatq2(n[1:])

def floatq7(n):
    if(len(n)==0):
        print("This is not a valid integer.")

    else:
        if(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            floatq4(n[1:])

def floatq8(n):
    if(len(n)==0):
        print("This is not a valid integer.")

    else:
        if(n[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
            floatq2(n[1:])
#-------------------------------------------------------------------------------
# Define lists of accepted inputs in each type
octalVal = ['0', '1', '2', '3', '4', '5', '6', '7', '_', 'o', 'O']
decimalVal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_']
hexVal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', '_', 'x', 'X']
floatVal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', 'e', 'E','-', '+', '_']

# Ask for input
print("Enter an Octal, Decimal, Hexadecimal, or Floating Point value:")
val = input()

# Check if string is Octal
if(len(val)>1 and (val[0]=='0' and val[1] in ['o', 'O'])):
    print("Input type: Octal")
    if any(L not in octalVal for L in val):
        print("This is an invalid integer.")
    else:
        octq0(val)

# Check if string is Hexadecimal
elif(len(val)>1 and (val[0]=='0' and val[1] in ['x', 'X'])):
    print("Input type: Hexadecimal")
    if any(L not in hexVal for L in val):
        print("This is an invalid integer.")
    else:
        hexq0(val)

# Check if string is Floating Point
elif ((('.' in val) or ('e' in val) or ('E' in val)) and ((val[0] in decimalVal) or (val[0] in '.'))):
    print("Input type: Floating Point")
    if any(L not in floatVal for L in val):
        print("This is an invalid integer.")
    else:
        floatq0(val)

# Check if string is Decimal
elif any(L in decimalVal for L in val):
    print("Input type: Decimal")
    if any(L not in decimalVal for L in val):
        print("This is an invalid integer.")
    else:
        decq0(val)

# If string is none of the above, print an error.
else:
    print("This input is invalid for every type of integer literal supported.")
