from langchain_core.prompts import ChatPromptTemplate

chat_template= ChatPromptTemplate(
    [('system', 'you are a helpful {domain} expeprt'),
    ('user', 'Explain in simple terms, what is {topic}?')]
)

prompt=chat_template.invoke({'domain': 'football', 'topic': 'FIFA'})

print(prompt)