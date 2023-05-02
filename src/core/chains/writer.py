from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from ..prompts import WRITER_PROMPT


llm = None
prompt = PromptTemplate(
    input_variables=["context"],
    template=WRITER_PROMPT,
)
chain = LLMChain(llm=llm, prompt=prompt)
