from django.shortcuts import render,redirect
from .models import  Project ,Skill ,Home,About
from .forms import  ProjectForm,SkillForm
from django.contrib.auth.decorators import login_required
from .filters import PostFilter
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string 
from django.contrib import messages




# Create your views here.
def home(request):
    projects = Project.objects.filter(active=True, featured=True)[0:3]
    detailedSkills = Skill.objects.exclude(body='')
    skills = Skill.objects.filter(body='')
    # endorsements = Endorsement.objects.all()
    HomeEdit = Home.objects.all()
    AboutEdit = About.objects.all()


 


    context = {'projects': projects, 'skills': skills,
               'detailedSkills': detailedSkills  , 'HomeEdit':HomeEdit,'AboutEdit':AboutEdit
              }

    return render(request,'base/home.html', context)



##----------Individual Project Page----------
def projectPage(request,slug):
    project = Project.objects.get(slug=slug)
    context = {'project':project}
    return render(request,'base/project.html', context)    
    # slug ----> primary key for each project






@login_required(login_url="home")
def addProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your project was successfully added!')
            return redirect('home')

    context = {'form':form}
    return render(request,'base/project_form.html', context)    


@login_required(login_url="home")
def editProject(request,slug):
    project = Project.objects.get(slug=slug)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Project has been updated!')
            return redirect('post-project')

    context = {'form':form}
    return render(request,'base/project_form.html', context) 



     
##------------- ALL PROJECTS PAGE VIEW -------------
def postProjects(request):
    projects = Project.objects.filter(active=True, featured=True)
    myfilter = PostFilter(request.GET, queryset=projects)
    projects = myfilter.qs
    page = request.GET.get('page')
    paginator = Paginator(projects,4)                        # creating a paginator object   # getting the desired page number from url

    try:
        projects = paginator.page(page)

    except PageNotAnInteger:                                     # if page_number is not an integer then assign the first page
        projects = paginator.page(1)

    except EmptyPage:                                            # if page is empty then return last page
        projects = paginator.page(paginator.num_pages)        


    context = {'projects': projects, 'myfilter':myfilter}   

    return render(request,'base/PostProject.html',context)   


@login_required(login_url="home")
def deleteProject(request,slug):
    project = Project.objects.get(slug=slug)
    context = {'item':project}

    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Your project was deleted!')
        return redirect('post-project')


    return render(request,'base/delete.html', context) 


def sendEmails(request):
    if request.method == 'POST':

        template = render_to_string('base/email_template.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
			'message':request.POST['message'],
			})


        email = EmailMessage(
                        request.POST['subject'], 
                        template,
                        settings.EMAIL_HOST_USER,
                        ['abhisheksinghjin@gmail.com']  )

        email.fail_silently=False
        email.send()            

    return render(request, 'base/email_sent.html')


@login_required(login_url="home")
def addSkills(request):
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        form.save()
        messages.success(request, 'Your skill was successfully added!')
        return redirect('home')

    context = {'form':form}
    return render(request,'base/skillform.html',context)







def addEndorsements(request):
    form = EndorsementForm()
    if request.method == "POST":
        form = EndorsementForm(request.POST)
        form.save()
        messages.success(request, 'Thank you, your endorsement was successfully added!')
        return redirect('home') 

    context = {'form':form}
    return render(request,'base/EndorsementForm.html',context)


def Nodemo(request):
 

    return render(request, 'base/Nodemo.html')





# @login_required(login_url="home")
# def homeEdit(request):
#     home = Home.objects.all()
#     form = HomeEditForm(instance=home)
#     if request.method == "POST":
#         form = HomeEditForm(request.POST,instance=home)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Successfully updated!')
#             return redirect('home')

#     context = {'form':form,'home':home}
#     return render(request,'base/HomeEdit.html', context)  


# @login_required(login_url="home")
# def aboutEdit(request):
#     about = About.objects.all()
#     form = AboutEditForm(instance=about)
#     if request.method == "POST":
#         form = AboutEditForm(request.POST,request.FILES,instance=about)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Successfully updated!')
#             return redirect('home')

#     context = {'form':form,'about':about}
#     return render(request,'base/AboutEdit.html', context)




# @login_required(login_url="home")
# def editSkill(request,slug):
#     project = Project.objects.get(slug=slug)
#     form = ProjectForm(instance=project)
#     if request.method == "POST":
#         form = ProjectForm(request.POST,request.FILES,instance=project)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your Project has been updated!')
#             return redirect('home')

#     context = {'form':form}
#     return render(request,'base/project_form.html', context)     