def recDC(coin_val_list, change, known_result):
    min_coin = change
    if change in coin_val_list:
        known_result[change] = 1
        return 1
    elif known_result[change] > 0:
        return known_result[change]
    else:
        for i in [c for c in coin_val_list if c <= change]:
            num_coins = 1 + recDC(coin_val_list, change - i, known_result)

            if num_coins < min_coin:
                min_coin = num_coins
                known_result[change] = min_coin

    return min_coin


# print(recDC([1,2,3,4,5,10,21,25], 63,[0]*64))


# func for finding minimum number of coins we need to give change
def recMC(coin_val_list, change):
    # min amount coins we found so far
    minCoins = change
    # see if we can give change with one coin in our coins nominal list () and return one if we can
    if change in coin_val_list:
        return 1
    else:
        # find how many coins we need to give change
        # look at every coin list if it less than current change
        for i in [c for c in coin_val_list if c <= change]:
            # start from pennie and call func again (for rest of change - 1 pennie if second call ect.)
            numCoins = 1 + recMC(coin_val_list, change - i)
            # if we found lesser amount of coin, we assign this value to minCoin and return it in the end
            if numCoins < minCoins:
                print(f'numCoins = {numCoins}')

                minCoins = numCoins
    return minCoins


print(recMC([1, 5, 10, 25], 11))
