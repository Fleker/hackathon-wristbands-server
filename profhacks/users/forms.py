from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div

class InfoForm(forms.Form):
    team = forms.CharField(
        label = "Any friends you'd like to work with?",
        max_length = 255,
        required = False,
    )
    
    journalism = forms.ChoiceField(
        label = "Data / Sensor Journalism Hack?",
        widget=forms.RadioSelect, 
        choices=(('1', 'Yes!',), ('2', 'No',)),
    )
    
    smart_buildings = forms.ChoiceField(
        label = "Smart Building Hack?",
        widget=forms.RadioSelect, 
        choices=(('1', 'Yes!',), ('2', 'No',)),
    )
    
    quantified_self = forms.ChoiceField(
        label = "Quantified Self Hack?",
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
            'team',
            'journalism',
            'smart_buildings',
            'quantified_self',
            'first_hackathon',
            'sms_notifications',
            Div(
                Submit('submit', 'Update', css_class='button white')
            )
        )