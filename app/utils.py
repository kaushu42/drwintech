import os
import time

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from pyresparser import ResumeParser

from app.models import Person, Skill


def calc_time(func, *args, **kwargs):
    def inner(*args, **kwargs):
        begin = time.time()
        output = func(*args, **kwargs)
        end = time.time()
        return output, format(end - begin, '.2f')

    return inner


def render_error(request, template_name, error_name):
    return render(request, template_name, context={
        error_name: True
    })


def save_file(file):
    fs = FileSystemStorage()
    file_extension = file.name.split('.')[-1]
    filename = fs.save(f'cv.{file_extension}', file)
    uploaded_file_url = fs.path(filename)
    return uploaded_file_url


@calc_time
def parse_resume(filepath, *, delete_file=True):
    try:
        data = ResumeParser(filepath).get_extracted_data()
    except Exception as e:
        print(e)
        data = None
    finally:
        if delete_file:
            os.remove(filepath)
        return data


def get_context_from_data(data, *, save_to_db=True):
    error = 'Not Available'
    phone = data.get('mobile_number')
    email = data.get('email')
    skills = data.get('skills')
    name = data.get('name')

    if save_to_db:
        _save_to_db(name, email, skills)

    context = {
        "name": error if name is None else name,
        "email": error if email is None else email,
        "phone": error if phone is None else phone,
        "skills": [] if not skills else skills,
    }
    return context


def _save_to_db(name, email, skills):
    if name is not None:
        try:
            Person(name=name, email=email).save()
        except:
            pass
    for skill in skills:
        try:
            Skill(name=skill).save()
        except Exception as e:
            print(e)
            pass
