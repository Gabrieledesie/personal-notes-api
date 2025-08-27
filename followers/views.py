from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request):
    return Response({"message": "Followed successfully"}, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request):
    return Response({"message": "Unfollowed successfully"}, status=200)
