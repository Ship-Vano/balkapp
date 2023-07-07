from django.shortcuts import render, get_object_or_404

def landing_index(request):
    return render(request, 'landing/index.html')
