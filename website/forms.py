from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, Professor, Course, Material, ChatBot

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('name', 'email')

class ProfessorCreationForm(CustomUserCreationForm):
    employee_code = forms.CharField(max_length=50, required=True, label="Código Funcional")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'PROFESSOR'
        if commit:
            user.save()
            Professor.objects.create(user=user, employee_code=self.cleaned_data['employee_code'])
        return user

class StudentCreationForm(CustomUserCreationForm):
    registration_number = forms.CharField(max_length=50, required=True, label="Número de Matrícula")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'STUDENT'
        if commit:
            user.save()
            Student.objects.create(user=user, registration_number=self.cleaned_data['registration_number'])
        return user

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']

class CourseProfessorForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label="Curso")
    professor = forms.ModelChoiceField(queryset=Professor.objects.all(), label="Professor")

class CourseStudentForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label="Curso")
    student = forms.ModelChoiceField(queryset=Student.objects.all(), label="Aluno")

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['title', 'file_path']
        labels = {
            'title': 'Título do Material',
            'file_path': 'Arquivo'
        }

class ChatBotForm(forms.ModelForm):
    class Meta:
        model = ChatBot
        fields = ['name', 'description']

class ChatBotMaterialForm(forms.Form):
    materials = forms.ModelMultipleChoiceField(queryset=Material.objects.none(), widget=forms.CheckboxSelectMultiple, required=True)

    def __init__(self, *args, **kwargs):
        professor = kwargs.pop('professor', None)
        super().__init__(*args, **kwargs)
        if professor:
            self.fields['materials'].queryset = Material.objects.filter(professor=professor)
