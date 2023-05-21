from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
from django.conf import settings
from .forms import LoginForm
from django.conf.urls.static import static


urlpatterns = [
    path('files/<slug:val>',views.Course.as_view(),name='files'),
    path('coursetitle/<val>',views.CourseTitle.as_view(),name='course_title'),
    path ('home/',views.home_view,name='home'),
    path ('base/',views.base_view,name='base'),
    path('registration/',views.UserRegistrationView.as_view(),name='registration'),
    path('',auth_view.LoginView.as_view(template_name="app/login.html",authentication_form=LoginForm),name = 'login'),
    path('profile/',views.profile,name='profile'),
    path('notes/',views.notes,name='notes'),
    path('about/',views.about_view,name='about'),
    path('contact/',views.contact_view,name='contact'),
    path('deleteNote/<int:pk>',views.deleteNote,name='delete_note'),
    path('notesDetail/',views.notesDetailView.as_view(),name='notes_detail'),
    path('homework/',views.homework,name='homework'),
    path('search/youtube/<slug:val>',views.youtube,name='youtube'),
    path('update_homework/<int:pk>',views.UpdateHomework,name='update_homework'),
    path('deleteHomework/<int:pk>',views.delete_homework,name='delete_homework'),
    path('todo/',views.todo,name='todo'),
    path('update_todo/<int:pk>',views.update_todo,name='update_todo'),
    path('delete_todo/<int:pk>',views.delete_todo,name='delete_todo'),
    path('books/',views.book,name='books'),
    path('dictionary/',views.dictionary,name='dictionary'),
    path('wiki/',views.wiki,name='wiki')

]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)