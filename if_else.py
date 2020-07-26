n = int(input("input value"))
def weird_check(n):
    if n % 2 == 0 and (n>=6 and n<=20):
        print ("Weird")
    elif (n % 2 == 0) :
        print("Not Weird")
    else :
        print("Weird") 

weird_check(n)