from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .models import Registration
from .serializers import RegistrationSerializer
from events.models import Event




@api_view(['GET'])
def registration_list(request):
    registrations = Registration.objects.all()
    serializer = RegistrationSerializer(registrations, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def register_event(request):
    user_id = request.data.get('user')
    event_id = request.data.get('event')

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        return Response({'error': 'Event not found'}, status=status.HTTP_404_NOT_FOUND)

    # Check duplicate registration
    if Registration.objects.filter(user=user, event=event).exists():
        return Response({'error': 'User already registered for this event'}, status=status.HTTP_400_BAD_REQUEST)

    # Check capacity
    current_registrations = Registration.objects.filter(event=event).count()
    if current_registrations >= event.capacity:
        return Response({'error': 'Event is full'}, status=status.HTTP_400_BAD_REQUEST)

    registration = Registration.objects.create(user=user, event=event)
    serializer = RegistrationSerializer(registration)
    return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def user_registrations(request, user_id):
    registrations = Registration.objects.filter(user_id=user_id)
    serializer = RegistrationSerializer(registrations, many=True)
    return Response(serializer.data)



@api_view(['DELETE'])
def cancel_registration(request, registration_id):
    try:
        registration = Registration.objects.get(id=registration_id)
    except Registration.DoesNotExist:
        return Response({'error': 'Registration not found'}, status=status.HTTP_404_NOT_FOUND)
    registration.delete()
    return Response({'message': 'Registration cancelled successfully'}, status=status.HTTP_200_OK)


