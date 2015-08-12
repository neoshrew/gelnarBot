import time
import random

import noun_util

from irc.bot import SingleServerIRCBot

MESSAGE_THRESHOLD = 1

class GelnarBot(SingleServerIRCBot):

	last_msg_time = time.time()

	def __init__(self, channel, nickname, server, port=6667):
		super(GelnarBot, self).__init__([(server, port)], nickname, nickname)
		self.channel = channel

	def on_nicknameinuse(self, c, e):
		c.nick(c.get_nickname() + "_")

	def on_welcome(self, c, e):
		c.join(self.channel)

	def on_privmsg(self, c, e):
		nick = e.source.split('!')[0]
		message = e.arguments[0]
		self.do_command(c, nick, nick, message, True)

	def on_pubmsg(self, c, e):
		curr_time = time.time()

		if self.last_msg_time + MESSAGE_THRESHOLD >= curr_time:
			return

		self.last_msg_time = curr_time

		my_nick = self.connection.get_nickname()
		nick = e.source.split('!')[0]
		message = e.arguments[0]

		at_me = my_nick in message

		self.do_command(c, e.target, nick, message, at_me)

	def do_command(self, c, target, nick, message, at_me):

		do = any([
			at_me,
			do_chance(),
			nick.startswith('earlbot'),
		])

		if do:
			nouns = noun_util.get_contained_nouns(message)
			if len(nouns) > 0:
				# Normall want the last noun
				nouns = sorted(nouns, key=lambda x: len(x))
				noun = nouns[-1]
			else:
				noun = noun_util.get_noun()

			article = noun_util.get_article(noun)
			msg = "{}: You're {} {}".format(nick, article, noun)

			c.privmsg(target, msg)


def do_chance():
	return random.random() > 0.8
