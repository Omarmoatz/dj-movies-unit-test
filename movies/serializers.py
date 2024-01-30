from rest_framework import serializers
from .models import Show


class ShowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    main_actor = serializers.StringRelatedField()
    sub_actor = serializers.StringRelatedField()
    class Meta:
        model = Show
        fields = '__all__'
