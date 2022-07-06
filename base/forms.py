from dataclasses import fields
import django

from django import forms


from django.forms import ModelForm
from .models import About, Home, Project,Skill


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','sub_headline','thumbnail', 'body','active','featured','tags','SourceLink','APILink']
        exclude = ['Clear']


        widgets = {
			'tags':forms.CheckboxSelectMultiple()
		}


    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['body'].widget.attrs.update(
            {'class': 'form-control' })  



class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        



    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'})

        self.fields['body'].widget.attrs.update(
            {'class': 'form-control' })  
        self.fields['sub_body'].widget.attrs.update(
            {'class': 'form-control' })  




# class EndorsementForm(ModelForm):
#     class Meta:
#         model = Endorsement
#         fields = '__all__'
#         # exclude = ['featured']
        



#     def __init__(self, *args, **kwargs):
#         super(EndorsementForm, self).__init__(*args, **kwargs)
#         self.fields['name'].widget.attrs.update(
#             {'class': 'form-control'})

#         self.fields['body'].widget.attrs.update(
#             {'class': 'form-control' })  



# class HomeEditForm(ModelForm):
#     class Meta:
#         model = Home
#         fields = '__all__'
        



#     def __init__(self, *args, **kwargs):
#         super(HomeEditForm, self).__init__(*args, **kwargs)
#         self.fields['title'].widget.attrs.update(
#             {'class': 'form-control'})

#         self.fields['sub_title'].widget.attrs.update(
#             {'class': 'form-control' })  
#         self.fields['description'].widget.attrs.update(
#             {'class': 'form-control' })      


            

# class AboutEditForm(ModelForm):
#     class Meta:
#         model = About
#         fields = '__all__'
       


       

#     def __init__(self, *args, **kwargs):
#         super(AboutEditForm, self).__init__(*args, **kwargs)
#         self.fields['title1'].widget.attrs.update(
#             {'class': 'form-control'})

#         self.fields['description1'].widget.attrs.update(
#             {'class': 'form-control' })

#         self.fields['title2'].widget.attrs.update(
#             {'class': 'form-control'})

#         self.fields['description2'].widget.attrs.update(
#             {'class': 'form-control' })  
#         self.fields['title3'].widget.attrs.update(
#             {'class': 'form-control'})

#         self.fields['description3'].widget.attrs.update(
#             {'class': 'form-control' })  
       