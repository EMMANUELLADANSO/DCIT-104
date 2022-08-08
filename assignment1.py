num_l=[]
y = int(input("enter till what number do you want the sum"))
for count in range(0,y):
           num_l.append(count)

total = 0 

for counter in range(0,y):
           num = num_l[counter]
           if num > 1:
              for i in range(2,num):  
                  if (num % i) == 0: 
                        
                        break  
              else:
                         total = total + num
                       
print(total)