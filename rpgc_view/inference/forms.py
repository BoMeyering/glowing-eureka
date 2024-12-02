# Inference forms
from django import forms
from .models import Image, Project

# class ImageUploadForm(forms.ModelForm):
#     """_summary_

#     Args:
#         forms (_type_): _description_
#     """
#     class Meta:
#         model = ImageUpload
#         fields = ['image']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'slug',
            'description',
        ]

class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={'allow_multiple_selected': True})
    )

    class Meta:
        model = Image
        fields = ['image']