from django.urls import path
from . import views

app_name = "images"
urlpatterns = [
    path("", view=views.Feed.as_view(), name="feed"),
    path("<image_id>/like", view=views.LikeImage.as_view(), name="like_image"),
]



# images/3/like
# images/3/unlike
# 
# 1. create the url and the view
# 2. take the id from the url
# 3. We want to find an image with this id
# 4. We want to create a like with that image