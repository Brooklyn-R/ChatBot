# import open library
import os
import openai

# set up open ai client
openai.api_key = "Your Api Key"

# continuous loop for questions
while True:
    #model and prompt
    model_engine = "text-davinci-003"
    prompt = input('Enter new prompt: ')
    if 'exit' in prompt or 'quit' in prompt:
        break

    # generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1, stop=None,
        temperature=0.5
    )

    # extracting useful part of response
    response = completion.choices[0].text

    # print responses
    print(response)
