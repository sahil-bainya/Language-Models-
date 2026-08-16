# Language Models

Language Models are AI systems designed to process, generate, and understand natural language text.

## 📚 LLMs vs Chat Models

### LLMs (Base Models)
- **General-purpose models** used for raw text generation
- Take a string (plain text) as input and return a string (plain text)
- Traditionally older models, not used much now

### Chat Models
- Language models specialized for conversational tasks
- Take a sequence of messages as inputs and return chat messages as outputs
- Traditionally newer models, used more compared to LLMs

---

## 📊 Feature Comparison

| Feature | LLMs (Base Models) | Chat Models (Instruction-Tuned) |
|---------|-------------------|----------------------------------|
| **Purpose** | Free-form text generation | Optimized for multi-turn conversations |
| **Training Data** | General text corpora (books, articles) | Fine-tuned on chat datasets (dialogues, user-assistant conversations) |
| **Memory & Context** | No built-in memory | Supports structured conversation history |
| **Role Awareness** | No understanding of "user" and "assistant" roles | Understands "system", "user", and "assistant" roles |
| **Example Models** | GPT-3, Llama-2-7B, Mistral-7B, OPT-1.3B | GPT-4, GPT-3.5-turbo, Llama-2-Chat, Mistral-Instruct, Claude |
| **Use Cases** | Text generation, summarization, translation, creative writing, code generation | Conversational AI, chatbots, virtual assistants, customer support, AI tutors |

---

# 🚀 Setup Guide

## Prerequisites
- Python 3.8 or higher
- VS Code (recommended)

## Installation Steps

### 1. Initialize Project
```bash
# Create a fresh directory
mkdir my-langchain-project
cd my-langchain-project

# Launch in VS Code
code .
```

### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\Activate

# Activate on macOS/Linux
source venv/bin/activate
```

### 3. Create requirements.txt
Create a `requirements.txt` file with the following dependencies:

```txt
# LangChain Core
langchain
langchain-core

# OpenAI Integration
langchain-openai
openai

# Anthropic Integration
langchain-anthropic

# Google Gemini Integration
langchain-google-genai
google-generativeai

# Hugging Face Integration
langchain-huggingface
transformers
huggingface-hub

# Environment Variables
python-dotenv

# Machine Learning Utilities
numpy
scikit-learn
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Verify Installation
```python
# Test your setup
from langchain.llms import OpenAI
print("LangChain setup successful!")
```

---

# 📦 Required Libraries

| Category | Libraries |
|----------|-----------|
| **LangChain Core** | `langchain`, `langchain-core` |
| **OpenAI Integration** | `langchain-openai`, `openai` |
| **Anthropic Integration** | `langchain-anthropic` |
| **Google Gemini** | `langchain-google-genai`, `google-generativeai` |
| **Hugging Face** | `langchain-huggingface`, `transformers`, `huggingface-hub` |
| **Environment** | `python-dotenv` |
| **ML Utilities** | `numpy`, `scikit-learn` |

---

# 🐍 Python Virtual Environment Guide

## What is a Virtual Environment?
A virtual environment (venv) creates a dedicated, isolated space for your project and its specific dependencies. It:
- Prevents versioning issues and library conflicts between Python projects
- Is functionally equivalent to `node_modules` in Node.js development

## Commands

### Create Environment
```bash
python -m venv venv
```
- `python` - Python interpreter
- `-m venv` - Runs the built-in venv module
- `venv` - Name of the environment folder

### Activate Environment
```bash
# Windows
venv\Scripts\Activate

# macOS/Linux
source venv/bin/activate
```
- Initializes the environment in your terminal
- Forces terminal to use localized Python and pip
- `(venv)` prefix appears in prompt when active

### Install Dependencies
```bash
pip install -r requirements.txt
```
- `pip` - Python package manager
- `-r` - Read requirements from file
- Packages install to: `venv/Lib/site-packages/`

### Deactivate
```bash
deactivate
```

---

# 🔄 Python vs Node.js Comparison

| Python Ecosystem | Node.js Ecosystem |
|------------------|-------------------|
| `pip` | `npm` |
| `requirements.txt` | `package.json` |
| `site-packages` | `node_modules` |
| PyPI | npm registry |
| `venv` | isolated project environment |

---

# 💻 Project Structure

```
my-langchain-project/
├── venv/                    # Virtual environment
├── requirements.txt         # Dependencies
├── .env                    # Environment variables
├── .gitignore              # Git ignore file
├── main.py                 # Main application
└── README.md               # This file
```

---

# 🔑 Environment Variables

Create a `.env` file in your project root:

```env
# OpenAI
OPENAI_API_KEY=your_openai_api_key

# Anthropic
ANTHROPIC_API_KEY=your_anthropic_api_key

# Google
GOOGLE_API_KEY=your_google_api_key

# Hugging Face
HUGGINGFACE_API_KEY=your_huggingface_api_key
```

Load them in your code:
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
```

---

# ✅ Quick Start Example

```python
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result= llm.invoke("what is the capital of india")

print(result)
```

---

# 📝 Notes

- Always activate your virtual environment before installing packages or running your code
- Keep your `requirements.txt` updated when adding new dependencies:
  ```bash
  pip freeze > requirements.txt
  ```
- Add `venv/` to your `.gitignore` file
- Never commit your `.env` file with actual API keys to version control

---

## 📚 Resources

- [LangChain Documentation](https://python.langchain.com/docs/)
- [OpenAI Documentation](https://platform.openai.com/docs)
- [Python venv Documentation](https://docs.python.org/3/library/venv.html)

---

**Happy Coding!** 🎉
