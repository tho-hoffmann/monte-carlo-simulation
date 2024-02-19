import random

roulette = list(range(1, 37))

print(roulette)

def returns(ball, my_number, bet, odds):
    if ball == my_number:
        return bet * (odds - 1)
    else:
        return -bet
    
def play_roulette(number_of_spins, my_number, bet): 

    roulette = list(range(1, 37))

    odds = len(roulette)

    my_return = 0

    for i in range(number_of_spins):
        ball = random.choice(roulette)
        my_return += returns(ball, my_number, bet, odds)

    print(f"Average return after {number_of_spins} spins: {my_return / number_of_spins:.2}")

my_number = 2
bet = 1

# First game, 100 spins, repeating them 3 times
number_of_spins = 100
repeat = 3
for i in range(repeat):
    play_roulette(number_of_spins, my_number, bet)

# Second game, 1000000 spins, repeating them 3 times
number_of_spins = 1000000
repeat = 3
for i in range(repeat):
    play_roulette(number_of_spins, my_number, bet)


# https://quantbrasil.com.br/como-criar-uma-simulacao-de-monte-carlo-no-mercado-financeiro-utilizando-python/
    
# https://anaiscbc.abcustos.org.br/anais/article/view/899
    
# https://maisretorno.com/portal/termos/s/simulacao-de-monte-carlo