
# Advanced_c 
# a math module prepared for helping students
# READ - README FILE PLEASE
# @author - Baibhab
# This code might have stupid useless long code as I am learning Python ,so apologies 
"NO EXTERNAL MODULES ARE USED !!!!!"                            



def qx(a=float(),b=float(),c=float()):
    "input a , b , c as floats.This function solves any Quadratic equations"
    alp = (-b + (b**2 - 4 *a *c)**(1/2))/(2*a) #    Quadratc Formula to find Alpha ( root )
    beta = (-b - (b**2 - 4 *a *c)**(1/2))/(2*a)# Quadratic Formula to Find Beta ( root )
    return alp,beta
def r(n=float(),e=float()):
    " returns nth root of any number , input n as number and e as nth root "
    root = n ** (1/e)
    return root
def cbx_(a=float(),b=float(),c=float(),d=float()):
    "returns One solution of cubic equation"
    x = ((((((-b)**3)/((27*a)**3))+((b*c)/((6*a)**2))-((d)/2*a))+(((((((-b)**3)/((27*a)**3))+((b*c)/((6*a)**2))-((d)/2*a))**2)+((c/(3*a))-(((b)**2)/((9*a)**2))**3))**(1/2)))**(1/3)) + ((((((-b)**3)/((27*a)**3))+((b*c)/((6*a)**2))-((d)/2*a))-(((((((-b)**3)/((27*a)**3))+((b*c)/((6*a)**2))-((d)/2*a))**2)+((c/(3*a))-(((b)**2)/((9*a)**2))**3))**(1/2)))**(1/3)) - ((b)/(3*a))   # Cubic Formula , bruh didnt knew so i googled it, i didnt know there was such thing called cubic formula
    x1 = float(str(x)[1:3])
    return x1
def cbx(a=float(),b= float(),c=float(),d=float()):
    'Returns root of a cubic equation in a list, Input a , b ,c as float'
    root = []
    for i in range(-10000,10000):
        if (a*(i**3)+b*(i**2)+c*i + d) == 0:
           root.append(i)  
    return root            
def pi():
    ' Used Leibnizs formula to find the value of Pi.'
    k =1
    s = 0
    for i in range(100000):
        if i % 2 == 0:
            s += 4/k
        else:
            s -= 4/k
        k+=2
    return s
is_odd = lambda x =float : False if x % 2 ==0 else True # one liner code YAY!
def factorial(n=float()):#fnds factorial
    if (n==0) or (n==1) :
        return 1
    else:
        return n * factorial(n-1) # used recursice !
sqr = lambda x=float() : x**2
def qx_c(a: float,b : float,c : float):
    "input a , b , c  ,Inform about the types of root"
    if a == 0:
        raise ZeroDivisionError ("a can't BE ZERO")
    x = (((b**2)-(4*a*c)))
    if x > 0 :
        print("Roots are Unequal and  real")
    elif x < 0 :
        print("roots are Complex")
    elif x == 0 :
        print("roots are real and equal")
    else:
        print("roots dont exist")
def qxr(a :float,b :float,c : float):
    "input a , b , c as floats. provides detailed summary of roots ie . sum of roots,product of roots"
    sumr = ((-b) /(a))
    pdr = (c/a)
    return [sumr,pdr]
def cnst_(a,b,c,a1,b1,c1):
    pass
def cnst(a,b,c,a2,b2,c2):
    "checks If the Equations are consistent"
    if (c and c2) == 0:
        n = "CONSISTENT"
        return n
    elif a2  == 0 :
        a1 = a
        a2 = a1
        a = 0
        # dont mind just researching here by useless code!
        b1 = b
        b = b2
        b2 = b1
        c1 = c
        c = c2
        c2 =c1
        if (a/a1) != (b/b1):
            n = "CONSISTENT"
            return n
            
        elif (a/a1) and (b/b1) ==(c/c1):
            n = "DEPENDENT"
            return n
            
        elif ((a/a1) == (b/b1)) !=(c/c1):
            n = "INCONSISTENT"
            return n           
    elif b2 == 0:
        b1 = b
        b2 = b1
        b = 0
        c1 = c
        c = c2
        c2 =c1
        a1 = a
        a = a2
        a2 = a1
        if (a/a1) != (b/b1):
            n = "CONSISTENT"
            return n
        elif (a/a1) and (b/b1) ==(c/c1):
            n = "DEPENDENT"
            return n
        elif ((a/a1) == (b/b1)) !=(c/c1):
            n = "INCONSISTENT"
            return n           
    elif c2 ==0:
        c1 = c
        c2 =c1
        c = 0
        b1 = b
        b = b2
        b2 = b1
        a1 = a
        a = a2
        a2 = a1
        if (a/a1) != (b/b1):
            n = "CONSISTENT"
            return n
            
        elif (a/a1) and (b/b1) ==(c/c1):
            n = "DEPENDENT"
            return n
            
        elif ((a/a1) == (b/b1)) !=(c/c1):
            n = "INCONSISTENT"
            return n
    elif (a/a2) != (b/b2):
        n = "CONSISTENT"
        return n
    elif (a/a2) and (b/b2) ==(c/c2):
        n = "DEPENDENT"
        return n
        
    elif ((a/a2) == (b/b2)) !=(c/c2):
        n = "INCONSISTENT"
        return n
