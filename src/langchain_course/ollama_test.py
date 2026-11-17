from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from dotenv import load_dotenv

load_dotenv()


llm = ChatOllama(model="gemma3:270m", temperature=0)

prompt = ChatPromptTemplate([
    ("system", "You are a helpful AI tutor."),
    ("human", "{question}"),
])

person = "Cristiano Ronaldo"
summary_template = """Tell my about {person}"""
summary_prompt_template = PromptTemplate (
    template=summary_template
    )


chain = summary_prompt_template | llm #runnable chain
print(chain.invoke({"person": person}))

# chain = summary_prompt_template | llm
#print(chain.invoke({"person": person}))





