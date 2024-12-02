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

    p.widget.attrs.update({'style': 'width: 600px;'})
    a.widget.attrs.update({'style': 'width: 600px;'})
    b.widget.attrs.update({'style': 'width: 600px;'})
    X.widget.attrs.update({'style': 'width: 600px;'})
    Y.widget.attrs.update({'style': 'width: 600px;'})
    A.widget.attrs.update({'style': 'width: 600px;'})
    chosen_curve.widget.attrs.update({'style': 'width: 600px;'})


class EcdhSharedForm(forms.Form):
    p = forms.IntegerField(label="Liczba pierwsza (p)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    a = forms.IntegerField(label="Współrzędna krzywej (a)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    b = forms.IntegerField(label="Współrzędna krzywej (b)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    X = forms.IntegerField(label="Pierwsza współrzędna klucza publicznego (X)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    Y = forms.IntegerField(label="Druga współrzędna klucza publicznego (Y)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    A = forms.IntegerField(label="Klucz prywatny (A)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))

    p.widget.attrs.update({'style': 'width: 600px;'})
    a.widget.attrs.update({'style': 'width: 600px;'})
    b.widget.attrs.update({'style': 'width: 600px;'})
    X.widget.attrs.update({'style': 'width: 600px;'})
    Y.widget.attrs.update({'style': 'width: 600px;'})
    A.widget.attrs.update({'style': 'width: 600px;'})
