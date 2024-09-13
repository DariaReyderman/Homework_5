# START

counter: int = 1
age: float = float(input("How old are you? "))

while age >= 18 and counter <= 10:
    counter += 1
    print("Enjoy your beer! ")
    beers_left: int = int(input("Beers left: "))
    age: float = float(input("How old are you? "))

if counter == 11:
    print("Oh no! We're out of beer :( ")
else:
    print("You are too young for beer...")


# STOP
