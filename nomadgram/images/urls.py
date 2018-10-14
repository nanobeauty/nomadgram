from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    path("", view=views.Feed.as_view(), name="feed"),
#    path("comments/", view=views.ListAllComments.as_view(), name="all_comments"),
#    path("likes/", view=views.ListAllLikes.as_view(), name="all_likes"),
]

# from django.conf.urls import url
# from . import views
# 
# urlpatterns = [
#     url(
#         regex=r'^all/$',
#         view=views.ListAllImages.as_view(),
#         name='all_images'
#     )
# ]