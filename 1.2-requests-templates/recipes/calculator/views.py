from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def index_view(request):
    # Передаем список рецептов в шаблон
    context = {
        'recipes': DATA
    }
    return render(request, 'calculator/index.html', context)

def recipe_view(request, dish_name):
    # Получаем количество порций из параметров запроса
    servings = request.GET.get('servings', 1)  # По умолчанию 1 порция
    try:
        servings = int(servings)
        if servings < 1:
            raise ValueError
    except ValueError:
        return render(request, 'calculator/error.html', {'error': 'Параметр servings должен быть положительным целым числом.'})

    # Получаем рецепт из DATA
    recipe = DATA.get(dish_name)
    if recipe is None:
        return render(request, 'calculator/error.html', {'error': 'Рецепт не найден.'})

    # Умножаем количество ингредиентов на количество порций
    adjusted_recipe = {ingredient: quantity * servings for ingredient, quantity in recipe.items()}

    # Передаем рецепт и название блюда в шаблон
    context = {
        'dish_name': dish_name,
        'recipe': adjusted_recipe
    }
    return render(request, 'calculator/index.html', context)
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
