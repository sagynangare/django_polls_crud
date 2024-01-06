from django.urls import path
from . import views

urlpatterns=[
	path("", views.index, name='index'),
	path("<int:question_id>/",views.detail, name="detail"),
	path("<int:question_id>/votes/", views.vote, name="vote"),
	path("add_question/",views.add_question, name="add_question"),
	path("<int:question_id>/add_choice/", views.add_choice, name="add_choice"),
]