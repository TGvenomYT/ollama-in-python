
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

template = '''
Answer the question below.

here is the conversation history: {history}
question: {question}
Answer: '''

model = OllamaLLM(model='phi')
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def conversation():

    history = ''
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
            break
        result = chain.invoke({'history': history, 'question': user_input})
        print('bot:', result)
        history += f'You: {user_input}\nbot: {result}\n'

conversation()

