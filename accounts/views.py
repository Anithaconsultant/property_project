import http
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from .models import property, propertyDocument
from .forms import PropertyForm, DocumentForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render
from django.http import JsonResponse,FileResponse,HttpResponseRedirect,HttpResponseNotFound
from django.core.exceptions import ObjectDoesNotExist
import os
from django.conf import settings


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # To keep the user logged in
            update_session_auth_hash(request, user)
            return redirect('password_change_done')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change-password/change_password.html', {'form': form})


def password_change_done(request):
    return render(request, 'change-password/password_change_done.html')


def search_view(request):
    if request.method == 'GET':
      propnumber = request.GET.get('propnumber')
      saledeedpdf_files = []
      pattapdf_files = []
      taxpdf_files = []
      field_files = []
      adangalpdf_files = []
      ecpdf_files = []
      approvalpdf_files = []
      EBpdf_files = []
      parentpdf_files = []
      Legalpdf_files = []
      Mortgagepdf_files = []
      Poweratornypdf_files = []
      FormRegisterpdf_files = []
      Revenuepdf_files = []
      Miscellaneouspdf_files = []
      if propnumber:
           try:
                property_data = property.objects.filter(
                    propnumber=propnumber).first()
                property_document_data = propertyDocument.objects.filter(
                    propnumber=propnumber).first()

                if property_document_data.Saledeed:
                    saledeed_string = str(property_document_data.Saledeed)
                    print(saledeed_string)
                    saledeedpdf_files = [filesname.strip()
                                         for filesname in saledeed_string.split(',')]
                    print(saledeedpdf_files)

                if property_document_data.Patta:
                    patta_string = str(property_document_data.Patta)
                    pattapdf_files = [filename.strip()
                                      for filename in patta_string.split(',')]

                if property_document_data.Taxpayments:
                    taxpay_string = str(property_document_data.Taxpayments)
                    taxpdf_files = [filename.strip()
                                    for filename in taxpay_string.split(',')]

                if property_document_data.Fieldmeasurement:
                    field_string = str(property_document_data.Fieldmeasurement)
                    field_files = [filename.strip()
                                   for filename in field_string.split(',')]

                if property_document_data.Adangal:
                    adangal_string = str(property_document_data.Adangal)
                    adangalpdf_files = [filename.strip()
                                        for filename in adangal_string.split(',')]

                if property_document_data.Encumbrance:
                    ec_string = str(property_document_data.Encumbrance)
                    ecpdf_files = [filename.strip()
                                   for filename in ec_string.split(',')]

                if property_document_data.Approvals:
                    Approvals_string = str(property_document_data.Approvals)
                    approvalpdf_files = [filename.strip()
                                         for filename in Approvals_string.split(',')]

                if property_document_data.EB:
                    EB_string = str(property_document_data.EB)
                    EBpdf_files = [filename.strip()
                                   for filename in EB_string.split(',')]

                if property_document_data.Parent:
                    parent_string = str(property_document_data.Parent)
                    parentpdf_files = [filename.strip()
                                       for filename in parent_string.split(',')]

                if property_document_data.Legal:
                    Legal_string = str(property_document_data.Legal)
                    Legalpdf_files = [filename.strip()
                                      for filename in Legal_string.split(',')]

                if property_document_data.Mortgage:
                    Mortgage_string = str(property_document_data.Mortgage)
                    Mortgagepdf_files = [filename.strip()
                                         for filename in Mortgage_string.split(',')]

                if property_document_data.Poweratorny:
                    Poweratorny_string = str(
                        property_document_data.Poweratorny)
                    Poweratornypdf_files = [
                        filename.strip() for filename in Poweratorny_string.split(',')]

                if property_document_data.FormRegister:
                    FormRegister_string = str(
                        property_document_data.FormRegister)
                    FormRegisterpdf_files = [
                        filename.strip() for filename in FormRegister_string.split(',')]

                if property_document_data.Revenue:
                    Revenue_string = str(property_document_data.Revenue)
                    Revenuepdf_files = [filename.strip()
                                        for filename in Revenue_string.split(',')]

                if property_document_data.Miscellaneous:
                    Miscellaneous_string = str(
                        property_document_data.Miscellaneous)
                    Miscellaneouspdf_files = [
                        filename.strip() for filename in Miscellaneous_string.split(',')]

                property_form = PropertyForm(instance=property_data)
                property_document_form = DocumentForm(
                    instance=property_document_data)
                return render(request, 'search.html', {'property_data': property_data,   'saledeedpdf_files': saledeedpdf_files, 'pattapdf_files': pattapdf_files, 'taxpdf_files': taxpdf_files, 'field_files': field_files, 'adangalpdf_files': adangalpdf_files, 'ecpdf_files': ecpdf_files, 'approvalpdf_files': approvalpdf_files, 'EBpdf_files': EBpdf_files, 'parentpdf_files': parentpdf_files, 'Legalpdf_files': Legalpdf_files, 'Mortgagepdf_files': Mortgagepdf_files, 'Poweratornypdf_files': Poweratornypdf_files, 'FormRegisterpdf_files': FormRegisterpdf_files, 'Revenuepdf_files': Revenuepdf_files, 'Miscellaneouspdf_files': Miscellaneouspdf_files, 'property_form': property_form, 'property_document_form': property_document_form})
           except ObjectDoesNotExist:
                return render(request, 'search.html', {'message': 'No property found for the given property number.'}, status=404)
    return render(request, 'search.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


document_types = {
    'Saledeed': 'Saledeed',
    'Patta': 'Patta',
    'Taxpayments': 'Taxpayments',
    'Fieldmeasurement': 'Fieldmeasurement',
    'Adangal': 'Adangal',
    'Encumbrance': 'Encumbrance',
    'Approvals': 'Approvals',
    'EB': 'EB',
    'Parent': 'Parent',
    'Legal': 'Legal',
    'Mortgage': 'Mortgage',
    'Poweratorny': 'Poweratorny',
    'FormRegister': 'FormRegister',
    'Revenue': 'Revenue',
    'Miscellaneous': 'Miscellaneous'
}

def download_file(request, file_name):
    file_path = os.path.join(settings.MEDIA_ROOT, 'documents', file_name)
    print(file_path)
    try:
        return FileResponse(open(file_path, 'rb'))
    except FileNotFoundError:
        # Handle file not found error appropriately
        return HttpResponseNotFound('The requested file was not found.')
    
def property_view(request):
    if request.method == 'POST':
        property_form = PropertyForm(request.POST)
        document_form = DocumentForm(request.POST, request.FILES)
        if property_form.is_valid() and document_form.is_valid():
            property_instance = property_form.save()
            document_instance = document_form.save(commit=False)
            for doc_type, form_field in document_types.items():
                uploaded_images = request.FILES.getlist(doc_type)
                filenames = ', '.join(file.name for file in uploaded_images)
                setattr(document_instance, form_field, filenames)
                print(filenames)
            document_instance.propnumber = property_instance
            document_instance.save()
            context = {
                'property_form': PropertyForm(),
                'document_form': DocumentForm(),
            }
            return render(request, 'property.html', context)
    else:
        context = {
            'property_form': PropertyForm(),
            'document_form': DocumentForm(),
        }
    context = {
        'property_form': PropertyForm(),
        'document_form': DocumentForm(),
    }

    return render(request, 'property.html', context)
