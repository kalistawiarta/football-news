from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406351491',
        'name': 'Kalista Wiarta',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)