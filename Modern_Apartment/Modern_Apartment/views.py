from django.shortcuts import redirect,render
from TeamMembers.models import team
from Testimonials.models import feedback
from Property_Data.models import property
from django.core.paginator import Paginator
from Modern_Apartment.forms import ContactForm,LoginForm,SignupForm,NewsletterForm,PropertyForm,searchform
from ContactForm_Data.models import contactform
from Newsletter_Data.models import Newsletter
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def homepage(request):
    feedbackdata=feedback.objects.all()[:8]
    propertydata=property.objects.all()[:6]
    form4=NewsletterForm(request.POST)
    form6=searchform(request.POST)
    if request.method == "GET":
        category = request.GET.get("category")
        location = request.GET.get("Location")

        if category != None and location != None:
             # Perform filtering based on category and location
            propertydata = property.objects.filter(Property_category__icontains=category, Property_location__icontains=location)
            return render(request, "searchresult.html", {'propertydata': propertydata})
    

    context={
        'feedbackdata':feedbackdata,
        'propertydata':propertydata,
        'form4':form4,
        'form6':form6,
    }
    return render(request,"index.html",context)

@login_required(login_url='loginpage')
def aboutpage(request):
    teamdata=team.objects.all()[:4]
    form4=NewsletterForm(request.POST)
    context={
        'teamdata':teamdata,
         'form4':form4,
    }
    return render(request,"about.html",context)

@login_required(login_url='loginpage')
def propertypage(request):
    propertydata=property.objects.all()
    form4=NewsletterForm(request.POST)
    paginator=Paginator(propertydata,4)
    page_num=request.GET.get('page')
    page_call=paginator.get_page(page_num)
    totalpage=page_call.paginator.num_pages
    sort_option = request.GET.get('sort_option')  # filter property by selecting options
    if sort_option == 'new_to_old':
        propertydata = propertydata.order_by('-date')
    elif sort_option == 'low_to_high':
        propertydata = propertydata.order_by('price')
    elif sort_option == 'for_rent':
        propertydata = propertydata.filter(property_status='For Rent')
    elif sort_option == 'for_sale':
        propertydata = propertydata.filter(property_status='For Sale')
    
    context={
        'propertydata':page_call,
        'totalpagelist':{n+1 for n in range(totalpage)},
        'form4':form4,
    }
    return render(request,"property.html",context)


def contactpage(request):
    form=ContactForm(request.POST)
    form4=NewsletterForm(request.POST)
    context={
        'form':form,
        'form4':form4,
    }
    return render(request,"contact.html",context)

