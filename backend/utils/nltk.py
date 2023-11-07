from random import randint

messages = [
  "alou",
  "oi",
  "vai",
  "xau",
  "simbora"
]

def get_message(phrase):
  i = randint(0, 4)
  return phrase + ' ' + messages[i]