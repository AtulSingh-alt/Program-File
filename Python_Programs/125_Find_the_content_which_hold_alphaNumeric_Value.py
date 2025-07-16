name = input("Enter the sentence here :").split()
for i in name:
    for j in i:
       if '0' <= j <= '9':
            print(i,end="")
            break
