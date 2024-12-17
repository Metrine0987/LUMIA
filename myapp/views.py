from django.shortcuts import render

# Create your views here.
def home_page(request):
     return render(request, 'index.html')
 
def about_page(request):
    return render(request ,'about.html')

def contact_page(request):
    return render(request , 'contact.html')

def starter_page(request):
    return render(request , 'starter-page.html')

def service_page(request):
    return render(request ,'service-details.html')

def portfolio_page(request):
    return render(request ,'portfolio-details.html')

def team_page(request):
    return render(request ,'team.html')