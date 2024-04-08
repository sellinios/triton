# inspections/views.py
from django.shortcuts import render, redirect
from .models import Inspection, InspectionResponse, Question
from .forms import InspectionForm

# inspections/views.py
from django.shortcuts import render
from .models import Inspection


def list_inspections(request):
    inspections = Inspection.objects.all()
    return render(request, 'inspections/list_inspections.html', {'inspections': inspections})


def create_inspection(request):
    if request.method == 'POST':
        form = InspectionForm(request.POST)
        if form.is_valid():
            inspection = form.save()
            # Now handle the dynamic question responses
            for key, value in request.POST.items():
                if key.startswith('response_'):
                    question_id = key.split('_')[1]
                    question = Question.objects.get(id=question_id)
                    InspectionResponse.objects.create(
                        inspection=inspection,
                        question=question,
                        response=value,
                        # Assuming 'response' is a text field; adjust if it's another type
                    )
            return redirect('inspections:list')  # Adjust the redirect as needed
    else:
        form = InspectionForm()
    return render(request, 'inspections/create_inspection.html', {'form': form})
