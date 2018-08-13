from django.shortcuts import render, redirect
from personal.models import Personal, Stats
from personal.forms import PersonalForm, StatsForm_postcode, StatsForm_theme, ComplaintsForm
from django.contrib import messages
from django.http import HttpResponse

def index(request):
    """
    Postcode entry
    """
    
    if request.method == 'POST':
        post_code = StatsForm_postcode(request.POST)
        
        if post_code.is_valid():
            this_session = post_code.save()
            request.session['complaint_id'] = this_session.pk
            return redirect('personal')
            
    else:
        post_code = StatsForm_postcode()

    return render(request, 'index.html', {"post_code": post_code})


def personal(request):
    """
    Enter details
    """
    if request.method == "POST":
        personal_form = PersonalForm(request.POST)
        
        if personal_form.is_valid():
            data = personal_form.cleaned_data
            
            request.session['personal_data'] = data
            
        if id:
            messages.success(request, "Details submitted")
            return redirect('report')

    else:
        personal_form = PersonalForm()
    return render(request, 'personal.html', {"personal_form": personal_form})


def report(request):
    """
    Report an issue
    """
    
    complaint_id = request.session.get('complaint_id')
    
    if request.method == "POST":
            
        t = Stats.objects.get(pk=complaint_id)
        theme = StatsForm_theme(request.POST, instance=t)
            
        if theme.is_valid():
            theme.save()
    
            return redirect('complaint')
                
    else:
        theme = StatsForm_theme()
    
    return render(request, 'report.html', {"theme": theme})
    
def complaint(request):
    """
    Get Complaint Details
    """
    if request.method == "POST":
        
        complaints_form = ComplaintsForm(request.POST)
        
        if complaints_form.is_valid():
            data = complaints_form.cleaned_data
            
            request.session['complaint_data'] = data
            
            p = request.session.get('personal_data')
            c = request.session.get('complaint_data')
            
            """
            Submit Complaint Email
            """
            
            #str(p[0])
            return redirect ('confirmed')
            
    else:
            complaints_form = ComplaintsForm()

        #if id:
        #    messages.success(request, "Details submitted")
        #    return redirect('thanks')
    return render(request, 'complaint.html', { 'complaint' : complaints_form })

def confirmed(request):
    """
    Complaint Submitted
    """
    
    return render(request, 'confirmed.html')