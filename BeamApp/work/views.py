from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import numpy as np
import pandas
from pandas import Series, DataFrame

from PIL import Image
from PIL import ImageTk
import random
import pandas
from pandas import Series, DataFrame
import math
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from django import forms
import math
from scipy.optimize import minimize
from scipy.optimize import Bounds

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .forms import InputForm
import numpy as np
import math
from scipy.optimize import minimize
from scipy.optimize import Bounds
from . import bbeam

global_list=[]

from django.contrib.auth.decorators import login_required
@login_required
def index(request):
    form = InputForm()
    return render(request, 'work/numbers.html', {'form': form})

@login_required
def create(request):
    del global_list[:]
    form = InputForm(request.POST)
    rez1 = None  
    rez2 = None  
    if form.is_valid():
        var1 = form.cleaned_data['var1']
        global_list.append(var1)
        var2 = form.cleaned_data['var2']
        global_list.append(var2)
        var3 = form.cleaned_data['var3']
        global_list.append(var3)
        var4 = form.cleaned_data['var4']
        global_list.append(var4)
        var5 = form.cleaned_data['var5']
        global_list.append(var5)
        var6 = form.cleaned_data['var6']
        global_list.append(var6)
        var7 = form.cleaned_data['var7']
        global_list.append(var7)
        var8 = form.cleaned_data['var8']
        global_list.append(var8)
        var9 = form.cleaned_data['var9']
        global_list.append(var9)
        var10 = form.cleaned_data['var10']
        global_list.append(var10)
        var11 = form.cleaned_data['var11']
        global_list.append(var11)
        var12 = form.cleaned_data['var12']
        global_list.append(var12)
        var = form.cleaned_data['var']
        global_list.append(var)
        
        rez1, rez2 = bbeam.opt(global_list)
        
        return render(request, 'work/numbers.html', {'form': form, 'rez1': rez1, 'rez2': rez2})
    else:
        form = InputForm() 
        return render(request, 'work/numbers.html', {'form': form})
        







