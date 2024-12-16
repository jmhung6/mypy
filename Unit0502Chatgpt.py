import openai

openai.api_key

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Test1"},
            {"role": "user", "content": "Test2"},
        ],
        max_tokens=100,
        temperature=0.7,
    )

    completed_text = response["choices"][0]["message"]["content"]
    print(completed_text)
except openai.error.apierror as e:
    if "R1" in str(e):
        print("R11")
    else:
        print(f"R2:{e}")
except openai.error.authenticationerror:
    print("R3")
except exception as e:
    print(f"R5{e}")
