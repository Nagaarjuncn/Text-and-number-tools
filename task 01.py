'''Write a script that reports word count, longest word and the reverse of a sentence, then tells you whether a number is prime.'''
def wc(s):
    a=s.split()
    return len(a)
def lw(s):
    a=s.split()
    return max(a,key=len)
def rs(s):
    a=s[::-1]
    return a
def pc(b):
    f=True
    if b>1:
        for i in range(2,int(b**(1/2))+1):
            if b%i==0:
                f=False
                break
            else:
                continue
        if f==True:
            return "Prime Number"
        else:
            return "not a prime number"
    else:
        return "enter a valid integer"
c=input("enter a sentence:")
d=int(input("enter a number:"))
print(f"word count : {wc(c)}")
print(f"longest word : {lw(c)}")
print(f"reverse sentence : {rs(c)}")
print(f"prime count : {pc(d)}")
