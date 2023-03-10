from ..models import *
from user.models import User
from rest_framework import serializers, status
from user.api.serializer import UserSerializer
from rest_framework.response import Response


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

    def delete(self, instance):
        super().delete(instance)

        instance.src.delete(save=False)


class FeedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedImage
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    def delete(self, instance):
        super().delete(instance)

        instance.src.delete(save=False)


class FeedVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedVideo
        fields = '__all__'


class FeedLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedLike
        exclude = ['feed', 'user']

    feed = None

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        feed_id = request.data.get('feed')
        feed = Feed.objects.filter(id=feed_id).first()
        if feed:
            instance = FeedLike.objects.filter(user=user, feed=feed).first()
            if instance:
                instance.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                like = FeedLike.objects.create(user=user, feed=feed)
                return like
        else:
            raise serializers.ValidationError('Feed does not exist')


class FeedSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedLike
        exclude = ['feed', 'user']

    feed = None

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        feed_id = request.data.get('feed')
        feed = Feed.objects.filter(id=feed_id).first()
        if feed:
            instance = FeedSave.objects.filter(user=user, feed=feed).first()
            if instance:
                instance.delete()
                return Response({'message': 'Unsave successfully'}, status=status.HTTP_204_NO_CONTENT)
            else:
                like = FeedSave.objects.create(user=user, feed=feed)
                return like
        else:
            raise serializers.ValidationError('Feed does not exist')


class FeedSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    has_liked = serializers.SerializerMethodField()
    is_saved = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    carousel_media = serializers.SerializerMethodField()

    def get_has_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(id=request.user.id).exists()
        return False

    def get_is_saved(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.saved.filter(id=request.user.id).exists()
        return False

    def get_tags(self, obj):
        return TagSerializer(obj.tags.all(), many=True).data

    def get_carousel_media(self, obj):
        videos = obj.videos.all()
        images = obj.images.all()
        video_data = VideoSerializer(videos, many=True).data
        images_data = ImageSerializer(images, many=True).data

        return {"videos": video_data, "images": images_data}

    def get_like_count(self, obj):
        return len(UserSerializer(obj.likes.all(), many=True).data)

    class Meta:
        model = Feed
        # fields = '__all__'
        exclude = ('images', 'videos')
        depth = 5


class FeedCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        exclude = ['user']

    def update(self, instance, validated_data):
        print("KAKA", validated_data["images"])
        # instance.caption_text = validated_data.get()

        print("HEHEHE")
        print("instance", instance)
        return instance

    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        images = request.FILES.getlist('images')
        videos = request.FILES.getlist('videos')

        feed = Feed.objects.create(user=user, **validated_data)

        for image_data in images:
            image = Image.objects.create(src=image_data)
            FeedImage.objects.create(feed=feed, image=image)

        for video_data in videos:
            video = Video.objects.create(src=video_data)
            FeedVideo.objects.create(feed=feed, video=video)

        return feed


class FeedCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedLike
        exclude = ['feed', 'user']

    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        content = request.data.get('content')
        feed_id = request.data.get('feed')
        comment_id = request.data.get('comment_id')
        print("CONTENET", content)
        print("FEED_ID", feed_id)

        feed = Feed.objects.filter(id=feed_id).first()

        if feed:
            if comment_id:
                comment = Comment.objects.filter(id=comment_id).first()
                if comment:
                    comment_reply = CommentReply.objects.create(
                        user=user, text=content, comment=comment)

                    comment.reply.add(comment_reply)

                pass
            else:
                comment = Comment.objects.create(text=content, user=user)
                FeedComment.objects.create(comment=comment, feed=feed)

        return feed
