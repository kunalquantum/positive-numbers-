positive_list = []
n = int(input("Enter the lower bound of the list "))
m = int(input("Enter the upper bound of the list "))
# Check range
if n & m <0:
    print("There is no positive number in the given range")
else:
# Using for loop
    for i in range(n,m+1):
        if i >= 0:
            positive_list.append(i)
    print("Positive numbers in the given range {0} and {1} using for loop are {2}".format(n, m, positive_list))