# 4_program :find the factor of input number

num=int(input("Enter your no: "))

for i in range(1,num+1):

    if num%i==0:
        print(i)
