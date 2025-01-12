from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import *


def adminhome(request):
    return render(request,'admin/admin_index.html')

def login_get(request):
    return render(request,'login_index.html')

def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    a= Login.objects.filter(username= username, password=password)
    if a.exists():
        b = Login.objects.get(username= username, password = password)
        request.session['lid']=b.id
        if b.type == "admin":
            return HttpResponse("<script>alert('Welcome admin home'); window.location = '/myapp/admin_home/'</script>")
        elif b.type == 'company' :
            return HttpResponse("<script>alert('Welcome company home'); window.location = '/myapp/company_home/'</script>")
        elif b.type == 'college' :
            return HttpResponse("<script>alert('Welcome college home'); window.location = '/myapp/college_home/'</script>")
        else :
            return HttpResponse("<script>alert('Invalid User'); window.location = '/myapp/login_get/'</script>")
    else :
        return HttpResponse("<script>alert('Invalid User and password'); window.location = '/myapp/login_get/'</script>")

def add_college_get(request):
    return render(request,'admin/ADD COLLEGE.html')

def add_college_post(request):
    name=request.POST['textfield']
    university=request.POST['textfield2']
    email=request.POST['textfield3']
    phone=request.POST['textfield4']
    photo=request.FILES['textfield5']
    place=request.POST['textfield6']
    post=request.POST['textfield7']
    pin=request.POST['textfield8']
    district=request.POST['textfield9']
    state=request.POST['textfield10']
    since=request.POST['textfield11']


    date=datetime.now().strftime('%Y%m%d-%H%M%S')+".jpg"
    fs = FileSystemStorage()
    fs.save(date,photo)
    path = fs.url(date)


    login = Login()
    login.username = email

    import random
    login.password = random.randint(0000, 9999)
    login.type = "college"
    login.save()
    savetoCollege = College()
    savetoCollege.name = name
    savetoCollege.university_name= university
    savetoCollege.email = email
    savetoCollege.phone = phone
    savetoCollege.photo = path
    savetoCollege.place = place
    savetoCollege.post = post
    savetoCollege.pin = pin
    savetoCollege.district = district
    savetoCollege.state = state
    savetoCollege.since = since
    savetoCollege.LOGIN = login
    savetoCollege.save()
    return HttpResponse("<script>alert('success'); window.location = '/myapp/admin_home/'</script>")


def add_notification_get(request):
    return render(request,'admin/ADD NOTIFICATION.html')

def add_notification_post(request):
    notification=request.POST['textfield']

    notif=Notification()
    notif.date=datetime.now().today()
    notif.notification=notification
    notif.save()

    return HttpResponse("<script>alert('success'); window.location = '/myapp/admin_home/'</script>")



def add_skill_get(request):
    res = Skill.objects.all()
    return render(request, 'admin/ADD SKILL.html', {'data': res})


def add_skill_post(request):
    skill=request.POST['textfield']
    print(skill)

    sobj=Skill()
    sobj.skillname=skill
    sobj.save()
    return HttpResponse("<script>alert('success'); window.location = '/myapp/admin_home/'</script>")




def change_password_get(request):
    return render(request,'admin/change password.html')

def change_password_post(request):
    current_password=request.POST['textfield']
    new_password=request.POST['textfield2']
    confirm_password=request.POST['textfield3']
    change_pass = Login.objects.filter(id = request.session['lid'],password= current_password)
    if change_pass.exists() :
        Login.objects.get(id = request.session['lid'], password = current_password)
        if new_password == confirm_password :
            Login.objects.filter(id=request.session['lid']).update( password=confirm_password)
            return HttpResponse("<script>alert('Successfully updated password'); window.location = '/myapp/admin_home/'</script>")
        else :
            return HttpResponse("<script>alert('Password mismatched'); window.location = '/myapp/change_password_get/'</script>")
    else :
        return HttpResponse("<script>alert('Please check your current password'); window.location = '/myapp/change_password_get/'</script>")

def edit_college_get(request,id):
    clg=College.objects.get(id=id)
    return render(request,'admin/EDIT COLLEGE.html',{'data':clg})

