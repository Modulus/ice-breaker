import os 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from langchain_core.output_parsers import StrOutputParser

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

def ice_break_with(name: str) -> str:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username,mock=True)


    summary_template = """
        Given the {information} about a person from I want you to create:
        1. A Short summary
        2. two interesting facts about them
    """




    summary_prompt_template = PromptTemplate(input_variables=["infromation"], template=summary_template)
    # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    llm = ChatOllama(temperature=0, model="llama3.2")
    # llm = ChatOllama(temperature=0, model="mistral")

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/eden-marco/", mock=True)

    chain = summary_prompt_template | llm | StrOutputParser()
    res = chain.invoke(input={"information": linkedin_data})

    print(res)


if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker")
    ice_break_with("Eden Marco Udemy")