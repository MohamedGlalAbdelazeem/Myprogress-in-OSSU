



# take input form user 

def complet_price(coin):
    total_price = 50 - coin
    print("Amount Due :" , total_price)
    
    
    
def main():
    coin = int(input("Insert Coin:"))
    amount_due = complet_price(coin)
    return amount_due

main()