def edit_college_post(request):
    name = request.POST['textfield']
    university = request.POST['textfield2']
    email = request.POST['textfield3']
    phone = request.POST['textfield4']
    place = request.POST['textfield6']
    post = request.POST['textfield7']
    pin = request.POST['textfield8']
    district = request.POST['textfield9']
    state = request.POST['textfield10']
    since = request.POST['textfield11']
    id=request.POST['id']

    savetoCollege = College.objects.get(id=id)

    if 'textfield5' in request.FILES:
        photo = request.FILES['textfield5']

        date = datetime.now().strftime('%Y%m%d-%H%M%S') + ".jpg"
        fs = FileSystemStorage()
        fs.save(date, photo)
        path = fs.url(date)
        savetoCollege.photo = path
        savetoCollege.save()

    savetoCollege.name = name
    savetoCollege.university_name = university
    savetoCollege.email = email
    savetoCollege.phone = phone
    savetoCollege.place = place
    savetoCollege.post = post
    savetoCollege.pin = pin
    savetoCollege.district = district
    savetoCollege.state = state
    savetoCollege.since = since
    savetoCollege.save()
    return HttpResponse("<script>alert('updated'); window.location = '/myapp/view_college_get/'</script>")


def delete_college(request,id):
    College.objects.get(LOGIN=id).delete()
    Login.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted'); window.location = '/myapp/view_college_get/'</script>")

def delete_notification(request,id):
    Notification.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted'); window.location = '/myapp/view_notification_get/'</script>")

def delete_skill(request,id):
    Skill.objects.get(id=id).delete()
    return HttpResponse("<script>alert('deleted'); window.location = '/myapp/view_skill_get/'</script>")



def edit_notification_get(request,id):
    notify=Notification.objects.get(id=id)
    return render(request,'admin/EDIT NOTIFICATION.html',{'data':notify})

def edit_notification_post(request):
    notification = request.POST['textfield']
    id=request.POST['id']

    notif = Notification.objects.get(id=id)
    notif.date = datetime.now().today()
    notif.notification = notification
    notif.save()

    return HttpResponse("<script>alert('updated'); window.location = '/myapp/view_notification_get/'</script>")


def send_reply_get(request,id):
    return render(request,'admin/SEND REPLY.html',{'id':id})

def send_reply_post(request):
    reply=request.POST['textfield']
    id=request.POST['id']
    res=Complaint.objects.filter(id=id).update(reply=reply,status="replied")
    return HttpResponse("<script>alert('replied'); window.location = '/myapp/view_complaints_get/'</script>")






def view_skill_get(request):
    res=Skill.objects.all()
    return render(request,'admin/VIEW SKILL.html',{'data':res})

def view_skill_post(request):
    skillname=request.POST['textfield']
    res = Skill.objects.filter(skillname__icontains=skillname)
    return render(request, 'admin/VIEW SKILL.html', {'data': res})


def view_college_get(request):
    res=College.objects.all()
    return render(request,'admin/VIEW COLLEGE.html',{'data':res})

def view_college_post(request):
    search=request.POST['textfield']
    res = College.objects.filter(name__icontains=search)
    return render(request, 'admin/VIEW COLLEGE.html', {'data': res})


################company view

def company_home(request):
    return render(request,'company/COMPANY HOME.html')



def view_company_get(request):
    res = Company.objects.filter(status="pending")
    return render(request, 'admin/VIEW COMPANY.html', {'data': res})


def view_company_post(request):
    search=request.POST['textfield']
    res = Company.objects.filter(status="pending",name__icontains=search)
    return render(request, 'admin/VIEW COMPANY.html', {'data': res})


def view_rejected_company_get(request):
    res = Company.objects.filter(status="rejected")
    return render(request, 'admin/VIEW REJECTED COMPANY.html', {'data': res})


def view_rejected_company_post(request):
    search = request.POST['textfield']
    res = Company.objects.filter(status="rejected",name__icontains=search)
    return render(request, 'admin/VIEW REJECTED COMPANY.html', {'data': res})

def view_approved_company_get(request):
    res=Company.objects.filter(status="approved")
    return render(request,'admin/VIEW APPROVED COMPANY.html',{'data':res})

def view_approved_company_post(request):
    search=request.POST['textfield']
    res = Company.objects.filter(status="approved",name__icontains=search)
    return render(request, 'admin/VIEW APPROVED COMPANY.html', {'data': res})



def approve_company(request,id):
    approve=Company.objects.filter(LOGIN=id).update(status="approved")
    savelogin=Login.objects.filter(id=id).update(type="company")
    return HttpResponse("<script>alert('approved'); window.location = '/myapp/view_company_get/'</script>")

