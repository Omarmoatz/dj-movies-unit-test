from rest_framework import serializers
from .models import *


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ShowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    main_actor = serializers.StringRelatedField()
    sub_actor = serializers.StringRelatedField()
    class Meta:
        model = Show
        fields = '__all__'

class ShowDetailSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    category = CategorySerializer()
    main_actor = ActorSerializer()
    sub_actor = ActorSerializer()
    class Meta:
        model = Show
        fields = '__all__'