@login_required(login_url='loginpage')
def Contactform(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        
        # saving data in database
        cd=contactform(name=name,email=email,subject=subject,message=message)
        cd.save()
        
        # sending email to staff
        subject1="New Contact Enquiry"
        email_content=f"Name : {name}<br>Email : {email}<br>Subject : {subject}<br>Message : {message}"
        from_email="example@gmail.com"
        recipient_list=["example@gmail.com"]
        send_mail(subject1,"",from_email, recipient_list,html_message=email_content)
    return render(request,"contactthank.html")

@login_required(login_url='loginpage')
def Newsletterdata(request):
    if request.method == "POST":
        email = request.POST.get('email')

        # Check if an entry with the same email already exists
        existing_subscriber = Newsletter.objects.filter(Email=email).exists()
        if existing_subscriber:
            # Email already exists, display an error message
            messages.error(request, "This email address is already subscribed.")
            return redirect('/#footer')
        else:
            new_subscriber = Newsletter(Email=email)
            new_subscriber.save()

            # Send thank-you email
            subject = 'Thank You for Subscribing!'
            message = (f'Dear {email},\n\n'
                       f'Thank you for subscribing to our newsletter! We are excited to have you on board. '
                       f'You will now receive the latest updates, news, and exclusive content directly to your inbox.\n\n'
                       f'If you ever have any questions or feedback, feel free to reply to this email. We appreciate your interest '
                       f'and look forward to keeping you informed.\n\nBest regards,\nModernApartment')
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [email]

            try:
                send_mail(subject, message, from_email, recipient_list)
                print(f"Thank-you email sent to: {email}")
            except Exception as e:
                print(f"Error sending email: {e}")

    return render(request, "subscribethank.html")
     
def loginpage(request):
    form2 = LoginForm(request.POST)
    form4=NewsletterForm(request.POST)
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use the Q object to create a complex query that checks both email and phone number fields
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else: 
            messages.error(request, "Username or Password didn't match")
            print("Authentication failed")  # Debugging statement
            return redirect("loginpage")

    context = {'form2': form2,
               'form4':form4,}
    return render(request, "login.html", context)

def signuppage(request):
    form3 = SignupForm(request.POST)
    form4=NewsletterForm(request.POST)
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phoneno = request.POST.get('Phoneno')  # Use 'phoneno' instead of 'Phoneno'
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        number_check=User.objects.filter(username=phoneno).exists()
        
        if len(phoneno) != 10:
            messages.error(request, "Number should be 10 digits")
            return redirect("signuppage")
        elif password != cpassword:
            messages.error(request, "Password and Confirm Password didn't match")
            return redirect('signuppage')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email address is already in use.')
                return redirect('signuppage')
        
            elif number_check==True:  # Check 'username' for phone number uniqueness
                messages.error(request, 'Phone number is already in use.')
                return redirect('signuppage')
            
            else:
                username =  email or phoneno
                user = User.objects.create_user(username=username, email=email, password=password)
                user.first_name = firstname
                user.last_name = lastname
                user.save()
                return redirect('loginpage')
    else:
        form3 = SignupForm()    
    context = {
        'form3': form3,
        'form4':form4,
    }
    return render(request, "signup.html", context)

@login_required(login_url='loginpage')
def logoutpage(request):
    logout(request)
    return redirect("/")

@login_required(login_url='loginpage')
def privacypolicy(request):
    form4=NewsletterForm(request.POST)
    context={
        'form4':form4,
    }
    
    return render(request,"privacypolicy.html",context)

@login_required(login_url='loginpage')
def termsofuse(request):
    form4=NewsletterForm(request.POST)
    context={
        'form4':form4,
    }
    return render(request,"termsofuse.html",context)

@login_required(login_url='loginpage')
def helpdesk(request):
    form4=NewsletterForm(request.POST)
    context={
        'form4':form4,
    }
    return render(request,"helpdesk.html",context)

@login_required(login_url='loginpage')
def searchresult(request):
    form4=NewsletterForm(request.POST)
    propertydata=property.objects.all()[:2]
    context={
        'form4':form4,
        'propertydata':propertydata
    }
    return render(request, 'searchresult.html',context)    

@login_required(login_url='loginpage')
def addproperty(request):
    form4=NewsletterForm(request.POST)
    form5=PropertyForm
    context={
        'form4':form4,
        'form5':form5,
        
    }
    return render(request,"Addproperty.html",context)            

@login_required(login_url='loginpage')
def Propertydata(request):
    if request.method == 'POST':
        Property_images = request.POST.get('Property_images')
        Property_category = request.POST.get('Property_category')
        Property_Description = request.POST.get('Property_Description')
        Property_location = request.POST.get('Property_location')
        Property_area = request.POST.get('Property_area')
        Property_price = request.POST.get('Property_price')

        # Save data to the Property model
        pd = property(
            Property_images=Property_images,
            Property_category=Property_category,
            Property_Description=Property_Description,
            Property_location=Property_location,
            Property_area=Property_area,
            Property_price=Property_price
        )
        pd.save()
        
    context={
        'form5': PropertyForm
    }    

    return render(request, "Addproperty.html",context)

@login_required(login_url='loginpage')
def process_payment(request):
    form4=NewsletterForm(request.POST)
    context={
        'form4':form4,    
    }
    return render(request, 'paymentgetaway.html',context)

@login_required(login_url='loginpage')
def Profilepage(request):
    form4=NewsletterForm(request.POST)
    user = request.user

    if request.method == 'POST':
        print(request.POST)  # Debug statement to print form data

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        print(f'Before update: {user.first_name}, {user.last_name}, {user.email}')  # Debug statement

        if first_name and last_name and email:
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            return redirect('profilepage')
        else:
            print(f'After update: {user.first_name}, {user.last_name}, {user.email}')  # Debug statement

    context={
        'form4':form4,
        'user': user
    }
    return render(request, 'Profilepage.html',context)