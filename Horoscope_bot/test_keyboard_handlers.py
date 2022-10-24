from pytest_mock import MockerFixture
import requests


from Handler import start, echo
from Horoscope_bot.Handler import signRequest


class TestHandlers:

#context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    def test_SignRequest(self, mocker: MockerFixture):
        context = mocker.MagicMock()
        update = mocker.MagicMock()
        bot = mocker.MagicMock()
        effective_chat = mocker.MagicMock()
        message = mocker.MagicMock()
        send_message = mocker.MagicMock()

        bot.send_message = send_message
        effective_chat.id = 10
        message.text = "Taurus"

        context.bot = bot
        update.effective_chat = effective_chat
        update.message = message

        signRequest(update, context)
        params = (
            ('sign', 'Taurus'),
            ('day', 'today')
        )
        response = requests.post('https://aztro.sameerkumar.website/', params=params)
        jresponse = response.json()

        send_message.assert_called_once_with(chat_id=10, text=jresponse['description'])

#context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

    def test_start(self, mocker: MockerFixture):
        context = mocker.MagicMock()
        update = mocker.MagicMock()
        bot = mocker.MagicMock()
        effective_chat = mocker.MagicMock()
        message = mocker.MagicMock()
        send_message = mocker.MagicMock()

        bot.send_message = send_message
        effective_chat.id = 10
        message.text = "I'm a bot, please talk to me!"

        context.bot = bot
        update.effective_chat = effective_chat
        update.message = message

        start(update, context)

        send_message.assert_called_once_with(chat_id=10, text="I'm a bot, please talk to me!")

