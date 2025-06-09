# 27) Find HCF or GCD

def findhcf(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if ((x%i == 0) and (y%i == 0)):
            hcf = i
    return hcf
print(f"The HCF of the given two numbers is : {findhcf(int(input("Enter the first value: ")), int(input("Enter the second value: ")))}")