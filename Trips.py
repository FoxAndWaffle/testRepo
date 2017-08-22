city = raw_input("Where do you wanr ro go? Charlotte, Tampa, Pittsburgh, Los Angeles?")
days = raw_input("For how long?")
spending_money = raw_input("How much spending money will you bring?")


def hotel_cost(days):
  return 140 * days

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475

def rental_car_cost(days):
  cost = days * 40
  if days >= 7:
    cost -= 50
  elif days >= 3:
    cost -= 20
  return cost

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    
print "Your trip will cost " + trip_cost()