# Telegator
This Python module will help you easily create your own bot in Telegram.
## 
We import the `TelegramBot` class from the `TelegramBot` module.\
Then we create an instance of this class, passing your bot’s `token` to the constructor.
```python
from TelegramBot import TelegramBot


token = '***YOUR_TOKEN***'
bot = TelegramBot(token)
```
Then, using decorators, we create handlers for different types of messages.
> **Note:** There can be several handlers for one data type; they will simply be called sequentially.
```python
@bot.bot_handler('all')
def handler(message: Message):
    response = 'Data type: ' + message.data_type
    bot.send_text(message.data['chat']['id'], response, reply_message=message)

@bot.bot_handler('text')
def handler(message: Message):
    response = 'You say: ' + message.data['text']
    bot.send_text(message.data['chat']['id'], response)

@bot.bot_handler('photo')
def handler(message: Message):
    response = 'I can\'t process images!'
    bot.send_text(message.data['chat']['id'], response)

@bot.bot_handler('sticker')
def handler(message: Message):
    response = 'This is so cool sticker!'
    bot.send_text(message.data['chat']['id'], response)
```
Having configured the handlers, we call the `run` method on the `bot`. \
Eureka! The bot is running!
```python
bot.run()
```