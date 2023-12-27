from django.shortcuts import render
from django.http import HttpResponse

import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend (e.g., Agg)


def home_page(request):
    return render(request, 'test.html')
def survey_ques(request):
    return render(request,'questions.html')
def analysis_procedure(request):
    return render(request, 'processsurveyy.html')
def start_process(request):
    return render(request,'login.html')
def post_login(request):
    return render(request,'postlogin.html')







import tempfile 
from django.core.files.temp import NamedTemporaryFile
from django.core import files
from pandas.errors import EmptyDataError
from patient import reportscript

temp_file = None

def enter_csv(request):
    global temp_file
    if request.method == 'POST':
        uploaded_file = request.FILES['csvfile']
        emaill=request.POST['email']
        temp_file = NamedTemporaryFile(suffix='.csv')
        temp_file.write(uploaded_file.read())
        temp_file.flush()
        response_message = f'CSV file processed successfully. Processed email: {emaill}'
        return HttpResponse(response_message)
        
    return render(request, 'entercsv.html')



def view_report(request):
    global temp_file
    if temp_file is not None:
        report_output = reportscript.myfunction(temp_file)
        temp_file.close()
        return render(request, 'report.html', {'report_output': report_output})
    else:
        # Handle the case where temp_file is not defined
        return HttpResponse('Error: No CSV file uploaded.')


