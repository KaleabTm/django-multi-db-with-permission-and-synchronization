from django.urls import path
from .apis import DepartmentCreateView, JobTitleCreateView


urlpatterns = [
    path('create_department/', DepartmentCreateView.as_view(),name='create_department'),
    path('create_position/', JobTitleCreateView.as_view(),name='create_position'),
]