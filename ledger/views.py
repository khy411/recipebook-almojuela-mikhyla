from django.shortcuts import render

# Recipe Data
recipes_data = [
    {
        "name": "Recipe 1",
        "ingredients": [
            {"name": "tomato", "quantity": "3pcs"},
            {"name": "onion", "quantity": "1pc"},
            {"name": "pork", "quantity": "1kg"},
            {"name": "water", "quantity": "1L"},
            {"name": "sinigang mix", "quantity": "1 packet"}
        ]
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
        ]
    }
]

def recipe_list(request):
    return render(request, 'ledger/recipe_list.html', {"recipes": recipes_data})

def recipe_1(request):
    return render(request, 'ledger/recipe_detail.html', {"recipe": recipes_data[0]})

def recipe_2(request):
    return render(request, 'ledger/recipe_detail.html', {"recipe": recipes_data[1]})
