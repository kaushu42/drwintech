import os

from django.http import HttpResponse
from django.shortcuts import render


from app import utils


def index(request):
    if request.method == 'POST':
        file = request.FILES.get('resume', None)

        if file is None:
            return utils.render_error(request, 'upload.html', 'is_file_empty')

        uploaded_file_url = utils.save_file(file)

        data, processing_time = utils.parse_resume(uploaded_file_url)

        if data is None:
            return utils.render_error(request, 'upload.html', 'is_bad_file')

        context = utils.get_context_from_data(data)
        context['is_post'] = True
        context['time'] = processing_time

        print(context)
        return render(request, 'upload.html', context=context)

    return render(request, 'upload.html', context={
        'is_post': False,
    })


def handleUpload(request):

    return HttpResponse('Uploaded')
