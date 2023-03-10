from rest_framework import generics, permissions
from ..models import Feed, Image, FeedImage, Video, FeedVideo, FeedLike, FeedSave
from .serializer import *
from utils.permissions.is_owner import IsOwner


class FeedCreate(generics.CreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedCreateSerializer
    permission_classes = [permissions.IsAuthenticated]


class FeedList(generics.ListAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-created_at')


class FeedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    permission_classes = [IsOwner]


class FeedComment(generics.ListCreateAPIView):
    queryset = Feed.objects.all()
    serializer_class = FeedCommentSerializer


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class FeedImageList(generics.ListCreateAPIView):
    queryset = FeedImage.objects.all()
    serializer_class = FeedImageSerializer


class VideoList(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class FeedVideoList(generics.ListCreateAPIView):
    queryset = FeedVideo.objects.all()
    serializer_class = FeedVideoSerializer


class FeedLikeAPIView(generics.CreateAPIView):
    queryset = FeedLike.objects.all()
    serializer_class = FeedLikeSerializer
    permission_classes = [permissions.IsAuthenticated]


class FeedSaveAPIView(generics.CreateAPIView):
    queryset = FeedSave.objects.all()
    serializer_class = FeedSaveSerializer
