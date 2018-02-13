from django.shortcuts import render

# Create your views here.
from .models import Subjects


def subject_list(request):
    if request.user.is_staff:
        subject = Subjects.objects.all()
        return render(request,'subjects/subjects.html')