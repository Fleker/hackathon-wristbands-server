from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div

class ResumeUploadForm(forms.Form):
    resume  = forms.FileField()
    
    def __init__(self, *args, **kwargs):
        super(ResumeUploadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'resume_upload'
        self.helper.form_class = 'upload-control'
        self.helper.form_method = 'post'
        self.helper.form_action = 'upload_resume/'
        self.helper.layout = Layout(
            Div(
                'resume',
                css_class = 'resume-upload upload ui button',
            ),
            Div(
                Submit('submit', 'Upload', css_class='button white')
            )
        )

class InfoForm(forms.Form):
    teammates = forms.CharField(
        label = "Any friends you'd like to work with?",
        max_length = 255,
        required = False,
    )
    
    journalism = forms.ChoiceField(
        label = "Interested in a Data / Sensor Journalism Hack?",
        widget=forms.RadioSelect, 
        choices=(('1', 'Yes!',), ('2', 'No',)),
    )
    
    smart_buildings = forms.ChoiceField(
        label = "Interested in a Smart Building Hack?",
        widget=forms.RadioSelect, 
        choices=(('1', 'Yes!',), ('2', 'No',)),
    )
    
    quantified_self = forms.ChoiceField(
        label = "Interested in a Quantified Self Hack?",
        widget=forms.RadioSelect, 
        choices=(('1', 'Yes!',), ('2', 'No',)),
    )
    
    first_hackathon = forms.ChoiceField(
        label = "Will this be your first hackathon?",
        widget=forms.RadioSelect, 
        choices=(('1', 'Yes!',), ('2', 'No',)),
    )
    
    sms_notifications = forms.ChoiceField(
        label = "Can we notify you via text?",
        widget=forms.RadioSelect, 
        choices=(('1', 'Yes!',), ('2', 'No',)),
    )    

    def __init__(self, *args, **kwargs):
        super(InfoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'info_form'
        self.helper.form_class = 'ui form inner_container'
        self.helper.form_method = 'post'
        self.helper.form_action = 'update_info/'
        self.helper.layout = Layout(
            'teammates',
            'journalism',
            'smart_buildings',
            'quantified_self',
            'first_hackathon',
            'sms_notifications',
            Div(
                Submit('submit', 'Update', css_class='button white')
            )
        )