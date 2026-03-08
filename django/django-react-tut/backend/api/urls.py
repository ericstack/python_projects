from django.urls import path
from . import views
urlpatterns = [
    path("notes/", views.NoteListCreateView.as_view(), name="note-list-create"),
    path("notes/<int:pk>/delete/", views.NoteDelete.as_view(), name="note-delete"),
]