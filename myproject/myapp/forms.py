from django import forms
from django.core import validators

#function to check if the string has special characters
def has_special_char(word):
    if word.isaphanum():
        return False
    else:
        return True

def check_for_uppercase(word):
    count = 0
    for letter in word:
        if letter.isupper():
            count +=1
    if count>0:
        return True
    else:
        return False

def check_for_lowercase(word):
    count = 0
    for letter in word:
        if letter.islower():
            count +=1
    if count>0:
        return True
    else:
        return False


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Full Name'}))
    email = forms.EmailField(max_length= 100, widget=forms.TextInput(attrs={'placeholder': 'Enter your email address'}))
    verify_email = forms.EmailField(max_length= 100, widget=forms.TextInput(attrs={'placeholder': 'Please verify your email address'}))
    text  = forms.CharField(widget=forms.Textarea)
    # password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Enter a Password'}), validators = [validators.MinLengthValidator(6)])
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder': 'Enter a Password'}))


    def clean_password(self):
        data = self.cleaned_data['password']

        if not (has_special_char(data) and check_for_lowercase(data) and check_for_uppercase(data) and len(data)>=5):
            raise forms.ValidationError('- Must contain a special character''\n'
                                        '- Must one uppercase and one lowercase character'
                                        '- Length of password must 5 or more characters')
        
        return data

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        v_email = cleaned_data.get("verify_email")

        print(cleaned_data.keys())


        if email!= v_email:
            raise forms.ValidationError("Email addresses did not match")

