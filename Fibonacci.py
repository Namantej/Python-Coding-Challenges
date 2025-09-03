
num = int(input("Enter number wanted: "))
fib_list = []
fib_list.append(0)
fib_list.append(1)
for i in range(0,num+1):
    fib_list.append(0)
    fib_list[i+2] = fib_list[i+1] + fib_list[i]

print(fib_list)
