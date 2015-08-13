import random
import re

import data_util

import EXCEPTIONS

NOUNS = ["I've not been implemented properly!"]

BASE_ARTICLE = 'a'
EXCEPTION_ARTICLE = 'an'

_LETTERS = set('abcdefghijklmnopqrstuvwxyz')


def init_nouns():
	global NOUNS
	nouns_file = data_util.file_handle()

	NOUNS = {}
	with nouns_file as fandle:
		NOUNS = {
			reduce_noun(noun): noun.replace('_', ' ')
			for noun in (line.strip() for line in fandle)
		}

def reduce_noun(noun):
	n = noun.lower()
	n = ''.join(
		c for c in n
		if c in _LETTERS
	)
	return n

def get_article(noun):
	regex = '[aeiou].*'

	if noun in EXCEPTIONS.ARTICLE_EXCEPTIONS_LIST or \
		noun.startswith('eu') or \
		noun.startswith('uni'):
		return BASE_ARTICLE
	elif noun in EXCEPTIONS.INDEF_ARTICLE_EXCEPTIONS_LIST or \
		re.match(regex, noun) is not None:
		return EXCEPTION_ARTICLE
	else:
		return BASE_ARTICLE

def get_noun():
	return random.choice(NOUNS.values())

def stem(word):
	exception_map = EXCEPTIONS.PLURAL_EXCEPTIONS_MAP
	plur_to_sing_map = {
		'ies': 'y',
		'es' : '',
		's'  : '',
	}
	if word not in NOUNS:

		if word in exception_map:
			return exception_map[word]

		for k, v in plur_to_sing_map.iteritems():
			if word.endswith(k):
				new_word = word[:-len(k)]+v
				if new_word in NOUNS:
					return new_word

		return word

	return word


def get_contained_nouns(cont_str):
	words = [reduce_noun(i) for i in cont_str.split(' ')]
	words = [stem(i) for i in words if i]

	retval = []
	for i in word_chunk_iter(words):
		if i in NOUNS:
			retval.append(NOUNS[i])

	return retval

def word_chunk_iter(words):
	for i in xrange(len(words)):
		for j in xrange(len(words) - i):
			yield ''.join(words[i:i+j+1])


