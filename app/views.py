import os
import subprocess

from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from pyresparser import ResumeParser


def index(request):
    if request.method == 'POST':
        file = request.FILES.get('resume', None)
        if file is None:
            return render(request, 'upload.html', context={
                "file_empty": True
            })
        fs = FileSystemStorage()
        filename = fs.save('cv.' + file.name.split('.')[-1], file)
        uploaded_file_url = fs.path(filename)
        try:
            data = ResumeParser(uploaded_file_url).get_extracted_data()
        except:
            return render(request, 'upload.html', context={
                'is_bad_file': true
            })
        os.remove(uploaded_file_url)

        error = 'Not Available'

        context = {
            'is_post': True,
            'phone': data.get('mobile_number', error),
            'email': data.get('email', error),
            'skills': data.get('skills', error),
            'name': data.get('name', error),
        }
        print(context)
        return render(request, 'upload.html', context=context)

    return render(request, 'upload.html', context={
        'is_post': False,
    })


def handleUpload(request):

    return HttpResponse('Uploaded')
