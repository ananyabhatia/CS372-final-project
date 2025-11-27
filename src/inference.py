import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


def load_text_generator(model_name="microsoft/phi-2"):
    return pipeline("text-generation", model=model_name, device_map="auto")

def build_prompt(ingredients, dish_name=None):
    base = "Create a step-by-step cooking recipe using the following ingredients:\n"
    ing_list = ", ".join(ingredients)

    if dish_name:
        return f"Dish name: {dish_name}\nIngredients: {ing_list}\n\nWrite a detailed recipe with 5–8 steps."
    else:
        return f"Ingredients: {ing_list}\n\nWrite a detailed recipe with 5–8 steps."

def generate_recipe_from_image(img, model, val_tfms, inv_label_map, device, pipe, threshold=0.5):
    """Full inference pipeline."""

    model.eval()
    with torch.no_grad():
        inputs = val_tfms(img).unsqueeze(0).to(device)
        outputs = model(inputs)
        probs = torch.sigmoid(outputs)[0].cpu().numpy()

    indices = (probs > threshold).nonzero()[0]
    ingredients = [inv_label_map[int(i)] for i in indices]

    prompt = build_prompt(ingredients)

    recipe = pipe(prompt, max_new_tokens=500, do_sample=True)[0]["generated_text"]

    return ingredients, recipe