def lnp(a,b,c):
    "UNDER CONSTRUCTION :: MAYNOT BE AVAILABLE FURTHER"
    xr = []
    yr= []
    for i in range (-10000,10000):
        x = (((-(b*i)-c)/a))
        if type(x) == float():
            xr.append(x)
            yr.append(i)
        else:
            continue
        pass
def lnpr(a,b,c,a2,b2,c2):
    "Finds the solution of a pair of linear equation"
    m = cnst(a,b,c,a2,b2,c2)
    if (c2,c) == 0:
        return [0,0]
    if m == "CONSISTENT":
        k =(a*b2)-(a2*b)
        if k  == 0:
            print(" PARALLEL OR TRY REVERSING THE EQUATIONS") 
        else:
            x = (((b*c2)-(b2*c))/((a*b2)-(a2*b)))
            y = ((((c*a2)-(c2*a))/((a*b2)-(a2*b))))
            return [x,y]
    elif m == "DEPENDENT":
        raise OverflowError("Infinite Solutions !, try changing the c or c2")                                                                                                                                                                                                                                                                                                                       # watch over flow
    elif m == "INCONSISTENT":
        raise ValueError("STFU ! EQUATIONS ARE PARALLEL")   # easter egg !
def exf(number):
    s = isprime(number)
    if s != True:
        n = pfactr(number)
        if len(set(n)) == 1:
            result = [n[0],len(n)]
        else:
            result = None
    else:
        result = None
    return result
def isprime(x : int):
    n = []
    for i in  range(2,x):
        if x %i == 0:
            n.append(i)
            continue
        else:
            continue
    if len(n) == 0:
        return True
    else:
        return False
