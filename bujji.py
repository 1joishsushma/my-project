from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot=ChatBot('bujji')
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/Users/csc/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
     data=open('C:/Users/csc/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
     bot.train(data)

while True:

    
         message=input('yes,sush tell me:')
         if message.strip!='Bye' or message.strip!='bye':
             reply=bot.get_response(message)
             print('chatbot:',reply)
         if message.strip=='Bye' or message.strip=='bye':
             print('chatbot:it was nice talking to u')
             break
