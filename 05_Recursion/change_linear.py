def change_machine(coin_list, change, min_coins, coins_used):
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 11
        for j in [c for c in coin_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[change]


def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin)
        coin = coin - this_coin


def main():
    amount = 63
    coin_list = [1, 3, 5, 10, 21, 25]
    coins_used = [0] * (amount + 1)
    coins_count = [0] * (amount + 1)

    print("Making change for ", amount, " requires")
    print(change_machine(coin_list, amount, coins_count, coins_used), 'coins')
    print("They are: ")
    print_coins(coins_used, amount)
    print("The used list is as follows: ")
    print(coins_used)


if __name__ == '__main__':
    main()
