from langchain_core.prompts import PromptTemplate
import os

project_path=os.path.join(os.path.dirname(__file__), "template.json")

template=PromptTemplate(template="What is the capital of {country}? Tell me about {number} beautiful places here.", input_variables=['country', 'number'])

template.save(project_path)