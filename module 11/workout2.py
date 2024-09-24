

def calculate_tax(amount,rate=5): # DEFAULT ARGUMENT
    return amount * (rate / 100) # RETURN THE VALUE


ans = calculate_tax(400,3)

print("Answer : ",ans)