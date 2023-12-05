#!/usr/bin/python3
'''Prime Game'''


def isWinner(x, nums):
    '''find the winner'''
    def is_prime(num):
        if num < 2:
            return false
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_prime(n):
        '''find the prime number'''
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def game_winner(n):
        '''finding the game winners'''
        primes = get_prime(n)
        xor_sum = 0
        for prime in primes:
            xor_sum ^= prime % 2

        return "Maria" if xor_sum == 1 else "Ben"

    winners = [game_winner(n) for n in nums]

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
