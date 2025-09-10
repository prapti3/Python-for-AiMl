# Types of Arguments

def add(a,b):
    print(f"{a} + {b} = ", a+b)
    
add(2,3) 

def intro(name,age):
    print(f"I am {name} and I am {age} years old.")

intro(age = 34, name = "prapti")


def greet(name = "Prapti"):  #default parameter value is set
    print(f"Hello {name}!!")
    
greet("Rahul")
greet()  # default value is used

