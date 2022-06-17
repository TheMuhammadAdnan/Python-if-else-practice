def evenodd(a):
    if a%2==0:
        if a>=2 and a<=5:
                return "not weird"
        else:
            if a>=6 and a<=20:
                return "weird"
            if a>20:
                return "not weird"
    else:
        return "weird"                     
a = int(input("Please enter number : "))
ans = evenodd(a)
print("return value is")
print(ans) 
            