def reject_company(request,id):
    reject=Company.objects.filter(LOGIN=id).update(status="rejected")
    savelogin=Login.objects.filter(id=id).update(type="rejected")
    return HttpResponse("<script>alert('rejected'); window.location = '/myapp/view_company_get/'</script>")


###################################################




def view_complaints_get(request):
    res = Complaint.objects.all()
    return render(request, 'admin/VIEW COMPLAINTS.html', {'data': res})

def view_complaints_post(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    res = Complaint.objects.filter(date__range=[fromdate,todate])
    return render(request, 'admin/VIEW COMPLAINTS.html', {'data': res})


def view_course_get(request,id):
    res = Course.objects.filter(COLLEGE_id=id)
    request.session['cid']=id
    return render(request, 'admin/VIEW COURSE.html', {'data': res})

def view_course_post(request):
    search = request.POST['textfield']
    res = Course.objects.filter(COLLEGE_id=request.session['cid'],course_name__icontains=search)
    return render(request, 'admin/VIEW COURSE.html', {'data': res})


def view_notification_get(request):
    res = Notification.objects.all()
    return render(request, 'admin/VIEW NOTIFICATION.html', {'data': res})


def view_notification_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    res = Notification.objects.filter(date__range=[fromdate,todate])
    return render(request, 'admin/VIEW NOTIFICATION.html', {'data': res})


def view_vaccancy_get(request,id):
    res = Vaccancy.objects.filter(COMPANY_id=id)
    request.session['vid']=id
    return render(request, 'admin/VIEW VACCANCY.html', {'data': res})


def view_vaccancy_post(request):
    search = request.POST['textfield']
    res = Vaccancy.objects.filter(COMPANY_id=request.session['vid'],job_title__icontains=search)
    return render(request, 'admin/VIEW VACCANCY.html', {'data': res})




############################################3


def add_vaccancy_company_get(request):
    return render(request,'company/ADD VACCANCY COMPANY.html')

def add_vaccancy_company_post(request):
    vaccancy_no=request.POST['textfield']
    job_title=request.POST['textfield2']
    start_date=request.POST['textfield3']
    end_date=request.POST['textfield4']
    experience=request.POST['textfield5']

    v=Vaccancy()
    v.vaccancy_no=vaccancy_no
    v.job_title=job_title
    v.start_date=start_date
    v.end_date=end_date
    v.experience=experience
    v.COMPANY=Company.objects.get(LOGIN_id= request.session['lid'])
    v.save()


    return HttpResponse("<script>alert('success'); window.location = '/myapp/company_home/'</script>")


def company_change_password_get(request):
    return render(request,'company/CHANGE PASSWORD COMPANY.html')

def company_change_password_post(request):

    current_password=request.POST['textfield']
    new_password=request.POST['textfield2']
    confirm_password=request.POST['textfield3']
    change_pass = Login.objects.filter(id = request.session['lid'],password= current_password)
    if change_pass.exists() :
        Login.objects.get(id = request.session['lid'], password = current_password)
        if new_password == confirm_password :
            Login.objects.filter(id=request.session['lid']).update( password=confirm_password)
            return HttpResponse("<script>alert('Successfully updated password'); window.location = '/myapp/admin_home/'</script>")
        else :
            return HttpResponse("<script>alert('Password mismatched'); window.location = '/myapp/change_password_get/'</script>")
    else :
        return HttpResponse("<script>alert('Please check your current password'); window.location = '/myapp/change_password_get/'</script>")



def edit_profile_get(request):
    data=Company.objects.get(LOGIN_id=request.session['lid'])

    return render(request,'company/EDIT PROFILE COMPANY.html',{"data":data})
def edit_profile_post(request):
    name=request.POST['textfield']
    since=request.POST['textfield2']
    email=request.POST['textfield3']
    phone=request.POST['textfield4']
    place=request.POST['textfield5']
    post=request.POST['textfield6']
    pin=request.POST['textfield7']
    district=request.POST['textfield8']
    state=request.POST['textfield9']


    fs = FileSystemStorage()
    cobj = Company.objects.get(LOGIN_id=request.session['lid'])

    if 'fileField2' in request.FILES:
        photo = request.FILES['fileField2']
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + "1.jpg"
        fs.save(date, photo)
        path = fs.url(date)
        cobj.photo = path
        cobj.save()

    if 'fileField' in request.FILES:
        proof = request.FILES['fileField']
        date1 = datetime.now().strftime('%Y%m%d-%H%M%S') + "2.jpg"
        fs.save(date1, proof)
        path2 = fs.url(date1)
        cobj.proof = path2
        cobj.save()

    if 'textfield10' in request.FILES:
        logo = request.FILES['textfield10']
        date2 = datetime.now().strftime('%Y%m%d-%H%M%S') + "3.jpg"
        fs.save(date2, logo)
        path3 = fs.url(date2)
        cobj.logo = path3
        cobj.save()

    cobj.name = name
    cobj.since = since
    cobj.email = email
    cobj.phone = phone
    cobj.place = place
    cobj.post = post
    cobj.pin = pin
    cobj.district = district
    cobj.state = state

    cobj.save()
    return HttpResponse("<script>alert('Updated'); window.location = '/myapp/view_profile_get/'</script>")

def delete_vaccancy_get(request,id):
    Vaccancy.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted'); window.location = '/myapp/view_vaccancy_company_get/'</script>")

def edit_vaccancy_get(request,id):
    data = Vaccancy.objects.get(id=id)
    return render(request,'company/EDIT VACCANCY COMPANY.html',{"data":data})

def edit_vaccancy_post(request):
    vaccancy_no=request.POST['textfield']
    job_title = request.POST['textfield2']
    start_date = request.POST['textfield3']
    end_date = request.POST['textfield4']
    experience = request.POST['textfield5']

    id = request.POST['id']


    v = Vaccancy.objects.get(id=id)
    v.vaccancy_no = vaccancy_no
    v.job_title = job_title
    v.start_date = start_date
    v.end_date = end_date
    v.experience = experience
    v.COMPANY = Company.objects.get(LOGIN_id=request.session['lid'])
    v.save()
    return HttpResponse("<script>alert('updated'); window.location = '/myapp/view_vaccancy_company_get/'</script>")


def signup_company_get(request):
    return render(request,'company/SIGNUP COMPANY.html')

def signup_company_post(request):
    name = request.POST['textfield']
    since = request.POST['textfield2']
    email = request.POST['textfield3']
    phone = request.POST['textfield4']
    place = request.POST['textfield5']
    post = request.POST['textfield6']
    pin = request.POST['textfield7']
    district = request.POST['textfield8']
    state = request.POST['textfield9']
    logo = request.FILES['textfield10']
    photo = request.FILES['fileField2']
    proof = request.FILES['fileField']
    password=request.POST['textfield11']
    confirm_password=request.POST['textfield12']



    if Login.objects.filter(username=email).exists():
        return HttpResponse("<script>alert('email already exists'); window.location = '/myapp/signup_company_get/'</script>")


    if password==confirm_password:


        fs = FileSystemStorage()

        date = datetime.now().strftime('%Y%m%d-%H%M%S') + "1.jpg"
        date1 = datetime.now().strftime('%Y%m%d-%H%M%S') + "2.jpg"
        date2 = datetime.now().strftime('%Y%m%d-%H%M%S') + "3.jpg"

        fs.save(date, photo)
        path = fs.url(date)

        fs.save(date1, proof)
        path2 = fs.url(date1)

        fs.save(date2, logo)
        path3 = fs.url(date2)



        lobj=Login()
        lobj.username=email
        lobj.password=confirm_password
        lobj.type='pending'
        lobj.save()


        cobj=Company()
        cobj.name=name
        cobj.since=since
        cobj.email=email
        cobj.phone=phone
        cobj.place=place
        cobj.post=post
        cobj.pin=pin
        cobj.district=district
        cobj.state=state
        cobj.logo=path3
        cobj.photo=path
        cobj.proof=path2
        cobj.status="pending"
        cobj.LOGIN=lobj
        cobj.save()
        return HttpResponse("<script>alert('success'); window.location = '/myapp/login_get/'</script>")
    else:
        return HttpResponse("<script>alert('mismatched'); window.location = '/myapp/signup_company_get/'</script>")



def view_approved_request_get(request):
    id = request.session['lid']
    obj = Vaccancy_Request.objects.filter(VACANCY__COMPANY__LOGIN_id=id, status='approved')
    return render(request,'company/VIEW APPROVED REQUEST.html',{"data":obj})

def view_approved_request_post(request):
    fromdate=request.POST['textfield']
    todate=request.POST['textfield2']
    id = request.session['lid']
    obj = Vaccancy_Request.objects.filter(VACANCY__COMPANY__LOGIN_id=id, status='approved',date__range=[fromdate,todate])
    return render(request, 'company/VIEW APPROVED REQUEST.html', {"data": obj})

def approve_request_get(request,id):
    Vaccancy_Request.objects.filter(id=id).update(status= "approved")
    return HttpResponse("<script>alert('APPROVED'); window.location = '/myapp/view_approved_request_get/'</script>")

def reject_request_get(request,id):
    Vaccancy_Request.objects.filter(id=id).update(status= "rejected")
    return HttpResponse("<script>alert('REJECT'); window.location = '/myapp/view_rejected_request_get/'</script>")


def view_profile_get(request):
    data=Company.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'company/VIEW PROFILE COMPANY.html',{"data":data})




