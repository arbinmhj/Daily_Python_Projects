prices = input("Write the given prices you have researched: ").split()
for n in range(0, len(prices)):
  prices[n] = int(prices[n])
print(prices)

highest_price = 0
lowest_price = 0
for price in prices:
  if price > highest_price :
    highest_price = price
  elif price < lowest_price :
    lowest_price = price
print(f"The highest price is {highest_price}!") 
print(f"The lowest price is {lowest_price}!")

total_price = 0
num_of_items = 0
for price in prices:
  total_price += price
print(f"The total price is {total_price}!")

for price in prices:
  num_of_items += 1
average_price = round(total_price/num_of_items, 2)
print(f"The average price is {average_price}")