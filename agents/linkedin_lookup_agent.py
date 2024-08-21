from langchain_ollama import ChatOllama
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor
)
from langchain import hub
from langchain_core.messages import AIMessage

from tools.tools import get_profile_url_tavily


def chat_ollama():
    llm = ChatOllama(
        model="gemma:2b",
        temperature=0,
        # other params...
    )
    return llm


def prompt(name_of_person: str):
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
                          Your answer should contain only a URL"""

    prompt_template = PromptTemplate(
        input_variable=name_of_person,
        template=template)
    return prompt_template


def example_chat_ollama():
    messages = [
        (
            "system",
            "You are a helpful assistant that translates English to French. Translate the user sentence.",
        ),
        ("human", "I love programming."),
    ]
    llm = chat_ollama()
    ai_msg = llm.invoke(messages)
    print(ai_msg.content)


def tool():
    t = [
        Tool(
        name="Crawl Google 4 linkedin profile page",
        func=get_profile_url_tavily, # python function
        description="useful for when you need get the Linkedin Page URL", # super super important, because that's how the llm is going to determine whether to use this tool or not
        )
    ]
    return t


def lookup(name: str):
    llm = chat_ollama()
    template = prompt(name_of_person=name)
    tool_for_agent = tool()

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tool_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tool_for_agent, verbose=True, handle_parsing_errors=True)

    result = agent_executor.invoke(
        input={"input": template.format_prompt(name_of_person=name)}
    )
    linked_profile_url = result["output"]
    return linked_profile_url


if __name__ == '__main__':
    print('Hello LangChain!')
    # example_chat_ollama()
    linked_url = lookup("David Do")
    print(linked_url)