def view_rejected_request_get(request):
    id = request.session['lid']
    obj = Vaccancy_Request.objects.filter(VACANCY__COMPANY__LOGIN_id=id, status='rejected')
    return render(request,'company/VIEW REJECTED REQUEST.html',{"data": obj})
def view_rejected_request_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    id = request.session['lid']
    obj = Vaccancy_Request.objects.filter(VACANCY__COMPANY__LOGIN_id=id, status='rejected',date__range=[fromdate,todate])
    return render(request, 'company/VIEW REJECTED REQUEST.html', {"data": obj})

def view_skill_company_get(request):
    data = Skill.objects.all()
    return render(request,'company/VIEW SKILL.html',{"data":data})
def view_skill_company_post(request):
    search=request.POST['textfield']
    data = Skill.objects.filter(skillname__icontains=search)
    return render(request, 'company/VIEW SKILL.html', {"data": data})


def view_vaccancy_company_get(request):
    data=Vaccancy.objects.filter(COMPANY__LOGIN_id=request.session['lid'])
    return render(request,'company/VIEW VACCANCY COMPANY.html',{'data':data})
def view_vaccancy_company_post(request):
    search=request.POST['textfield']
    data = Vaccancy.objects.filter(COMPANY__LOGIN_id=request.session['lid'],job_title__icontains=search)
    return render(request, 'company/VIEW VACCANCY COMPANY.html', {'data': data})

