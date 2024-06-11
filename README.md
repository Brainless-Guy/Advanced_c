# Advanced C
 -A module Library to solve mathmatical numbers
-please ignore small mistakes as I am learning Python

# How to use (All Functions Explained!)

Download the Module by this command ( on linux or Windows if you have git)
>`$ git clone https://github.com/Brainless-Guy/Advanced_c.git`

- After Downloading , Place the module on the same place where the project exists on which you want to import the module
>  `import advanced_c`
OR
> `import advanced_c as avc`
EXAMPLES :
- `print(advanced_c.qx(a,b,c))` OR `print(avc.qx(a,b,c))`

- `print(advanced_c.r(16,2))` OR `print(avc.r(16,2))`
# ***Usage*** :-
" Note Please use print and it return the result not print it " example : print(qx(a,b,c)) -> Output : [x,y,z]
1. > qx(a,b,c)
- solve any quadratic equation
- input as a = ax**2 , b = bx , c  [ax**2+bx+c]
- The Output which be in list with [alpha,beta]

2. > r(n,e) n -> number , e -> eth root 
- Example : To find root 16 , you will need to put r(16,2) and to find cube root r(8,3) e = eth root
- _***print(r(32,5))  -> output : 5***_

3. > cbx(a,b,c,d) 
- Returns root of a cubic equation in a list, Input a , b ,c ,d as integer or float
- The output will be in list form
- a = a from a x **3 , b = b from b x **2 , c = c from c x ** 1 , d = d
- - The Output which be in list with [alpha,beta,gamma]

4. > pi() = 3.14

5. > is_odd = checks if the number is odd ,
- example is_odd(5) -> output : True
- _***is_odd(2)*** - > False

6. > factorial(n) , finds the factorial of any number 
- Example ***print(factorial(4))*** = 4*3*2*1 = Output : 24

7. > qx_c(a , b, c) 
- Tells you about the  root : whether the roots are real /complex/ Unequal / equal
- It doesnt return it prints , so you may not use print here
8. > qxr(a, b, c)
- finds sum and product of roots
- the sum and product output will be in list [sum,product]
9. > cnst(a,b,c,a2,b2,c2):
- checks whether the equation is consistent,inconsistent, dependent
- a , b , c = from first equation , a2 , b2 ,c2 = from second equation
- you need to print the function
- Example = ***print(cnst(2,3,4,2,3,4))*** : Output: DEPENDENT

10. > lnpr(a,b,c,a2,b2,c2)
- "Finds the solution of a pair of linear equation"
- note that if c2 is zero , you need to reverse it 
- Output : [x,y]

11. > exf(number)
- finds exponential form of perfect numbers 
- example : ***print(exf(32))*** : ***Output : [2,5]*** . output format [base,exponent/power]

12. > isprime(number)
- Example ***print(isprime(19))*** : Output : True
- ***print(isprime(1009))*** : Output : True
- helps to find if the number is prime any large number not bigger then overflow limit

13. > lcm(x,y):                " sorry for now it couldnt do multiple numbers"  
- finds lcm
- ***print(lcm(2,4))*** , output: 4
14. > hcf(*args)  
- it can find hcf of multiple number
- ***print(hcf(2,3,5,7,11))*** -> Output: 1

15. > pfactr(number): 
- prime factorise any number
- the result will be in list
- Example: _***print(pfactr(69))***_ -> Output: [3,23]
> _***" ARITHMETIC PROGRESSION "***_ {sed, was hard} _***please Read The Following :-***_
16. n(a= , d= , An=  , Sn =)      
- find the n (number of terms ) or in which term An exists
- Listen Here, you need to specify things now like print(n(a = 1, d =1 , An=69)) output -> 69
- a  = first term
- d = common difference
- An = nth Term
- If you dont need Sn , dont specify
- But if you dont have d and you have Sn  specify Sn
- Example : _***print(n(An=4,a=1,Sn = 10))***_  -> Output : 4

17. > APn(n,a,d = None,Sn=None )

- Finds the nth term of an AP
- if you have d  , leave  Sn
- if you have Sn . leave d
- _***print(APn(n=3,a=5,d=1))***_ : Output : 7
- _***print(APn(n=3,a=5,Sn=18))***_ :Output : 7

18. nSn(n) : sum of natural number
- Example _***nSn(10)***_ = 45 = [`(10*9)/2`]

19. > Sn(n,a,d=None,an = None)
- finds sum of terms of an AP
- specify an if d is not present
- specify d if an is not present
- Example : _***Sn(n = 10,a = 1 , d = 1)***_ : _Output_ : 55
- Example : _***Sn(n = 10,a = 1 , an = 10)***_ : _Output_ : 55

20. > FirstTerm(n=None,d=None,An= None,Sn = None)
- Finds a or first term
- Specify Sn only if you dont have An
- Specify An only if you dont have Sn
- Example _***print(FirstTerm(n = 3,d=2,Sn=12))***_ : _Output_: 2
- _***print(FirstTerm(n = 3,d=2,An=6))***_ : _Output_: 2

21. > comdef(a=None,Sn= None,An=None,n=None)
- finds common difference
- if you dont have Sn , specify An
- if you dont have An , specify Sn
- Example _***print(comdef(a=2,n=6,An=12))***_ : _Output_ : 2
- Example _***print(comdef(a=2,n=6,Sn=42))***_ : _Output_ : 2


22. >  AP(a = None,an= None,Sn=None,d= None,n=None)
- Provides Ap upto 3 terms
- Provide what you have BRUH

>> _***LOGARITHM***_ 


23. > log(base, number)
- finds log of any number
- used Taylor series but it is automated to approximation as taylor series takes alot of time 

- Example _***print(log(2,8))***_ OUTPUT : 3
