from recipe import Recipe, RecipeManager

def add_recipe_input(manager): #Manager exists in the main function. It is not defined until then but is simply a reference to RecipeManager.
    title = input("Enter the recipe title: ")
    ingredients = input("Enter the ingredients (comma-separated): ").split(',')
    instructions = input("Enter the instructions: ")
    while True:
        try:
            cook_time = int(input("Enter the cooking time (in minutes): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number (in minutes) for cooking time.")
    dietary = input("Enter the dietary information: ")
    
    #Because we are refering back to RecipeManager which already knows what title, ingredients etc are (it's a child of Recipe) we don't need to specify them again for the function other than that they become the input.

    new_recipe = Recipe(title, ingredients, instructions, cook_time, dietary) #We are setting the function to use the Recip Class. new_recipe becomes the parts of Recipe in the defined dictionary.
    manager.add_recipe(new_recipe) #RecipeManager.add_recipe(new_recipe)

def update_recipe_input(manager):
    index = int(input("Enter the index of the recipe to update: ")) - 1
    if 0 <= index < len(manager.recipes): #Checking that it's greater than or equal to 0. (Remember we start at 0 but we have - 1 to account for users expecting 1 for the first). Also checking it isn't less than the number of recipes in the list.
        title = input("Enter the updated recipe title: ")
        ingredients = input("Enter the updated ingredients (comma-separated): ").split(',')
        instructions = input("Enter the updated instructions: ")
        cook_time = int(input("Enter the updated cooking time (in minutes): "))
        dietary = input("Enter the updated dietary information: ")

        updated_recipe = Recipe(title, ingredients, instructions, cook_time, dietary) #Calling the update recipe function in RecipeManager.
        manager.update_recipe(index, updated_recipe)
    else:
        print("Invalid recipe index.") #For if the input isn't correct. May need to catch ValueError, I haven't accounted for this.

def delete_recipe_input(manager):
    index = int(input("Enter the index of the recipe to delete: ")) - 1
    manager.delete_recipe(index) #Should be clear that this is basically the same as the others but calling a different function. In this case delete_recipe.

def display_recipes(manager):
    for i, recipe in enumerate(manager.recipes, start=1):
        print(f"\nRecipe {i}:")
        print(f"Title: {recipe['title']}")
        print(f"Ingredients: {', '.join(recipe['ingredients'])}")
        print(f"Instructions:\n{recipe['instructions']}")
        print(f"Cook Time: {recipe.get('cook_time', 'N/A')} minutes")
        print(f"Dietary: {recipe['dietary']}")

def main(): #This is our main important loop after the inputs. We can also have some manual recipes exist here prior to running so that we do not start blank. I have not done that here. This has nothing to do with unrelated Belgian techno anthem Pump Up The Jam.
    
    manager = RecipeManager() #Here is where manager becomes RecipeManager.
    
    manager.load_recipe("recipes.txt") #Load recipes from the file recipes.txt.

    while True: #While it is running this is the output.
        print("\n--- Recipe Manager Menu ---")
        print("1. Add Recipe")
        print("2. Update Recipe")
        print("3. Delete Recipe")
        print("4. Display Recipes")
        print("5. Save Recipes")
        print("6. Quit")

        command = input("> ") #Definitely not reusing this from room game.

        if command == '1':
            add_recipe_input(manager)
        elif command == '2':
            update_recipe_input(manager)
        elif command == '3':
            delete_recipe_input(manager)
        elif command == '4':
            display_recipes(manager)
        elif command == '5':
            manager.save_recipe("recipes.txt")  #Save recipes to a recipes.txt
            print("Recipes saved to 'recipes.txt'.")
        elif command == '6':
            break #Breakout of the program, cue the flashdance maniac music.
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main() #Run main() while __name__ is __main__.