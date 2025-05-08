from django.shortcuts import render
from new_site.forms import FeedbackForm
from new_site.models import Feedback

def index_page(request):
    return render(request, "index.html")

def second_page(request):
    if request.method == "POST":
        form = FeedbackForm()
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            feedback_type = form.cleaned_data['feedback_type']
            message = form.cleaned_data['feedback']
            
    
    
    
    
    
    
    return render(request, 'second.html', context)
