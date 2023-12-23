from langchain.utils.openai_functions import convert_pydantic_to_openai_function
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from dotenv import load_dotenv
import os

from tagging_functions.tagging import Tagging

class AI_understanding:
    def __init__(self):
        load_dotenv()
        
        OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
        self.model = ChatOpenAI(temperature=0, model='gpt-4',openai_api_key=OPENAI_API_KEY)
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Ты помогаешь найти подходящие билеты, если пользователь ничего не написал о каком-то пункте, то запиши в нем прочерк -"),
            ("user", "{input}")
        ])
        tagging_functions = [convert_pydantic_to_openai_function(Tagging)]
        self.model_with_functions = self.model.bind(
            functions=tagging_functions,
            function_call={"name": "Tagging"}
        )
        self.chain = prompt | self.model_with_functions | JsonOutputFunctionsParser()

    async def ask_ai(self, talk):
        answer = self.chain.invoke({"input": talk})
        return answer
