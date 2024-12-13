"""def morning(name):
    print("good morning I hope you will have a good day",name)
a=input("enter your name:")
morning(a)"""
def add(a,d):
    return a+d
def sub(a,d):
    return a-d
def pro(a,d):
    return a*d
def div(a,d):
    return a/d
a=int(input("enter a number:"))
d=int(input("enter a number:"))
ans=add(a,d)
print("the sum of two number are:",ans)
ans=sub(a,d)
print("the sub of two number are:",ans)
ans=pro(a,d)
print("the product of two number are:",ans)
ans=div(a,d)
print("the division of two number are:",ans)