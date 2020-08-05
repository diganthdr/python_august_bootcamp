
coins = [2,1,5,2,1,1,2,2,1,1,5]
def count_coins(coins):
    '''
    this function calculates sum of coins.
    coins are in list
    v2.3: fixed bug in counting new coins
    '''
    #comment
    sum = 0 
    for coin in coins: #coin is a varialbe, you can use any name like 'for x in coins' is also fine.
        #iterator --> finger. for(i = 0, i< len(coins); i++)
        print(coin)
        sum = sum + coin

    print(sum)
    return sum

count_coins(coins)













# def loop_example():
    
#     coins = [2,1]
#     sum = 0 

#     for coin in coins:
#         sum = sum + coin
    
#     print(sum)
















# import dis
# print(dis.dis(loop_example))