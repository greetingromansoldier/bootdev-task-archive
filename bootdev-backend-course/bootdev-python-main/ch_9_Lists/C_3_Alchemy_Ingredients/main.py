# code before changes:

# def check_ingredient_match(recipe, ingredients):
#     pass

# assignment:

# Finish the check_ingredient_match function by looping over the recipe list. 
# The function should calculate and return a percentage of ingredients the character has, 
# as well as a list of missing from the recipe.

# For example, if these were the lists:

# recipe = ["Dragon Scale", "Unicorn Hair", "Phoenix Feather", "Troll Tusk"]
# ingredients = ["Dragon Scale", "Goblin Ear", "Phoenix Feather", "Troll Tusk"]

# percentage, missing_ingredients = check_ingredient_match(recipe, ingredients)
# print(percentage, missing_ingredients)
# # Prints: 75.00 ["Unicorn Hair"]

# actual code:

# plan:

# 1) set for match ingredients
# 2) set for missing ingredients
# 3) divide match/missing
# 3.1) return percentage
# 4) return missing ingredients

def check_ingredient_match(recipe, ingredients):
    match_ingredients = []
    missing_ingredients = []
    percentage = 0
    
    for ingredient in recipe: # здесь была самая большая проблема: я сначала перепутал собранные ингредиенты и рецептовые местами и почему-то это вызывало ошибку, но в итоге всё окейси
        check_ingredient = ingredient in ingredients # благодаря тому что решил баг создал эту логику, вспомнил из конспекта, что эта переменная будет принимать значения True/False, в зависимости от нахождения элемента в искомом списке. и таким образом ещё избежал сложностей с двумя циклами
        if check_ingredient == True:
            match_ingredients.append(ingredient)
        else:
            missing_ingredients.append(ingredient)
        
    percentage = (len(match_ingredients) / len(recipe)) * 100    
            

    


    return percentage, missing_ingredients


