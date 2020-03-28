market = {"dairy":["yogurt", "cheese"], "fruits": ['banana', 'apple', 'orange', 'lemon', 'apple', 'banana','banana']}

market["candies"] = ['mars', 'kinder', 'twix']

market['fruits'].sort(reverse=False)
market['fruits'] = list(set(market['fruits']))

print(market)