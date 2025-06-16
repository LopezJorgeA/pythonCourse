def hello(name, age):
    print("Hola " + name + ", tienes " + str(age) + " años")

# hello("Jorge",23)
# hello("Tilin", 12)

def change(value):
    value = 2
val = 1
change(val)
# print(val)

def hello1(name):
    print("hello " + name + '!')
    return

def talk(phrase):
    def say(word):
        print(word)
    words = phrase.split(' ')
    for word in words:
        say(word)
talk("I am going to buy the milk")

def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return(count)
    return increment
increment = counter()
print(increment()) #1
print(increment()) #2
print(increment()) #3