# Ex 1 & 2

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

if user_age < 16:
    print("You are too young to vote and too young to drive.")
elif user_age < 18:
    print("You are too young to vote.")
else:
    print("You are eligible to vote.")

if user_age == 100:
    print("Wow! A century old!")
    
# Ex 3

topics_list = ["machine learning","ai","neural networks","foo_bar","milk"]
for topic in topics_list:
    print(topic)

# ex 4

from collections import namedtuple

Item = namedtuple("Item", ["name","watts", "hours"])

items = [
    Item("refrigerator", 20, 12),
    Item("food_processor", 12, 4),
    Item("dryer", 30, .5)
]

def calculate_consumption(watts, hours):
    return watts * hours

for device in items:
    consumption = calculate_consumption(device.watts, device.hours)
    print(f"{device.name} Watts per hour: {consumption}")


# ex 5
distance_to_stop = 40
while distance_to_stop > 0:
    print(f"Distance to stop: {distance_to_stop} meters")
    distance_to_stop -= 2
   
print("Stopping...")

