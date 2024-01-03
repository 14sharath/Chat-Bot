from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a ChatBot instance
bot = ChatBot('chatbot', read_only=False, logic_adapters=['chatterbot.logic.BestMatch'])

# Define a list of training data
list_to_train = [
    ("hi", "hi, there"),
    ("whats your name", "my name is chat bot")
]

# Train the chatbot with the list of training data
list_trainer = ListTrainer(bot)
list_trainer.train(list_to_train)

# Define the index view
def index(request):
    return render(request, 'index.html')

# Define the getResponse view
def getResponse(request):
    # Get the user's message from the request's GET parameters
    userMessage = request.GET.get('userMessage')

    # Get the chatbot's response
    botResponse = bot.get_response(userMessage)

    # Return the chatbot's response as JSON
    response_data = {'botResponse': str(botResponse)}
    return JsonResponse(response_data)



























# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer

# # Create a new chat bot
# bot = ChatBot('MyBot')

# # Create a new trainer for the chat bot
# trainer = ChatterBotCorpusTrainer(bot)

# # Train the chat bot on English language data
# trainer.train('chatterbot.corpus.english')

# # Now the bot is ready for use
# response = bot.get_response('Hello')
# print(response)










# def index(request):
#    return HttpResponse("this is my first url")



# def specific(request):
#    list=[1,2,3]

#    return HttpResponse(list)


# def article(request,article_id):
#    return HttpResponse(article_id)