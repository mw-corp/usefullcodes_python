#removing duplicates 
#convert list to set
my_list = [1,2,3,4,4,5,2,3,4]
print(set(my_list))
#output {1, 2, 3, 4, 5}

#function to convert string with camel case to separate by space camelCase -> camel Case
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)


#modyfying passed argument
def change_list_data (data)
    data[:]= ['NEW'] # this will overwrite data in a passed argument'
    data= ['NEW'] # this will change but only within function body / nevertheless you should not modify argument you should return new value

# unpacking list
def move_position(x, y, z):
    print (f' moving character to {x} {y} {z}')
data = [10, 20, 30]
print(move_position(*data) ) # unpacking 

