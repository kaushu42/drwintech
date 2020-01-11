from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'upload.html', context={
        'location': 'Kumarigal, Kathmandu',
        'country': 'Nepal',
        'phone': '+977 9843533621',
        'email': 'kaushu42@gmail.com',
        'first_name': 'Kaushal Raj',
        'last_name': 'Mishra',
        'description': 'I AM A BLAH BLAH BLAH'
    })


def handleUpload(request):
    if request.method == 'POST':
        print(request.FILES)
        print(request.POST)
    return HttpResponse('Uploaded')
