from django.shortcuts import render

# Recipe Data

def home(request):
    return render(request, 'ledger/home.html')

recipes_data = {
    "recipes": [
        {
            "name": "Recipe 1",
            "ingredients": [
                {"name": "tomato", "quantity": "3pcs"},
                {"name": "onion", "quantity": "1pc"},
                {"name": "pork", "quantity": "1kg"},
                {"name": "water", "quantity": "1L"},
                {"name": "sinigang mix", "quantity": "1 packet"}
            ],
            "link": "/recipe/1"
        },
        {
            "name": "Recipe 2",
            "ingredients": [
                {"name": "garlic", "quantity": "1 head"},
                {"name": "onion", "quantity": "1pc"},
                {"name": "vinegar", "quantity": "1/2cup"},
                {"name": "water", "quantity": "1 cup"},
                {"name": "salt", "quantity": "1 tablespoon"},
                {"name": "whole black peppers", "quantity": "1 tablespoon"},
                {"name": "pork", "quantity": "1 kilo"}
            ],
            "link": "/recipe/2"
        }
    ]
}

def recipe_list(request):
    return render(request, 'ledger/recipe_list.html', {"recipes": recipes_data["recipes"]})

def recipe_1(request):
    recipe = next((r for r in recipes_data["recipes"] if r["link"] == "/recipe/1"), None)
    return render(request, 'ledger/recipe_detail.html', {"recipe": recipe})

def recipe_2(request):
    recipe = next((r for r in recipes_data["recipes"] if r["link"] == "/recipe/2"), None)
    return render(request, 'ledger/recipe_detail.html', {"recipe": recipe})
