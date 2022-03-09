hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
for price in prices:
  total_price += price
average_price = total_price / len(prices)
print("Average Haircut Price : " + str(average_price))
new_prices = [price -5 for price in  prices]
print("New Price: " +str(new_prices))
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue = prices[i] + last_week[i]
print("Total Revenue: " + str(total_revenue))
average_daily_revenue = total_revenue / 7
print("Average daily revenue: " + str(average_daily_revenue))
cuts_under_30 = [new_prices[i] for i in range(len(new_prices)-1) if new_prices[i] < 30]
print("Cuts under 30: " + str(cuts_under_30))