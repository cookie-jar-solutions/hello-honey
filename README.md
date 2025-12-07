# Hello World for Using the honey library

## A Review from ChatGPT
Below is the **same minimal chatbot**, rewritten using the **traditional OpenAI Python client**, followed by a **direct comparison** of the two approaches.

---

## 1. Equivalent chatbot using the OpenAI library

Assumes:

* You’re running an OpenAI-compatible server (e.g. Ollama) at `http://localhost:11434/v1`
* You want chat-style interaction
* You manually manage messages and prompts

```python
"""Minimal chatbot example using OpenAI client."""

from openai import OpenAI

from system import chatbot  # type: ignore

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="not-required",  # ignored by Ollama
)

messages = [
    {"role": "system", "content": chatbot()}
]

while True:
    user_input = input("You: ")

    if user_input.lower() in ("quit", "exit"):
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gemma3:4b",
        messages=messages,
    )

    assistant_text = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_text})

    print(f"Bot: {assistant_text}\n")
```

---

## 2. Your Honey version (for reference)

```python
"""Minimal chatbot example using Honey framework."""

import honey
from honey import openai_compatible_jar
from system import chatbot  # type: ignore
from greetings import blank  # type: ignore

jar = openai_compatible_jar(
    model="gemma3:4b",
    base_url="http://localhost:11434/v1",
    system_prompt=chatbot()
)

with jar:
    while True:
        user_input = input("You: ")

        if user_input.lower() in ['quit', 'exit']:
            break
        
        response = blank(text=user_input) 
        print(f"Bot: {response}\n")
```

---

## 3. Compare & contrast (the important part)

### A. Mental model

| Aspect      | OpenAI client         | Honey                        |
| ----------- | --------------------- | ---------------------------- |
| Abstraction | Low-level API calls   | High-level prompt runtime    |
| State       | You manage `messages` | Jar owns conversation state  |
| Prompting   | Inline strings        | Named prompt functions/files |
| Scope       | Imperative            | Declarative                  |

**Key shift:**
OpenAI = *conversation as data*
Honey = *conversation as program*

---

### B. Prompt management

**OpenAI**

* Prompts are:

  * Inline strings
  * Easy to accidentally tangle logic + text
* Reuse = copy/paste or template strings

**Honey**

* Prompts are:

  * First-class functions/files (`blank`, `chatbot`)
  * Composable
  * Testable on their own

This is the single biggest structural difference.

---

### C. State & context

**OpenAI**

```python
messages.append(...)
```

You:

* Decide what gets remembered
* Decide truncation
* Decide ordering
* Decide system updates

**Honey**

```python
with jar:
    response = blank(text=...)
```

Jar:

* Owns message history
* Handles system prompt injection
* Handles compatibility quirks
* Encourages cleaner boundaries

Honey trades *control* for *correctness by default*.

---

### D. Extensibility

| Feature           | OpenAI         | Honey     |
| ----------------- | -------------- | --------- |
| Multiple prompts  | Manual routing | Natural   |
| Prompt reuse      | Weak           | Strong    |
| Prompt testing    | Awkward        | Easy      |
| Swapping backends | Medium         | Very easy |
| Long-lived apps   | Messy          | Cleaner   |

OpenAI scales well for **scripts**.
Honey scales well for **systems**.

---

### E. When to use which

**Use OpenAI directly when:**

* You want raw control
* You’re prototyping fast
* You’re inside a notebook or script
* You don’t care about prompt structure yet

**Use Honey when:**

* Prompts are *assets*
* You need separation between logic and language
* You expect many prompts or behaviors
* You want OpenAI/Anthropic/Ollama interchangeability
* You’re building something with longevity

---

## Bottom line (no fluff)

OpenAI client:

> “Make a request, get a response.”

Honey:

> “Build a language runtime.”

If you’re writing throwaway glue code → OpenAI is fine.
If you’re building a real product or framework → Honey is the right abstraction.

If you want, next we can:

* Refactor the OpenAI version **toward** Honey-style structure
* Show how Honey handles **tool calls / routing**
* Compare to LangChain / DSPy / Promptfoo directly
