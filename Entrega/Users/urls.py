from django.urls import path
from Users.views import login_view, signup, update_user,update_profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
        path('login/', login_view, name = 'login'),
        path('logout/', LogoutView.as_view(template_name = 'Users/logout.html')),
        path('signup/', signup, name = 'signup'),
        path('update/', update_user, name='update'),
        path('update/profile', update_profile, name='update_profile')
]