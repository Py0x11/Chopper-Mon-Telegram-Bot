#pip install telebot
#pip install openai
import telebot
import openai

#For a function that is still under build LOL
class mai:
	msg_count = 0
oaikey = "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" # Your OpenAI API Key
bot = telebot.TeleBot("6028050477:AAHmwuV7coka6opw6m0ta5sPSFyErsuGyYU") # Telegram BOT Token

openai.api_key = oaikey # Setting OPENAI API Key

# The LOG here is the preface of the BOT i mean its charachter !!
LOG = "You are a Telegram AI Bot which was made by 'GOD' and was Trained Simillar to ChatGPT 3.5 Turbo Model but is Parallel to each other in basis of Intelegence, talks like a anime charachter called 'Tony Tony Chopper' from Anime 'One Piece' can use evilish curse words in every end of the sentence reply as so"

#This is the fucntion i told it was in build
def QuotaOver():
	print("You have used up all you quota for today now you cant send more messages")

#Jus the init for GPT Engine
def replier(question, chat_log):
    model_engine = "gpt-3.5-turbo"
    input_text = f"{chat_log}You: {question}\nChopperMon : "
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[{"role": "user", "content": input_text }]
        )
    output_text = response['choices'][0]['message']['content']
    return output_text

#Inbuild Command Handler for /Start
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Hey i am Chopper Mon !!, how can i help you today ??")
	
#Inbuild Command Handler for /Help
@bot.message_handler(commands=['help'])
def send_help(message):
	bot.reply_to(message, """
    1.You can chat with me like normal user.\n \n2.set your own API Key : By typing : ++oaikey="YOUR OPENAI API KEY"
    """)
	
#Message Processing
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, replier(message,LOG))
	mai.msg_count = mai.msg_count + 1   
	if mai.msg_count >=10:
		message.text.replace(message.text,"")
		nami = bot.reply_to(message, )
	elif "++oaikey" in message.text:
			bot.reply_to(message, "Setting API Key to your own")
			if not "sk" in message.text:
			    bot.reply_to(message, "invlid api key provided !!")
			else: #if you are in VS CODE you may see a error line under the else but its nothing its cause of the Nested if and else inside Elif
				new = message.text.replace("++","")
				bot.reply_to(message, f"Setting API KEY to {new}")
				exec(new)    
	else:
		pass

#Driver Code 	
bot.infinity_polling()
