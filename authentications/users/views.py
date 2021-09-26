from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        try:
            user = request.data.get('user', {})
            serializer = self.serializer_class(data=user)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as error:
            print("Error occurred: ", error)
            return Response({
                "error": f"Error Occurred: {error}"
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "response": serializer.data
        }, status=status.HTTP_201_CREATED)
