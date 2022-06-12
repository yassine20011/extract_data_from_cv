from pyresparser import ResumeParser
import warnings
warnings.filterwarnings("ignore")

#data = ResumeParser(r'C:\Users\AMJAD\Desktop\extract_data_from_cv\project_MARA\uploads\CV_1_O6b5Xmo.pdf').get_extracted_data()
#print(data)



import glob
import os

list_of_files = glob.glob('project_MARA/uploads/*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)
