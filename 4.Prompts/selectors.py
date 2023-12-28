import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.prompts import FewShotPromptTemplate

llm = OpenAI(temperature=.7, model_name="gpt-3.5-turbo-instruct")
examples = [
    {
        "query": "Why is Neptune denser and physically smaller than Uranus, despite having a greater mass?",
        "answer": "Neptune is denser and smaller than Uranus due to its greater mass, which causes more gravitational compression of its atmosphere."
    },
    {
        "query": "How was Neptune discovered, and what led to its prediction before its actual observation?",
        "answer": "Neptune was discovered through mathematical predictions prompted by unexpected changes in Uranus's orbit. Astronomers John Couch Adams and Urbain Le Verrier independently predicted Neptune's position, which was later observed in 1846 by Johann Galle."
    }
]

example_template = """
Question: {query}
Response: {answer}
"""
example_prompt = PromptTemplate(
    input_variables=["query", "answer"],
    template=example_template
)
prefix = ''' Yor are a science expert, who knows everything about Solar System:  
Here are some examples:
'''
suffix = '''
Question:{user_input}
Response:
'''
few_short_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=['user_input'],
    example_separator="\n\n"
)
user_query = "what is new planets of solar system?"
resp = llm(few_short_prompt.format(user_input=user_query))
print(resp)
