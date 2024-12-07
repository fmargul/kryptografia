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
class KeysRSAForm(forms.Form):
    p = forms.IntegerField(label="Liczba pierwsza (p)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    q = forms.IntegerField(label="Liczba pierwsza (q)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    e = forms.IntegerField(label="Współczynnik klucza publicznego (e)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    #choices_ = ((1024, 1024), (2048, 2048), (4096, 4096)) 
    #chosen_length = forms.ChoiceField(label="Długość klucza (w bitach)", widget=forms.RadioSelect, choices=choices_, required=True)
    
    p.widget.attrs.update({'style': 'width: 600px;'})
    q.widget.attrs.update({'style': 'width: 600px;'})
    e.widget.attrs.update({'style': 'width: 600px;'})
    #chosen_length.widget.attrs.update({'style': 'width: 60px;'})

class RSAEncryptForm(forms.Form):
    e = forms.IntegerField(label="Współczynnik klucza publicznego (e)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    n = forms.IntegerField(label="Iloczyn p i q (n)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    Wiadomość = forms.CharField(label="Wiadomość do zaszyfrowania", widget=forms.Textarea(attrs={'placeholder': 'Obowiązkowe pole'}),required=False)

    n.widget.attrs.update({'style': 'width: 600px;'})
    e.widget.attrs.update({'style': 'width: 600px;'})
    Wiadomość.widget.attrs.update({'style': 'width: 600px;'})

class RSADecryptForm(forms.Form):
    d = forms.IntegerField(label="Współczynnik klucza prywatnego (d)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    p = forms.IntegerField(label="Liczba pierwsza (p)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    q = forms.IntegerField(label="Liczba pierwsza (q)", required=False, widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    Zaszyfrowana_wiadomość = forms.CharField(label="Zaszyfrowana wiadomość", widget=forms.Textarea(attrs={'placeholder': 'Obowiązkowe pole'}),required=False)

    p.widget.attrs.update({'style': 'width: 600px;'})
    q.widget.attrs.update({'style': 'width: 600px;'})
    d.widget.attrs.update({'style': 'width: 600px;'})
    Zaszyfrowana_wiadomość.widget.attrs.update({'style': 'width: 600px;'})

class DiffieHellmanPublicForm(forms.Form):
    p = forms.IntegerField(label="Liczba pierwsza (p)", required=False, initial="", widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    g = forms.IntegerField(label="Generator (g)", required=False, initial="", widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    private_key = forms.IntegerField(label="Klucz prywatny", required=False, initial="", widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))

    p.widget.attrs.update({'style': 'width: 600px;'})
    g.widget.attrs.update({'style': 'width: 600px;'})
    private_key.widget.attrs.update({'style': 'width: 600px;'})

class DiffieHellmanSharedForm(forms.Form):
    p = forms.IntegerField(label="Liczba pierwsza (p)", required=False, initial="", widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    g = forms.IntegerField(label="Generator (g)", required=False, initial="", widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    partners_public_key = forms.IntegerField(label="Klucz publiczny drugiej strony", required=False, initial="", widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    private_key = forms.IntegerField(label="Twój klucz prywatny", required=False, initial="", widget=forms.NumberInput(attrs={'placeholder': 'Obowiązkowe pole'}))

    p.widget.attrs.update({'style': 'width: 600px;'})
    g.widget.attrs.update({'style': 'width: 600px;'})
    partners_public_key.widget.attrs.update({'style': 'width: 600px;'})
    private_key.widget.attrs.update({'style': 'width: 600px;'})