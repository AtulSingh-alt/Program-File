# Power of a number using function
def compute_value(base,exponent):
    result=1
    while exponent!=0:
        result = result*base
        exponent=exponent-1
    return (f"The compute value is : {result}")

base= int(input("Enter the base number: "))
exponent= int(input("Enter the exponent number: "))
print(compute_value(base,exponent))
