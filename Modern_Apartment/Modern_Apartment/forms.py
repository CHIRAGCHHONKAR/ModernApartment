from django import forms
from Property_Data.models import property
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Your Name'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    subject=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Subject'}))
    message=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder': 'message','rows':7,'cols':49}))


class LoginForm(forms.Form):
    username= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg','type':'text','name':'username','placeholder':'Email' }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg','type':'password','name':'password','placeholder':'Password','id':'myInput'}))
    

class SignupForm(forms.Form):
    firstname=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg','type':'text','name':'firstname'})) 
    lastname=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg','type':'text','name':'lastname'})) 
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg','type':'email','name':'email'})) 
    Phoneno=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg','type':'number','name':'Phoneno'})) 
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg','type':'password','name':'password','id':'myInput'}))  
    cpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg','type':'password','name':'cpassword','id':'myInput2'})) 


class NewsletterForm(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control my-3 border-0', 'type':'email', 'name':'email', 'placeholder':'Email'}))
   
    
class PropertyForm(forms.ModelForm):
    class Meta:
        model = property
        fields = [
            'Property_images',
            'Property_category',
            'Property_Description',
            'Property_location',
            'Property_area',
            'Property_price'
        ]
        widgets = {
            'Property_images': forms.FileInput(attrs={'class': 'form-control form-control-lg',}),
            'Property_category': forms.Select(attrs={'class': 'p-2 form-control'}),
            'Property_Description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'Property_location': forms.TextInput(attrs={'class': 'form-control'}),
            'Property_area': forms.TextInput(attrs={'class': 'form-control'}),
            'Property_price': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        
class searchform(forms.Form):
        category=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control p-2 mb-2','type':'text','name':'category','id':"myInput",'onkeyup':"myFunction()" ,'placeholder':"Search your categories"})) 
        Location=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control p-2 mb-2','type':'text','name':'location','id':"myInput2",'onkeyup':"myFunction()" ,'placeholder':"Location"}))
        
        
# class UserProfileForm(forms.ModelForm):
#     firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'name', 'name':'name','value':'{{ request.user.first_name }}'}))
#     # lastname = forms.CharField(max_length=30, required=True(attrs={'class':'form-control my-3 border-0', 'type':'email', 'name':'email', 'placeholder':'Email'}))
#     # email = forms.EmailField(required=True(attrs={'class':'form-control my-3 border-0', 'type':'email', 'name':'email', 'placeholder':'Email'}))        
         