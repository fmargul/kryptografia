from django.shortcuts import render
from .models import Dictionary
from django.views.generic import TemplateView
from .forms import EcdhPublicForm, EcdhSharedForm, RSADecryptForm, RSAEncryptForm, KeysRSAForm, DiffieHellmanPublicForm, DiffieHellmanSharedForm 
from .ecdh_public import generate_ecdh_public, validate_ecdh_public, calculate_ecdh_public
from .ecdh_shared import validate_ecdh_shared, calculate_ecdh_shared
from .rsa_crypt import rsa_get_private_key_primes, validate_p_q, validate_p_q_e, rsa_get_random_e, rsa_encrypt_message, rsa_decrypt_message
from .diffie_hellman_public import generate_generator, generate_private_key, calculate_public_key, validate_dh_data_public 
from .diffie_hellman_shared import calculate_shared_secret, validate_dh_data_shared

def home(request):
  return render(request, "home.html")

def multiply_points(request):
  return render(request, "multiply_points.html")

def crt(request):
  return render(request, "crt.html")

def exponentiation(request):
  return render(request, "exponentiation.html")

class EcdhSharedView(TemplateView):
  template_name = 'ecdh_shared.html'

  def get(self, request):
    form = EcdhSharedForm()
    return render(request, self.template_name, {'form': form})
  
  def post(self, request):
    form = EcdhSharedForm(request.POST)
    result = None
    if "validate" in request.POST:
            if form.is_valid():
                p = form.cleaned_data["p"]
                a = form.cleaned_data["a"]
                b = form.cleaned_data["b"]
                X = form.cleaned_data["X"]
                Y = form.cleaned_data["Y"]
                A = form.cleaned_data["A"]
                valid, error = validate_ecdh_shared(p, a, b, X, Y, A)
                
                if not valid:
                    form.add_error(None, error)
                else:
                    p, a, b, X, Y, A, cx, cy = calculate_ecdh_shared(error[0],error[1],error[2],error[3],error[4],error[5],)

                    result = {
                        "p": p,
                        "a": a,
                        "b": b,
                        "gx": X,
                        "gy": Y,
                        "A": A,
                        "cx": cx,
                        "cy": cy,
                    }
    elif "reset" in request.POST:
      form = EcdhSharedForm() 

    return render(request, self.template_name, {"form": form, "result": result})



class EcdhPublicView(TemplateView):
  template_name = 'ecdh_public.html'

  def get(self, request):
    form = EcdhPublicForm()
    return render(request, self.template_name, {'form': form})
  
  def post(self, request):
    form = EcdhPublicForm(request.POST)
    result = None
    if "generate" in request.POST:
      if form.is_valid():
        curve = form.cleaned_data["chosen_curve"]
        p, a, b, X, Y, A = generate_ecdh_public(curve)
        form = EcdhPublicForm(initial={
          "p": p,
          "a": a,
          "b": b,
          "X": X,
          "Y": Y,
          "A": A,
          "chosen_curve": curve,
        })
    elif "validate" in request.POST:
      if form.is_valid():
        p = form.cleaned_data["p"]
        a = form.cleaned_data["a"]
        b = form.cleaned_data["b"]
        X = form.cleaned_data["X"]
        Y = form.cleaned_data["Y"]
        A = form.cleaned_data["A"]
        valid, error = validate_ecdh_public(p, a, b, X, Y, A)
        
        if not valid:
          form.add_error(None, error)
        else:
          p, a, b, X, Y, A, cx, cy = calculate_ecdh_public(error[0],error[1],error[2],error[3],error[4],error[5],)

          result = {
              "p": p,
              "a": a,
              "b": b,
              "gx": X,
              "gy": Y,
              "A": A,
              "cx": cx,
              "cy": cy,
          }
    elif "reset" in request.POST:
      form = EcdhPublicForm() 
    return render(request, self.template_name, {"form": form, "result": result})

