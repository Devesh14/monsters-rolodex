from rest_framework import serializers
from ..models import contestPortfolio
 
 
 
class userPortfolio(serializers.Serializer):
    class Meta:
        model = contestPortfolio
        fields = [ 'contestId', 'planId', 'isCancelled', 'poolId', 'isFilled', 'paymentStatus', 'spotsLeft']
 
 
 
    def create(self, validated_data):
 
        # Create and return a new `Article` instance, given the validated data.
        return contestPortfolio.objects.create(validated_data)
 
 
    def update(self, instance, validated_data):
 
        #Update and return an existing `Article` instance, given the validated data.
 
        instance.contestId = validated_data.get('contestId', instance.contestId)
        instance.planId = validated_data.get('planId', instance.planId)
        instance.poolId = validated_data.get('poolId', instance.poolId)
        instance.isCancelled = validated_data.get('isCancelled', instance.isCancelled)
        instance.isFilled = validated_data.get('isFilled', instance.isFilled)
        instance.paymentStatus = validated_data.get('paymentStatus', instance.paymentStatus)
        instance.spotsLeft = validated_data.get('spotsLeft', instance.spotsLeft)
        instance.save()
        return instance