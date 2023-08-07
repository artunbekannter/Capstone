import tkinter as tk
from tkinter import messagebox
from recipe import Recipe, RecipeManager



# ⠀⠀⠀⠀⠀⠀⠀⠀⠀▄   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀▄    
# ⠀⠀⠀⠀⠀⠀⠀⠀▌▒█⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀▄▀▒▌   
# ⠀⠀⠀⠀⠀⠀⠀⠀▌▒▒█⠀⠀⠀⠀⠀⠀⠀⠀▄▀▒▒▒▐   
# ⠀⠀⠀⠀⠀⠀⠀▐▄█▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐   
# ⠀⠀⠀⠀⠀▄▄▀▒▒▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐   
# ⠀⠀⠀▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒⠀▌   
# ⠀⠀▐▒▒▒▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄▒▌  
# ⠀⠀ ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐  
# ⠀▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌
# ⠀▌░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌ 
# ▌▒▒▒▄██▄▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▐ 
# ▐▒▒▐▄█▄█▌▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
# ▐▒▒▐▀▐▀▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▐ 
# ⠀▌▒▒▀▄▄▄▄▄▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▒▌ 
# ⠀▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒▒▄▒▒▐  
# ⠀⠀▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒▄▒▒▒▒▌  
# ⠀⠀⠀⠀▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀   
# ⠀⠀⠀⠀⠀⠀▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀     
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀▀▀▀▀▀▀▀▀▀▀▀▀        


manager = RecipeManager() #Same principle as in main.py but we need this now for the tkinter GUI because we are no longer using input() - this is GUI not CLI.

manager.load_recipe("recipes.txt") #Gotta load in that recipes.txt

def add_recipe():
    title = entry_title.get()
    ingredients = entry_ingredients.get().split(',')
    instructions = text_instructions.get("1.0", tk.END)
    while True:
        try:
            cook_time = int(entry_cook_time.get())
            break
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a number (in minutes) for cooking time.")
            return
    dietary = entry_dietary.get()

#We are defining what each variable in the function is. The entry_ etc are referred to by tkinter later on, as these are the inputs in the GUI that the variables become.

    new_recipe = Recipe(title, ingredients, instructions, cook_time, dietary) #We are saying that new_recipe uses the class Recipe with the important variables of that class.
    manager.add_recipe(new_recipe) #Manager is RecipeManager, we are using the add_recipe function with RecipeManager, the information is new_recipe (Recipe class variables).
    display_recipes() #We display the recipes after adding.

def update_recipe():
    selected_recipe = listbox_recipes.curselection() #Selected index is essentially what recipe we have selected from the list.
    if not selected_recipe:
        messagebox.showwarning("Warning", "Please select a recipe to update.")
        return #We can't update the recipe if no recipe is selected so we need a warning that warns us we are trying to update nothing.

    index = selected_recipe[0]
    title = entry_title.get()
    ingredients = entry_ingredients.get().split(',')
    instructions = text_instructions.get("1.0", tk.END)
    while True:
        try:
            cook_time = int(entry_cook_time.get())
            break
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a number for Cook Time.")
            return
    dietary = entry_dietary.get()

    updated_recipe = Recipe(title, ingredients, instructions, cook_time, dietary)
    manager.update_recipe(index, updated_recipe)
    display_recipes() #This is almost identical to add_recipe. The only difference is that here updating rather than adding. The code is similar, except we are accounting for the index of the selected recipe as well as updating the recipe.

def delete_recipe():
    selected_recipe = listbox_recipes.curselection()
    if not selected_recipe:
        messagebox.showwarning("Warning", "Please select a recipe to delete.")
        return

    index = selected_recipe[0]
    manager.delete_recipe(index) #Delete recipe function is used with RecipeManager to delete the selected recipe index (i.e Recipe 1 if it's selected.)
    display_recipes()

def display_recipes():
    listbox_recipes.delete(0, tk.END)
    for recipe in manager.recipes:
        listbox_recipes.insert(tk.END, recipe['title'])

def on_recipe_select(click):
    selected_recipe = listbox_recipes.curselection()
    if selected_recipe:
        index = selected_recipe[0]
        recipe = manager.recipes[index]
        entry_title.delete(0, tk.END) #Basically we want to clear anything that's already in the GUI field for tkinter, for example the previously selected recipe. We don't want things to overlap.
        entry_title.insert(tk.END, recipe['title']) #Once we've deleted anything that was already displayed we add what is new from the recipe we have selected.

        entry_ingredients.delete(0, tk.END)
        entry_ingredients.insert(tk.END, ", ".join(recipe['ingredients']))

        text_instructions.delete("1.0", tk.END)
        text_instructions.insert(tk.END, recipe['instructions'])

        entry_cook_time.delete(0, tk.END)
        entry_cook_time.insert(tk.END, str(recipe['cook_time']))

        entry_dietary.delete(0, tk.END)
        entry_dietary.insert(tk.END, recipe['dietary'])

