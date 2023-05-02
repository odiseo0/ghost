from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
)

from ..prompts import QA_PROMPT


human_message_prompt = HumanMessagePromptTemplate(
    prompt=PromptTemplate(
        template=QA_PROMPT,
        input_variables=["history", "question"],
    )
)
memory = ConversationBufferMemory(memory_key="history")
chat_prompt_template = ChatPromptTemplate.from_messages([human_message_prompt])

llm = ChatOpenAI(temperature=0.9)
chat_chain = LLMChain(memory=memory, llm=llm, prompt=chat_prompt_template, verbose=True)
