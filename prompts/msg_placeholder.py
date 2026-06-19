from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template= ChatPromptTemplate([
    ('system', 'you are a helpful {domain} expeprt'), 
    MessagesPlaceholder(variable_name='chat_hist'),
    ('user', '{query}')
])

chat_hist=[]
with open ('chaht_hist.txt') as f:
    chat_hist.append(f.readlines())

chat_template.invoke({'chat_hist': chat_hist, 'query': 'where is my refund?'})

