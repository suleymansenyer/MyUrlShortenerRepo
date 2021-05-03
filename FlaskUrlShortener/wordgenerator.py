import random

def wordGenerator():
    randomNumber = random.randint(4,8)
    keys = 'qwertyuopasdfghjklizxcvbnmQWERTYASDFGHJKZXCVBNM'
    myword =  ''.join(random.choices(keys,k=randomNumber))
    return myword