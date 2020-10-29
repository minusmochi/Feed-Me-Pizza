import random
import tweetBuilder
def getPizzaTweet():
    toppings = ["whipped cream", "hands of lego people", "gummy bears", "toothpaste", "super glue", "fresh pubes", "motor oil", 
    "pebbles", "wood shavings", "sticky notes", "sand", "dust mites", "oxygen", "sea shells", "daisies", "paper people",
    "tiny Yoshis", "diamonds", "toe nails", "playdough", "bullets", "golf balls", "body lotion", "confetti", "scissors", 
    "paper clips", "coasters", "bow ties", "flapjacks", "percy pigs", "snails", "monocles", "bibles"]
    #print (toppings [random.randint(0, len(toppings)-1)])
    topping = toppings [random.randint(0, len(toppings)-1)]
    return tweetBuilder.constructTweet(topping)

#print (getPizzaTweet())