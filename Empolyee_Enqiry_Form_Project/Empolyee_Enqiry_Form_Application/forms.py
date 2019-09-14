from django import forms

class Employee_Enquiry_Form(forms.Form):

    first_name=forms.CharField(
        label='Enter Your First Name:',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your First Name',
                'class':'form-control'
            }

        )
    )
    last_name = forms.CharField(
        label='Enter Your Last Name:',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your Last Name',
                'class': 'form-control'
            }

        )
    )
    email = forms.EmailField(
        label='Enter Your Email Name:',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Your Email id',
                'class': 'form-control'
            }

        )
    )
    mobile_no = forms.IntegerField(
        label='Enter Your Mobile No:',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Your Mobile No',
                'class': 'form-control'
            }

        )
    )
    qualification=forms.CharField(
        label='Enter Your Qualification',
        widget=forms.TextInput(
            attrs={
            'placeholder':'Your Highest Qualification ',
            'class':'form-control'
            }
        )

    )
    location = forms.CharField(
        label='Enter Your Location',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your Location ',
                'class': 'form-control'
            }
        )

    )
    skill = forms.CharField(
        label='Enter Your Skill',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your Skill',
                'class': 'form-control'
            }
        )

    )

