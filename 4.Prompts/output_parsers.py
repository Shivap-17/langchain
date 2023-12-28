import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser

llm = OpenAI(temperature=.7, model_name="gpt-3.5-turbo-instruct")
#
#
# '''COMMA SEPARATED OUTPUT'''
# output_parser = CommaSeparatedListOutputParser()
# prompt_template = PromptTemplate(
#     template="Provide an answer as best as you can.\n{query} \n {format_instructions}",
#     input_variables=["query"],
#     partial_variables={"format_instructions": output_parser.get_format_instructions()}
# )
# prompt = prompt_template.format(query="List me some rose flower names")
# resp = llm(prompt)
# print(resp)


''' JSON FORMATTED OUTPUT'''
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

examples = [
    {
        "question": "Who discovered Neptune's largest moon, Triton?",
        "multiple_choices": "Alexis Bouvard, John Couch Adams, Johann Galle, Urbain Le Verrier",
        "answer": "Johann Galle"
    },
    {
        "question": "What led to the discovery of Neptune?",
        "multiple_choices": "Direct observation by telescope, Chance during a survey of the night sky, "
                            "Mathematical predictions prompted by changes in Uranus's orbit, Apollo moon missions",
        "answer": "Mathematical predictions prompted by changes in Uranus's orbit"
    },
]

example_template = """
Question: {question}
Choices:  {multiple_choices}
Answer:   {answer}
"""
example_prompt = PromptTemplate(
    input_variables=["query", "answer", "choices"],
    template=example_template
)
prefix = ''' Yor are a teacher who can set questions for the exams from the given context:  
Here are some examples:
'''
suffix = '''
Question:{user_input}
Response:  \n {format_instructions}
'''

response_schema = [
    ResponseSchema(name='question', description=' A question from input content'),
    ResponseSchema(name='multiple_choices', description='list of choices for the question'),
    ResponseSchema(name='answer', description=' Answer for the question')
]
output_parser = StructuredOutputParser.from_response_schemas(response_schema)

few_short_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix=prefix,
    suffix=suffix,
    input_variables=['user_input'],
    example_separator="\n\n",
    partial_variables={"format_instructions": output_parser.get_format_instructions()}
)

prompt = few_short_prompt.format(
    user_input="Neptune is the eighth and farthest planet from the Sun. It is the fourth-largest planet in the Solar System by diameter, the third-most-massive planet, and the densest giant planet. It is 17 times the mass of Earth, and slightly more massive than its near-twin Uranus. Neptune is denser and physically smaller than Uranus because its greater mass causes more gravitational compression of its atmosphere. Being composed primarily of gases and liquids, it has no well-defined solid surface. The planet orbits the Sun once every 164.8 years at an orbital distance of 30.1 astronomical units (4.5 billion kilometres; 2.8 billion miles). It is named after the Roman god of the sea and has the astronomical symbol ♆, representing Neptune's trident.[d] "
               "Neptune is not visible to the unaided eye and is the only planet in the Solar System found by mathematical predictions rather than by empirical observation. Unexpected changes in the orbit of Uranus led Alexis Bouvard to hypothesise that its orbit was subject to gravitational perturbation by an unknown planet. After Bouvard's death, the position of Neptune was predicted from his observations, independently, by John Couch Adams and Urbain Le Verrier. Neptune was subsequently observed with a telescope on 23 September 1846[1] by Johann Galle within a degree of the position predicted by Le Verrier. Its largest moon, Triton, was discovered shortly thereafter, though none of the planet's remaining 14 known moons were located telescopically until the 20th century. The planet's distance from Earth gives it a very small apparent size, making it challenging to study with Earth-based telescopes. Neptune was visited by Voyager 2, when it flew by the planet on 25 August 1989; Voyager 2 remains the only spacecraft to have visited Neptune.[18][19] The advent of the Hubble Space Telescope and large ground-based telescopes with adaptive optics has allowed for additional detailed observations from afar. \n Generate 3 questions from above content")

resp = llm(prompt);

print(resp)
