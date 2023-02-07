str = input("Enter a string:")


result = "".join(dict.fromkeys(str))
print(f"user's word {str} - output = {result}")



