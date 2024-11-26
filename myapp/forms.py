from django import forms


class AddPointsForm(forms.Form):
    X1 = forms.IntegerField()
    X2 = forms.IntegerField()
    Y1 = forms.IntegerField()
    Y2 = forms.IntegerField()
    _a = forms.IntegerField()
    _b = forms.IntegerField()
    _p = forms.IntegerField()
