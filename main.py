import pandas as pd
from funcs import *


print('[ X ] EXIT')
while True:
    
    data = pd.read_json('bot.json')
    submit = input("You: ").lower()

    if submit == 'X':
        break
    found = False
    for object, item in data.iterrows():
        if submit == item['question']:
            print("Ava: ", item['answer'])
            found = True
            break

    if not found:
        new_answer = input("I don't know that, can you tell me the answer?")
        new = [{"question": submit, "answer": new_answer}]
        writeInJson(new)

        