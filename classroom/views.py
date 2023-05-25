from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, DeleteView, ListView, DetailView, UpdateView
from classroom.forms import ContactForm
from .models import Teacher

# Create your views here.
# def home_view(request):
#     return render(request, "classroom/home.html")

# Template view example
class HomeView(TemplateView):
    template_name = "classroom/home.html"
    
class ThankYouView(TemplateView):
    template_name = "classroom/thank_you.html"

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "classroom/contact.html"
    
    # success url. put the url defined in urls.py
    # Can either put the url or use reverse_lazy
    
    # success_url = "/classroom/thank_you/"
    success_url = reverse_lazy('classroom:thank_you')
    
    # what to do with form
    # def form_valid(self, form: any) -> HttpResponse:
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
    
class TeacherCreateView(CreateView):
    model = Teacher    # It will automatically look for model_form.html and in this case teacher_form.html
    
    fields = "__all__"
    # can also include the fields that you want to make available
    # fields = ['first_name', 'last_name']
    
    success_url = reverse_lazy('classroom:thank_you')
    
class TeacherListView(ListView):
    model = Teacher    # This will look for teacher_list.html
    # fields = "__all__"  # DOn't have to do this but we can if we want to control which field(s) is/are available
    
    # We can also do this if we want to filter or order the list before viewing
    #
    # queryset = Teacher.objects.all()    # Overwrite the queryset
    # 
    # queryset = Teacher.objects.order_by("first_name")
    #
    # context_object_name = "teacher_list"

class TeacherDetailView(DetailView):
    model = Teacher  # WIll look for model_detail.html - teacher_detail.html
    
    # It uses the pk of the object to get the details of the teacher and send to the html
    # will be send as teacher

class TeacherUpdateView(UpdateView):
    model = Teacher  # Share the same model_form.html
    
    # Can also includes fields = [] to limit which field(s) can be update
    fields = "__all__"
    
    success_url = reverse_lazy('classroom:teacher_list')
    
class TeacherDeleteView(DeleteView):
    model = Teacher  # Only Confirm Delete button. Default template name = model_confirm_delete.html ie teacher_confirm_delete.html
    
    success_url = reverse_lazy('classroom:teacher_list')