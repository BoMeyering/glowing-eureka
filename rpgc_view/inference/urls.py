from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.index, name='app_index'),
    path("upload", views.create_project, name='upload'),
    path("projects/", views.project_listing, name="project"),
    path("<slug:id>/", views.project_detail, name="project_detail"),
    path("project/new", views.create_project),
    # path('uploads', views.upload_images, name='uploads'),
    # path('upload', views.upload_image, name='img_upload'),
    # path('inference', views.inference, name='inference'),
    # path('status', views.status, name='status'),
    # path('results', views.results, name='results'),
    # path('account', views.account, name='account'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
