import art
print("\n" * 15)

print(art.pic)

name = input("Enter your name: ")
bid_price = int(input("Enter your bid:$ "))

bid = {}
bid[name] = bid_price
print(bid)

should_continue = input("'yes' if there is other bidder 'no' if there is no other bidder").lower()


