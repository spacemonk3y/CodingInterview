
# https://practice.geeksforgeeks.org/problems/print-the-pattern-set-1/1

def printPat(n):
    #Code here
    total = ""
    k = n
    while k>0:
        j=n
        while j>0:
            for x in range(k):
                total = total + str(j) + " "
            j-=1
        k-=1
        total = str(total) + "$"
    print(total)

printPat(3)