def view_vaccancy_request_get(request,id):
    # id= request.session['lid']
    obj=Vaccancy_Request.objects.filter(VACANCY_id=id,status = 'pending')
    request.session['rid']=id
    return render(request,'company/VIEW VACCANCY REQUEST.html',{'data':obj})
def view_vaccancy_request_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    obj=Vaccancy_Request.objects.filter(VACANCY_id=request.session['rid'],status = 'pending',date__range=[fromdate,todate])
    return render(request,'company/VIEW VACCANCY REQUEST.html',{'data':obj})

def view_resume(request,id):
    obj=Resume.objects.get(USER_id=id)
    return render(request,'company/VIEW RESUME.html',{'data':obj})


##########################

def college_change_password_get(request):
    return render(request,'COLLEGE/COLLEGE CHANGE PASSWORD.html')

def college_change_password_post(request):

    current_password=request.POST['textfield']
    new_password=request.POST['textfield2']
    confirm_password=request.POST['textfield3']
    change_pass = Login.objects.filter(id = request.session['lid'],password= current_password)
    if change_pass.exists() :
        Login.objects.get(id = request.session['lid'], password = current_password)
        if new_password == confirm_password :
            Login.objects.filter(id=request.session['lid']).update( password=confirm_password)
            return HttpResponse("<script>alert('Successfully updated password'); window.location = '/myapp/admin_home/'</script>")
        else :
            return HttpResponse("<script>alert('Password mismatched'); window.location = '/myapp/change_password_get/'</script>")
    else :
        return HttpResponse("<script>alert('Please check your current password'); window.location = '/myapp/change_password_get/'</script>")






def college_home(request):
    return render(request,'COLLEGE/collegeHome.html')


def add_course_get(request):
    a=Department.objects.all()
    return render(request,'COLLEGE/ADD COURSE.html',{"data":a})

def add_course_post(request):
    course_name=request.POST['textfield']
    semester=request.POST['textfield2']
    id=request.POST['select']

    a=Course()
    a.course_name=course_name
    a.semester=semester
    a.DEPARTMENT_id=id
    a.save()
    return HttpResponse(
        "<script>alert('add successfully'); window.location = '/myapp/college_home/'</script>")


def add_department_get(request):
    return render(request,'COLLEGE/ADD DEPARTMENT.html')

