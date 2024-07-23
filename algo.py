from random import randint

# Vegetarian options
vegetarian_protein = ['Yogurt (1 cup)', 'Tofu (125g)', 'Egg whites (4)']
vegetarian_fruit = ['Berries (80g)', 'Apple', 'Orange', 'Banana', 'Dried Fruit (Handful)', 'Fruit Juice (125ml)']
vegetarian_vegetable = ['Any vegetable (80g)', 'Leafy greens (Any amount)']
vegetarian_grains = ['Cooked Grain (150g)', 'Whole Grain Bread (1 slice)', 'Half Large Potato (75g)', 'Oats (250g)', '2 Corn Tortillas']
vegetarian_protein_snack = ['Soy nuts (30g)', 'Low-fat milk (250ml)', 'Hummus (4 Tbsp)', 'Cottage cheese (125g)', 'Flavored yogurt (125g)']
vegetarian_taste_enhancer = ['2 tsp (10 ml) olive oil', '2 tbsp (30g) reduced-calorie salad dressing', '1/4 medium avocado', 'Small handful of nuts', '1/2 ounce grated Parmesan cheese', '1 tbsp (20g) jam, jelly, honey, syrup, sugar']

# Non-Vegetarian options
non_vegetarian_protein = ['Cooked meat (85g)', 'Cooked fish (100g)', '1 whole egg + 4 egg whites']
non_vegetarian_fruit = ['Berries (80g)', 'Apple', 'Orange', 'Banana', 'Dried Fruit (Handful)', 'Fruit Juice (125ml)']
non_vegetarian_vegetable = ['Any vegetable (80g)', 'Leafy greens (Any amount)']
non_vegetarian_grains = ['Cooked Grain (150g)', 'Whole Grain Bread (1 slice)', 'Half Large Potato (75g)', 'Oats (250g)', '2 Corn Tortillas']
non_vegetarian_protein_snack = ['Soy nuts (30g)', 'Low-fat milk (250ml)', 'Hummus (4 Tbsp)', 'Cottage cheese (125g)', 'Flavored yogurt (125g)']
non_vegetarian_taste_enhancer = ['2 tsp (10 ml) olive oil', '2 tbsp (30g) reduced-calorie salad dressing', '1/4 medium avocado', 'Small handful of nuts', '1/2 ounce grated Parmesan cheese', '1 tbsp (20g) jam, jelly, honey, syrup, sugar']

# Vegan options
vegan_protein = ['Tofu (125g)']
vegan_fruit = ['Berries (80g)', 'Apple', 'Orange', 'Banana', 'Dried Fruit (Handful)', 'Fruit Juice (125ml)']
vegan_vegetable = ['Any vegetable (80g)', 'Leafy greens (Any amount)']
vegan_grains = ['Cooked Grain (150g)', 'Whole Grain Bread (1 slice)', 'Half Large Potato (75g)', 'Oats (250g)', '2 Corn Tortillas']
vegan_protein_snack = ['Soy nuts (30g)', 'Hummus (4 Tbsp)']
vegan_taste_enhancer = ['2 tsp (10 ml) olive oil', '2 tbsp (30g) reduced-calorie salad dressing', '1/4 medium avocado', 'Small handful of nuts', '1/2 ounce grated Parmesan cheese', '1 tbsp (20g) jam, jelly, honey, syrup, sugar']

def calc_tdee(name, weight, height, age, gender, phys_act):
    if gender == 'Female':
        bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    else:
        bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)

    phys_act_multipliers = {'value1': 1.2, 'value2': 1.375, 'value3': 1.55, 'value4': 1.735, 'value5': 1.9}
    tdee = bmr * phys_act_multipliers.get(phys_act, 1.2)
    return tdee

def generate_diet_plan(tdee, diet_plan):
    common_snack = "Fruit (e.g., Apple or Banana)"
    result = {}

    if diet_plan == 'veg':
        result['breakfast'] = _generate_meal(tdee, vegetarian_protein, vegetarian_fruit, vegetarian_grains)
        result['snack1'] = _generate_snack(tdee, vegetarian_protein_snack)
        result['lunch'] = _generate_meal(tdee, vegetarian_protein, vegetarian_vegetable, vegetarian_taste_enhancer, vegetarian_grains, vegetarian_fruit)
        result['snack2'] = _generate_snack(tdee, vegetarian_protein_snack, vegetarian_vegetable)
        result['dinner'] = _generate_meal(tdee, vegetarian_protein, vegetarian_vegetable, vegetarian_taste_enhancer, vegetarian_grains, vegetarian_fruit)
        result['snack3'] = common_snack
    elif diet_plan == 'nonveg':
        result['breakfast'] = _generate_meal(tdee, non_vegetarian_protein, non_vegetarian_fruit, non_vegetarian_grains)
        result['snack1'] = _generate_snack(tdee, non_vegetarian_protein_snack)
        result['lunch'] = _generate_meal(tdee, non_vegetarian_protein, non_vegetarian_vegetable, non_vegetarian_taste_enhancer, non_vegetarian_grains, non_vegetarian_fruit)
        result['snack2'] = _generate_snack(tdee, non_vegetarian_protein_snack, non_vegetarian_vegetable)
        result['dinner'] = _generate_meal(tdee, non_vegetarian_protein, non_vegetarian_vegetable, non_vegetarian_taste_enhancer, non_vegetarian_grains, non_vegetarian_fruit)
        result['snack3'] = common_snack
    elif diet_plan == 'vegan':
        result['breakfast'] = _generate_meal(tdee, vegan_protein, vegan_fruit, vegan_grains)
        result['snack1'] = _generate_snack(tdee, vegan_protein_snack)
        result['lunch'] = _generate_meal(tdee, vegan_protein, vegan_vegetable, vegan_taste_enhancer, vegan_grains, vegan_fruit)
        result['snack2'] = _generate_snack(tdee, vegan_protein_snack, vegan_vegetable)
        result['dinner'] = _generate_meal(tdee, vegan_protein, vegan_vegetable, vegan_taste_enhancer, vegan_grains, vegan_fruit)
        result['snack3'] = common_snack

    return result

def _generate_meal(tdee, protein_list, vegetable_list, taste_enhancer_list, grains_list=None, fruit_list=None):
    meal = _random_choice(protein_list) + ", "
    meal += _random_choice(vegetable_list) + ", "
    meal += "Leafy greens, "
    meal += _random_choice(taste_enhancer_list)

    if grains_list and tdee >= 1800:
        meal += ", " + _random_choice(grains_list)

    if fruit_list and tdee >= 2200:
        meal += ", " + _random_choice(fruit_list)

    return meal

def _generate_snack(tdee, snack_list, additional_list=None):
    snack = ""

    if tdee >= 1800:
        snack += _random_choice(snack_list)

    if additional_list and tdee >= 1800:
        snack += ", " + _random_choice(additional_list)

    return snack

def _random_choice(lst):
    return lst[randint(0, len(lst) - 1)]
