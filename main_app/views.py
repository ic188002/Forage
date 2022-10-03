from django.shortcuts import render, redirect
from .models import Image
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# Define the home view:
def home(request):

  return render(request, 'home.html')

# Define about view:
def about(request):
  return render(request, 'about.html')

     # image views
class ImageCreate(CreateView):
    model = Image
    fields = ['img', 'subject', 'description', 'created_at'] # All fields mentioned in models.py file
    # success_url = '/cats/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ImageUpdate(UpdateView):
    model = Image
    fields = ['img', 'subject', 'description', 'created_at']

class ImageDelete(DeleteView):
    model = Image
    success_url = '/images/'

def images_index(request):
    images = Image.objects.filter(user = request.user)
    return render(request, 'images/index.html', { 'images': images})







# def images_detail(request, image_id):
#     # SELECT * FROM main_app_image WHERE id = image_id
#     image = Image.objects.get(id = image_id)

# def add_to_board(request, image_id):
#     return redirect('detail', image_id = image_id)

     # userprofile views



     

    # authenitcation views








     # board views 