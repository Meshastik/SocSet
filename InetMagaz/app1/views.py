from django.shortcuts import render


def main(request):
    return render(request, 'app1\main.html')

