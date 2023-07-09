from django import forms

class InputForm(forms.Form):
    var1 = forms.FloatField(label='A1, мм^2')
    var2 = forms.FloatField(label='A3, мм^2')
    var3 = forms.FloatField(label='A4, мм^2')
    var4 = forms.FloatField(label='E1, МПа')
    var5 = forms.FloatField(label='E2, МПа')
    var6 = forms.FloatField(label='E3, МПа')
    var7 = forms.FloatField(label='E4, МПа')
    var8 = forms.FloatField(label='L1, мм')
    var9 = forms.FloatField(label='L3, мм')
    var10 = forms.FloatField(label='L4, мм')
    var11 = forms.FloatField(label='F1, H')
    var12 = forms.FloatField(label='F2, H')
    var_choices = [
        (0, 'Downhill'),
        (1, 'L-BFGS-B')
    ]
    var = forms.ChoiceField(label='Method', choices=var_choices)