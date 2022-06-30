import contextlib
from itertools import count
from turtle import pd, pos
from unicodedata import name
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from numpy import append
from .forms import upload_form
from pyresparser import ResumeParser
from django.conf import settings
import glob, os, warnings, re, json, random, string
from django.contrib import messages
from .models import upload_file
from uuid import uuid4
from django.utils.safestring import SafeString
from django.views.generic.edit import FormView
import pandas as pd
warnings.filterwarnings("ignore")




class UploadView(FormView):

    form_class = upload_form
    template_name = 'app.html'
    success_url = '/'

  
    def post(self, request, *args, **kwargs):
        # sourcery skip: remove-unnecessary-else, swap-if-else-branches

        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file')
        if form.is_valid():
            list_resumes = []
            form.save()
            for count, f in enumerate(files, start=1):
                # save files to disk
                filePath = os.path.join(settings.MEDIA_ROOT, f.name)
                with open(filePath, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
                        # parse resume
                resume_data = ResumeParser(filePath).get_extracted_data()
                resume_data['id'] = count
                # save resume data to database
                list_resumes.append(resume_data)
            #clear uploads folder
            for file in glob.glob(os.path.join(settings.MEDIA_ROOT, '*')):
                os.remove(file)
            resume_data_json_safe = SafeString(json.dumps(list_resumes))
            #convert list of dictionaries to dataframe in csv format
            df = pd.DataFrame(list_resumes)
            #generate name for csv file
            name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
            df.to_csv( f'uploads/{name}.csv', index=True)
            #link to csv file
            link = f'download/{name}.csv'
            #generate list of dictionaries to dataframe in xslx format
            df_xslx = pd.DataFrame(list_resumes)
            #generate name for xslx file
            name_xslx = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
            df_xslx.to_excel( f'uploads/{name_xslx}.xlsx', index=True)
            #link to xslx file
            link_xslx = f'download/{name_xslx}.xlsx'
            return render(request, 'app.html', {'resume_data_json': resume_data_json_safe, "resume_data": list_resumes, "form": form, "file_name": link, "file_name_xslx": link_xslx})


        return self.form_invalid(form)
