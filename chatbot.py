from chatterbot import ChatBot

from flask import Flask, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer
from flask import request
from flask import render_template
from flask import flash
from flask import jsonify

app = Flask(__name__)

english_bot = ChatBot("Career",storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ])
#english_bot.set_trainer(ChatterBotCorpusTrainer)

# trainer = ListTrainer(english_bot)
# trainer.train("chatterbot.corpus.english")
# trainer.train('chatterbot.corpus.english.greetings')
# trainer.train('chatterbot.corpus.english.conversations')

trainer = ListTrainer(english_bot)
conv = open('Meet.txt','r').readlines()
conv1 = open('greeting.txt','r').readlines();
trainer.train(conv)
trainer.train(conv1)




@app.route("/")
def home1():
    return render_template("index1.html")

@app.route("/ask", methods=['GET','POST'])
def ask():
	message = (request.form['messageText'])
	print(request.form['messageText']);


	while True:
	    if message == "":
	        continue

	    else:
	        bot_response =   str(english_bot.get_response(message))
	        print (bot_response)
	        return jsonify({'status':200, 'answer':bot_response})


if __name__ == "__main__":
    app.debug = True
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.run()
