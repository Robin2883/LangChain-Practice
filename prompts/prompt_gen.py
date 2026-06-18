from langchain_core.prompts import PromptTemplate
from langchain_core.load import dumps
import os

project_path=os.path.join(os.path.dirname(__file__), "template.json")

template=PromptTemplate(template="What is the capital of {country}? Tell me about {number} beautiful places here.", input_variables=['country', 'number'])

#template.model_dump_json("template.json")

template.save(project_path)