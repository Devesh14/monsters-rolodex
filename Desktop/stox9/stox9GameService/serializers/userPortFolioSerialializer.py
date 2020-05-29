from rest_framework import serializers
from ..models import userPortfolio
 
 
 
class userPortfolio(serializers.Serializer):
    class Meta:
        model = userPortfolio
        fields = ['portfolioId', 'portfolioName', 'portfolioIndex', 'userId', 'userUniqueId', 'status', 'clonedFrom']

    
 
 
 
    def create(self, validated_data):
 
        # Create and return a new `Article` instance, given the validated data.
        return userPortfolio.objects.create(validated_data)
 
 
    def update(self, instance, validated_data):
 
        #Update and return an existing `Article` instance, given the validated data.
 
        instance.portfolioId = validated_data.get('portfolioId', instance.portfolioId)
        instance.portfolioName = validated_data.get('portfolioName', instance.portfolioName)
        instance.portfolioIndex = validated_data.get('portfolioIndex', instance.portfolioIndex)
        instance.userId = validated_data.get('userId', instance.userId)
        instance.userUniqueId = validated_data.get('userUniqueId', instance.userUniqueId)
        instance.status = validated_data.get('status', instance.status)
        instance.clonedFrom = validated_data.get('clonedFrom', instance.clonedFrom)
        instance.save()
        return instance