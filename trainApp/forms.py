from django.contrib.auth.forms import UserCreationForm
from trainApp.models import UserDetails
from django.contrib.auth.models import User
from django import forms


class Booking(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = '__all__'

        widgets = {
            #'Name':forms.TextInput(attrs={'class':'boxes'}),
            #'Email':forms.EmailInput(attrs={'class':'boxes'}),
            'From_location':forms.Select(attrs={'class':'boxes'}),
            'To_location':forms.Select(attrs={'class':'boxes'}),
            'Mobile':forms.TextInput(attrs={'class':'boxes'}),
            'Date':forms.DateInput(attrs={'class':'boxes'}),
            'Gender':forms.Select(attrs={'class':'boxes'})
        }


class Register(UserCreationForm):

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'boxes'})
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'class': 'boxes'})
    )


    class Meta:
        model = User
        fields = ['username','first_name','last_name','password1','password2']
        

        widgets = {
            'username':forms.TextInput(attrs={'class':'boxes'}),
            'first_name':forms.TextInput(attrs={'class':'boxes'}),
            'last_name':forms.TextInput(attrs={'class':'boxes'}),
            #'password1':forms.PasswordInput(attrs={'class':'boxes'}),
            #'password2':forms.PasswordInput(attrs={'class':'boxes'})
        }
    
    

class SearchForm(forms.Form):
    from_choose = [('Hyderabad','Hyderabad'),('Mumbai','Mumbai'),('Tirupati','Tirupati'),('Delhi','New Delhi'),('Tamil Nadu','Tamil Nadu'),('Vizag','Vizag'),('Karnataka','Karnataka')]
    to_choose = [('Hyderabad','Hyderabad'),('Mumbai','Mumbai'),('Tirupati','Tirupati'),('Delhi','New Delhi'),('Tamil Nadu','Tamil Nadu'),('Vizag','Vizag'),('Karnataka','Karnataka')]

    From_location = forms.ChoiceField(choices=from_choose,widget=forms.Select(attrs={'class': 'boxes'}))
    To_location = forms.ChoiceField(choices=to_choose,widget=forms.Select(attrs={'class': 'boxes'}))

