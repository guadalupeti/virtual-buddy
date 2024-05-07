import json
import os

def writeInJson(submit):
    with open('bot.json', 'rb+') as file:
        file.seek(-1, os.SEEK_END)
        file.truncate()


    with open('bot.json', 'a') as file:
        for item in submit:
            file.write(',')
            json.dump(item, file, indent=4)
            file.write('\n')

    with open('bot.json', 'a') as file:
        file.write(']')