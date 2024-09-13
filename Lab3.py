# #ques->
print("Finding squares of number->")
n=int(input("Enter the number : "));
i=1
while(i<=n):
    print(i," ",i*i)
    i+=1

# #ques->2
print("Sum of Digits->")
num=int(input("Enter the number : "))
count=0
sum=0
print("Number is : ",num)
while(num>0):
    count=num%10
    sum+=count
    num//=10
print("Sum = ",sum)

#ques->3
print("Printing Fabonacci sequence->")
term=int(input("Enter the terms : "))
a=0
b=1
sum=a+b
print(a,"",b," ",end='')
j=0
while(j<term-2):
    print(sum," ",end='')
    a=b
    b=sum
    sum=a+b
    j=j+1
print("\n")

# #ques->4
print("Printing Table->")
table=int(input("Enter the number : "))
limit=int(input("Limit : "))
for i in range(1,limit+1):
    print(table*i)

#ques->5
print("Counting occurence of character->")
str=input("Enter the string : ")    
Isvalid=True
for i in range(0,len(str)):
    if(str[i]>='a' and str[i]<='z'):
        continue
    elif(str[i]>='A' and str[i]<='Z'):
        continue
    elif(str[i]>='0' and str[i]<='9'):
        continue
    else:
        Isvalid=False
print(Isvalid)

#ques->6
str1=input("Enter string : ")
ch=input("Enter the char to be find : ")
count=0
for i in range(0,len(str1)):
    if(str1[i]==ch):
        count=count+1

if(count>0):
    print("Occurence of",ch,"is = ",count)        
else:
    print(ch," Not occur in string")    