# Descending Order
# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
# Examples:
# Input: 42145 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321

def descending_order(num:int) -> int:
    list_num = [str(i) for i in str(num)]
    list_num.sort(reverse=True)
    return int(''.join(list_num))
