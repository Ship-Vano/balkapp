from django.shortcuts import render
from .models import Scheme
from django.http import HttpResponseRedirect, HttpResponseNotFound

#Получение данных из БД
def index(request):
    parameters = Scheme.objects.all()
    return render(request, 'work/index.html', {'parameters': parameters})
#Сохранение БД
def create(request):
    if request.method == 'POST':
        scheme = Scheme()
        scheme.var1 = request.POST.get('A1_var')
        scheme.var2 = request.POST.get('A3_var')
        scheme.var3 = request.POST.get('A4_var')
        scheme.var4 = request.POST.get('E1_var')
        scheme.var5 = request.POST.get('E2_var')
        scheme.var6 = request.POST.get('E3_var')
        scheme.var7 = request.POST.get('E4_var')
        scheme.var8 = request.POST.get('L1_var')
        scheme.var9 = request.POST.get('L3_var')
        scheme.var10 = request.POST.get('L4_var')
        scheme.var11 = request.POST.get('F1_var')
        scheme.var12 = request.POST.get('F2_var')
        scheme.save()
    return HttpResponseRedirect("/account/work/")







