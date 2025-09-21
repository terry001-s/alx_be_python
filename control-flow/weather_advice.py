weather = ["sunny","rainy","cold"]
Question = input("What's the weather like today? (sunny/rainy/cold): ").lower()
if Question == "sunny":
    print(" Wear a t-shirt and sunglasses.")
elif Question == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif Question == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else :
    print("Sorry, I don't have recommendations for this weather.")