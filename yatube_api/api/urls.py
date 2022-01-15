from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet
from api.views import FollowViewSet
from api.views import GroupViewSet
from api.views import PostViewSet


v1_router = DefaultRouter()
v1_router.register(
    r'posts',
    PostViewSet,
    basename='posts'
)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
v1_router.register(
    r'groups',
    GroupViewSet,
    basename='groups'
)
v1_router.register(
    r'follow',
    FollowViewSet,
    basename='follows'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
