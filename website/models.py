import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O usuário deve ter um endereço de email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'ADMIN')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    ROLE_CHOICES = [
        ('STUDENT', 'Student'),
        ('PROFESSOR', 'Professor'),
        ('ADMIN', 'Admin'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None  # Remover username, usar apenas email
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, db_index=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, db_index=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'role']

    objects = UserManager()

    def __str__(self):
        return self.email

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    registration_number = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} ({self.registration_number})"

class Professor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professor_profile')
    employee_code = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} ({self.employee_code})"

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    students = models.ManyToManyField(Student, related_name='courses', blank=True)
    professors = models.ManyToManyField(Professor, related_name='courses', blank=True)

    def __str__(self):
        return self.name

class Material(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='materials', db_index=True)
    title = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)
    file_path = models.FileField(upload_to='materials/')
    extracted_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ChatBot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='chatbots', db_index=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    materials = models.ManyToManyField(Material, related_name='chatbots', blank=True)
    courses = models.ManyToManyField(Course, related_name='chatbots', blank=True)

    def __str__(self):
        return self.name

class Conversation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='conversations', db_index=True)
    chatbot = models.ForeignKey(ChatBot, on_delete=models.CASCADE, related_name='conversations', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"Conversation: {self.student.user.name} - {self.chatbot.name}"

class Message(models.Model):
    SENDER_CHOICES = [
        ('USER', 'User'),
        ('BOT', 'Bot'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages', db_index=True)
    sender_type = models.CharField(max_length=20, choices=SENDER_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.sender_type}: {self.content[:50]}"
