import random
#rock paper scissor game
print('welcome to the rock,paper,scissors game...')
is_running=True
feedback=['r','p','s']


while is_running:
        secret_response=(random.choice(feedback))
        response=input('enter your choice for (r),(p),(s):')
        if response not in feedback:
              print('invalid input')
        else:
                  print(secret_response)
        if response==secret_response:
          print('its is a tie!')
        elif response =='p' and secret_response== 's':
          print('you have been cut in pieces...you failed')
        elif response=='s' and secret_response=='p':
          print('sliced ..nice cut,way to go!')
        elif response=='s' and secret_response=='r':
          print('you have been smashed')
        elif response=='r' and secret_response=='s':
          print('you smashed..yayy!')
          print('wow..you are good at this..')
        elif response=='p' and secret_response=='r':
              print('game over..you loose!')
        elif response=='quit':
              break
print('keep trying...')