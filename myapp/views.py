from django.shortcuts import render
from .models import Dictionary
from django.views.generic import TemplateView
from .forms import EcdhPublicForm, EcdhSharedForm
from .ecdh_public import generate_ecdh_public, validate_ecdh_public, calculate_ecdh_public
from .ecdh_shared import validate_ecdh_shared, calculate_ecdh_shared
def home(request):
  return render(request, "home.html")

def multiply_points(request):
  return render(request, "multiply_points.html")

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


