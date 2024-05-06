from django.urls import path
from . import views

urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name='note-list'),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name='delete-note'),
]

# for every route that did not specifie in /backend/backend/urls.py,
# e.g., additional operations, functions, by defining in this file,
# the backend can resolve the requested url and map to the function