class RSAKeysView(TemplateView):
  template_name = 'rsa_keys.html'

  def get(self, request):
    form = KeysRSAForm(initial={'chosen_length': '2048'})
    return render(request, self.template_name, {'form': form})
  
  def post(self, request):
    form = KeysRSAForm(request.POST)
    result = None
    if "generate_p_q" in request.POST:
      if form.is_valid():
        #leng = form.cleaned_data['chosen_length']
        leng = 1024
        p,q = rsa_get_private_key_primes(int(leng)//2)
        print(p, q)
        form = KeysRSAForm(initial={
          "p": p,
          "q": q,
          #'chosen_length': leng,
        })
    elif "generate_e" in request.POST:
      if form.is_valid():
        p = form.cleaned_data['p']
        q = form.cleaned_data['q']
        #leng = form.cleaned_data['chosen_length']
        valid, error = validate_p_q(p, q)
        if not valid:
          form.add_error(None, error)
        else:
          e, d = rsa_get_random_e(p,q)
          form = KeysRSAForm(initial={
          "p": p,
          "q": q,
          "e": e,
          #'chosen_length': leng,
        })
    elif "validate" in request.POST:
      if form.is_valid():
        p = form.cleaned_data['p']
        q = form.cleaned_data['q']
        e = form.cleaned_data['e']
        valid, error, *d = validate_p_q_e(p, q, e)
        if not valid:
          form.add_error(None, error)
        else:
          result = {
                      "p": p,
                      "q": q,
                      "n": p*q,
                      "e": e,
                      "d": d[0],
                  }
    elif "reset" in request.POST:
      form = KeysRSAForm(initial={'chosen_length': '2048'}) 

    args = {'form': form,  "result": result}
    return render(request, self.template_name, args) 
class RSAEncryptView(TemplateView):
  template_name = "rsa_encrypt.html"

  def get(self, request):
    form_en = RSAEncryptForm()
    return render (request, self.template_name, {'form':form_en})

  def post(self, request):
    form_en = RSAEncryptForm(request.POST)
    text_en=""

    if "validate" in request.POST:
      if form_en.is_valid():
        n = form_en.cleaned_data['n']
        e = form_en.cleaned_data['e']
        msg = form_en.cleaned_data['Wiadomość']
        if n == None or e == None or msg == "":
          form_en.add_error(None, "Pola nie mogą być puste.")
        elif n == 0:
          form_en.add_error(None, "Właśnie podzieliłeś przez zero >:(")
        elif n < 256:
          form_en.add_error(None, "n nie może być mniejsze od 256. Zweryfikuj poprawność klucza.")
        else:
          encrypted = rsa_encrypt_message(msg,n,e)
          if encrypted == -1:
            form_en.add_error(None, "Właśnie podzieliłeś przez zero >:(")
          else:
            text_en="Zaszyfrowana wiadomość (w formacie base64): " + encrypted
    elif "reset" in request.POST:
      form_en = RSAEncryptForm() 

    args = {'form':form_en,'text_en':text_en}
    return render(request, self.template_name, args)
  
class RSADecryptView(TemplateView):
  template_name = "rsa_decrypt.html"

  def get(self, request):
    form_dec = RSADecryptForm()
    return render (request, self.template_name, {'form':form_dec })

  def post(self, request):
    form_dec = RSADecryptForm(request.POST)
    text_dec=""
    
    if "validate" in request.POST:
      if form_dec.is_valid():
        p = form_dec.cleaned_data['p']
        q = form_dec.cleaned_data['q']
        d = form_dec.cleaned_data['d']
        msg = form_dec.cleaned_data['Zaszyfrowana_wiadomość']
        if p == None or q == None or d == None or msg == "":
          form_dec.add_error(None, "Pola nie mogą być puste")
        elif p == 0 or q == 0:
          form_dec.add_error(None, "Właśnie podzieliłeś przez zero >:(")
        else:
          decrypted = rsa_decrypt_message(msg,p,q,d)
          if decrypted == -1:
            form_dec.add_error(None, "Podana zaszyfrowana wiadomość jest uszkodzona. Upewnij się czy została poprawnie wprowadzona.")
          elif decrypted == -2:
            form_dec.add_error(None, "Błąd odszyfrowywania. Składowe klucza są błędne lub wiadomość została błędnie zaszyfrowana.")
          else:
            text_dec="Odszyfrowana wiadomość: " + decrypted
    elif "reset" in request.POST:
      form_dec = RSADecryptForm() 

    args = {'form':form_dec, 'text_dec':text_dec}
    return render(request, self.template_name, args)
  
class DiffieHellmanPublicView(TemplateView):
    template_name = "diffie_hellman_public.html"

    def get(self, request):
        form = DiffieHellmanPublicForm()
        result = None
        return render(request, self.template_name, {"form": form, "result": result})

    def post(self, request):
        form = DiffieHellmanPublicForm(request.POST)
        result = None

        if "generate" in request.POST:
            if form.is_valid(): 
                selected_p = form.cleaned_data.get("p_choice")
                if selected_p:
                    p = int(selected_p)
                    g = generate_generator(p)
                    private_key = generate_private_key(p)

                    form = DiffieHellmanPublicForm(initial={
                        "p_choice": selected_p,
                        "p": p,
                        "g": g,
                        "private_key": private_key,
                    })
        elif "validate" in request.POST:
            if form.is_valid():
                p = form.cleaned_data["p"]
                g = form.cleaned_data["g"]
                private_key = form.cleaned_data["private_key"]

                try:
                    p = int(p)
                    g = int(g)
                    private_key = int(private_key)
                except ValueError:
                    form.add_error(None, "Wszystkie wartości muszą być liczbami całkowitymi!")
                    return render(request, self.template_name, {"form": form})

                valid, error = validate_dh_data_public(p, g, private_key)
                if not valid:
                    form.add_error(None, error)
                else:
                    public_key = calculate_public_key(g, private_key, p)
                    other_private_key = generate_private_key(p)
                    other_public_key = calculate_public_key(g, other_private_key, p)

                    result = {
                        "p": p,
                        "g": g,
                        "private_key": private_key,
                        "public_key": public_key,
                        "other_public_key": other_public_key,
                    }
        elif "reset" in request.POST:
            form = DiffieHellmanPublicForm()

        return render(request, self.template_name, {"form": form, "result": result})

class DiffieHellmanSharedView(TemplateView):
    template_name = 'diffie_hellman_shared.html'

    def get(self, request):
        form = DiffieHellmanSharedForm()
        result = None
        
        return render(request, self.template_name, {"form": form, "result": result})

    def post(self, request):
        form = DiffieHellmanSharedForm(request.POST)
        result = None
        
        if "validate" in request.POST:
            if form.is_valid():
                p = form.cleaned_data["p"]
                other_public_key = form.cleaned_data["other_public_key"]
                private_key = form.cleaned_data["private_key"]

                valid, error = validate_dh_data_shared(p, other_public_key, private_key)
                
                if not valid:
                    form.add_error(None, error)
                else:
                    shared_secret = calculate_shared_secret(other_public_key, private_key, p)

                    result = {
                        "p": p,
                        "other_public_key": other_public_key,
                        "private_key": private_key,
                        "shared_secret": shared_secret,

                    }
        elif "reset" in request.POST:
            form = DiffieHellmanSharedForm() 
        
        return render(request, self.template_name, {"form": form, "result": result})  
