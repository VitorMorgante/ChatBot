import pytest
from django.urls import reverse
from website.models import User

@pytest.mark.django_db
def test_login_view_get(client):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_login_view_post_success(client):
    User.objects.create_user(email='test@email.com', password='password123', name='Test User', role='STUDENT')
    url = reverse('login')
    response = client.post(url, {'username': 'test@email.com', 'password': 'password123'})
    assert response.status_code == 302
    assert response.url == reverse('student_dashboard')

@pytest.mark.django_db
def test_admin_dashboard_access_denied(client):
    User.objects.create_user(email='test@email.com', password='password123', name='Test User', role='STUDENT')
    client.login(username='test@email.com', password='password123')
    url = reverse('admin_dashboard')
    response = client.get(url)
    # STUDENT tries to access ADMIN dashboard
    assert response.status_code == 302
    assert response.url == reverse('login')

@pytest.mark.django_db
def test_admin_dashboard_access_granted(client):
    User.objects.create_user(email='admin@email.com', password='password123', name='Admin', role='ADMIN')
    client.login(username='admin@email.com', password='password123')
    url = reverse('admin_dashboard')
    response = client.get(url)
    assert response.status_code == 200
