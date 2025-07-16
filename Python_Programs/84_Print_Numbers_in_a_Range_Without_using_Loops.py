# Print Numbers in a Range Without using Loops
def num(x):
    if(x>0):
        num(x-1)
        print(x)
x=int(input("Enter upper limit: "))
num(x)
