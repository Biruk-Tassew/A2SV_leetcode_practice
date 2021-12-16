#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    integerArr = []
    for i in grades:
        if(i >= 38):
            if(i%5==0):
                integerArr.append(i)
            elif(i%5 >= 3):
                integerArr.append(i + (5-i%5)) 
            else:
                integerArr.append(i)    
        else:
            integerArr.append(i)
    return integerArr
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
