# Finished "Lost"
def finish_lost():
    print("Finally finished watching LOST!")
    questions = [
        "1. What was the smoke monster?",
        "2. Why was the island magical?",
        "3. What actually happened in the end?"
    ]
    
    print("\nI'm still wondering about these questions:")
    for question in questions:
        print(question)
    
    choice = input("\nPick a question to ponder (1, 2, or 3): ")

    try:
        choice = int(choice)
        if 1 <= choice <= 3:
            if choice == 1:
                print(f"You chose: {questions[0]}")
                print("Monster that smokes a lot :=")
            elif choice == 2: 
                print(f"You chose: {questions[1]}") 
                print("Hmm... ") 
            elif choice == 3: 
                print(f"You chose: {questions[2]}")
                print("Watch again")
    except ValueError:
        print("Invalid input. Were you even watching the show? 🤔")

# Call the function
finish_lost()
# test comment