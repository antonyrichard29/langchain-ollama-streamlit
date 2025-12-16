# LangChain + Ollama + Streamlit Chat App

This project is a simple AI chat application built using **LangChain**, **Ollama**, and **Streamlit**.  
It allows users to enter a query and receive responses from a locally running LLM.

## Tech Stack
- Python
- LangChain
- Ollama (Gemma 3 - 1B)
- Streamlit

### 1️⃣ Install Prerequisites
- Python 3.9 or above
- Ollama installed on your system

### 2️⃣ Pull the Required Model
Run the following command to download the model if not already installed:
ollama run gemma3:1b. 
You can also use your preferred Ollama model by updating the model name in the code:
llm = Ollama(model="your-preferred-model")

### 3️⃣ Run the Application
Start the Streamlit app using:
streamlit run app.py
