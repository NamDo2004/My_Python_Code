  
sum=0  
 
num=int(input())  
 
temp=num  

while(num):  
    
    i=1  
    
    fact=1  
    rem=num%10  
    while(i<=rem):  
        fact=fact*i   
        i=i+1  
    sum=sum+fact  
    num=num//10  
if(sum==temp):  
    print("True")  
else:  
    print("False")  