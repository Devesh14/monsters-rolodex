from ..models import contestPortfolio, userPortfolio, plan, pool
from ..serializers import userPortFolioSerialializer, contestPortfolioSerialializer, planSerialializer, poolSerialializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
 
 
class ContestDetails(APIView):
 
    def get_object(self, id):
        try:
            return plan.objects.get(planId=id)
        except plan.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)