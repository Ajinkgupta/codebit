import uuid
from django.shortcuts import render, get_object_or_404, redirect
from .models import CodePen
from .forms import CodePenForm

def pen_detail(request, unique_id):
    codepen = get_object_or_404(CodePen, unique_id=unique_id)
    return render(request, 'app/pen.html', {'codepen': codepen})

def generate_unique_id():
    # Generate a random UUID and convert it to a string
    return str(uuid.uuid4())

def pen_create(request):
    if request.method == 'POST':
        form = CodePenForm(request.POST)
        if form.is_valid():
            codepen = form.save(commit=False)
            codepen.unique_id = generate_unique_id()
            codepen.save()
            return redirect('pen_detail', unique_id=codepen.unique_id)
    else:
        form = CodePenForm()

    return render(request, 'app/pen_create.html', {'form': form})


def pen_list(request):
    pens = CodePen.objects.all()
    return render(request, 'app/home.html', {'pens': pens})
