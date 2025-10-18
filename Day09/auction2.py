import art
print(art.pic)

def find_highest_bidder(bidding_dictionary):
  highest_bid = 0
  winner = ''
  for bidder in bidding_dictionary:
    bid_amound = bidding_dictionary[bidder]
    if bid_amound > highest_bid:
      highest_bid = bid_amound
      winner = bidder
  print(f"the winner is {winner}, with bid {highest_bid}")


bid = {}
continue_bidding = True
while continue_bidding:
  name = input("Enter your name: ")
  bid_price = int(input("Enter your bid:$ "))
  bid[name] = bid_price
  # print(bid)
  should_continue = input("'yes' if there is other bidder 'no' if there is no other bidder\n").lower()
  if should_continue == "no":
    continue_bidding = False
    find_highest_bidder(bid)
  else:
    print('\n' * 20)
    print(art.pic)