def hcf_(x,y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i            
    return gcd
def lcm(x,y):
    z = (x*y)/(hcf(x,y))
    return z
def pfactr(n : int):
    if isprime(n) == True:
        return False
    else:
        factors = []
        divisor = 2
        while n > 1:
            while n % divisor == 0:
                factors.append(divisor)
                n //= divisor
            divisor += 1
        return factors

def hcf(*numbers):
    def calculate_hcf(x, y):
        while(y):
            x, y = y, x % y
        return x
    hcf_result = numbers[0]
    for i in range(1, len(numbers)):
        hcf_result = calculate_hcf(hcf_result, numbers[i])
    return hcf_result
# AP = ARITHMETIC PROGRESSION       # Please Read Readme , or else , you wont be able to use
def n(d= None,a : int= None,An:int = None,Sn = None):
    if Sn == None:
        n = ((An - a)/d)+1
    elif (d) == None:
        try:
            n = 2*Sn/(a+An)
        except:
            if An and Sn is None:
               raise needArgs("Please Provide Tn and Sn")
    return n 
def APn(n,a,d = None,Sn=None ):
    if (a and n and d) != None:
        An = a + (n-1)*d    
    elif Sn != None:
        An= (2*Sn)/n - a
    return An
def nSn(n):
    S = (n*(n-1))/2
    return S
def Sn(n,a,d=None,an = None):
    if an == None:
        S = n/2*(2*a + d*(n-1))
    elif d == None:
        S = (n/2)*(a+an)
    elif d and an is None:
        raise needArgs("need Arguments")
    return S
def FirstTerm(n=None,d=None,An= None,Sn = None):
    if Sn == None:
        a = An - (n-1)*d
    elif An == None:
        a = ((2*Sn) - (d*(n**2))+(d*n))/(2*n) 
    return a
def comdef(a=None,Sn= None,An=None,n=None):
    if Sn == None:
        d = (An - a)/(n-1)
    elif An == None :
        d =(2*Sn -2*a*n)/((n)*(n-1))
    return d
def AP(a = None,an= None,Sn=None,d= None,n=None):
    if (a and d) != None:
        AP = a
        if n != None:
            s = APn(n,a,d )
            return [AP , AP + d , AP + 2*d ,...,s]        
        else:
            return [AP,AP+d,AP+2*d,...]
    elif d == None:
        AP = a
        if (Sn) != None and n != None:
            s = APn(a,n,Sn=Sn)
            d1 = comdef(a,Sn= Sn,n=n)
            return [[ AP , AP + d1 , AP + 2*d1  ],d1]       
        else:
            raise needArgs()
# LOGARITHM HAHAHA (half work by me , half work (got suggestion from discord))
def log(base, number, precision=0.00001): # you can make precision more lower for better accuracy
    if exf(number=number) != None:
        n = exf(number=number)
        s = n[1]
        m = n[0]
        result = s * (log(10,m)/log(10,number =base))
    else:
        if base <= 0 or base == 1:
            return invalidInput("Base > 1")
        elif number <= 0:
            return invalidInput("naah")
        elif number == 1:
            return 0  
        result = 0.0
        increment = 0.001 # so you can set it to lower , it makes it accurate but it also makes it slower to calculate
        while abs(base ** result - number) > precision:
            if base ** result < number:
                result += increment
            else:
                result -= increment
                increment /= 2.0
    return result


class needArgs(Exception):
    def __init__(self,message):        
        self.message = "Need More Argument to Solve"
        return self.message
        
class invalidInput(Exception):
    def __init__(self,message) :
        self.message = message
        







# LOG
log2 = 0.301
log3 = 0.477
log4 = 0.602
log5 = 0.699
log6 = 0.778
log7 = 0.845
log8 = 0.903
log9 = 0.954









if __name__ == "__main__":
    "EXAMPLES HERE < HOW TO USE"
    # print(factorial(2))
    # print(qx(1,-34,-320))
    # print(sqr(-4,0.5))
    # qxr(1,0,1)
    # # cnst_(1,2,3,1,0,0) => outdated
    # # cnst(1,-1,0,1,-1,0)
    # # lnpr(1,-1,1,1,-1,0) => when reversing it may work ! so yay! you dont have to reverse in cnst cause it will do it by itself
    # lnpr(1,-4,3,1,-1,6)f
    # print(hcf(3,9))
    # print(lcm(195,165))
    # s = (4) *(3**(1/2))
    # print(qx(1,-s,3))
    # sub = lambda x = float(),y = float() : x - y
    # k =list(map(sub,qxr(1,-s,3)))
    # print(k)
    # lnpr(2,3,7,1,3,6)
    # print(qx(1,99,127))
    # print(sqr(99))
    # print(qx(1,0,-324))
    # print(hcf(384,12))
    # print(hcf(12,24))
    # print(hcf(5,7,23))
    # print(APn(3,5,1))

    # u = Sn(n=n(5,a=200,An=500),a=200,d=5)
    # v = Sn(n=n(1,200,500),a=200,d=1)
    # print(v-u)# WORKED MAN!!!!!! 
    # print(n(d=3,a=5,An=50))
    # print(comdef(a=7,Sn=273,n=13))
    # print(Sn(n=13,a=7,an=35))
    # print(AP(a=1,Sn=1,n=20))
    # print(2**(1/10))
    # print(n(An=95,a=-1,Sn=1175))
    # # print(AP(n_=2,a=2,an =1))
    # print(log(2,8))
    # print(pfactr(57))
    # print(exf(8))
    # print(isprime(2))
    # print(pfactr(69))
    # print(n(An=69,a=1,d=1))
    # print(APn(n=3,a=5,Sn=18))
    # print(FirstTerm(n = 3,d=2,Sn=12))
    # print(AP(a=2,d=2,n=6))
    # print(comdef(a=2,n=6,An=12))
    # print(comdef(a=2,n=6,Sn=42))































































































































































































































































































































































# errors for making the math




















    # @ author = BAIBHAB
