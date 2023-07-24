from django import forms

class InputForm(forms.Form):
    var1 = forms.FloatField(label='C1, Н/м')
    var2 = forms.FloatField(label='С4, Н/м')
    var3 = forms.FloatField(label='P2, Н')
    var4 = forms.FloatField(label='P3, H')
    var_choices = [
        (0, 'Downhill'),
        (1, 'L-BFGS-B')
    ]
    var = forms.ChoiceField(label='Method', choices=var_choices)