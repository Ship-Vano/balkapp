from django.shortcuts import render
#3from .models import Scheme
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


def index(request):
    form = InputForm()
    return render(request, 'work/numbers.html', {'form': form})


def create(request):
    form = InputForm(request.POST)
    rez1 = None  # Initialize rez1 with a default value
    rez2 = None  # Initialize rez2 with a default value
    if form.is_valid():
        var1 = form.cleaned_data['var1']
        var2 = form.cleaned_data['var2']
        var3 = form.cleaned_data['var3']
        var4 = form.cleaned_data['var4']
        var5 = form.cleaned_data['var5']
        var6 = form.cleaned_data['var6']
        var7 = form.cleaned_data['var7']
        var8 = form.cleaned_data['var8']
        var9 = form.cleaned_data['var9']
        var10 = form.cleaned_data['var10']
        var11 = form.cleaned_data['var11']
        var12 = form.cleaned_data['var12']
        var = form.cleaned_data['var']
        
        def gaussElimin(a, b):
            # Implementation of gaussElimin function
            n=len(b)
            for k in range(0, n-1):
                for i in range(k+1,n):
                    if a[k,k] != 0.0:
                        lam=a[i,k]/a[k,k]
                        a[i,k+1:n]=a[i,k+1:n]-lam*a[k,k+1:n]
                        b[i]=b[i]-lam*b[k]
            for k in range(n-1,-1,-1):
                b[k]=(b[k]-np.dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
            return b

        def downhill(F, xStart, side=1, tol=0.1):
            # Implementation of downhill function
            # xStart - начальный вектор данных
            # side - длина стороны симплекса (по умолчанию 0.1)
           n=len(xStart)  # Число варьируемых параметров
           x=np.zeros((n+1,n))
           f=np.zeros(n+1)
            
            # создаем начальный симплекс:
           x[0]=xStart
           for i in range(1,n+1):
               x[i]=xStart
               x[i,i-1]=xStart[i-1]+side
            # определение значений функции F в вершинах симплекса:
           for i in range(n+1): f[i]=F(x[i])
                
            # Главный цикл
           for k in range(4000):
                # Находим вершины с наибольшим и наименьшим значениями:
               iLo=np.argmin(f)
               iHi=np.argmax(f)
                # Вычисляем вектор смещения:
               d=(-(n+1)*x[iHi]+np.sum(x,axis=0))/n
                # Проверка условия достижения минимума:
               if math.sqrt(np.dot(d,d)/n)<tol: return x[iLo]
                
                # Попытка отражения 
               xNew=x[iHi]+2.0*d
               fNew=F(xNew)
               if fNew<=f[iLo]: #то принимаем отражение
                   x[iHi]=xNew
                   f[iHi]=fNew
                    
                   # Пытаемся еще продлить отражение
                   xNew=x[iHi]+d
                   fNew=F(xNew)
                   if fNew<=f[iLo]: # то принмиаем продление
                       x[iHi]=xNew
                       f[iHi]=fNew
               else:
                    # Снова пробуем продление:
                   if fNew<=f[iHi]: # то принмиаем продление
                       x[iHi]=xNew
                       f[iHi]=fNew
                   else:
                        #Применяем сжатие
                       xNew=x[iHi]+0.5*d
                       fNew=F(xNew)
                       if fNew<=f[iHi]: # то принмиаем продление
                           x[iHi]=xNew
                           f[iHi]=fNew
                       else:
                            # Используем уменьшение площади
                           for i in range(len(x)):
                               if i!=iLo:
                                   x[i]=(x[i]-x[iLo])*0.5
                                   f[i]=F(x[i])
           print("Too many iterations in downhill")
           return x[iLo]
          

        def F(x, form_data):
            # Implementation of F function
            #A1_var, A3_var, A4_var, E1_var, E2_var, E3_var, E4_var, L1_var, L3_var, L4_var, F1_var, F2_var = create()
            A1_var = float(form_data['var1'])
            A3_var = float(form_data['var2'])
            A4_var = float(form_data['var3'])
            E1_var = float(form_data['var4'])
            E2_var = float(form_data['var5'])
            E3_var = float(form_data['var6'])
            E4_var = float(form_data['var7'])
            L1_var = float(form_data['var8'])
            L3_var = float(form_data['var9'])
            L4_var = float(form_data['var10'])
            F1_var = float(form_data['var11'])
            F2_var = float(form_data['var12'])  
            elementNodes=np.array([[1,2],[2,3],[3,4]])
            numberNodes=elementNodes.max()
            numberElements=elementNodes.shape[0]
            prescribedDof=np.array([1,4])
            A=np.array([A1_var,x[0],A3_var, A4_var])
            E=np.array([E1_var,E2_var,E3_var, E4_var])
            L=np.array([L1_var,x[1],L3_var, L4_var])
            L_obr=1/L
            k_st=E*A/L
            V=A[0]*L[0]+A[1]*L[1]+A[2]*L[2]+A[3]*L[3]
            displacements=np.zeros((numberNodes,1))
            force=np.zeros((numberNodes,1))
            stiffness=np.zeros((numberNodes,numberNodes))
            Sigma=np.zeros((numberElements,1))
             
            force[1]=F1_var
            force[2]=F2_var
             
            for e in range (0,numberElements):
                elementDof=elementNodes[e]
                stiffness[elementDof[0]-1,elementDof[0]-1]=stiffness[elementDof[0]-1,elementDof[0]-1]+k_st[e]
                stiffness[elementDof[0]-1,elementDof[1]-1]=stiffness[elementDof[0]-1,elementDof[1]-1]-k_st[e]
                stiffness[elementDof[1]-1,elementDof[0]-1]=stiffness[elementDof[1]-1,elementDof[0]-1]-k_st[e]
                stiffness[elementDof[1]-1,elementDof[1]-1]=stiffness[elementDof[1]-1,elementDof[1]-1]+k_st[e]
             
            stiffness2=stiffness
            Nodes_num=list(range(1,numberNodes+1))
            activeDof=[]
            for i in Nodes_num:
                if i not in prescribedDof:
                    activeDof.append(i)
             
            stiffness2=np.delete(stiffness2,(prescribedDof-1),axis=1)
            stiffness2=np.delete(stiffness2,(prescribedDof-1),axis=0)
            force2=force
            force2=np.delete(force2,(prescribedDof-1),axis=0)
             
            displacements2=gaussElimin(stiffness2,force2)
            for i in range (0, len(activeDof)):
                displacements[activeDof[i]-1]=displacements2[i]
            Reactions=np.dot(stiffness,displacements)
             
            for i in range (0,numberElements):
                Sigma[i]=E[i]/L[i]*(displacements[i+1]-displacements[i])
            dd=(displacements[2]).tolist()
            dd1=dd[0]
             
            return (V+(displacements[3]*10000)+(x[0]-50)**4+(x[1]-150)**2+(Sigma[1]-500)*2)

        def opt(form_data):
            # Implementation of opt function
            nonlocal rez1, rez2
            rez1 = str(random.randint(10, 100))
            rez2 = str(random.randint(10, 100))
            try:
                if var == 0:
                    xStart=np.array([50,100])
                    x = downhill(F, xStart, form_data)
                    rez1 = str(int(x[0]))
                    rez2 = str(int(x[1]))
                   
                elif var == 1:
                    bounds=Bounds([10,10],[200,200])
                    xStart = np.array([50, 100]) 
                    x = minimize(F, xStart, args=(form_data,), method='L-BFGS-B', bounds=bounds, options={'disp': True})
                    rez1 = str(int(x.x[0]))
                    rez2 = str(int(x.x[1]))
                       
            except:
                rez1 = 'error'
                rez2 = 'error'
            return rez1, rez2
            
        rez1, rez2 = opt(form.cleaned_data)
        
        return render(request, 'work/numbers.html', {'form': form, 'rez1': rez1, 'rez2': rez2})
    else:
        form = InputForm() 
        return render(request, 'work/numbers.html', {'form': form})
    







