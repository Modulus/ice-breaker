import os
from dotenv import load_dotenv

load_dotenv()

import sys

# pythonpath = "/Users/john.sigvald.skauge/Courses/ice_breaker" 
# if pythonpath and pythonpath not in sys.path: 
#     sys.path.append(pythonpath) 
#     print(sys.path)

pythonpath = os.getenv('PYTHONPATH')
if pythonpath and pythonpath not in sys.path:
    sys.path.append(pythonpath)



from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent, 
    AgentExecutor
)


from tools.tools import get_profile_url_tavily
from langchain import hub



def lookup(name: str):

    llm = ChatOllama(temperature=0, model="llama3.2")

    template = """
    Given the full name of {name_of_person} i want you to get me a link to their Linkedin profile page. Please ignore udemy.com domain. Your answer should be a URL that is in https://linkedin.com something.
    """

    promt_template = PromptTemplate(input_variables=["name_of_person"], template=template)

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 Linkedin profile page",
            func=get_profile_url_tavily,
            description="Useful for when you need to get the Linkedin Page URL of a person"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(input={"input": promt_template.format_prompt(name_of_person=name)})
    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__ == "__main__":
    linkedin_url = lookup(name="Eden Marco")
    print(f"Final result is: {linkedin_url}")