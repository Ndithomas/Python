# Number of rows in the pattern
# range(rows, 0, -1) generates numbers starting from rows (which is 10) down to 1, decreasing by 1 each time.
# So, the loop will run with the following values of i: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1. 
# The expression '*' * i means that the * character is repeated i times.


rows = 10
for i in range(rows, 0, -1):
    print('*' * i)