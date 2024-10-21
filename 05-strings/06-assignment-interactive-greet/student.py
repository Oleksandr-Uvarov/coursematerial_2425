# write your code here
def interactive_greet(): 
    user_name = input("Hello, what's your name? ")
    print(greet(user_name))

def greet(name):
    return f"Hello, {name}!"