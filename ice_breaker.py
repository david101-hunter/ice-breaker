from dotenv import load_dotenv
import os
from langchain.prompts.prompt import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

# from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twiiter_lookup_agent import lookup as twitter_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.twitter import scrape_user_tweets


def ice_break_with(name: str) -> str:
    linkin_username = linkedin_lookup_agent(name)
    linkin_data = scrape_linkedin_profile(linkedin_profile_url=linkin_username)

    twitter_username = twitter_lookup_agent(name)
    tweets = scrape_user_tweets(username=twitter_username, mock=True)

    summary_template = """
        given the information about a person from linkedin {information},
        and their latest twitter posts {twitter_posts} I want you to create:
        1. a short summary
        2. two interesting facts about them
        
        Use both information from twitter and Linkedin
    """

    # create a prompt template from PromptTemplate constructor
    summary_prompt_template = PromptTemplate(
        input_variable=["information", "twitter_posts"], template=summary_template
    )

    llm = ChatOllama(temperature=0, model="gemma:2b")

    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": linkin_data, "twitter_posts": tweets})  # ai message object
    print(res)


information = """
Elon Reeve Musk FRS (/ˈiːlɒn/; born June 28, 1971) is a businessman and investor known for his key roles in space company SpaceX and automotive company Tesla, Inc. Other involvements include ownership of X Corp., formerly Twitter, and his role in the founding of The Boring Company, xAI, Neuralink and OpenAI. He is one of the wealthiest people in the world; as of July 2024, Forbes estimates his net worth to be US$221 billion.[4]

Musk was born in Pretoria to model Maye and businessman and engineer Errol Musk, and briefly attended the University of Pretoria before immigrating to Canada at age 18, acquiring citizenship through his Canadian-born mother. Two years later, he matriculated at Queen's University at Kingston in Canada. Musk later transferred to the University of Pennsylvania and received bachelor's degrees in economics and physics. He moved to California in 1995 to attend Stanford University, but dropped out after two days and, with his brother Kimbal, co-founded online city guide software company Zip2. The startup was acquired by Compaq for $307 million in 1999. That same year, Musk co-founded X.com, a direct bank. X.com merged with Confinity in 2000 to form PayPal. In October 2002, eBay acquired PayPal for $1.5 billion. Using $100 million of the money he made from the sale of PayPal, Musk founded SpaceX, a spaceflight services company, in 2002.

In 2004, Musk was an early investor who provided most of the initial financing in electric vehicle manufacturer Tesla Motors, Inc. (later Tesla, Inc.), assuming the position of the company's chairman. He later became the product architect, and in 2008 the CEO. In 2006, Musk helped create SolarCity, a solar energy company that was acquired by Tesla in 2016 and became Tesla Energy. In 2013, he proposed a hyperloop high-speed vactrain transportation system. In 2015, he co-founded OpenAI, a nonprofit artificial intelligence research company. The following year, Musk co-founded Neuralink—a neurotechnology company developing brain–computer interfaces—and The Boring Company, a tunnel construction company. In 2018, the U.S. Securities and Exchange Commission (SEC) sued Musk, alleging that he had falsely announced that he had secured funding for a private takeover of Tesla. To settle the case, Musk stepped down as the chairman of Tesla and paid a $20 million fine. In 2022, he acquired Twitter for $44 billion, merged the company into newly created X Corp. and rebranded the service as X the following year. In March 2023, Musk founded xAI, an artificial intelligence company.

Musk has expressed views that have made him a polarizing figure.[5] He has been criticized for making unscientific and misleading statements, including COVID-19 misinformation, promoting right-wing conspiracy theories, and "endorsing an antisemitic theory",[6] the latter of which he later apologized for.[5][7] His ownership of Twitter has been similarly controversial, being marked by layoffs of large numbers of employees, an increase in hate speech, misinformation and disinformation posts on the website, and changes to Twitter Blue verification.
"""

summary_template = """
    given the information {information} about a person from I want you to create
    1. a short summary
    2. two interesting facts about them
"""

#  các loại String PromptTemplates


def example():
    # create a prompt template from PromptTemplate constructor
    summary_prompt_template = PromptTemplate(
        input_variable="information", template=summary_template
    )
    llm = ChatOllama(temperature=0, model="gemma:2b")
    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": information})  # ai message object
    print(res)
    print("================================================")
    chain2 = summary_prompt_template | llm | StrOutputParser()
    res2 = chain2.invoke(input={"information": information})  # content of message
    print(res2)


def example2():
    """
        String PromptTemplates
    :return:
    """
    # create a prompt template from from_template method
    prompt_template = PromptTemplate.from_template("Tell me a joke about {topic} in {place}")
    # pass values to the prompt template
    res = prompt_template.invoke({"topic": "cats", "place": "the kitchen"})
    return res.text


def example3():
    """
        ChatPromptTemplate
    :return:
    """
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant"),
        ("user", "Tell me a joke about {topic} in {place} at {time}"),
    ])
    res = prompt_template.invoke({"topic": "cats", "place": "the kitchen", "time": "night"})
    return res.messages


def example4():
    """
        ChatPromptTemplate
    :return:
    """
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant"),
        MessagesPlaceholder("msgs")
    ])

    res = prompt_template.invoke({"msgs": [HumanMessage(content="hi!")]})
    return res


if __name__ == "__main__":
    load_dotenv()
    # print("Hello LangChain!")
    # print("================================================")
    # print(example2())
    # print("================================================")
    # print(example3())
    # print("================================================")
    # print(example4())
    # # An alternative way to accomplish the same thing without using the MessagesPlaceholder class explicitly is:
    # prompt_template = ChatPromptTemplate.from_messages([
    #     ("system", "You are a helpful assistant"),
    #     ("placeholder", "{msgs}")  # <-- This is the changed part
    # ])
    # res = prompt_template.invoke({"msgs": [HumanMessage(content="hi!")]})
    # print(res)

    print("Ice Breaker Enter:")
    ice_break_with(name="Eden Marco Udemy")

