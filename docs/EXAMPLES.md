# Example Results

### Result 1 - Loaded Sweet Potato Skins

**Input Image:**

![Dish Image](/docs/result_images/val_9.png)

**CNN Output (Ingredients):** ['salt', 'garlic', 'butter', 'water', 'sugar', 'onion', 'vegetable oil', 'tomatoes', 'bell pepper', 'sour cream', 'chili pepper', 'scallions', 'paprika', 'gouda cheese', 'sweet potato', 'seasoning', 'texmex seasoning', 'black beans', 'red chili pepper', 'smoked paprika']

**LLM Output (Recipe):**
Dish name: Loaded Sweet Potato Skins
Ingredients: salt, garlic, butter, water, sugar, onion, vegetable oil, tomatoes, bell pepper, sour cream, chili pepper, scallions, paprika, gouda cheese, sweet potato, seasoning, texmex seasoning, black beans, red chili pepper, smoked paprika

Write a detailed recipe with 5–8 steps.

Answer: 1. Preheat oven to 400°F (200°C).
1. Cut sweet potatoes into thin slices.
2. In a small bowl, mix together salt, garlic, and butter.
3. Lay the sweet potato slices on a baking sheet and sprinkle with salt, garlic butter, and water.
4. Bake for 25-30 minutes or until the sweet potatoes are tender.
5. In a separate pan, heat up oil and add diced onions, bell pepper, and tomatoes.
6. Cook until the vegetables are soft and add chilis and chili powder for additional spice.
7. In a blender, mix together sweet potato, seasoning, texmex seasoning, black beans, red chili pepper, and smoked paprika.
8. Add the blended mixture to the pan with the vegetables and mix well.
9.  Top with scallions and shredded gouda cheese.
10. Enjoy your delicious Loaded Sweet Potato Skins!

This recipe seems realistic to me, it seems like all the seasonings are plausible and I am happy that the ResNet model got sour cream as one of the ingredients. I don't see black beans in the image but it is definitely in theme with the dish to have black beans so I am honestly not mad about that. I do think it is interesting that the LLM suggests to blend the black beans with the sweet potato -- not something I would've personally done but still realistic. 

### Result 2 - Crispy Chicken
**Input Image:**

![Dish Image](/docs/result_images/val_20.png)

**CNN Output (Ingredients):** ['salt', 'chicken breast', 'vegetable oil', 'egg', 'bread crumbs', 'panko bread crumbs']


**LLM Output (Recipe):**
Dish name: Crispy chicken
Ingredients: salt, chicken breast, vegetable oil, egg, bread crumbs, panko bread crumbs

Write a detailed recipe with 5–8 steps.

Answer:
1. Preheat the oven to 425°F (220°C).
2. In a shallow dish, mix salt and flour. Set aside.
3. In another shallow dish, combine the beaten egg and bread crumbs.
4. Dip each chicken breast into the flour mixture, making sure it is evenly coated.
5. Next, dip the chicken into the egg mixture, coating it completely.
6. Finally, coat the chicken in the bread crumb mixture, pressing it firmly onto the surface.
7. Place the breaded chicken on a baking sheet lined with parchment paper.
8. Repeat the process with the remaining chicken pieces.
9. Bake the chicken in the oven for 20–25 minutes, or until it is golden brown and cooked through.
10. Once done, remove the chicken from the oven and let it rest for a few minutes before serving.

I think that this recipe is pretty spot on. Crispy chick is relatively simple and the LLM is able to give a super realistic recipe for dredging the chicken in flour, then eggs, then breadcrumbs which is a super classic cooking technique and I was really happy that the LLM was able to predict that. 

### Result 3 - Buddha Bowl
**Input Image:**

![Dish Image](/docs/result_images/val_40.png)

**CNN Output (Ingredients):** ['salt', 'olive oil', 'jasmine rice']

**LLM Output (Recipe):**
Dish name: Buddha Bowl
Ingredients: salt, olive oil, jasmine rice

Write a detailed recipe with 5–8 steps.

