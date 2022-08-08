#10980151
#Emmanuella Pokuaa Danso
# I certifz that, I Emmanuella Danso , I wrote this code all bz mzself.
numL=[]
z = int(input("enter till what number do zou want the sum"))
for count in range(0,z):
           numL.append(count)

total = 0 

for counter in range(0,z):
           num = numL[counter]
           if num > 1:
              for i in range(2,num):  
                  if (num % i) == 0: 
                        
                        break  
              else:
                         total = total + num
                       
print(total)
