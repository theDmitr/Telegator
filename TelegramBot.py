from threading import Thread

from TelegramAPI import TelegramAPI


class Message:
    def __init__(self, update, data_type: str):
        self.data = update['message']
        self.data_type = data_type
        self.message_id = self.data['message_id']


class TelegramBot:
    long_polling_timeout: int
    request_timeout: int

    def __init__(self, token: str):
        self.token = token
        self.running = False
        self.updates_count = 0
        self.handlers = dict()

    def __handler(self, update):
        data_type: str = list(update['message'].keys())[4]

        if data_type == 'media_group_id':
            data_type = list(update['message'].keys())[5]

        for handler_data_type, handler_functions in self.handlers.items():
            if handler_data_type == data_type or handler_data_type == 'all':
                for handler_function in handler_functions:
                    handler_function(Message(update, data_type))

    def bot_handler(self, data_type: str):
        def decorator(handler_function):
            if data_type not in self.handlers:
                self.handlers[data_type] = list()
            self.handlers[data_type].append(handler_function)

        return decorator

    def get_updates(self) -> list:
        response = TelegramAPI.request(self.token, 'getUpdates', self.request_timeout,
                                       offset=self.updates_count, timeout=self.long_polling_timeout)
        updates = response.json()['result']
        if len(updates) != 0:
            self.updates_count = updates[-1]['update_id'] + 1
        return updates

    def run(self, long_polling_timeout=10, request_timeout=15):
        self.long_polling_timeout = long_polling_timeout
        self.request_timeout = request_timeout

        self.running = True
        while self.running:
            updates = self.get_updates()
            for update in updates:
                Thread(target=self.__handler, args=(update,)).start()

    def send_text(self, chat_id: int, text: str, reply_message: Message = None):
        kwargs = dict()
        if reply_message is not None:
            kwargs['reply_to_message_id'] = reply_message.message_id
        TelegramAPI.request(self.token, 'sendMessage', self.request_timeout,
                            chat_id=chat_id, text=text, **kwargs)
