from django import forms
from .models import property, propertyDocument
from django.forms import ChoiceField, DateField, ModelForm, ClearableFileInput, TextInput
from django.contrib.auth.forms import AuthenticationForm, UsernameField
size_choices = [('acres', 'Acres'), ('sqft', 'Sq.ft'), ('cents', 'Cents')]
mort_choices = [('yes', 'Yes'), ('no', 'No')]
approvedplan_chc = [('yes', 'Yes'), ('no', 'No')]
assetcate_choices = [('land', 'Land'), ('leasehold', 'Lease hold land'), ('building', 'Building'), ('landbuilding', 'Land and Building'), ('factory',
                                                                                                                                           'Factory Building'), ('agriland', 'Agricultural Land'), ('commercial', 'Commercial Building'), ('resident', 'Residential Building'), ('other', 'Other Asset')]


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': '',
            'id': 'hi',
        }
    ))

# class MultipleFileInput(forms.ClearableFileInput):
#     allow_multiple_selected = True


# class MultipleFileField(forms.FileField):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault("widget", MultipleFileInput())
#         super().__init__(*args, **kwargs)

#     def clean(self, data, initial=None):
#         single_file_clean = super().clean
#         if isinstance(data, (list, tuple)):
#             result = [single_file_clean(d, initial) for d in data]
#         else:
#             result = single_file_clean(data, initial)
#         return result
class DocumentForm(forms.ModelForm):
    Saledeed = forms.FileField(widget=forms.TextInput(
        attrs={"name": "Saledeed", "type": "File", "class": "form-control", "multiple": "True"}), label="Sale deed", required=False)
    Patta = forms.FileField(widget=forms.TextInput(attrs={
                            "name": "Patta", "type": "File", "class": "form-control", "multiple": "True"}), label="Patta", required=False)
    Taxpayments = forms.FileField(widget=forms.TextInput(
        attrs={"name": "Taxpayments", "type": "File", "class": "form-control", "multiple": "True"}), label="Tax Payments", required=False)
    Fieldmeasurement = forms.FileField(widget=forms.TextInput(
        attrs={"name": "Fieldmeasurement", "type": "File", "class": "form-control", "multiple": "True"}), label="Field Measurement Book[FMB]", required=False)
    Adangal = forms.FileField(widget=forms.TextInput(
        attrs={"name": "Adangal", "type": "File", "class": "form-control", "multiple": "True"}), label="Adangal", required=False)
    Encumbrance = forms.FileField(widget=forms.TextInput(
        attrs={"name": "Encumbrance", "type": "File", "class": "form-control", "multiple": "True"}), label="Encumbrance Certificate", required=False)
    Approvals = forms.FileField(widget=forms.TextInput(
        attrs={"name": "Approvals", "type": "File", "class": "form-control", "multiple": "True"}), label="Approvals", required=False)
    EB = forms.FileField(widget=forms.TextInput(attrs={
                         "name": "EB", "type": "File", "class": "form-control", "multiple": "True"}), label="EB Information", required=False)
    Parent = forms.FileField(widget=forms.TextInput(attrs={
                             "name": "Parent", "type": "File", "class": "form-control", "multiple": "True"}), label="Parent Document", required=False)
    Legal = forms.FileField(widget=forms.TextInput(attrs={
                            "name": "Legal", "type": "File", "class": "form-control", "multiple": "True"}), label="Legal Opinion", required=False)
    Mortgage = forms.FileField(widget=forms.TextInput(
        attrs={"name": "Mortgage", "type": "File", "class": "form-control", "multiple": "True"}), label="Mortgage Document", required=False)
    Poweratorny = forms.FileField(widget=forms.TextInput(
        attrs={"name": "Poweratorny", "type": "File", "class": "form-control", "multiple": "True"}), label="Power of Attorney", required=False)
    FormRegister = forms.FileField(widget=forms.TextInput(
        attrs={"name": "FormRegister", "type": "File", "class": "form-control", "multiple": "True"}), label="Form A Register", required=False)
    Revenue = forms.FileField(widget=forms.TextInput(
        attrs={"name": "Revenue", "type": "File", "class": "form-control", "multiple": "True"}), label="Revenue Document", required=False)
    Miscellaneous = forms.FileField(widget=forms.TextInput(
        attrs={"name": "Miscellaneous", "type": "File", "class": "form-control", "multiple": "True"}), label="Miscellaneous", required=False)

    class Meta:
        model = propertyDocument
        fields = '__all__'
        exclude = ['propnumber']


class PropertyForm(forms.ModelForm):
    Size = ChoiceField(choices=size_choices)
    mortagage = ChoiceField(choices=mort_choices)
    assetcategory = ChoiceField(choices=assetcate_choices)
    approvedplan = ChoiceField(choices=approvedplan_chc)

    class Meta:
        model = property
        fields = '__all__'
        labels = {
            'propnumber': 'Property Number',
            'OwnerName': 'Owner Name',
            'Village': 'Village',
            'District': 'District',
            'Taluk': 'Taluk',
            'City': 'City',
            'State': 'State',
            'Location': 'Location',
            'Size': 'Size',
            'Bookvalue': 'Book Value',
            'guidelinevalue': 'Guideline Value',
            'mortagage': 'Mortagage',
            'assetcategory': 'Asset Category',
            'approvedplan': 'Approved Plan',
            'registrationdate': 'Registration Date',
            'disposaldate': 'Disposal Date',
            'documentloc': 'Document Location',
            'description': 'Description',

        }

        widgets = {
            'propnumber': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Property Number'
            }),
            'OwnerName': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Owner name'
            }),
            'Village': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Village'
            }),
            'District': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'District'
            }),
            'Taluk': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Taluk'
            }),
            'City': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'City'
            }),
            'State': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'State'
            }),
            'Location': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Location'
            }),

            'Bookvalue': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Book Value'
            }),
            'guidelinevalue': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Guideline Value'
            }),

            'documentloc': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Document Location'
            }),

        }