Solution:
1. In a large pot, bring water to a boil.
2. Add 2 cups of jasmine rice and stir.
3. Reduce heat to low and cover the pot with a lid.
4. Let the rice cook for 18–20 minutes, until all the water is absorbed.
5. While the rice is cooking, prepare the Buddha Bowl by heating some olive oil in a pan.
6. Add some salt and your choice of seasoning to the pan, and stir-fry the rice for about 3–5 minutes until it is slightly browned.
7. Add your choice of protein, vegetables, and sauce to the pan, and stir-fry for 2–3 minutes.
8. Serve the Buddha Bowl in a bowl, and top it with some fresh herbs for garnish.

This is an interesting example of the model not doing very well. It could only pinpoint three ingredients of salt, olive oil, and jasmine rice. However, you can see that the LLM caught onto that and in step 7 suggests to add your choice of protein and vegetables. 

### Result 4 - Tandoori Shrimp
**Input Image:**

![Dish Image](/docs/result_images/val_80.png)

**CNN Output (Ingredients):** ['salt', 'garlic', 'butter', 'sugar', 'black pepper', 'chili flakes', 'cucumber', 'rice', 'jasmine rice', 'shrimp', 'yogurt', 'red onion', 'mint', 'mango', 'coconut', 'lime juice', 'tikka masala']


**LLM Output (Recipe):** 
Dish name: Tandoori Shrimp
Ingredients: salt, garlic, butter, sugar, black pepper, chili flakes, cucumber, rice, jasmine rice, shrimp, yogurt, red onion, mint, mango, coconut, lime juice, tikka masala

Write a detailed recipe with 5–8 steps.

Answer:
Step 1: In a small pan, mix salt, garlic, butter, sugar, black pepper, and chili flakes.
Step 2: Add cucumber and sauté for a few minutes until it becomes tender.
Step 3: Add jasmine rice and cook until it is soft.
Step 4: Add shrimp and sauté until it turns pink.
Step 5: In a separate pan, mix yogurt, red onion, mint, mango, coconut, and lime juice.
Step 6: Pour the mixture over the shrimp and rice.
Step 7: Cook for a few more minutes until the rice is heated through.
Step 8: Serve hot with tikka masala on the side.

I think that the recipe for this was also relatively realistic and the ingredients that it uses is relatively spot on to what it seems like is in this dish. One interesting note is that this thinks in step 2 that we should be cooking cucumber which is probably not great and it probably should just be served raw. 

### Result 5 - Brazilian Prawn and Coconut Stew
**Input Image:**

![Dish Image](/docs/result_images/val_110.png)

**CNN Output (Ingredients):** ['salt', 'olive oil', 'butter', 'water', 'lime', 'tomatoes', 'cilantro', 'peanuts', 'shrimp', 'coconut milk', 'red onion', 'corn', 'basmati rice', 'lime juice']

**LLM Output (Recipe):**
Dish name: Brazilian Prawn and Coconut Stew
Ingredients: salt, olive oil, butter, water, lime, tomatoes, cilantro, peanuts, shrimp, coconut milk, red onion, corn, basmati rice, lime juice

Write a detailed recipe with 5–8 steps.

Solution:
Step 1: Rinse the rice in cold water until the water runs clear.
Step 2: Place the rinsed rice in a pot with 2 cups of water and bring it to a boil over high heat.
Step 3: Once the water is boiling, reduce the heat to low and cover the pot with a lid. Let the rice simmer for 15–20 minutes or until all the water is absorbed.
Step 4: While the rice is cooking, heat the olive oil in a large skillet over medium-high heat.
Step 5: Add the shrimp to the skillet and cook until pink and opaque, about 2-3 minutes. Remove the shrimp from the skillet and set them aside.
Step 6: In the same skillet, add the red onion, corn, and basmati rice. Cook for 2-3 minutes or until the rice is slightly toasted.
Step 7: Add the coconut milk, lime juice, and cilantro to the skillet and stir well.
Step 8: Return the shrimp to the skillet and stir everything together until well combined.
Step 9: Serve the fried rice topped with peanuts and lime wedges.

I thought that the model did pretty well with this image and got a decent amount of ingredients out of the dish and also gives a relatively normal looking recipe for it. 

## Comparison of Baseline to ResNet: American Burger

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
