password = "2919"   
num_guess = 0         

for code in range(10000):          
    guess = str(code)     
    num_guess += 1
    print("Combination tried:", guess)     

    if guess == password:         
        print("Password found:", guess)
        break              

print("Total tries:", num_guess)
