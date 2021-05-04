def spiralize(size, n=1):
   total = sum(all_numbers)

   #realized that the 4 corners increase by twos (2nd ring adds 2, 3rd ring adds 4, 4th ring adds 6)
d = 1 #starting value is 1
n = 3 #n is dimension, and first dimension is 3x3
m = 0
total_sum = 0

while n <= 501: #change the value here to get nxn matrix
    m = m + 2 #the increase in each corner based on dimension, starting dimension is 2
    a = d + m
    b = a + m
    c = b + m
    d = c + m

    sum_corners = a + b + c + d
    total_sum += sum_corners
    n += 2

actual_total_sum = total_sum + 1 #I needed to add back in the initial 1 at the end
    
print(actual_total_sum)

#tried putting this into a function and couldn't get it to work with returning the values
#for some reason it won't work unless I keep the total = sum(all_numbers) even though it isn't used
