import pytest
from website.models import User, Student, Professor, Course

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(email='test@email.com', password='password123', name='Test User', role='STUDENT')
    assert user.email == 'test@email.com'
    assert user.role == 'STUDENT'
    assert user.check_password('password123')

@pytest.mark.django_db
def test_create_professor():
    user = User.objects.create_user(email='prof@email.com', password='password123', name='Prof', role='PROFESSOR')
    prof = Professor.objects.create(user=user, employee_code='P001')
    assert prof.employee_code == 'P001'
    assert str(prof) == 'Prof (P001)'

@pytest.mark.django_db
def test_create_student():
    user = User.objects.create_user(email='aluno@email.com', password='password123', name='Aluno', role='STUDENT')
    student = Student.objects.create(user=user, registration_number='M001')
    assert student.registration_number == 'M001'
    assert str(student) == 'Aluno (M001)'

@pytest.mark.django_db
def test_create_course():
    course = Course.objects.create(name='Django 101', description='Learn Django')
    assert course.name == 'Django 101'
    assert course.is_active == True
