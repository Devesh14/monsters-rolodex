from rest_framework import serializers
from ..models import contestPortfolio
 
 
 
class userPortfolio(serializers.Serializer):
    class Meta:
        model = contestPortfolio
        fields = ['portfolioId', 'contestId', 'planId', 'userId', 'poolId', 'userUniqueId', 'totalPoints', 'wonTurtles', 'rank', 'refTxnId']
    
 
 
 
    def create(self, validated_data):
 
        # Create and return a new `Article` instance, given the validated data.
        return contestPortfolio.objects.create(validated_data)
 
 
    def update(self, instance, validated_data):
 
        #Update and return an existing `Article` instance, given the validated data.
 
        instance.portfolioId = validated_data.get('portfolioId', instance.portfolioId)
        instance.contestId = validated_data.get('contestId', instance.contestId)
        instance.planId = validated_data.get('planId', instance.planId)
        instance.poolId = validated_data.get('poolId', instance.poolId)
        instance.userId = validated_data.get('userId', instance.userId)
        instance.userUniqueId = validated_data.get('userUniqueId', instance.userUniqueId)
        instance.totalPoints = validated_data.get('totalPoints', instance.totalPoints)
        instance.wonTurtles = validated_data.get('wonTurtles', instance.wonTurtles)
        instance.rank = validated_data.get('rank', instance.rank)
        instance.refTxnId = validated_data.get('refTxnId', instance.refTxnId)
        instance.save()
        return instance