main_window = tk.Tk() #So this is the main part of the tkinterface. To make it easy we're calling it main_window. It's the primary window that everything else displays in.
main_window.title("Recipe Manager") #We gotta give it a name. This is like the warning boxes we have above. "Recipe Manager" is what we want the top bar to say because that's what the main program is.

frame_recipes = tk.Frame(main_window)
frame_recipes.pack(side=tk.LEFT, padx=10, pady=10) #Padding makes it's debut. This is similar to CSS, but the padding is the margin in CSS. We are also saying tht we want the recipes to be on the LEFT. Why the left? Well we are reading left to right. We want to select a recipe first before we read it. Not read the recipe then select.

listbox_recipes = tk.Listbox(frame_recipes, width=30) #We're making a listbox, in this case we are using frame_recipes
listbox_recipes.pack(side=tk.LEFT, fill=tk.BOTH) #Well we definitely want the list on the left, and we also want it to be able to fill up that space. tk.BOTH lets us say that it can expand in width and height.

scrollbar_recipes = tk.Scrollbar(frame_recipes, command=listbox_recipes.yview) 
scrollbar_recipes.pack(side=tk.RIGHT, fill=tk.Y) #It's a scrollbar. We don't want it to fill X, it should get taller, but not wider. And well, aren't scrollbars usually on the right?

listbox_recipes.config(yscrollcommand=scrollbar_recipes.set)

frame_buttons = tk.Frame(main_window)
frame_buttons.pack(side=tk.LEFT, padx=10) #Buttons are going on the left of the main window, but think of this in terms of code going from top to bottom, it will be on the left, but less on the left than the list and scrollbar.

btn_add = tk.Button(frame_buttons, text="Add Recipe", command=add_recipe) #Definitely not using command from the room lesson again, nope no way.
btn_add.pack(side=tk.TOP, pady=5)#This goes on top of the left side after our list.

btn_update = tk.Button(frame_buttons, text="Update Recipe", command=update_recipe)
btn_update.pack(side=tk.TOP, pady=5) #Yep you guessed it, this is on the top, but less on top than add.

btn_delete = tk.Button(frame_buttons, text="Delete Recipe", command=delete_recipe)
btn_delete.pack(side=tk.TOP, pady=5) #Need I say it again? This is on the top but it's at the bottom.

frame_details = tk.Frame(main_window)
frame_details.pack(side=tk.LEFT, padx=10)

label_title = tk.Label(frame_details, text="Title:")
label_title.pack(side=tk.TOP)

entry_title = tk.Entry(frame_details, width=30)
entry_title.pack(side=tk.TOP)

label_ingredients = tk.Label(frame_details, text="Ingredients:")
label_ingredients.pack(side=tk.TOP)

entry_ingredients = tk.Entry(frame_details, width=30)
entry_ingredients.pack(side=tk.TOP)

label_instructions = tk.Label(frame_details, text="Instructions:")
label_instructions.pack(side=tk.TOP)

text_instructions = tk.Text(frame_details, width=30, height=10) #Hmm I wonder why we added height here. Have you seen Jaws? "We're gonna need a bigger boat". Well here we're gonna need a bigger box.
text_instructions.pack(side=tk.TOP)

label_cook_time = tk.Label(frame_details, text="Cook Time (minutes):")
label_cook_time.pack(side=tk.TOP)

entry_cook_time = tk.Entry(frame_details, width=30)
entry_cook_time.pack(side=tk.TOP)

label_dietary = tk.Label(frame_details, text="Dietary Information:")
label_dietary.pack(side=tk.TOP)

entry_dietary = tk.Entry(frame_details, width=30)
entry_dietary.pack(side=tk.TOP)

display_recipes() #Time to callback to that function above in the code.

listbox_recipes.bind("<<ListboxSelect>>", on_recipe_select) #well we gotta bind the selection to the listbox when you select a recipe haven't we?

btn_quit = tk.Button(frame_details, text="Quit", command=main_window.quit) #We gotta .quit out if somebody wants to quit.
btn_quit.pack(side=tk.BOTTOM, pady=10) #This button goes at the bottom of the right?

main_window.mainloop() #Because VSCode isn't replit, if we don't mainloop it it won't keep the GUI open. This was a nightmare to figure out, thank goodness for StackOverflow.

#https://stackoverflow.com/questions/68547433/window-is-not-showing-up-at-all-in-vscode-tkinter
