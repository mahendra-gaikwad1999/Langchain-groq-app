## we will create core pipeline

from langchain_core.output_parsers import StrOutputParser
from app.llm import get_llm
from app.prompts import get_prompt

def get_chain():
    llm = get_llm()
    prompt = get_prompt()
    parser = StrOutputParser()

    chain = prompt | llm | parser  ## Means pass the output of one step to other and create pipeline
    return chain
