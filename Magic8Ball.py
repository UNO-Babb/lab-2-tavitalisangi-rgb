#Magic8Ball.py
#Name: Tavita Afata
#Date:9/7/25
#Assignment:Magic 8 ball

#We will need random for this program, import to use this package.
import random

def main():
  print("Welcome to Magic 8 ball")
  answers= ["As I see it, yes", "Ask me again later." 
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Do not count on it.",
"It is certain.",
"It is decidedly so.",
"Most likely.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Outlook good.",
"Reply hazy, try again.",
"Signs point to yes.",
"Very doubtful.",
"Without a doubt.",
"Yes.",
"Yes-definitely.",
"You may rely on it."]
  Magic1 = input("Ask a question?: ")

  response = random.choice(answers)
  print("The Ball knows best so the Ball says:", response)


  #Create a list of your responses.
  #Prompt the user for their question.

  #Answer question randomly with one of the options from your earlier list.


if __name__ == '__main__':
  main()
