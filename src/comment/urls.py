from rest_framework import routers
from django.urls import path
from . import apiviews
router = routers.SimpleRouter()
router.register(r'api-comment', apiviews.CommentViewSet)
app_name = "comment"
urlpatterns = [
        ]
urlpatterns += router.urls