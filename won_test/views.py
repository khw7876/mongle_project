from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from won_test.serializers import UserSignupSerializer


# Create your views here.
class UserView(APIView):
    """
    회원정보 추가, 수정 및 탈퇴 기능
    """

    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입 성공하였습니다"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        return Response({"message": "수정이 완료되었습니다!"}, status=status.HTTP_200_OK)

    def delete(self, request):
        return Response({"message": "탈퇴가 완료되었습니다!"}, status=status.HTTP_200_OK)
