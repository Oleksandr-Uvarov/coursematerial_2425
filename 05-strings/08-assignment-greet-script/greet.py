#!/usr/bin/env python3
def interactive_greet(): 
    user_name = input("Hello, what's your name? ")
    print(greet(user_name))

def greet(name):
    return f"Hello, {name}!"


def main():
    print("Hello")


if __name__ == "__main__":
    main()


interactive_greet()