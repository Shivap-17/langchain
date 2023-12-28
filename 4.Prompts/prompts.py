import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

template = """ {user_input} 

can you create a post for tweeter  in {number_of_words} words with above content

"""

prompt = PromptTemplate(
    input_variables=['user_input', 'number_of_words'],
    template=template
)
final_prompt=prompt.format(number_of_words='3', user_input='I love trips, and I have been to 6 countries. I plan to visit few more soon.')

llm= OpenAI(temperature=.7,model_name="text-davinci-003")

resp=llm(final_prompt)
print(resp)