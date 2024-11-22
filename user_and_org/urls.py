from django.urls import path
from .apis import UserCreateView, UserOrgRelationCreateView


urlpatterns = [
    path('create_user/', UserCreateView.as_view(),name='create_user'),
    path('user_relation/', UserOrgRelationCreateView.as_view(),name='user_org_relation')
]