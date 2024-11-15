from django import forms


class AddPointsForm(forms.Form):
    X1 = forms.IntegerField()
    X2 = forms.IntegerField()
    Y1 = forms.IntegerField()
    Y2 = forms.IntegerField()
    _a = forms.IntegerField()
    _b = forms.IntegerField()
    _p = forms.IntegerField()

class EcdhForm(forms.Form):
    Numer_krzywej = forms.IntegerField(required=False)

class EcdhForm2(forms.Form):
    Numer_krzywej = forms.IntegerField(required=False)
    Klucz_prywatny = forms.IntegerField(required=False)
    X_klucza_publicznego = forms.IntegerField(required=False)
    Y_klucza_publicznego = forms.IntegerField(required=False)

class EcdsaGenerateKeys(forms.Form):
    Krzywa = forms.ChoiceField(choices=( 
    ("NIST192p", "NIST192p"), # przechowywana wartość, co się wyświetla
    ("NIST224p", "NIST224p"), 
    ("NIST256p", "NIST256p"), 
    ("NIST384p", "NIST384p"), 
    ("NIST521p", "NIST521p"), 
    ("SECP256k1", "SECP256k1"), 
) )
    Wiadomość = forms.CharField(required=False)

class EcdsaVerify(forms.Form):
    Krzywa = forms.ChoiceField(choices=( 
    ("NIST192p", "NIST192p"), # przechowywana wartość, co się wyświetla
    ("NIST224p", "NIST224p"), 
    ("NIST256p", "NIST256p"), 
    ("NIST384p", "NIST384p"), 
    ("NIST521p", "NIST521p"), 
    ("SECP256k1", "SECP256k1"), 
) )
    Wiadomość = forms.CharField(required=False)
    Podpis = forms.CharField(required=False)
    Klucz_publiczny = forms.CharField(required=False)