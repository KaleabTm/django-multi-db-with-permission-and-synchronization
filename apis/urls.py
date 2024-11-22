from django.urls import include, path
from django.urls.resolvers import URLResolver

urlpatterns:list[URLResolver] = [
    path('auth/', include(('authentication.urls','authentication'), namespace='authentication')),
    path('posts/',include(('posts.urls','posts'),namespace='posts')),
    path('main/',include(('user_and_org.urls','user_and_org'),namespace='user_and_org')),
    path('departments/',include(('departments.urls','departments'),namespace='departments')),
]