from random import randrange
import re

hangman_words = ['jungle', 'happy', 'report', 'hospital', 'singularity', 'relgion', 'kingdom', 'opportunity', 'feather', 'hexagon', 'charity', 'forgiving', 'dictionary', 'brainwash', 'quarter']

previous_letters = []

max_guesses = 9
incorrect_count = 0
random_num = randrange(len(hangman_words))
word = hangman_words[random_num]
full_word = word

display_word = re.sub('[a-zA-Z]', '_', full_word)

print('Hangman')
print('You have {} chances. Start guessing.'.format(max_guesses))
print('Your word: ', " ".join(display_word), '\n')

while word != '':
  getch = input('Type Letter: ').lower()

  if len(getch) != 1:
    print('Only Type one letter')
  elif getch.isalpha() == False:
    print('Type in letters only')
  else:
    if getch not in previous_letters:
      previous_letters.append(getch)

      if getch in word:
        # find position of character
        for position in range(len(full_word)):
          if getch == full_word[position]:
            disp_list = list(display_word)
            disp_list[position] = getch
            display_word = "".join(disp_list)

        word = word.replace(getch, '')
        if word != '':
          print(getch + ' was in the word. Continue!')
      else:
        incorrect_count = incorrect_count + 1
        if incorrect_count == max_guesses:
          print('{} incorrect guesses. Your man died'.format(max_guesses))
          break
        else:
          print(getch + ' was not in the word, {} incorrect guesses'.format(incorrect_count))
    else:
      print('Already tried this letter!')
    
    if word == '':
      print('Congratulations, you have won the game. Your word was:')
    else:
      print('Letters tried so far [%s]' % ', '.join(map(str, previous_letters)))

  print(" ".join(display_word))
  print('\n')