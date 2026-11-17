from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from dotenv import load_dotenv


load_dotenv()

llm = ChatOllama(model="gemma3:270m", temperature =0)



prompt_template = ChatPromptTemplate(
    [("system", "Eres un analista de futbol no de baloncesto. Si te pregunta algo de baloncesto, responde No se."),
      ("human","Hablame de la posicion de {posicion}")]
)

chain = prompt_template | llm

print(chain.invoke({"posicion": "pivot"}).content)