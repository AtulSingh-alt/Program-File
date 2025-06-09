# 45) Palindrome numbers with function
def is_pldm(n):
    org_num = n
    revr = 0
    while n>0:
        dig = n%10
        revr = revr*10 + dig
        n = n // 10
    return org_num == revr
print(is_pldm(int(input("Enter the number here: "))))