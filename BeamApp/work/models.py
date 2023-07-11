from django.db import models
from django.shortcuts import render
import pathlib 
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

import pandas
from pandas import Series, DataFrame
import math
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

import math
from scipy.optimize import minimize
from scipy.optimize import Bounds
from django.http import JsonResponse
var = 0
class Scheme(models.Model):
    var1 = models.FloatField(null=False, default=0)
    var2 = models.FloatField(null=False, default=0)
    var3 = models.FloatField(null=False, default=0)
    var4 = models.FloatField(null=False, default=0)
    var5 = models.FloatField(null=False, default=0)
    var6 = models.FloatField(null=False, default=0)
    var7 = models.FloatField(null=False, default=0)
    var8 = models.FloatField(null=False, default=0)
    var9 = models.FloatField(null=False, default=0)
    var10 = models.FloatField(null=False, default=0)
    var11 = models.FloatField(null=False, default=0)
    var12 = models.FloatField(null=False, default=0)
    rez1 = models.FloatField(null=False, default=0)
    rez2 = models.FloatField(null=False, default=0)



    var = 0


     ### ФУНКЦИИ

     # Решение СЛАУ
    def gaussElimin(a,b):
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


     # Поиск минимума функции (Симплекс-метод)
    def downhill(F,xStart,side=1,tol=0.1):
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


     # Модуль МКЭ
    def F(x):
        A1_var = float(Scheme.var1)
        A3_var = float(Scheme.var2)
        A4_var = float(Scheme.var3)
        E1_var = float(Scheme.var4)
        E2_var = float(Scheme.var5)
        E3_var = float(Scheme.var6)
        E4_var = float(Scheme.var7)
        L1_var = float(Scheme.var8)
        L3_var = float(Scheme.var9)
        L4_var = float(Scheme.var10)
        F1_var = float(Scheme.var11)
        F2_var = float(Scheme.var12)

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

        displacements2 = gaussElimin(stiffness2,force2)
        for i in range (0, len(activeDof)):
            displacements[activeDof[i]-1]=displacements2[i]
        Reactions=np.dot(stiffness,displacements)

        for i in range (0,numberElements):
            Sigma[i]=E[i]/L[i]*(displacements[i+1]-displacements[i])
        dd=(displacements[2]).tolist()
        dd1=dd[0]

        return (V+(displacements[3]*10000)+(x[0]-50)**4+(x[1]-150)**2+(Sigma[1]-500)*2)


     # Поиск оптимального решения
    def opt(self):
        try:
            if var == 0:
                xStart=np.array([50,100])
                x=downhill(F,xStart)
                rez1 = int(x[0])
                rez2 = int(x[1])
            elif var == 1:
                bounds=Bounds([10,10],[200,200])
                xStart = np.array([50, 100])
                x=minimize(F, xStart, method='L-BFGS-B', bounds=bounds,
                             options={'disp': True})
                rez1 = int(x.x[0])
                rez2 = int(x.x[1])

        except:
            rez1 = 'error'
            rez2 = 'error'

