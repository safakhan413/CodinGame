'''Algo:
Output: Lucky numbers between teh range L and H
Input: 2 numbers L and H
Constraints:
Lucky nuymebrs are numebrs with 6 and 8 in its digits but not both at the same time e.g 16, 38, 666 all lucky. Non lucky:
234 and 687
Steps: convert each of the nums to string
check if 6 or 8 then lucky+1
Otherwise if 6 and 8 both or none then continue
'''

# def luckyNums(L,H):
#     lucky = 0
#     # for i in range(L,H+1):
#     #     numS = str(i)
#     #     f = ('6' in numS) + ('8' in numS)
#     #     if f == 1:
#     #         lucky +=1
#     #     else:
#     #         continue
#     # return lucky
#     num = l
#     while num <= H:
#         # m = num % 10
#         # print(num)
#         #
#         #


def is_lucky(nbr):
    nbr = str(nbr)
    return ('6' in nbr) + ('8' in nbr) == 1

def luckyNums(L,H):
    number, s = L, 0
    n_lucky_number =0
    while number <= H:
        x = is_lucky(number)
        n_lucky_number += x
        m = number % 10
        if not x and m < 5:
            number += 6-m
        else:
            number += 1
    print(n_lucky_number)

print(luckyNums(92871036442,3363728910382456))
# print(luckyNums(1,10))