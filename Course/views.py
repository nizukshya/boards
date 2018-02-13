from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .forms import CourseForm
from django.utils import timezone
from .models import Course
from django.contrib import messages
from .forms import CourseForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db.models import ProtectedError


def course_create(request):
    data = dict()
    if request.method == "POST":
        form = CourseForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            courses = Course.objects.all()
            data['html_course_list'] = render_to_string('course/includes/partial_course_list.html',
                                                        {'courses': courses
                                                         })
        else:
            data['form_is_valid'] = False

    else:
        form = CourseForm()
    context = {
        'form': form
    }
    data['html_form'] = render_to_string('course/includes/partial_course_create.html',
                                         context, request=request)
    return JsonResponse


# Create your views here.
def course_home(request):
    return render(request, 'configuration/configuration_home.html')


def course_new(request):
    if request.method == "POST":
        course_form = CourseForm(request.POST or None, request.FILES or None)  # it request form from form.py
        if course_form.is_valid():
            course = course_form.save(commit=False)
            course.author = request.user
            course.published_date = timezone.now()
            course.save()
            return redirect('/')
    else:
        course_form = CourseForm()
    return render(request, 'course/courses.html', {'course_form': course_form})


def course_list(request):
    if request.user.is_staff:
        courses = Course.objects.all().order_by('name')
        context = {
            'courses': courses,

        }
        return render(request, 'course/courses.html', context)
    else:
        messages.error(request, 'Not enough Previliges ')
        return redirect('accounts:dashboard')


def course_edit(request, pk):
    if request.user.is_staff:
        course = get_object_or_404(Course, id=pk)
        if request.method == 'POST':
            course_form = CourseForm(request.POST, request.FILES or None, instance=course)
            if course_form.is_valid():
                course = course_form.save(commit=False)
                course.author = request.user
                course.save()
                return redirect('course:course_list')

        else:
            course_form = CourseForm(instance=Course)

        return render(request, 'course/courses.html', {'course_form': course_form}, )


def course_delete(request, pk):
    if request.user.is_staff:
        try:
            course = get_object_or_404(Course, id=pk)
            course.delete()
            messages.error(request, 'Course has been deleted . ')
        except ProtectedError:
            messages.warning(request, "Error Deleting Delete first associated batch")

        return redirect('course:course_list')
