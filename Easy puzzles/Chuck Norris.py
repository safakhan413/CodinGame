import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(7) for x in s] # zfill just puts in the 0s to make teh strong as longa s you like e.g. here 7

res = string2bits(message)
newS = ''
for x in res:
    newS = newS + x
is_one = False
first_one = False
first_zero = False
final_string = ''
for ind,i in enumerate(newS):
    if i == '1':

        if not is_one:
            first_one = True
        is_one = True
        if first_one:
            if ind !=0:
                final_string = final_string + ' 0 0'
            else:
                final_string = final_string + '0 0'
            first_one = False
        else:
            final_string = final_string + '0'
    else: ## only when 0 occurs
        if is_one or ind ==0:
            first_zero = True
        is_one = False
        if first_zero:
            if ind == 0:
                final_string = final_string + '00 0'
            else:
                final_string = final_string + ' ' + '00 0'
                first_zero = False
        else:
            final_string = final_string + '0'


print(final_string)

