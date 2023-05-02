from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

from ..prompts import WRITER_PROMPT


llm = OpenAI(temperature=0.9, max_tokens=-1)
prompt = PromptTemplate(
    input_variables=["context"],
    template=WRITER_PROMPT,
)
writer_chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
