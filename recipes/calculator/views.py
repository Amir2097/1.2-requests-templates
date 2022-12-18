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
    'plov': {
        'рис, г': 500,
        'лук, г': 100,
        'курица, кг': 1,
        'перец, г': 10,
    },
    'lagman': {
        'лук, г': 100,
        'лапша, г': 400,
        'говядина, кг': 1,
        'перец, г': 10,
    },
}


def omlet(request):
    servings = int(request.GET.get('servings', 1))

    context = {
      'recipe': {
        'яйца, шт': 2 * servings,
        'молоко, л': 0.1 * servings,
        'соль, ч.л.': 0.5 * servings,
      }
    }
    return render(request, 'calculator/index.html', context)

def pasta(request):
    servings = int(request.GET.get('servings', 1))

    context = {
      'recipe': {
        'макароны, г': 0.3 * servings,
        'сыр, г': 0.05 * servings,
      }
    }
    return render(request, 'calculator/index.html', context)

def buter(request):
    servings = int(request.GET.get('servings', 1))

    context = {
      'recipe': {
        'хлеб, ломтик': 1 * servings,
        'колбаса, ломтик': 1 * servings,
        'сыр, ломтик': 1 * servings,
        'помидор, ломтик': 1 * servings,
      }
    }
    return render(request, 'calculator/index.html', context)

def plov(request):
    servings = int(request.GET.get('servings', 1))

    context = {
      'recipe': {
        'рис, г': 500 * servings,
        'лук, г': 100 * servings,
        'курица, кг': 1 * servings,
        'перец, г': 10 * servings,
      }
    }
    return render(request, 'calculator/index.html', context)

def lagman(request):
    servings = int(request.GET.get('servings', 1))

    context = {
      'recipe': {
        'лук, г': 100 * servings,
        'лапша, г': 400 * servings,
        'говядина, кг': 1 * servings,
        'перец, г': 10 * servings,
      }
    }
    return render(request, 'calculator/index.html', context)

