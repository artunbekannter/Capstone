import os

class Recipe():
    def __init__(self, title, ingredients, instructions, cook_time, dietary):
        self.recipe = {
            'title': title,
            'ingredients': ingredients,
            'instructions': instructions,
            'cook_time': cook_time,
            'dietary': dietary
        }
               
    def get_title(self): #Get the title of the recipe
        return self.recipe['title']

    def set_title(self, title): #Set the title of the recipe
        self.recipe['title'] = title #self.recipe title in dictionary = title.

    def get_ingredients(self):
        return self.recipe['ingredients']

    def set_ingredients(self, ingredients):
        self.recipe['ingredients'] = ingredients
        
class RecipeManager(Recipe):
    def __init__(self):
        super().__init__("", [], "", 0, "") #Title string, ingredients list, instructions string, cook time integer, dietary string.
        self.recipes = []

    def load_recipe(self, filename):
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                recipe_data = file.readlines()
            current_recipe = None

            for line in recipe_data:
                line = line.strip()
                if line:
                    if line.startswith('Title:'):
                        if current_recipe is not None:
                            self.recipes.append(current_recipe)
                        current_recipe = {'title': line[len('Title: '):]}
                    elif line.startswith('Ingredients:'):
                        current_recipe['ingredients'] = [ingredient.strip() for ingredient in line[len('Ingredients: '):].split(',')]
                    elif line.startswith('Instructions:'):
                        current_recipe['instructions'] = line[len('Instructions: '):]
                    elif line.startswith('Cook Time:'):
                        current_recipe['cook_time'] = int(line[len('Cook Time: '):])
                    elif line.startswith('Dietary:'):
                        current_recipe['dietary'] = line[len('Dietary: '):]
            if current_recipe is not None:
                self.recipes.append(current_recipe)

        else:
            print(f"File {filename} not found. Creating a new file.")
            self.save_recipe(filename)

    def add_recipe(self, recipe):
        self.recipes.append(recipe.recipe) #Appending a recipe to recipe to add to file.
        self.save_recipe("recipes.txt") #Added to also save the added recipe.

    def delete_recipe(self, index):
        if index >= 0 and index < len(self.recipes): #We need the index to be greater than or equal to 0 otherwise nothing exists to delete. We also need to check the index is less than the number of recipes in the list. Otherwise we would delete a non-existant entry
            del self.recipes[index]

    def update_recipe(self, index, recipe):
        if index >= 0 and index < len(self.recipes):
            self.recipes[index] = recipe.recipe #Same as prior but update instead of delete.
            self.save_recipe("recipes.txt") #Added to also save when a recipe is deleted.
            print(f"Recipe deleted and recipes saved.") 
        else:
            print(f"Invalid recipe index.") #Added so that returned error if deletion selection doesn't exist.
    
    def save_recipe(self, filename):
        with open(filename, 'w') as file:
            for recipe in self.recipes:
                file.write(f"Title: {recipe['title']}\n")
                file.write(f"Ingredients: {', '.join(recipe['ingredients'])}\n")
                file.write(f"Instructions: {recipe['instructions']}\n")
                file.write(f"Cook Time: {recipe['cook_time']}\n")
                file.write(f"Dietary: {recipe['dietary']}\n")
                file.write("---\n")