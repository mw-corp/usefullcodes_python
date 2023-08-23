#removing duplicates 
#convert list to set
my_list = [1,2,3,4,4,5,2,3,4]
print(set(my_list))
#output {1, 2, 3, 4, 5}

#function to convert string with camel case to separate by space camelCase -> camel Case
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
