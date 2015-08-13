import gelnarBot_IRC
import noun_util


def main():

#	server = 'registry-0.lohs.geneity'
	server = '192.168.0.8'
	port = 6667
	nickname = 'gelnarBot'
#	channel = '#frontend'
	channel = '#test'

	noun_util.init_nouns()
	bot = GelnarBot(channel, nickname, server, port)
	bot.start()

if __name__ == "__main__":
	main()

def noun_test_console():
	"""
	Entry point for noun test console.
	"""
	noun_util.init_nouns()

	while True:
		message = raw_input("> ")
		for noun in noun_util.get_contained_nouns(message):
			print "{} {}".format(noun_util.get_article(noun), noun)
