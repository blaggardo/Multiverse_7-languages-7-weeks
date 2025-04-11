# Ex 1

name = "David"
city = "Burlingame"
temp = 25

print(f"Hi, I'm {name} from {city} . It's {temp} °C right now")

#Ex 2

if temp > 30:

    print("It's hot out today")

elif temp >= 20 and temp < 30:
    print("Nice Weather")
else:
    print("Kinda chilly.")

#Ex 3

loads = {
    "tor-1": 65,
    "nyc-2": 87,
    "la-3": 74,
    "lon-4": 91,
    "syd-5": 55
}
for location, load in loads.items():
    status = "OK" if load < 90 else "OVERLOADED"
    print(f"{location}: {load}% load - {status}")

#Ex 4

overloaded_found = False
for location, load in loads.items():
    if load > 85:
        print(f"WARNING: {location} is near critical limit!")
        overloaded_found = True

if not overloaded_found:
    print("✅ All systems nominal.")

#Ex 5

uptime_vals = [99.9, 98.5, 97.0, 99.2, 100.0]
for uptime_val in uptime_vals:
    if uptime_val < 98.0:
        print(f"{uptime_val}% Critical alert")
    elif uptime_val >= 98.0 and uptime_val < 99.0:
        print(f"{uptime_val} %Degraded")
    else:
        print (f"{uptime_val} %Healthy")

