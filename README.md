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
> **Note:** There can be several handlers; they will simply be called sequentially.
```python
@bot.bot_handler('text')
def handler(update):
    response = 'You say: ' + update['message']['text']
    bot.send_text(update['message']['chat']['id'], response)

@bot.bot_handler('photo')
def handler(update):
    response = 'I can\'t process images!'
    bot.send_text(update['message']['chat']['id'], response)

@bot.bot_handler('sticker')
def handler(update):
    response = 'This is so cool sticker!'
    bot.send_text(update['message']['chat']['id'], response)
```
Having configured the handlers, we call the `run` method on the `bot`. \
Eureka! The bot is running!
```python
bot.run()
```