def add_department_post(request):
    department_name=request.POST['textfield']

    a=Department()
    a.department_name=department_name
    a.save()
    return HttpResponse(
        "<script>alert('add successfully'); window.location = '/myapp/college_home/'</script>")


def add_facility_get(request):
    return render(request,'COLLEGE/ADD FACILITY.html')

def add_facility_post(request):
    facility_name=request.POST['textfield']
    details=request.POST['textfield2']
    photo=request.FILES['fileField']

    fs = FileSystemStorage()

    date = datetime.now().strftime('%Y%m%d-%H%M%S') + "1.jpg"

    fs.save(date, photo)
    path = fs.url(date)



    a=Facilities()
    a.facility_name=facility_name
    a.details=details
    a.photo=path
    a.save()

    return HttpResponse(
        "<script>alert('add successfully'); window.location = '/myapp/college_home/'</script>")


def add_fee_get(request):
    a=Course.objects.all()
    return render(request,'COLLEGE/ADD FEE.html',{"data":a})

def add_fee_post(request):
    semester=request.POST['textfield']
    fees=request.POST['textfield2']
    id=request.POST['select']

    a=FeeStruct()
    a.sem=semester
    a.fees=fees
    a.COURSE_id=id
    a.save()

    return HttpResponse(
        "<script>alert('add successfully'); window.location = '/myapp/college_home/'</script>")




def edit_course_get(request,id):
    a=Course.objects.get(id=id)
    a1=Department.objects.all()
    return render(request,'COLLEGE/EDIT COURSE.html',{"data":a,"data1":a1})

def edit_course_post(request):
    course_name = request.POST['textfield']
    semester = request.POST['textfield2']
    id = request.POST['select']
    idd = request.POST['id']

    a = Course.objects.get(id=idd)
    a.course_name = course_name
    a.semester = semester
    a.DEPARTMENT_id = id
    a.save()
    return HttpResponse(
        "<script>alert('edit successfully'); window.location = '/myapp/view_course_college_get/'</script>")

def delete_course(request,id):
    a=Course.objects.get(id=id).delete()
    return HttpResponse(
        "<script>alert('delete successfully'); window.location = '/myapp/view_course_college_get/'</script>")




def edit_department_get(request,id):
    a=Department.objects.get(id=id)
    return render(request,'COLLEGE/EDIT DEPARTMENT.html',{"data":a})

def edit_department_post(request):
    department_name=request.POST['textfield']
    id=request.POST['id']

    a=Department.objects.get(id=id)
    a.department_name=department_name
    a.save()
    return HttpResponse(
        "<script>alert('edit successfully'); window.location = '/myapp/view_department_get/'</script>")

def delete_department(request,id):
    a=Department.objects.get(id=id).delete()
    return HttpResponse(
        "<script>alert('delete successfully'); window.location = '/myapp/view_department_get/'</script>")

def edit_facility_get(request,id):
    a=Facilities.objects.get(id=id)
    return render(request,'COLLEGE/EDIT FACILITY.html',{"data":a})

def edit_facility_post(request):
    facility_name = request.POST['textfield']
    details = request.POST['textfield2']
    id = request.POST['id']

    a = Facilities.objects.get(id=id)


    if 'fileField' in request.FILES:
        photo = request.FILES['fileField']
        if photo !='':
            fs = FileSystemStorage()
            date = datetime.now().strftime('%Y%m%d-%H%M%S') + "1.jpg"
            fs.save(date, photo)
            path = fs.url(date)
            a.photo = path
            a.save()

    a.facility_name = facility_name
    a.details = details
    a.save()

    return HttpResponse(
        "<script>alert('edit successfully'); window.location = '/myapp/view_facility_get/'</script>")

def delete_facility(request,id):
    a=Facilities.objects.get(id=id).delete()
    return HttpResponse(
        "<script>alert('delete successfully'); window.location = '/myapp/view_facility_get/'</script>")




def edit_fee_get(request,id):
    a=FeeStruct.objects.get(id=id)
    a1=Course.objects.all()
    return render(request,'COLLEGE/EDIT FEE.html',{"data":a,"data1":a1})

def edit_fee_post(request):
    semester = request.POST['textfield']
    fees = request.POST['textfield2']
    id = request.POST['select']
    idd = request.POST['id']

    a = FeeStruct.objects.get(id=idd)
    a.sem = semester
    a.fees = fees
    a.COURSE_id = id
    a.save()

    return HttpResponse(
        "<script>alert('edit successfully'); window.location = '/myapp/view_fee_get/'</script>")


