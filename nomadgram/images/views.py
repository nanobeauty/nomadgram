from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

# Create your views here.

class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        image_list = []

        for following_user in following_users:

            user_images = following_user.images.all()[:2]

            for image in user_images:
               
                image_list.append(image)

        sorted_list = sorted(image_list, key=get_key, reverse=True)

        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(data = serializer.data)

def get_key(image):
    return image.created_at
        

#class ListAllComments(APIView):
#
#    def get(self, request, format=None):
#
#        all_comments = models.Comment.objects.all()
#
#        serializer = serializers.CommentSerializer(all_comments, many=True)
#
#        return Response(data=serializer.data)
#
#
#class ListAllLikes(APIView):
#
#    def get(self, request, format=None):
#
#        all_likes = models.Like.objects.all()
#
#        serializer = serializers.LikeSerializer(all_likes, many=True)
#
#        return Response(data=serializer.data)