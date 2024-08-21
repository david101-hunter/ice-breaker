LangChain Course

Agent was created at `./agents/linkedin_lookup_agent.py`
- the result may vary after each run, sometimes you'll get other result of other David Do because there are bunch of people with that name
- we need to make this query less ambiguous and more concise (add information to lookup function) - out of scope of this course
- although we did ask for the agent to give us only the URL, we got a bunch of fluff. So we don't need that text. However, our application use an LLM to later process this response, it robust enough to handle both of those use cases

Agent was created at `./agents/twitter_lookup_agent.py` same way like linkedin

Summary:
- give a name to get linkin url, twitter url from ProxyCurl api
- get relevant information from the linkin url, twitter url
- create (template prompt)
    - a short summary
    - two interesting facts about them
