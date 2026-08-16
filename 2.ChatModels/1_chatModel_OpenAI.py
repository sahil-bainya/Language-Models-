from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4" ,temperature=0, max_completion_tokens=10)
# temperature is a parameter that controls the randomness of a language model's output. It affects how creative or deterministic the responses are.
# -> Lower values (0.0-0.3) More deterministic and predictable.
# -> Higher values (0.7-1.5)More random, creative, and diverse.
# Use Case
# Recommended Temperature
# Factual answers (math, code, facts) - 0.0
# Balanced response (general QA, explanations) - 0.5-0.7
# Creative writing, storytelling, jokes - 0.9-1.2
# Maximum randomness (wild ideas, brainstorming) - 1.5+

result = model.invoke("what is the capital of india")

print(result.content)

