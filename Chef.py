import random

# Introduction
print("Welcome to Chef's Kitchen in Trypokaridos! 🍳👩‍🍳")

# List of ingredients and dishes
ingredients = ["tomatoes", "mushrooms", "cheese", "onions", "bell peppers", "basil"]
dishes = ["pizza", "pasta", "salad", "sandwich", "soup"]

# Get the chef's name
chef_name = input("What's your chef's name? ")

# Fun commands and interactions
print(f"\nHello, Chef {chef_name}! Let's get cooking in Trypokaridos! 🌟")

# Randomly select ingredients and a dish
selected_ingredients = random.sample(ingredients, 3)
selected_dish = random.choice(dishes)

# Display chosen ingredients and dish
print(f"\nToday, you will make a delicious {selected_dish} using:")
for ingredient in selected_ingredients:
    print(f"- {ingredient}")

# Fun cooking steps
print("\nFollow these steps to make your dish:")
print("1. Wash and chop the ingredients. 🥒")
print("2. Heat the pan and add a splash of olive oil. 🥘")
print(f"3. Add {', '.join(selected_ingredients)} to the pan and cook until tender. 🍳")
print(f"4. Mix everything together and voilà! You've made a wonderful {selected_dish}! 🎉")

# Finishing touch
print("\nBon appétit, Chef! Enjoy your culinary creation! 🍽️")

# Optional fun message
fun_messages = [
    "Try adding a sprinkle of magic for extra flavor! ✨",
    "Remember, a happy chef makes the best food! 😊",
    "Don't forget to share your dish with friends and family! 👨‍👩‍👧‍👦"
]

print("\n" + random.choice(fun_messages))
