import math 
import matplotlib.pyplot as plt

y = 1
my_list = []
my_list_1 = []
#even_tuples = []
#odd_tuples = []
#prime_tuples = []
gen_tuples = []

while y < 25000:
    my_list.append(y)
    y += 1

#def isPrime(n) : 
  
  #  if (n <= 1) : 
   #     return False
   # if (n <= 3) : 
    #    return True
    
    #if (n % 2 == 0 or n % 3 == 0) : 
     #   return False
  
 #   i = 5
    
  #  while(i * i <= n) : 
   #     if (n % i == 0 or n % (i + 2) == 0) : 
    #        return False
     #   i = i + 6
  
    #return True

for i in range(len(my_list)):
    z = my_list[i]
    my_list_1 = [z]
    x = 0
    while x < 500:
        numb = my_list_1[x]
        if numb == 1:
            break
        if (numb % 2) == 0:
            var = my_list_1[x] / 2
            my_list_1.append(var)
        else:
            var = 3 * my_list_1[x] + 1
            my_list_1.append(var)
        x += 1
    gen_tuples.append((z, len(my_list_1)))
    #if isPrime(z):
     #   prime_tuples.append((z, len(my_list_1)))
    #if z % 2 == 0:
     #   even_tuples.append((z, len(my_list_1)))
    #else:
     #   odd_tuples.append((z, len(my_list_1)))
#print(even_tuples)
#print(odd_tuples)
#print(prime_tuples)
#plt.scatter(*zip(*even_tuples))
#plt.scatter(*zip(*odd_tuples))
plt.scatter(*zip(*gen_tuples), 0.5)
#plt.scatter(*zip(*prime_tuples))
plt.xlabel("Initial value")
plt.ylabel("Stop count")
plt.title("Hailstone Sequence: Initial values and corresponding stop counts")
plt.show()

