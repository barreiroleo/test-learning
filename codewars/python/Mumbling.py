# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python
# This time no story, no theory. The examples below show you how to write function accum:
# Examples:
#
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(string:str) -> str:
    accum = []
    for i, char in zip(range(len(string)), string):
        accum.append(str(char*(i+1)).capitalize())
    return "-".join(accum)
