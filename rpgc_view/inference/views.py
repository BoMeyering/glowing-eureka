from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from guardian.shortcuts import get_objects_for_user

# from django.shortcuts import render, redirect
# from django.db import transaction
from .forms import ProjectForm, ImageForm
from .models import Image


# Create your views here.
def index(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, template_name='inf_index.html')

@login_required
@permission_required("project.view_project")
def project_listing(request):
    project_data = get_objects_for_user(
        request.user, "project.dg_view_project", klass=Project
    )
    return render(request, "project.html", {"projects": project_data})

@login_required
@permission_required("project.view_project")
def project_detail(request, id):
    project = get_object_or_404(Project, slug=id)
    return render(request, "detail.html", {"detail": project})

def create_project(request):

    if request.method == "POST":
        form = ProjectForm(request.POST)
        files = request.FILES.getlist("image")
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            for i in files:
                Image.objects.create(project=f, image=i)
            messages.success(request, "New Project Added")
            return HttpResponseRedirect("/projects")
        else:
            print(form.errors)
    else:
        form = ProjectForm()
        imageform = ImageForm()

    return render(request, "create_project.html", {"form": form, "imageform": imageform})

# def upload_image(request):
#     """_summary_

#     Args:
#         request (_type_): _description_

#     Returns:
#         _type_: _description_
#     """
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             try:
#                 with transaction.atomic():
#                     form.save()
#                 return redirect('inference')
#             except Exception as e:
#                 print(f"Error saving upload: {e}")
#                 form.add_error(None, "An error occured while saving the upload. Please try again.")
#                 return redirect('inference')
#     else:
#         form = ImageUploadForm()
#         context = {
#             'form': form
#         }
#     return render(request, 'upload_image.html', context)

# def upload_images(request):
#     """_summary_

#     Args:
#         request (_type_): _description_

#     Returns:
#         _type_: _description_
#     """
#     if request.method == 'POST':
#         print(request.FILES)
#         print(request.user)
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             try:
#                 with transaction.atomic():
#                     f = form.save()
#                     f.user = request.user
#                 return redirect('inference')
#             except Exception as e:
#                 print(f"Error saving upload: {e}")
#                 form.add_error(None, "An error occured while saving the upload. Please try again.")
#                 return redirect('inference')
#     else:
#         form = ImageUploadForm()
#         context = {
#             'form': form
#         }
#     return render(request, 'upload_images.html', context)

def account(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    return render(request, template_name='account.html')

def inference(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """

    return render(request, template_name='inference.html')

def status(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """

    return render(request, template_name='status.html')

def results(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """

    return render(request, template_name='results.html')

