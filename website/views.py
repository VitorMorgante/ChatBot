from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import User, Student, Professor, Course, Material, ChatBot, Conversation, Message
from .forms import (
    ProfessorCreationForm, StudentCreationForm, CourseForm, 
    CourseProfessorForm, CourseStudentForm, MaterialForm, 
    ChatBotForm, ChatBotMaterialForm
)
from .services.embedding_service import extract_text
from .services.chatbot_service import generate_answer


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.role == 'ADMIN':
                return redirect('admin_dashboard')
            elif user.role == 'PROFESSOR':
                return redirect('professor_dashboard')
            elif user.role == 'STUDENT':
                return redirect('student_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'website/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def admin_dashboard(request):
    if request.user.role != 'ADMIN':
        return redirect('login')
    return render(request, 'website/admin_dashboard.html')

@login_required
def professor_dashboard(request):
    if request.user.role != 'PROFESSOR':
        return redirect('login')
    return render(request, 'website/professor_dashboard.html')

@login_required
def student_dashboard(request):
    if request.user.role != 'STUDENT':
        return redirect('login')
    student = get_object_or_404(Student, user=request.user)
    courses = student.courses.all()
    chatbots = ChatBot.objects.filter(courses__in=courses, is_active=True).distinct()
    return render(request, 'website/student_dashboard.html', {'chatbots': chatbots})

# ---- ADMIN VIEWS ----

@login_required
def create_professor(request):
    if request.user.role != 'ADMIN': return redirect('login')
    if request.method == 'POST':
        form = ProfessorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Professor cadastrado com sucesso!')
            return redirect('admin_dashboard')
    else:
        form = ProfessorCreationForm()
    return render(request, 'website/form_template.html', {'form': form, 'title': 'Cadastrar Professor'})

@login_required
def create_student(request):
    if request.user.role != 'ADMIN': return redirect('login')
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Aluno cadastrado com sucesso!')
            return redirect('admin_dashboard')
    else:
        form = StudentCreationForm()
    return render(request, 'website/form_template.html', {'form': form, 'title': 'Cadastrar Aluno'})

@login_required
def create_course(request):
    if request.user.role != 'ADMIN': return redirect('login')
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso criado com sucesso!')
            return redirect('admin_dashboard')
    else:
        form = CourseForm()
    return render(request, 'website/form_template.html', {'form': form, 'title': 'Cadastrar Curso'})

@login_required
def enroll_professor(request):
    if request.user.role != 'ADMIN': return redirect('login')
    if request.method == 'POST':
        form = CourseProfessorForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']
            professor = form.cleaned_data['professor']
            course.professors.add(professor)
            messages.success(request, 'Professor vinculado ao curso com sucesso!')
            return redirect('admin_dashboard')
    else:
        form = CourseProfessorForm()
    return render(request, 'website/form_template.html', {'form': form, 'title': 'Vincular Professor ao Curso'})

@login_required
def enroll_student(request):
    if request.user.role != 'ADMIN': return redirect('login')
    if request.method == 'POST':
        form = CourseStudentForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']
            student = form.cleaned_data['student']
            course.students.add(student)
            messages.success(request, 'Aluno matriculado com sucesso!')
            return redirect('admin_dashboard')
    else:
        form = CourseStudentForm()
    return render(request, 'website/form_template.html', {'form': form, 'title': 'Matricular Aluno no Curso'})

# ---- PROFESSOR VIEWS ----

@login_required
def upload_material(request):
    if request.user.role != 'PROFESSOR': return redirect('login')
    professor = get_object_or_404(Professor, user=request.user)
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.professor = professor
            material.file_name = material.file_path.name
            # Extração simulada de texto do material
            material.extracted_text = extract_text(material.file_path)
            material.save()
            messages.success(request, 'Material enviado com sucesso!')
            return redirect('professor_dashboard')
    else:
        form = MaterialForm()
    return render(request, 'website/form_template.html', {'form': form, 'title': 'Upload de Material'})

@login_required
def create_chatbot(request):
    if request.user.role != 'PROFESSOR': return redirect('login')
    professor = get_object_or_404(Professor, user=request.user)
    if request.method == 'POST':
        form = ChatBotForm(request.POST)
        if form.is_valid():
            chatbot = form.save(commit=False)
            chatbot.professor = professor
            chatbot.save()
            messages.success(request, 'ChatBot criado com sucesso!')
            return redirect('professor_dashboard')
    else:
        form = ChatBotForm()
    return render(request, 'website/form_template.html', {'form': form, 'title': 'Criar ChatBot'})

@login_required
def associate_materials(request, chatbot_id):
    if request.user.role != 'PROFESSOR': return redirect('login')
    professor = get_object_or_404(Professor, user=request.user)
    chatbot = get_object_or_404(ChatBot, id=chatbot_id, professor=professor)
    if request.method == 'POST':
        form = ChatBotMaterialForm(request.POST, professor=professor)
        if form.is_valid():
            chatbot.materials.set(form.cleaned_data['materials'])
            messages.success(request, 'Materiais associados com sucesso!')
            return redirect('professor_dashboard')
    else:
        form = ChatBotMaterialForm(professor=professor)
    return render(request, 'website/form_template.html', {'form': form, 'title': f'Associar Materiais ao {chatbot.name}'})

# ---- STUDENT VIEWS ----

@login_required
def chatbot_view(request, chatbot_id):
    if request.user.role != 'STUDENT': return redirect('login')
    student = get_object_or_404(Student, user=request.user)
    chatbot = get_object_or_404(ChatBot, id=chatbot_id)
    
    # Verifica permissão (se o chatbot pertence a algum curso do aluno)
    if not chatbot.courses.filter(id__in=student.courses.all()).exists():
        messages.error(request, 'Você não tem permissão para acessar este ChatBot.')
        return redirect('student_dashboard')

    conversation, created = Conversation.objects.get_or_create(student=student, chatbot=chatbot)
    messages_list = conversation.messages.all().order_by('created_at')

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            # Salvar mensagem do usuário
            Message.objects.create(conversation=conversation, sender_type='USER', content=content)
            
            # Chamada para IA Service (RAG)
            bot_response = generate_answer(content, chatbot)
            
            Message.objects.create(conversation=conversation, sender_type='BOT', content=bot_response)
            return redirect('chatbot_view', chatbot_id=chatbot.id)

    return render(request, 'website/chatbot_view.html', {'chatbot': chatbot, 'messages_list': messages_list})
