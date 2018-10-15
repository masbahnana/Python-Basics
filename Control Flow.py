# Control flow
# if, else, elif
# while and for loops

trafficLightState = "yellow"
distanceFromLight = 10

# if trafficLightState == "green":
#     print("go")
# elif trafficLightState == "yellow" and distanceFromLight <= 15:
#     print("speed up")
# elif trafficLightState == "yellow" and distanceFromLight > 15:
#     print("slow down")
# elif trafficLightState == "red":
#     print("stop")
# else:
#     print("unknown action")

if trafficLightState == "green":
    print("go")
elif trafficLightState == "yellow":
    if distanceFromLight <= 15:
        print("speed up")
    else:
        print("slow down")
elif trafficLightState == "red":
    print("stop")
else:
    print("unknown action")

endPoint = 10
startPoint = 3
currentPos = startPoint
print(currentPos)

while currentPos < endPoint:
    currentPos += 1
    print(currentPos)

numArray = [13,53,2,67,9]

for num in numArray:
    print(num * 2)