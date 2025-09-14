secret_word = 'umbrella'
guess = ""
guess_count = 0
guess_limit = int(input('Set a guessing limit: '))
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
  if guess_count < guess_limit:
    guess = input('Enter the word: ')
    guess_count += 1
  else:
    out_of_guesses = True

if out_of_guesses == False:
  print('You win!')
else:
  print('You lose.')
