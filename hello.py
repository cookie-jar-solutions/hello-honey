from honey import mock_jar, openai_compatible_jar
import greetings # type: ignore

hello = greetings.greet(name="Alice")
farewell = greetings.farewell(name="Alice")

print(hello)
print(farewell)

print("---- Now with jars ----")
print("---- Mock Jar ----")
with mock_jar():
    print(greetings.greet(name="Alice"))
    print(greetings.farewell(name="Alice"))

print("---- OpenAI Compatible Jar ----")
with openai_compatible_jar(model="gemma3:4b", base_url="http://localhost:11434/v1"):
    print(greetings.greet(name="Alice"))
    print(greetings.farewell(name="Alice"))