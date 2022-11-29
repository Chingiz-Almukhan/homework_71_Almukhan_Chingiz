from rest_framework import routers
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token

from api.views import PostView, PostLikeView

router = routers.DefaultRouter()
router.register('posts', PostView)
urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='obtain_auth_token'),
    path('like/<int:pk>', PostLikeView.as_view()),
]
