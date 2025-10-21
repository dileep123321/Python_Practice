# Paying a utility bill with error handling

try:
    bill_amount = float(input("Enter your electricity bill amount: "))
    
    if bill_amount <= 0:
        raise ValueError("Bill amount must be positive!")  # manual exception
    
except ValueError as ve:
    print(f"Error: {ve}")  # handles wrong input or negative number
    
else:
    print(f"Payment of ₹{bill_amount} was successful!")  # runs only if no error
    
finally:
    print("Transaction attempt completed. Thank you!")  # always runs
