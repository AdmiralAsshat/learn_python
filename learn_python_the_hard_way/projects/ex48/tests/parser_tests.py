from nose.tools import *
from ex48 import parser

## Test every function in parser

def test_peek():
	blank=[]
	assert_equal(parser.peek(blank),(None))
	assert_equal(parser.peek([('verb', 'eat'), ('stop','a'), ('noun', 'bagel')]), ('verb'))
	assert_equal(parser.peek([('error', 'Purple_monkey_dishwasher')]),('error'))


def test_match():
	blank=[]
	assert_equal(parser.match(blank, None),(None))
	assert_equal(parser.match([('verb', 'eat'), ('stop','a'), 
							('noun', 'bagel')], 'verb'), ('verb', 'eat'))
	assert_equal(parser.match([('verb', 'eat'), ('stop','a'), 
							('noun', 'bagel')], 'noun'), (None))


def test_skip():
	blank=[]
	sentence = [('verb', 'eat'), ('stop', 'a'), ('noun', 'bagel')]
	parser.skip(sentence, 'verb')
	assert_equal(sentence, [('stop', 'a'),('noun', 'bagel')])


def test_parse_verb():
	passing_sentence = [('verb', 'eat'), ('stop', 'a'), ('noun', 'bagel')]
	failing_sentence = [('stop', 'a'), ('noun', 'bagel'), ('verb', 'appears')]
	assert_equal(parser.parse_verb(passing_sentence), ('verb', 'eat'))
	assert_raises(parser.ParserError, parser.parse_verb, failing_sentence)


def test_parse_object():
	failing_sentence = [('verb', 'eat'), ('stop', 'a'), ('noun', 'bagel')]
	passing_sentence = [('stop', 'a'), ('noun', 'bagel')]
	assert_equal(parser.parse_object(passing_sentence), ('noun', 'bagel'))
	assert_raises(parser.ParserError, parser.parse_object, failing_sentence)


def test_parse_subject():
	sentence = [('verb', 'eat'), ('stop', 'a'), ('noun', 'bagel')]
	passing_sentence = ['Player', 'eat', 'bagel']
	result = parser.parse_subject(sentence, ('noun', 'Player'))
	result_sentence = [result.subject, result.verb, result.object]
	assert_equal(result_sentence, passing_sentence)


def test_parse_sentence():
	sentence = [('noun', 'Dog'), ('verb', 'eats'), ('noun', 'dog')] 
	passing_sentence = ['Dog', 'eats', 'dog']
	result = parser.parse_sentence(sentence)
	result_sentence = [result.subject, result.verb, result.object]
	assert_equal(passing_sentence, result_sentence)