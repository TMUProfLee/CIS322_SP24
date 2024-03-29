from testing_base import *

# Display only

def test_display_marshall_single_guess():
    joe = Player('Joe', 'Marshall')
    joe.add_guess(5)
    assert(joe.show_guesses() == None)

def test_display_marshall_multiple_guesses():
    joe = Player('Joe', 'Marshall')
    joe.add_guess([3, 5, 7, 8, 10, 15])
    assert(joe.show_guesses() == None)

test_display_marshall_single_guess()
test_display_marshall_multiple_guesses()