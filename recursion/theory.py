'''
A function that calls itself ... until it doesn't 


Example:-

imagine you have a gift box 

we run the open_gift_box() function  to open it

while we run this function we have two possiblities

1.  it returns  a ball
2.  it returns  an other gift box again


psuedo code 

def open_gift_box():
    if foundBall:
        return Ball 
    open_gift_box()

##### There are two things to remember here 
-> each time the process of opening the gift box is the same
-> each time the we open the gift box , we make the problem smaller and increase 
   our chance of getting the ball

finding our ball in base case , this is where we should stop calling our funtion
having a base case is very important in before our function call which at some point will be true
and then we need to return .
'''

# Call Stack :-

def funcThree():
    print('Three')

def funcTwo():
    funcThree()
    print('Two')

def funcOne():
    funcTwo()
    print('One')

funcOne()

"""
if we call function one
it would create a call stack
which looks like this

|          | 
|funcThree |
|funcTwo   |
|funone    | 
|__________|

first function Three would be called , then it pops from the stack
then function Two would be called , then it pops from the stack
finally function one would be called and it also pops from the stack

The out put would be something like this :

>Three
>Two
>One


"""

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

print(factorial(4))



'''
it would create a call stack like this 

|factorial(1) | -> this is our base case where we see and return 1
|factorial(2) |-> this returns 1 to this function so 2*factorial(1) becomes 2*1 =2
|factorial(3) |-> this return 2 to this function so 3*factorial(2) becomes 3*2 = 6
|factorial(4) | .
|_____________| .
                .

                until our call stack becomes empty and return 24
'''