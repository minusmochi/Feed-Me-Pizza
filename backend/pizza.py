import random
import tweetBuilder
toppings = ["whipped cream", "hands of lego people", "gummy bears", "toothpaste"]
#print (toppings [random.randint(0, len(toppings)-1)])
topping = toppings [random.randint(0, len(toppings)-1)]
print (tweetBuilder.constructTweet(topping))