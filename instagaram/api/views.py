from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from api.serializer import PostSerializer

from typing import Any

from django import http
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from posts.models import Post


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer


class PostLikeView(View):
    post_object = None

    def dispatch(self, request: http.HttpRequest, *args: Any, **kwargs: Any):
        self.post_object = get_object_or_404(Post, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user_add_like = self.post_object.user_likes.values_list('id', flat=True)
        data = {}

        if request.user.pk in user_add_like:
            self.remove_like()
            data['result'] = 'deleted'
        else:
            self.add_like()
            data['result'] = 'added'
        return JsonResponse(data)

    def add_like(self):
        self.post_object.user_likes.add(self.request.user)

    def remove_like(self):
        self.post_object.user_likes.remove(self.request.user)
