import random
#create a bag with 10 marbles
bag = ('green','green','green','green','green','green','red','red','red','red',)
#starting amount of money
start_purse = 1000
# current money amount
purse = start_purse
#result of last round
result = 0
#how many rounds
rounds = 3
#last marble
marble = 'none'
# welcome user to game
print(f'You Start the game with {start_purse} gold pieces!')
# loop drawing marbles
for draw in range(1, rounds+1):
    #how much was bet
    bet = input(f'Current purse: {purse} Last draw: {marble} \nRound {draw} - How much do you want to bet?: ')
    #draw marble
    marble = random.choice(bag)
    # win or loss
    if marble == 'green':
        result = bet
    else:
        result = - bet
    #calc win or loss/ result and new amount/purse
    purse += result
    #lose game if lose half of money
    if purse < 0.5 * start_purse:
        print('Game Over! You lost to much gold!!')
        break
    #print results
    print(f'purse: {purse}, last result: ({marble}): {result}')
    print('')
# print final results
print(f'starting/ ending purse: {start_purse} / {purse}' )
print(f'gain/loss: {(purse-start_purse)/(start_purse)*100}%')