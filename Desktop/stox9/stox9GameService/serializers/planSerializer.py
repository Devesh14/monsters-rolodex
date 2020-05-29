from rest_framework import serializers
from ..models import plan
 
 
 
class userPortfolio(serializers.Serializer):
    class Meta:
        model = plan
        fields = ['planId', 'isConfirmWinnings', 'isDefault', 'isRepetitive', 'isActive', 'maxTeams', 'canApplyBonus', 'canApplyPass', 'entryFee', 'totalWinners', 'rake', 'prizePool', 'winDistributions']
    