def delete_fee(request,id):
    a=FeeStruct.objects.get(id=id).delete()
    return HttpResponse(
        "<script>alert('delete successfully'); window.location = '/myapp/view_fee_get/'</script>")




def view_college_profile_get(request):
    obj = College.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'COLLEGE/VIEW COLLEGE PROFILE.html',{"data":obj})





def view_course_college_get(request):
    a=Course.objects.all()

    return render(request, 'COLLEGE/VIEW COURSE COLLEGE.html',{"data":a})

def view_course_college_post(request):
    search = request.POST['textfield']
    a = Course.objects.filter(course_name__icontains=search)
    return render(request, 'COLLEGE/VIEW COURSE COLLEGE.html',{"data":a})


def view_department_get(request):
    a=Department.objects.all()
    return render(request,'COLLEGE/VIEW DEPARTMENT.html',{"data":a})

def view_department_post(request):
    search=request.POST['textfield']
    a=Department.objects.filter(department_name__icontains=search)
    return render(request,'COLLEGE/VIEW DEPARTMENT.html',{"data":a})




def view_facility_get(request):
    a=Facilities.objects.all()
    return render(request,'COLLEGE/VIEW FACILITY.html',{"data":a})

def view_facility_post(request):
    search = request.POST['textfield']
    a = Facilities.objects.filter(facility_name__icontains=search)
    return render(request,'COLLEGE/VIEW FACILITY.html',{"data":a})




def view_fee_get(request):
    a=FeeStruct.objects.all()
    return render(request,'COLLEGE/VIEW FEE.html',{"data":a})

def view_fee_post(request):
    search = request.POST['textfield']
    a = FeeStruct.objects.filter(fees__icontains=search)
    return render(request,'COLLEGE/VIEW FEE.html',{"data":a})


def logout(request):
    request.session['lid']=''
    return HttpResponse(
        "<script>alert('logout successfully'); window.location = '/myapp/login_get/'</script>")



# -----------------------------Flutter----------------------------------


def user_login(request):
    username=request.POST['username']
    password=request.POST['password']
    a= Login.objects.filter(username= username, password=password)
    if a.exists():
        b = Login.objects.get(username= username, password = password)
        lid=b.id
        if b.type == "user":
            return JsonResponse({"status":"ok"})
        else :
            return JsonResponse({"status":"no"})
    else :
        return JsonResponse({"status": "no"})



def user_change_password(request):
    current_password = request.POST['current_password']
    new_password = request.POST['new_password']
    confirm_password = request.POST['confirm_password']
    lid = request.POST['lid']

    change_pass = Login.objects.filter(id=lid, password=current_password)
    if change_pass.exists():
        Login.objects.get(id=lid, password=current_password)
        if new_password == confirm_password:
            Login.objects.filter(id=lid).update(password=confirm_password)
            return JsonResponse({"status": "ok"})
        else:
            return JsonResponse({"status": "no"})
    else:
            return JsonResponse({"status": "no"})


def user_signup(request):
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    dob = request.POST['dob']
    gender = request.POST['gender']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    district = request.POST['district']
    state = request.POST['state']
    photo = request.FILES['photo']
    password = request.POST['password']
    confirm_password = request.POST['confirmpassword']

    if Login.objects.filter(username=email).exists():
        return JsonResponse({"status": "Ok"})

    if password == confirm_password:
        from datetime import datetime
        import base64
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + "1.jpg"
        a = base64.b64decode(photo)
        fs= open("C:\\Users\\Lenovo\\PycharmProjects\\career_path_navigator\\media\\User\\" + date, "wb")
        photopath = '/media/user/' + date
        fs.write(a)
        fs.close()

        lobj = Login()
        lobj.username = email
        lobj.password = confirm_password
        lobj.type = 'pending'
        lobj.save()

        cobj = User()
        cobj.name = name
        cobj.email = email
        cobj.phone = phone
        cobj.dob = dob
        cobj.gender = gender
        cobj.place = place
        cobj.post = post
        cobj.pin = pin
        cobj.district = district
        cobj.state = state
        cobj.photo = photopath
        cobj.status = "pending"
        cobj.LOGIN = lobj
        cobj.save()
        return JsonResponse({"status": "Ok"})
    else:
        return JsonResponse({"status": "No"})

