from django.shortcuts import render
from .models import Dictionary
from django.views.generic import TemplateView
from .forms import AddPointsForm
from .add_points import ecc_check_data

def home(request):
  return render(request, "home.html")

class AddPointsView(TemplateView):
  template_name = 'add_points.html'

  def get(self, request):
    form = AddPointsForm()
    return render(request, self.template_name, {'form': form})
  
  def post(self, request):
    form = AddPointsForm(request.POST)
    if form.is_valid():
      x1 = form.cleaned_data['X1']
      x2 = form.cleaned_data['X2']
      y1 = form.cleaned_data['Y1']
      y2 = form.cleaned_data['Y2']
      a = form.cleaned_data['_a']
      b = form.cleaned_data['_b']
      p = form.cleaned_data['_p']
      text = ecc_check_data(x1, x2, y1, y2, a, b, p)
    args = {'form': form, 'text': text}
    return render(request, self.template_name, args)

