from django.contrib import admin
from django.urls import path, include
from website import views

urlpatterns = [
    path('admin_django/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboards
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('professor/', views.professor_dashboard, name='professor_dashboard'),
    path('student/', views.student_dashboard, name='student_dashboard'),

    # Admin Actions
    path('admin/create_professor/', views.create_professor, name='create_professor'),
    path('admin/create_student/', views.create_student, name='create_student'),
    path('admin/create_course/', views.create_course, name='create_course'),
    path('admin/enroll_professor/', views.enroll_professor, name='enroll_professor'),
    path('admin/enroll_student/', views.enroll_student, name='enroll_student'),

    # Professor Actions
    path('professor/upload_material/', views.upload_material, name='upload_material'),
    path('professor/create_chatbot/', views.create_chatbot, name='create_chatbot'),
    path('professor/chatbot/<uuid:chatbot_id>/associate_materials/', views.associate_materials, name='associate_materials'),

    # Student Actions
    path('student/chatbot/<uuid:chatbot_id>/', views.chatbot_view, name='chatbot_view'),
]
