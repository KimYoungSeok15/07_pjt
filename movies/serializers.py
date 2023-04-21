from rest_framework import serializers
from .models import Actor, Movie, Review


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


# class ArticleListSerializer(serializers.ModelSerializer):
#     # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     comment_set = CommentSerializer(many=True, read_only=True)

#     class Meta:
#         model = Article
#         # fields = ('id', 'title', 'content')
#         fields = '__all__'


#     def to_representation(self, instance):
#         rep = super().to_representation(instance)
#         rep['comments'] = rep.pop('comment_set', [])
#         return rep
