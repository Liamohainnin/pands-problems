# Liam O Hainnin    
# Check if one number divides another


m = 2
p = int(input ("Please enter a positive integer:"))

while m <= p :
    if p  %  m == 0:    # modulus remainder of numbers divided together
        p = p / 2
        print(p , end = ' ')

    else:
        p = (p*3)+1
        print(p , end = ' ')