def user_addownskill(request):
    skill = request.POST['skill']
    lid = request.POST['lid']

    obj= OwnSkill()
    obj.skill= skill
    obj.USER= User.objects.get(LOGIN__id=lid)
    obj.save()
    return JsonResponse({"status": "Ok"})

def user_viewownskill(request):
    obj= OwnSkill.objects.all()
    l=[]
    for i in obj :
        l.append({"id":i.id,
                  "skill":i.skill,
                  })
    return JsonResponse({"status": "Ok", 'data': l})


def user_editownskill(request):
    skill = request.POST['skill']
    id = request.POST['id']

    obj = OwnSkill.objects.get(id=id)
    obj.skill = skill
    obj.save()
    return JsonResponse({"status": "Ok"})

def user_deleteownskill(request,id):
    obj = OwnSkill.objects.get(id=id).delete()

    return JsonResponse({"status": "Ok"})


def user_viewapprovedcompany(request):
    obj= Company.objects.filter(status="approved")

    l= []
    for i in obj :
        l.append({"id":i.id,
                  "name" : i.name,
                  "since": i.since,
                  "email": i.email,
                  "phone": i.phone,
                  "place": i.place,
                  "post": i.post,
                  "pin": i.pin,
                  "district": i.district,
                  "state" : i.state,
                  "logo": i.logo,
                  "photo": i.photo,
        })

    return JsonResponse({"status": "Ok", 'data': l})


def user_viewvaccancy(request):
    obj = Vaccancy.objects.all()

    l = []
    for i in obj:
        l.append({"id": i.id,
                  "vaccancy_no": i.vaccancy_no,
                  "job_title": i.job_title,
                  "start_date": i.start_date,
                  "end_date": i.end_date,
                  "experience": i.experience,
                  "company" : i.COMPANY.name,
                  })

    return JsonResponse({"status": "Ok", 'data': l})


def user_jobrecommendation(request):
    pass

def user_send_request(request):
    lid=request.POST['lid']
    vid=request.POST['vid']
    r=Vaccancy_Request()
    r.date=datetime.now().today()
    r.status='pending'
    r.USER=User.objects.get(login_id=lid)
    r.VACANCY=Vaccancy.objects.get(id=vid)
    r.save()
    return JsonResponse({"status": "Ok"})

def user_send_complaint(request):
    complaint=request.POST['complaint']
    lid=request.POST['lid']
    c=Complaint()
    c.date=datetime.now().today()
    c.complaint=complaint
    c.reply='pending'
    c.status='pending'
    c.USER=User.objects.get(login_id=lid)
    c.save()
    return JsonResponse({"status": "Ok"})


def user_view_reply(request):
    obj = Complaint.objects.all()
    l = []
    for i in obj:
        l.append({"id": i.id,
                  "date": i.date,
                  "complaint": i.complaint,
                  "reply": i.reply,
                  "status": i.status,
                  })
        return JsonResponse({"status": "Ok",'data':l})



def user_view_college(request):
    obj = College.objects.all()
    l = []
    for i in obj:
        l.append({"id": i.id,
                  "name": i.name,
                  "university_name": i.university_name,
                  "email": i.email,
                  "phone": i.phone,
                  "photo": i.photo,
                  "place": i.place,
                  "post": i.post,
                  "pin": i.pin,
                  "district": i.district,
                  "state":i.state,
                  "since":i.since,
                  })
        return JsonResponse({"status": "Ok",'data':l})


def user_view_course(request):
    obj = Course.objects.all()
    l = []
    for i in obj:
        l.append({"id": i.id,
                  "course_name": i.course_name,
                  "semester": i.semester,
                  'department':i.DEPARTMENT.department_name,
                  })
        return JsonResponse({"status": "Ok",'data':l})


def user_view_fees(request):
    obj = FeeStruct.objects.all()
    l = []
    for i in obj:
        l.append({"id": i.id,
                  "fees": i.fees,
                  "sem": i.sem,
                  'course':i.COURSE.course_name,
                  })
        return JsonResponse({"status": "Ok",'data':l})



def user_view_facility(request):
    obj = Facilities.objects.all()
    l = []
    for i in obj:
        l.append({"id": i.id,
                  "facility_name": i.facility_name,
                  "details": i.details,
                  'photo':i.photo,
                  })
        return JsonResponse({"status": "Ok",'data':l})
















