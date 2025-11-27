# CS372 Final Project: Food Image to Recipe
## Ananya Bhatia

## What It Does
My project is a food image to recipe converter that takes in an image of a food, along with the name of the dish, and outputs a recipe for how to make that food. The goal of this project was to make something that people could potentially use at restaurants when they really like a dish. At a restaurant, you only really have a picture of the dish and the name from the menu, but have no idea how to make it. This is definitely a real world problem I have run into in my life and wish there was something that could help with it. The image is sent to a CNN which outputs a list of ingredients, then this list of ingredients along with the name of the dish is sent to a small LLM which generates the recipe. I have trained a baseline small CNN from scratch and fine tuned ResNet for the task. The project runs on a dataset from HuggingFace and any image from the dataset (can use validation or test split) can be selected to run the model on. 

## Quick Start
To run the project, create a Python environment and download all dependencies that are outlined in requirements.txt. After that, you can quickly run the project (assuming you have the model weights in the models folder) by going to notebooks/Inference.ipynb and running all the cells. Cells 7 and 9 are the cells that actually run inference. Cell 7 uses the fine tuned ResNet and cell 9 uses the baseline CNN model. Line 2 of both cell 7 and cell 9 can be changed to try different images of food from the test set. Simply change the number in the square brackets. See SETUP.md for a more comprehensive guide. 

## Video Links
- Demo Video Link
- Technical Walkthrough Link

## Evaluation
See docs/EXAMPLES.md for many examples. Below I will present just one example from testing comparing the baseline model to the fine tuned ResNet, both using the same LLM afterwards. 

### Comparison of Baseline to ResNet: American Burger

**Input Image:**

![Dish Image](/docs/result_images/val_45.png)

### Baseline
**CNN Output (Ingredients):** ['olive oil', 'mayonnaise', 'egg', 'parsley', 'beef', 'tomato', 'black pepper', 'potatoes', 'cream', 'wheat flour', 'shrimp', 'sour cream', 'oil', 'salmon', 'red onion', 'milk', 'mustard', 'avocado', 'mushrooms', 'bacon', 'pollock', 'gouda cheese', 'balsamic vinegar', 'honey', 'corn', 'shallots', 'apple', 'panko breadcrumbs', 'lettuce', 'broccoli', 'sweet potato', 'lentils', 'rosemary', 'pepper', 'bread', 'potato', 'texmex seasoning', 'sauce', 'tarragon', 'brioche bun', 'beef broth', 'cumin', 'baguette', 'coconut', 'tortilla chips', 'lemon juice', 'chili peppers', 'kale', 'red chili pepper', 'worcestershire sauce', 'red cabbage', 'red wine sauce', 'smoked paprika', 'barbecue sauce', 'jalapeno pepper', 'egg yolk', 'duck breast', 'sunflower oil', 'duck leg', 'mushroom']

**LLM Output (Recipe):** 
Dish name: American Burger
Ingredients: olive oil, mayonnaise, egg, parsley, beef, tomato, black pepper, potatoes, cream, wheat flour, shrimp, sour cream, oil, salmon, red onion, milk, mustard, avocado, mushrooms, bacon, pollock, gouda cheese, balsamic vinegar, honey, corn, shallots, apple, panko breadcrumbs, lettuce, broccoli, sweet potato, lentils, rosemary, pepper, bread, potato, texmex seasoning, sauce, tarragon, brioche bun, beef broth, cumin, baguette, coconut, tortilla chips, lemon juice, chili peppers, kale, red chili pepper, worcestershire sauce, red cabbage, red wine sauce, smoked paprika, barbecue sauce, jalapeno pepper, egg yolk, duck breast, sunflower oil, duck leg, mushroom

Write a detailed recipe with 5–8 steps.

Solution:
1. Preheat the oven to 400°F.
2. In a large bowl, mix together the olive oil, mayonnaise, egg, and parsley until well combined.
3. In a separate bowl, combine the beef, tomato, black pepper, potatoes, cream, wheat flour, shrimp, sour cream, oil, salmon, red onion, milk, mustard, avocado, mushrooms, bacon, pollock, gouda cheese, balsamic vinegar, honey, corn, shallots, apple, panko breadcrumbs, lettuce, broccoli, sweet potato, lentils, rosemary, pepper, bread, potato, texmex seasoning, sauce, tarragon, brioche bun, beef broth, cumin, baguette, coconut, tortilla chips, lemon juice, chili peppers, kale, red chili pepper, worcestershire sauce, red cabbage, red wine sauce, smoked paprika, barbecue sauce, jalapeno pepper, egg yolk, duck breast, sunflower oil, duck leg, and mushroom.
4. Add the mixture to the bowl with the olive oil and mayonnaise and mix well.
5. Pour the mixture into a baking dish and spread it evenly.
6. Bake for 30 minutes, or until the top is golden brown and the filling is heated through.
7. Serve hot and enjoy your delicious dish.

### ResNet
**CNN Output (Ingredients):** ['salt', 'olive oil', 'butter', 'beef', 'tomato', 'brioche bun']

**LLM Output (Recipe):** 
Dish name: American Burger
Ingredients: salt, olive oil, butter, beef, tomato, brioche bun

Write a detailed recipe with 5–8 steps.

Answer:
1. Gather your ingredients. You will need 1 pound of ground beef, 1/4 cup of salt, 2 tablespoons of olive oil, 2 tablespoons of butter, 1 onion, 1 tomato, and a brioche bun.
2. In a large bowl, mix together the ground beef, salt, and olive oil.
3. Shape the mixture into a patty and place it on a flat surface.
4. In a separate pan, melt the butter and add the chopped onion. Cook for about 5 minutes, until the onion is softened.
5. Add the tomato to the pan and let it cook for another 5 minutes.
6. Preheat your grill to medium-high heat. Place the patty on the grill and cook for about 5-7 minutes, flipping once, until it is cooked through.
7. Remove the patty from the grill and let it rest for a few minutes.
8. Place the brioche bun down and add the patty, onion, and tomato mixture. Top with a dollop of sour cream and enjoy your delicious dish!

From this test, we can see the impact of the fine tuned ResNet over the small CNN trained from scratch. The small CNN predicted many ingredients that are clearly not part of this dish and the recipe is much longer because of all the extra ingredients. The ResNet actually predicted a decent number of ingredients and it could definitely be realistic for a recipe. We can definitely still see some mistake, like how the last step says to top with a dollop of sour cream but that is not an ingredient that is even listed, but overall it seems decently realistic.  

## Individual Contributions
Solo project, so all work was done by me. 
