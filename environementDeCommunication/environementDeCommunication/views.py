from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from accounts.models import User
from posts.models import Post


class DashboardView(LoginRequiredMixin, View):
    login_url = "accounts:signin"
    template_name_admin = "dashbord/dashboard.html"
    template_name_user = "posts/post_list.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            users = User.objects.all()
            print(users)
            print(users.count())
            total_users_count = User.objects.all().count()
            print(total_users_count)
            active_users_count = User.objects.filter(is_active=True).count()
            print(active_users_count)            
            context = {"users": users,"total_users_count":total_users_count,"active_users_count":active_users_count}
            return render(request, "calendarapp/dashboard.html", context) 
        else:
            if request.user.is_authenticated:   
                posts = Post.objects.filter(is_public=True) | Post.objects.filter(author=request.user)
            else:
                posts = Post.objects.filter(is_public=True)                
            return render(request, 'posts/post_list.html', {'posts': posts})
