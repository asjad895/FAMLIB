from django.shortcuts import render,HttpResponse,redirect
from myapp.models import Message,Book,Users,Library
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
import os
import uuid
import requests
import string
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.forms import Form, CharField ,ValidationError
from django.http import HttpResponseBadRequest,HttpResponseRedirect,JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import LibrarySerializer,UserSerializer,BookSerializer

from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
#API Views
@api_view(['POST','GET'])
def create_library(request):
    libraries = Library.objects.all()
    if request.method == 'GET':
        serializer = LibrarySerializer(libraries, many=True)
        return Response(serializer.data)
    serializer = LibrarySerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        name = serializer.validated_data['name']
        print(email)
        print(name)
        if Library.objects.filter(email=email).exists():
            messages.warning(request,"A library already exists for this email address.")
            # return redirect('api/create_library/')
        try:
            library_id = uuid.uuid4()
            print(library_id)
        except ValueError:
            return Response({'error': 'Could not generate library ID.'}, status=status.HTTP_400_BAD_REQUEST)
        library = Library.objects.create(name=name, library_id=library_id,email=email)
        print("Generated Library ID: ", library_id)

        email_subject = 'Welcome to Famlib- AI Powered Library!'
        email_body = render_to_string('email.html', {'name': name, 'library_id': library_id})
        text_body = strip_tags(email_body)
        email_message = EmailMultiAlternatives(
            subject=email_subject,
            body=text_body,
            from_email='mdasjad895@gmail.com',
            to=[email]
        )
        email_message.attach_alternative(email_body, 'text/html')
        try:
            email_message.send()
            serializer = LibrarySerializer(library)
            return Response(serializer.data, status=status.HTTP_201_CREATED,headers={'success': 'Library created successfully. Check your mail for next steps. Thank you!'})
        except Exception as e:
            return e
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST','GET', 'PUT', 'DELETE'])
def library_detail(request, email=None):
    if email:
        try:
            library = Library.objects.get(email=email)
        except Library.DoesNotExist:
            return Response({'error': 'Library not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Library.MultipleObjectsReturned:
            return Response({'error': 'Multiple libraries found.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if request.method == 'GET':
            serializer = LibrarySerializer(library)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = LibrarySerializer(library, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            library.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    else:
        libraries = Library.objects.all()

        if request.method == 'GET':
            serializer = LibrarySerializer(libraries, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = LibrarySerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data['email']
                name = serializer.validated_data['name']
                if Library.objects.filter(email=email).exists():
                    messages.warning(request, "A library already exists for this email address.")
                else:
                    library_id = uuid.uuid4()
                    library = Library.objects.create(name=name, library_id=library_id, email=email)
                    email_subject = 'Welcome to Famlib- AI Powered Library!'
                    email_body = render_to_string('email.html', {'name': name, 'library_id': library_id})
                    text_body = strip_tags(email_body)
                    email_message = EmailMultiAlternatives(
                        subject=email_subject,
                        body=text_body,
                        from_email='mdasjad895@gmail.com',
                        to=[email]
                    )
                    email_message.attach_alternative(email_body, 'text/html')
                    try:
                        email_message.send()
                        serializer = LibrarySerializer(library)
                        return Response(serializer.data, status=status.HTTP_201_CREATED,
                                        headers={'success': 'Library created successfully. Check your mail for next steps. Thank you!'})
                    except Exception as e:
                        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST','GET'])
def signup(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            username = serializer.validated_data['username']
            libraryid = serializer.validated_data['libraryid']
            print(libraryid)
            # libraryid= uuid.UUID(libraryid)
            print(libraryid)
            age = serializer.validated_data['age']
            age=int(age)
            password = serializer.validated_data['password']
            married = serializer.validated_data['married']
            print(age)
            print(married)

            if Library.objects.filter(library_id=libraryid).exists():
                # Hash the password before storing it in the database
                hashed_password = make_password(password)
                print("hashed",hashed_password)
# call the userslevel API to get the user level
                userslevel_url = 'http://localhost:8000/api/userslevel/'
                response = requests.get(userslevel_url, params={'age': age, 'married': married})

    # check if the API call was successful
                if response.status_code != 200:
                    return Response({'error': 'Error getting user level.'}, status=500)

    # get the user level from the API response
                userlevel = response.json().get('level')
                new_user = Users.objects.create(
                    username=username,
                    libraryid=libraryid,
                    email=email,
                    age=age,
                    password=hashed_password,
                    married=married,
                    userlevel=userlevel
                )
                try:
                    serializer = UserSerializer(new_user)
                    messages.success(request, "User created!")
                    # request.session['username'] = username
                    # request.session['password'] = password
                    return HttpResponseRedirect(reverse('login_user'))
                except Exception as e:
                    messages.error(request, "Error: " + str(e))
                    return redirect(reverse('signup'))
            else:
                messages.warning(request, 'This library id does not exist!')
                return redirect(reverse('signup'))
        else:
            # Return a message for invalid serializer data
            messages.warning(request, 'Invalid data,may be This library id does not exist!')
            return redirect(reverse('signup'))

    return render(request, 'signup.html')

@api_view(['POST','GET'])
def login_user(request):
#     # If user is already logged in, redirect to home page
    if request.method == 'POST':
        username = request.POST['username']
        passwords = request.POST['password']
            # Check if user information is already in session
        if 'username' in request.session and 'password' in request.session:
            session_username = request.session['username']
            session_password = request.session['password']
            if passwords==session_password:
                messages.success(request,"yes u are in session")
                return render(reverse('home'))
        # Authenticate user and save user information to session
        try:
            # Get the user with the given username
            nuser = Users.objects.get(username=username)
            print(nuser)
            storep=nuser.password
            print(storep)


        # Check if the provided password matches the user's password
            if check_password(passwords, storep):
                request.session['username'] = username
                request.session['password'] = make_password(passwords)
                libraryid=Users.objects.get(username=username).libraryid
                request.user = nuser
                messages.success(request,"you are authenticated🙌")
                lname=Library.objects.get(library_id=libraryid).name
                data={'name':lname}
                print(data)
                # messages(request,data)
                # return HttpResponseRedirect(reverse('home'))
                return render(request,'home.html',data)
            messages.error(request,"Invalid login credentials. Please try again.😒")
            return redirect(reverse('login_user'))
        except User.DoesNotExist:
            messages.warning(request,'This username does not exist!👍')
            pass
    return render(request, 'login.html')


    
def index(request):
    return render(request,'index.html')
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')

def search(request):
    return render(request,'search.html')

@api_view(['POST','GET'])
def share(request):
    return render(request,'share.html')

# Create your views here.

def search(request):
    # Query all posts
    search_post = request.GET.get('search')
    if search_post:
        Books = Book.objects.filter(Q(title__icontains=search_post) & Q(desc__icontains=search_post))
    else:
    # If not searched, return default posts
        Books = Book.objects.all().order_by("title")
    return render(request, 'home.html', {'Books': Books})


def contactus(request):
    if request.method=="POST":
        name = request.POST.get('name')
        type=request.POST.get('type')
        email = request.POST.get('email')
        heading = request.POST.get('heading')
        message = request.POST.get('message')
        if message is None:
            messages.warning(request,"you have not entered any message!")
        new_contact = Message(name=name, type=type,email=email, heading=heading, message=message, date=datetime.today())
        try:
            new_contact.save()
            messages.success(request,"message successfully reached!")

        except Exception as e:
            messages.error(request,"Error: " + str(e))
    if request.method=="GET":
        return render(request,'contact.html')

@api_view(['GET'])
def userslevel(request):
    age = request.GET.get('age')
    married = request.GET.get('married')
    print(age)
    if age is None or married is None:
        return Response({'error': 'Age and marital status are required parameters.'}, status=400)

    try:
        age = int(age)
    except ValueError:
        return Response({'error': 'Age must be a valid integer.'}, status=400)

    if married not in ['True', 'False']:
        return Response({'error': 'Marital status must be "yes" or "no".'}, status=400)

    if age > 18 and married == "True":
        level = 3
    elif age >= 18:
        level = 2
    else:
        level = 1

    return Response({'level': level})
@api_view(['POST','GET'])
def upload(request):
    if request.method=='POST':
        serializer = BookSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            tags = serializer.validated_data['tags']
            desc = serializer.validated_data['desc']
            file = serializer.validated_data['file']
            access = serializer.validated_data['access']
            print(file)
            if file is not None:
                if request.session.get('username'):
                    username=request.session.get('username')
                    print(username)
                    date=datetime.utcnow()
                    id=str(title)+"_"+str(Users.objects.get(username=username).libraryid)
                    print(id)
                    new_book = Book.objects.create(id=id,title=title,tags=tags,desc=desc,date=date,blevel=access,file=file)
                    try:
                        serializer = BookSerializer(new_book)
                        messages.success(request, "book uploaded successfully!👍")
                        return HttpResponseRedirect(reverse('upload'))
                    except Exception as e:
                        messages.error(request, "Error: " + str(e))
                        return redirect(reverse('upload'))
                else:
                    messages.warning(request, 'You need to be logged in to create a book.')
                    return redirect(reverse('login'))
            else:
                messages.warning(request,"select a file.")
        else:
            # Return a message for invalid serializer data
            messages.warning(request, 'Invalid data,may be This file already exist exist!')
            return redirect(reverse('upload'))
    return render(request, 'share.html')
        
@api_view(['GET', 'POST'])
def users_list(request):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def users_detail(request, username):
    """
    Retrieve, update or delete a user.
    """
    try:
        user = Users.objects.get(username=username)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def book_list(request, user_pk=None, library_name=None):
    if request.method == 'GET':
        if user_pk and library_name:
            books = Book.objects.filter(libraryname=library_name,username=user_pk)
            print('both')
        elif user_pk:
            books = Book.objects.filter(username=user_pk)
            serializer = BookSerializer(books, many=True)
            print('user')
            return Response(serializer.data)
        elif library_name:
            books=Book.objects.filter(libraryname=library_name)
            serializer = BookSerializer(books, many=True)
            print('library')
            return Response(serializer.data)
        else:
            books=Book.objects.all()
            serializer=BookSerializer(books,many=True)
            print('books')
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)