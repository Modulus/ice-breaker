import os
from typing import Tuple 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from third_parties.twitter import scrape_user_tweets
from output_parsers import summary_parser, Summary

from model import MODEL

def ice_break_with(name: str) -> Tuple[Summary, str]:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username,mock=True)
    twitter_username = twitter_lookup_agent(name=name)
    tweets = scrape_user_tweets(username=twitter_username, mock=True)

    summary_template = """
    given the information about a person from linkedin {information},
    and their latest twitter posts {twitter_posts} I want you to create:
    1. A short summary
    2. two interesting facts about them 

    Use both information from twitter and Linkedin
    \n{format_instructions}
    """



    summary_prompt_template = PromptTemplate(
        input_variables=["information", "twitter_posts"], 
        template=summary_template,
        partial_variables={
                "format_instructions": summary_parser.get_format_instructions(),
            },
        )
    # llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    # For some reason this fails with llama3.2, meaning the summary_parser, no clue why
    # llm = ChatOllama(temperature=0, model="llama3.2")
    llm = ChatOllama(temperature=0, model=MODEL)
     
    # llm = ChatOllama(temperature=0, model="mistral")
    print(f"Using model {llm.model}")

    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/eden-marco/", mock=True)

    # Hack to get along with the course
    chain = summary_prompt_template | llm | summary_parser #JsonOutputParser()
    res : Summary = chain.invoke(input={"information": linkedin_data, "twitter_posts": tweets})

    print(res)
    return res, linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker")
    result = ice_break_with("Eden Marco")

    print("\n\nResult:")
    print(result)