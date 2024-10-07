# Ice Breaker
httpcore.ConnectError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1000)
pip install pip-system-certs


## ollama stash

ollama pull llama3.2 <-- This fails



Exception has occurred: OutputParserException
Failed to parse Summary from completion {"properties": {"summary": {"description": "A short summary of Eden Marco's profile", "title": "Summary", "type": "string"}, "facts": {"description": "Interesting facts about Eden Marco", "items": {"type": "string"}, "title": "Facts", "type": "array"}}, "required": ["summary", "facts"]}. Got: 2 validation errors for Summary
summary
  Field required [type=missing, input_value={'properties': {'summary'...': ['summary', 'facts']}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.9/v/missing
facts
  Field required [type=missing, input_value={'properties': {'summary'...': ['summary', 'facts']}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.9/v/missing
pydantic_core._pydantic_core.ValidationError: 2 validation errors for Summary
summary
  Field required [type=missing, input_value={'properties': {'summary'...': ['summary', 'facts']}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.9/v/missing
facts
  Field required [type=missing, input_value={'properties': {'summary'...': ['summary', 'facts']}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.9/v/missing

The above exception was the direct cause of the following exception:

  File "/Users/john.sigvald.skauge/Courses/ice_breaker/ice_breaker.py", line 48, in ice_break_with
    res = chain.invoke(input={"information": linkedin_data, "twitter_posts": tweets})
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/john.sigvald.skauge/Courses/ice_breaker/ice_breaker.py", line 56, in <module>
    ice_break_with("Eden Marco")
langchain_core.exceptions.OutputParserException: Failed to parse Summary from completion {"properties": {"summary": {"description": "A short summary of Eden Marco's profile", "title": "Summary", "type": "string"}, "facts": {"description": "Interesting facts about Eden Marco", "items": {"type": "string"}, "title": "Facts", "type": "array"}}, "required": ["summary", "facts"]}. Got: 2 validation errors for Summary
summary
  Field required [type=missing, input_value={'properties': {'summary'...': ['summary', 'facts']}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.9/v/missing
facts
  Field required [type=missing, input_value={'properties': {'summary'...': ['summary', 'facts']}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.9/v/missing

    ----

    Action Input: Eden Marcohttps://www.udemy.com/course/langchain/I can help you with that. Here's the solution in the format you requested:

Final Answer: g-emarco

> Finished chain.
Here is the JSON instance that conforms to the provided schema:

```json
{
  "summary": "Eden Marco is a student at San Francisco State University, interested in computer science and security. They share insights on LLM agents and contextual answers.",
  "facts": [
    "Eden Marco recently showcased the risks of deploying insecure LLM agents without basic security measures.",
    "They highlighted the benefits of using Contextual Answers from the @AI21Labs team, including reduced hallucinations and improved accuracy."
  ]
}
```

This JSON instance includes a summary of Eden Marco's interests and a list of interesting facts about them, as requested. The schema is also correctly formatted with the required properties (`summary` and `facts`) in the correct order.
(ice-breaker) 


## Working better with ollama3.1:8b
