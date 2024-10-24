from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import login  # Importar la función login
from .models import Thesis
from .forms import ThesisForm

@login_required
def upload_thesis(request):
    if request.method == 'POST':
        form = ThesisForm(request.POST, request.FILES)
        if form.is_valid():
            thesis = form.save(commit=False)
            thesis.uploaded_by = request.user
            thesis.save()
            return redirect('tesis:upload_thesis')
    else:
        form = ThesisForm()
    
    if request.user.is_superuser:
        theses = Thesis.objects.all()
    else:
        theses = Thesis.objects.filter(uploaded_by=request.user)
    
    return render(request, 'tesis/upload_thesis.html', {'form': form, 'theses': theses})

def home(request):
    return render(request, 'tesis/home.html')

def visitor_view_theses(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    year = request.GET.get('year')
    theses = Thesis.objects.filter(visible=True)
    
    if query:
        theses = theses.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(advisor__icontains=query) |
            Q(category__icontains=query)
        )
    
    if category and category != 'all':
        theses = theses.filter(category=category)
    
    if year and year != 'all':
        theses = theses.filter(year=year)
    
    categories = Thesis.objects.values_list('category', flat=True).distinct()
    years = Thesis.objects.values_list('year', flat=True).distinct().order_by('year')
    return render(request, 'tesis/visitor_view.html', {'theses': theses, 'categories': categories, 'years': years, 'selected_category': category, 'selected_year': year})

def thesis_detail(request, thesis_id):
    thesis = get_object_or_404(Thesis, id=thesis_id)
    return render(request, 'tesis/thesis_detail.html', {'thesis': thesis})

@login_required
def admin_toggle_visibility(request, thesis_id):
    thesis = get_object_or_404(Thesis, id=thesis_id)
    thesis.visible = not thesis.visible
    thesis.save()
    return redirect('tesis:upload_thesis')

from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        security_key = request.POST.get('security_key')
        if form.is_valid() and security_key == 'admin123':
            user = form.save()
            login(request, user)
            return redirect('tesis:home')
        else:
            if security_key != 'admin123':
                form.add_error(None, 'Clave de seguridad incorrecta.')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})