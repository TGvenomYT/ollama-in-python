Ollama Chatbot
==============

Your project appears to be a conversational AI application using the `langchain_core` and `langchain_ollama` libraries. 
It sets up a chatbot that interacts with users in a loop, maintaining a conversation history. 
The chatbot uses a language model (`OllamaLLM`) to generate responses based on the conversation history and user input. 
The conversation continues until the user types 'exit'.


FEATURES
========

1. **Conversational AI**: The chatbot interacts with users in a loop, maintaining a conversation history.
2. **Language Model Integration**: Utilizes the `OllamaLLM` language model to generate responses based on the conversation history and user input.
3. **Dynamic Prompting**: Uses `ChatPromptTemplate` to dynamically create prompts for the language model.
4. **Exit Command**: The conversation continues until the user types 'exit'.

Flow Of Control
===================
flowchart TD
    A[Start] --> B[Import Libraries]
    B --> C[Initialize Template and Model]
    C --> D[Define conversation Function]
    D --> E[Start Infinite Loop]
    E --> F[Get User Input]
    F --> G{User Input 'exit'?}
    G -- Yes --> H[End Loop]
    G -- No --> I[Generate and Print Response]
    I --> J[Update Conversation History]
    J --> E
    H --> K[End]

Requirements
=============

A good hardware configuration is recommended for running ollama chatbot as ollama needs a lot of memory to run.

Installation
=============

git clone https://github.com/TGvenomYT/ollama-in-python.git

cd ollama-in-python

pip install -r requirements.txt
         OR
       
pip install langchain_core langchain_ollama

Feel Free to contribute to this project.
=========================================
