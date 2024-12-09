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
    PREDEFINED_P_VALUES = [
        (179769313486231590770839156793787453197860296048756011706444423684197180216158519368947833795864925541502180565485980503646440548199239100050792877003355816639229553136239076508735759914822574862575007425302077447712589550957937778424442426617334727629299387668709205606050270810842907692932019128194467627007, "1024-bit Safe Prime"),
        (19027660487065029538943062067107733036665468833260957305549160709483156015139352088749012312781165107927097202123987000170221272552771063162169562521595613423667650443458634177712761048288634422363227505421369391093673158578693320029062140436798235092262951950177036226482562639817129758751666108637385641078673396468898798897778624142734019488179182138014413082882304521861358552910826010046426859688052972183926560157202084106792451467700605741268640874544281741868649789677644012065811432194174550914562421884980612575778073950734404006778619426381808934082927137044958369866999040984069671025718009520092720220907, "2048-bit Safe Prime"),
        (5687924184459875335429760183522788875109718513757215151795923361757421993544863264944172129119764910584404267554701620823555163900098837123611361458560212510241903666641115703116358482275011749738468276816060822721733011014718757729101511295346074620284161043664569818031627670813335688567590536863875281948497045437476509901619814958770657611949163635234335011354957166578693638699809990136970152073461423318081958058096624378403323359235893620602848122436210853579754502563499089678147235999928942772746347920131243788347415666805682906979679527227435668636038539128767214481856242311448599980615047878436897419283823509337026580784992922267080379626809120813163238955024167293896214533144889613136476465760111894573234803549858375158204766220206534384297737585659323204721525785204051177437974122993165739281832387252503732254686228536158582489968754831551137198546643859005732387257902058155027820785993784174811566283479, "3072-bit Safe Prime"),
        (567916686283763469065140949303025110615319714600342996675775719924106899667891904146314763110237357345881672890743519491958115339753581772048302132615941436854730440809597180409843702017188245442886742014124885728629437532573656164199519932537376593077540069563965006395715593679818976808456194265828999206177645021313962740632234779096623582870906251614076736496950052270248177557592134814036768268004359377661881540678185946153483649466194751423268833007472320132625670187930383226314946017834323050540930874407587952712202504249155515634481292628094050048254045672642647179854154083596626750002881274701761666194288834545951526463286539103071692846809757246155537679817947316786607202135048063520739554350211837212389160901842206990085160866449433013290309450044308673978484971169250969101858082760063034276844429340539305243067389475701065057625529823598861865930466215295092151891840898407380772363243795612324914202069165456340333169420174901025583340203882619420460223134829297841762056267387165344895249067586215275691065289210608810535183867652216628315934314414685256802526514622979979421692608811364654679256471628088808949909759135656941203204512908935198289505121049043796492942807459869791119567707129117599841794194559, "4096-bit Safe Prime"),
    ]

    p_choice = forms.ChoiceField(
        label="Wybierz liczbę pierwszą (p)",
        choices=PREDEFINED_P_VALUES,
        required=False,
        widget=forms.Select(attrs={'style': 'width: 600px;'}),
    )
 
    p = forms.CharField(label="Liczba pierwsza (p)", required=False, initial="", widget=forms.TextInput(attrs={'placeholder': 'Obowiązkowe pole'}),)
    g = forms.CharField(label="Generator (g)", required=False, initial="", widget=forms.TextInput(attrs={'placeholder': 'Obowiązkowe pole'}),)
    private_key = forms.CharField(label="Klucz prywatny", required=False, initial="", widget=forms.TextInput(attrs={'placeholder': 'Obowiązkowe pole'}))

    p.widget.attrs.update({'style': 'width: 600px;'})
    g.widget.attrs.update({'style': 'width: 600px;'})
    private_key.widget.attrs.update({'style': 'width: 600px;'})


class DiffieHellmanSharedForm(forms.Form):
    p = forms.CharField(label="Liczba pierwsza (p)", required=False, initial="", widget=forms.TextInput(attrs={'placeholder': 'Obowiązkowe pole'}),)
    other_public_key = forms.CharField(label="Klucz publiczny drugiej strony", required=False, initial="", widget=forms.TextInput(attrs={'placeholder': 'Obowiązkowe pole'}))
    private_key = forms.CharField(label="Twój klucz prywatny", required=False, initial="", widget=forms.TextInput(attrs={'placeholder': 'Obowiązkowe pole'}))

    p.widget.attrs.update({'style': 'width: 600px;'})
    other_public_key.widget.attrs.update({'style': 'width: 600px;'})
    private_key.widget.attrs.update({'style': 'width: 600px;'})