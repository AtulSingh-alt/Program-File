# def rev_str(s):
#     rev = ''
#     i = 0
#     while i < len(s):
#         rev = s[i] + rev
#         i += 1
#     return rev
# s = input("Enter a string: ")
# print("Reversed string:", rev_str(s))

w= input("enter the word")
rev=''
for i in range(len(w)-1,-1,-1):
    rev= rev + w[i]

print(rev)