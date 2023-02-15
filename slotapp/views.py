from django.shortcuts import render

from random import randint
from random import choice 

# Create your views here.

coins = 100

def index(request):
    global coins 

    if request.method == "POST":
        amount = int(request.POST.get("amount"))
        
        win = ['won', 'lost']
        t = choice(win)

        if t == "won":
            payoff = randint(1, 3*amount)
            coins += payoff
            message = f"You have won {payoff} coins"
            context = {
                'message': message,
                'coins': coins
                }
        else:
            coins -= amount
            message = f"You have lost {amount} coins"
            context = {
                'message': message,
                'coins': coins
            }

        return render(request, 'slotapp/index.html', context)
        
    return render(request, 'slotapp/index.html', {'coins': coins})   
