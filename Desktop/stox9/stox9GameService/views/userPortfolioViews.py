from ..models import contestPortfolio, userPortfolio, plan, pool
from ..serializers import userPortFolioSerialializer, contestPortfolioSerialializer, planSerialializer, poolSerialializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
 
 
class contestPortfolioAPIView(APIView):
 
    def get(self, request):
        userPortfolios = userPortfolio.objects.all()
        serializer = userPortFolioSerialializer(userPortfolios, many=True)
        return Response(serializer.data)
 
    def post(self, request):
        serializer = userPortFolioSerialializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
 
class ContestDetails(APIView):
 
    def get_object(self, id):
        try:
            return userPortfolio.objects.get(portfoioId=id)
        except userPortfolio.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
 
 
    def get(self, request, id):
        contest = self.get_object(id)
        serializer = userPortFolioSerialializer(contest)
        return Response(serializer.data)

 
 
    def put(self, request,id):
        contest = self.get_object(id)
        serializer = userPortFolioSerialializer(contest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, id):
        contest = self.get_object(id)
        contest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)