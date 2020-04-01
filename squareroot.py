#   Liam O Hainnin
#   Square root caluculation function using newtons method root = 0.5 * (X + (N / X))
#   Not including approximate root guess but setting guess to value of the figure submitted for the root calc

n = float(input("Please enter a Positive Number "))

y = float('inf')      # given input of positive number wont result in infinite loop crashing program as iteration count will end while loop once root is found.

#Function for root
def sqrt(n , y):
    ans = n
    m = 0         # count number of iterations
    
    while y > 0:
        x = ans
        ans = 0.5*(ans+(n/ans))
        m = m + 1
        print (("Number of iterations and approx root"),m,ans)
        if x == ans: y = 0   # check if you have reached the absolute square root stop unneccesary loops through calculation by setting y to 0
        else: y = y - 1
        
    return round (ans,1) ,m

print (sqrt(n, y),"iterations")

