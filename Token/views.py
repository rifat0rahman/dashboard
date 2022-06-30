from logging.config import listen

from .serializers import LicenseSer
from .models import Account,License
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['POST'])
def create_token(request):
    if request.method == 'POST':
        email = request.data['email']
        account = Account.objects.filter(email=email)

        if len(account) != 0:
            if account[0].paid == True:
                license = License(account = account[0])
                license.save()
                return Response({'license':license.license})
            else:
                return Response({'Account is not paid'})
        else:
            return Response({'Account not found'},status=status.HTTP_406_NOT_ACCEPTABLE)


    context = {
        'status':'this is the front page'
    }
    return Response(context)



@api_view(['POST'])
def get_token(request):

    if request.method == 'POST':
        email = request.data['email']
        account = Account.objects.filter(email=email)
        
        if len(account) != 0:
            license = License.objects.filter(account=account[0],expired=False)
            serializer = LicenseSer(license,many=True)
            return Response(serializer.data)
        else:
            return Response({'Account not found'},status=status.HTTP_406_NOT_ACCEPTABLE)


    context = {
        'status':'this is the front page'
    }
    return Response(context)


@api_view(['POST'])
def authenticate_token(request):

    if request.method == 'POST':
        email = request.data['email']
        token = request.data['license']
        website = request.data['website']

        account = Account.objects.filter(email=email)
        license = License.objects.filter(license=token,account=account[0])
        
        if license:
            if license[0].expired == False:
                license[0].expired = True
                license[0].website = website
                license[0].save()

                context = {
                    'responce':'The license has been verified',
                    'license':license[0].license
                }
                return Response(context)

            return Response({'license expired'},status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response({'license not found'},status=status.HTTP_406_NOT_ACCEPTABLE)


    context = {
        'status':'this is the front page'
    }
    return Response(context)

{
    "email":"thedramaclubz@gmail.com"
}

{
    "email":"thedramaclubz@gmail.com",
    "license":"6d42b01d-52c2-40d0-9b13-239915be2545",
    "website":"facebook.com"
}