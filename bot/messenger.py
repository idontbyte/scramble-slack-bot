import logging
import random

logger = logging.getLogger(__name__)

class Messenger(object):
    def __init__(self, slack_clients):
        self.clients = slack_clients

    def send_message(self, channel_id, msg):
        # in the case of Group and Private channels, RTM channel payload is a complex dictionary
        if isinstance(channel_id, dict):
            channel_id = channel_id['id']
        logger.debug('Sending msg: {} to channel: {}'.format(msg, channel_id))
        channel = self.clients.rtm.server.channels.find(channel_id)
        channel.send_message("{}".format(msg.encode('ascii', 'ignore')))

    def write_help_message(self, channel_id):
        bot_uid = self.clients.bot_user_id()
        txt = '{}\n{}\n{}'.format(
            "Scramble bot has entered the building:",
            "> `<@" + bot_uid + "> scramble` - starts the game",
            "> `<@" + bot_uid + "> guess xyz` - guess the word")
        self.send_message(channel_id, txt)
        
    def write_prompt(self, channel_id):
        bot_uid = self.clients.bot_user_id()
        txt = "I'm sorry, I didn't quite understand... Can I help you? (e.g. `<@" + bot_uid + "> help`)"
        self.send_message(channel_id, txt)

    def write_error(self, channel_id, err_msg):
        txt = ":face_with_head_bandage: my maker didn't handle this error very well:\n>```{}```".format(err_msg)
        self.send_message(channel_id, txt)
            
    def scramble(self, channel_id):
        bot_uid = self.clients.bot_user_id()
        txt = "starting the game..."
        self.send_message(channel_id, txt)

    def guess(self, channel_id):
        bot_uid = self.clients.bot_user_id()
        txt = "guess test"
        self.send_message(channel_id, txt)
   
    def add_words(self, channel_id, msg_txt):
        bot_uid = self.clients.bot_user_id()
        txt = "adding words: " + msg_txt
        self.send_message(channel_id, txt)