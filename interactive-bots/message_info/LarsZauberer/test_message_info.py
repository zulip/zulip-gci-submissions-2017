<<<<<<< HEAD
import zulip_bots.test_lib
from typing import Any
=======
>>>>>>> 0d253aa... interactive bots: Run the message_info bot for LarsZauberer.
from zulip_bots.test_lib import BotTestCase

class TestHelpBot(BotTestCase):
    bot_name = "message_info"  # type: str

    def test_followup_stream(self) -> None:
        message = dict(
<<<<<<< HEAD
            content='You sent a message with {} words',
            type='privat',
            sender_email='message-info-bot@zulip.larszauberer.zulipdev.org',
        )

        with self.mock_config_info({'stream': 'followup'}):
            response = self.get_response(message)

        self.assertEqual(response['content'], 'from foo@example.com: feed the cat')
        self.assertEqual(response['to'], 'followup')

    def test_different_stream(self) -> None:
        message = dict(
            content='feed the cat',
            type='stream',
            sender_email='foo@example.com',
        )

        with self.mock_config_info({'stream': 'issue'}):
            response = self.get_response(message)

        self.assertEqual(response['content'], 'from foo@example.com: feed the cat')
        self.assertEqual(response['to'], 'issue')

    def test_bot_responds_to_empty_message(self) -> None:
        bot_response = 'Please specify the message you want to send to followup stream after @mention-bot'

        with self.mock_config_info({'stream': 'followup'}):
            self.verify_reply('', bot_response)

    def test_help_text(self) -> None:
        request = 'help'
        bot_response = '''
            This plugin will allow users to flag messages
            as being follow-up items.  Users should preface
            messages with "@mention-bot".
            Before running this, make sure to create a stream
            called "followup" that your API user can send to.
            '''

        with self.mock_config_info({'stream': 'followup'}):
            self.verify_reply(request, bot_response)
=======
            type='privat',
            sender_email='message-info-bot@zulip.larszauberer.zulipdev.org',
        )
>>>>>>> 0d253aa... interactive bots: Run the message_info bot for LarsZauberer.
