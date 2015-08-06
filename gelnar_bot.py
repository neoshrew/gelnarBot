#! /usr/bin/env python
#
# Example program using irc.bot.
#
# Joel Rosdahl <joel@rosdahl.net>

"""A simple example bot.

This is an example bot that uses the SingleServerIRCBot class from
irc.bot.  The bot enters a channel and listens for commands in
private messages and channel traffic.  Commands in channel messages
are given by prefixing the text by the bot name followed by a colon.
It also responds to DCC CHAT invitations and echos data sent in such
sessions.

The known commands are:

    stats -- Prints some channel information.

    disconnect -- Disconnect the bot.  The bot will try to reconnect
                  after 60 seconds.

    die -- Let the bot cease to exist.

    dcc -- Let the bot invite you to a DCC CHAT connection.
"""
import random

from irc.bot import SingleServerIRCBot

class GelnarBot(SingleServerIRCBot):
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
			nouns = get_contained_nouns(message)
			if len(nouns) > 0:
				# Normall want the last noun
				noun = nouns[-1]
			else:
				noun = get_noun()

			msg = "{}: You're a {}".format(nick, noun)

			c.privmsg(target, msg)


def do_chance():
	return random.random() > 0.8


NOUNS = ["I've not been implemented properly!"]
def get_noun():
	return random.choice(NOUNS.values())


def get_contained_nouns(cont_str):
	words = [reduce_noun(i) for i in cont_str.split(' ')]

	retval = []
	for i in word_chunk_iter(words):
		if i in NOUNS:
			retval.append(NOUNS[i])

	return retval

def word_chunk_iter(words):
	for i in xrange(len(words)):
		for j in xrange(len(words) - i):
			yield ''.join(words[i:i+j+1])


_LETTERS = set('abcdefghijklmnopqrstuvwxyz')
def reduce_noun(noun):
	n = noun.lower()
	n = ''.join(
		c for c in noun
#		if c not in set("_' -")
		if c in _LETTERS
	)
	return n

def pop_nouns():
	global NOUNS
	with open('nounlist.txt', 'r') as fandle:
		NOUNS = {
			reduce_noun(noun): noun.replace('_', ' ')
			for noun in (line.strip() for line in fandle)
		}


def main():
	pop_nouns()

	server = 'registry-0.lohs.geneity'
	port = 6667
	nickname = 'gelnarBot'
	channel = '#frontend'
#	channel = '#test'

	bot = GelnarBot(channel, nickname, server, port)
	bot.start()

if __name__ == "__main__":
	main()
