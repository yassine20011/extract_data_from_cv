from django.shortcuts import render
from .forms import upload_form
from pyresparser import ResumeParser
from pyresparser import ResumeParser
from django.conf import settings
import glob, os, warnings



warnings.filterwarnings("ignore")


def app(request):
    if request.method == 'POST':
        form = upload_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            list_of_files = glob.glob(r'C:\Users\AMJAD\Desktop\extract_data_from_cv\project_MARA\uploads\*') # * means all if need specific format then *.csv
            latest_file = max(list_of_files, key=os.path.getctime)
            data = ResumeParser(latest_file).get_extracted_data()        
            return render(request, 'app.html', {'form': form, 'resume': data})

    else:
        form = upload_form()
        return render(request, 'app.html', {'form': form})
