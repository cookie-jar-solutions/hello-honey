"""Minimal chatbot example using Honey framework."""

import sys
import os

import honey
from honey import openai_compatible_jar
from system import chatbot # type: ignore
from greetings import blank # type: ignore

# Create jar and set system prompt
jar = openai_compatible_jar(model="gemma3:4b", 
                            base_url="http://localhost:11434/v1",
                            system_prompt=chatbot())

with jar:
    while True:
        user_input = input("You: ")

        if user_input.lower() in ['quit', 'exit']:
            break
        
        response = blank(text=user_input) 
        print(f"Bot: {response}\n")