from django import forms


class EcdhPublicForm(forms.Form):
    p = forms.IntegerField(label="Liczba pierwsza (p)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    a = forms.IntegerField(label="Współrzędna krzywej (a)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    b = forms.IntegerField(label="Współrzędna krzywej (b)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    X = forms.IntegerField(label="Pierwsza współrzędna generatora (X)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Opcjonalne pole'}))
    Y = forms.IntegerField(label="Druga współrzędna generatora (Y)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Opcjonalne pole'}))
    A = forms.IntegerField(label="Klucz prywatny (A)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Opcjonalne pole'}))
    choices_ = (("NIST256p", "NIST256p"), ("NIST384p", "NIST384p"), ("NIST521p", "NIST521p")) 
    chosen_curve = forms.ChoiceField( label='Krzywa dla generatora', choices=choices_, required=False) 

class EcdhSharedForm(forms.Form):
    X1 = forms.IntegerField()
    X2 = forms.IntegerField()
    Y1 = forms.IntegerField()
    Y2 = forms.IntegerField()
    _a = forms.IntegerField()
    _b = forms.IntegerField()
    _p = forms.IntegerField()
