from CardGames import *
def main():
  #initialization section
  StartGame = StartScreen()
  #print(StartGame)
  formattedAnswer = StartGame.upper()
  #print(formattedAnswer)
  if formattedAnswer == 'YES':
    print('Rules are listed & Game has begun')
  else:
    print('sorry you feel that way')

if __name__ == '__main__':
    main()