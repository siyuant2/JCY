from django.shortcuts import render

from django.http import HttpResponse
from django.db import connection

# Create your views here.
def index(request):
    return render(request, 'Signup/signup.html')

def changepassword(request):
    return render(request, 'Signup/changepassword.html')

def addperson(request):
    if request.method == 'POST':
        temp_email = request.POST.get('UIUC Email Address')
        temp_password = request.POST.get('Password')
        temp_major = request.POST.get('major')
        temp_skills = request.POST.get('skills')
        temp_interests = request.POST.get('interests')
        print(temp_email)
        #models.Students.objects.raw("insert into signup_students values('1@1.edu', '123')")
        # temp_student = models.Students(EmailAddress = temp_email, PassWord = temp_password,
        # major = temp_major, skills = temp_skills, interests = temp_interests)
        # temp_student.save()
        with connection.cursor() as cursor:
            cursor.execute("insert into signup_students(EmailAddress, PassWord, major, skills, interests) values(%s, %s, %s, %s, %s)", (temp_email, temp_password,
                                                                                      temp_major, temp_skills,
                                                                                      temp_interests))
        return HttpResponse("<h2>You are successfully registered!</h2>")

def updatepassword(request):
    if request.method == 'POST':
        temp_email = request.POST.get('UIUC Email Address')
        temp_oldpassword = request.POST.get('Enter your old Password')
        temp_new = request.POST.get('Enter your new Password')
        temp_confirm = request.POST.get('Enter your new Password again')
        print(temp_email)
        with connection.cursor() as cursor:
            cursor.execute("select PassWord from signup_students where EmailAddress = %s;", (temp_email,))
            data = cursor.fetchone()
            print(data)


        if data == temp_oldpassword and temp_new == temp_confirm:
            with connection.cursor() as cursor:
                cursor.execute("update signup_students set PassWord = %s where EmailAddress = %s;", (temp_new, temp_email))
            return HttpResponse("<h2>Your PassWord is successfully changed </h2>")
# def delete_account(request):
#     if request.method == 'POST':
#         temp_email = request.POST.get('UIUC Email Address')
#
#         with connection.cursor() as cursor:
#             cursor.execute("select EmailAddress from signup_students where EmailAddress = %s;", (temp_email,))
#             data = cursor.fetchone()
#         if data == temp_email:
#             with connection.cursor() as cursor:
#                 cursor.execute("delete from signup_students where EmailAddress = %s;", (temp_new, temp_email))
#             return HttpResponse("<h2>Your account is successfully closed </h2>")