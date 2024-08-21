LangChain Course

Agent was created at `./agents/linkedin_lookup_agent.py`
- the result may vary after each run, sometimes you'll get other result of other David Do because there are bunch of people with that name
- we need to make this query less ambiguous and more concise (add information to lookup function) - out of scope of this course
- although we did ask for the agent to give us only the URL, we got a bunch of fluff. So we don't need that text. However, our application use an LLM to later process this response, it robust enough to handle both of those use cases

Finish (lession 17)
- give a name to get linkin url from ProxyCurl api
- get relevant information from the linkin url
- create
    - a short summary
    - two interesting facts about them