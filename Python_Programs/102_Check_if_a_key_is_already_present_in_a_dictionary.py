# Check if a key is already present in a dictionary
friends= {"Rachel":"Ross","Monica":"Chandler","Phoebe":"Joe"}
name= input("Enter a key here: ")
if name in friends.keys():
    print("It is present.")
else:
    print("It is not present.")
