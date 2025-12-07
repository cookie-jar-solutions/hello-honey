from honey import mock_jar
import greetings

hello = greetings.greet(name="Alice")
farewell = greetings.farewell(name="Alice")

print(hello)
print(farewell)

with mock_jar():
    print(greetings.greet(name="Alice"))
    print(greetings.farewell(name="Alice"))
