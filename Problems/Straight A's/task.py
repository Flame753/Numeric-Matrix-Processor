# put your python code here
grades = str(input())
list_of_grades = grades.split()
number_of_A = list_of_grades.count('A')
ratio = number_of_A/len(list_of_grades)
print(round(ratio, 2))
