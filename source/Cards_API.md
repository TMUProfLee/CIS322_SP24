**CardGames API**

**Version 1.0.0**

**Card** class

`	`Member variables

- *cardBack* – list of strings to print the back of the card
- *image* – list of strings to print the front of the card
- *shortImage* – list of strings to print a partial view of the front of the card
- *suit* – string denoting the card’s suit (“Spades”, “Clubs”, “Hearts”, “Diamonds”)
- *values* – integer denoting the cards value (Ace = 1, Jack = 10, Queen = 11, King = 12]

Functions

- \_\_init\_\_(suit, value, image, cardBack)

Creates a card with a specific suit, value, and card back image

Input:

- suit – string for the card’s suit (“Spades”, “Clubs”, “Hearts”, “Diamonds”]
- value – integer for the card’s value (Ace = 1, Jack = 10, Queen = 11, King = 12)
- image = list of string to print the front of the card
- cardBack = list of strings to print the back of the card

**Deck** class

`	`Member variables

- *cards* – list of **Card** objects that can still be dealt
- *size* – the number of unused **Card**s in *cards*
- *cardBack* – list of strings representing the image on the back of the **Card**s in *cards*
- *discarded* – list of **Card** objects that have already been dealt

Functions

- \_\_init\_\_()

  Builds a deck of cards

- shuffle()

  Randomizes self.*cards*

- getCard()

  Removes first card from self.*cards* and puts it at the end of self.*discarded*

Returns:

- First card in self.*cards*

**Player** class

`	`Member variables

- *name* – string representing the player’s name
- *hand* – list of **Card** objects representing the player’s cards
- *money* – integer for amount of money the player currently has

Functions

- \_\_init\_\_(name, money=0)

Sets the player’s name, gives them 0 money, and no cards for their hand

Input:

- name – string for the player’s name
- money – integer for amount of initial money the player has
- addMoney(amount)

Adds more money to the player.

Input:

- amount – integer number of money to add to the player

Returns:

- amount – integer number of money to add to the 
- makeBet(amount)

Removes money from the player only if the player has at least the bet *amount* currently.

Input:

- amount – integer number of money to remove from the player

Returns:

- integer - new amount of money the player has
- addCard(card, isKnown = True)

Adds one card to the player’s hand.

Input:

- card – **Card** object to add to self.*hand*
- isKnown – boolean whether the card is known to everyone
- clearHand()

Removes all cards from the player’s hand.

**Dealer** class

`	`Member variables

- *None*

Functions

- \_\_init\_\_()

Does nothing

- printCards(cards, showFront, printShort = True)

Displays a list of cards, either face up or face down.

Input:

- cards – list of **Card** objects to display
- showFront – boolean for whether to show the front of the card (value)
- printShort – boolean for whether to show only part of the card. Defaults is True to show partial card images

- printPlayerCards(player, printShort = False)

Displays a player’s cards, based on which cards are known.

Input:

- player – **Player** object
- printShort – boolean for whether to show only part of the card. Defaults is True to show partial card images

- dealCards(numCards, players)

Deals a certain number of cards to each player.

Input:

- numCards – integer number of cards to deal to each player
- players – a list of **Player** objects to deal cards to

Returns:

- True – cards are dealt successfully
- False – not enough cards in the deck to deal to all players
