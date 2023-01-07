from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import os

#create a list of possible quotes from a Churchil's speech

lineList = []
directoy = os.getcwd()

def soudLikeChurchill():
    line = ""       
    while line != "exit":
        user_prompt = prompt(">", history=FileHistory("churchill.txt"),
                 auto_suggest=AutoSuggestFromHistory())
        print(user_prompt)
        
        
if __name__ == "__main__":
    soudLikeChurchill()




