#!/usr/bin/env python
'''
Mastermind solver

Given feedback from a game of mastermind, makes guesses to try and
determine the answer.
'''

import itertools
import collections
from netcat import Netcat


Feedback = collections.namedtuple('Feedback', ['correct', 'close'])


def generate_initial_pool(choices, holes):
    '''Generates the initial set of possible answers.'''
    return list(itertools.product(*[range(choices) for _ in range(holes)]))


def find_correct(actual, guess):
    '''Finds the sum of all correct matches.'''
    return sum([1 for (a, b) in zip(actual, guess) if a == b])


def remove_correct(actual, guess):
    '''Removes all correct matches from two "rows"'''
    actual2 = [a for (a, b) in zip(actual, guess) if a != b]
    guess2 = [b for (a, b) in zip(actual, guess) if a != b]
    return actual2, guess2


def find_close(actual, guess):
    '''Finds the sum of all close matches.'''
    actual, guess = remove_correct(actual, guess)

    close = 0
    for possible in guess:
        if possible in actual:
            del actual[actual.index(possible)]
            close += 1
    return close


def get_feedback(actual, guess):
    '''Compares two "rows" to each other and returns feedback.'''
    return Feedback(find_correct(actual, guess), find_close(actual, guess))


def is_match(guess, feedback, possible):
    '''Returns true if hypothetical could be the answer given the feedback
    and the guess'''
    return feedback == get_feedback(possible, guess)


def filter_pool(pool, guess, feedback):
    '''Filters through the pool of possibilities and removes ones which
    couldn't possibly be the answer.'''
    for possible in pool:
        if is_match(guess, feedback, possible) and (possible != guess):
            yield possible


def make_guess(pool, feedback):
    '''Makes an educated guess between the pool of possibilities and
    the user feedback.'''
    min_length = float('infinity')
    best_choice = None
    for possible in pool:
        length = len(list(filter_pool(pool, possible, feedback)))
        if min_length > length:
            min_length = length
            best_choice = possible
    return best_choice

def parse_respone(inn):
	correct = b"\xf0\x9f\x8f\xb4" 		#🏴
	almoust = b"\xf0\x9f\x8f\xb3\xef\xb8\x8f" 	#🏳️
	
	correct_count = inn.count(correct)
	almoust_count = inn.count(almoust) 
	
	print("almoust_count:", almoust_count)
	print("correct_count:", correct_count)
	
	
	return correct_count, almoust_count

def send_guess(guess, nc):
	nc.write(guess + b'\n')
	temp = nc.read_until(b">")
	print(temp.decode())
	correct_count, almoust_count = parse_respone(temp)
	return correct_count, almoust_count
	

def build_guess(guess):
    zero = b"\xf0\x9f\x90\xb0" #🐰
    one = b"\xf0\x9f\x90\x87" #🐇
    two = b"\xf0\x9f\x90\xa3" #🐣
    three = b"\xf0\x9f\x90\xa4" #🐤
    four = b"\xf0\x9f\x90\xa5" #🐥
    five = b"\xf0\x9f\xa5\x9a" #🥚
    new_guess = b""
    for i in guess:
    	if i == 0:
    	    new_guess += zero
    	if i == 1:
    	    new_guess += one
    	if i == 2:
    	    new_guess += two
    	if i == 3:
    	    new_guess += three
    	if i == 4:
    	    new_guess += four
    	if i == 5:
    	    new_guess += five 
    return new_guess


def round(nc):
    choices = 6
    holes = 4
    print('Staring Game....')

    pool = generate_initial_pool(choices, holes)
    guess = [0 if (i < (holes / 2)) else 1 for i in range(holes)]
    initial_guess = b"\xf0\x9f\x90\xb0\xf0\x9f\x90\xb0\xf0\x9f\x90\x87\xf0\x9f\x90\x87" #🐰🐰🐇🐇
    nc.write(initial_guess + b'\n')
    temp = nc.read_until(b">")
    print(temp)
    correct, close = parse_respone(temp)
    feedback = Feedback(correct, close)
    if feedback.correct == holes:
    	print("===== Win! =====")
    pool = list(filter_pool(pool, guess, feedback))
    print("{0} possible choices left. Thinking...\n".format(len(pool)))
    guess = make_guess(pool, feedback)
    print("Try this: {0}".format(guess))
    new_guess = build_guess(guess)
    #print(new_guess)

    while True:
        nc.write(new_guess + b'\n')
        temp = nc.read_until(b">")
        print(temp)
        correct, close = parse_respone(temp)
        
        feedback = Feedback(correct, close)
        if feedback.correct == holes:
            print("===== Win! =====")
            break
        pool = list(filter_pool(pool, guess, feedback))
        print("{0} possible choices left. Thinking...\n".format(len(pool)))
        guess = make_guess(pool, feedback)
        print("Try this: {0}".format(guess))
        new_guess = build_guess(guess)
        #print(new_guess)
    return
    

def play():
    nc = Netcat("challenges.ctfd.io", 30035)
    temp = nc.read_until(b'>')
    round(nc)
    round(nc)
    round(nc)



if __name__ == '__main__':
    play()

