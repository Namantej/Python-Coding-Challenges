
#Swapping w/ temp

def temp(a,b):
    temp = a
    a = b 
    b = temp
    return a,b


#Swapping without temp
swap_list = [] 
def notemp(x,y):
    swap_list.append(x)
    swap_list.append(y)
    x = swap_list[1]
    y = swap_list[0]
    return x,y

def no_temp(x,y):
   x = x+y
   y = x-y
   x = x-y
   return x,y

a = input("Enter a: ")
b = input("Enter b: ")

a,b = no_temp(int(a),int(b))
print("a value:", a)
print("b value:", b)
