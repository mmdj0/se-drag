from django.shortcuts import render, get_object_or_404, redirect
from .models import Group
from .forms import GroupForm
 

def details_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    groups = Group.objects.all()
    context = {"group": group, "group_html": groups}
    return render(request, "groups/group_detail.html", context)
#creation / modification / supression d'un groupe



def create_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.admin = request.user
            group.save()
            form.save_m2m()
            # Redirect to the group list page
            return redirect('groups:group_list')
    else:
        form = GroupForm()

    return render(request, "groups/create_group.html", {'form': form})




# groups/views.py
from django.shortcuts import render
from .models import Group

def groups_list(request):
    groups = Group.objects.all()
    return render(request, "groups/group_list.html", {'groups': groups})


# groups/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Group
from .forms import GroupForm

def update_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            group = form.save(commit=False)
            group.admin = request.user
            group.save()
            form.save_m2m()
            return redirect('groups:group_detail', group_id=group.id)
    else:
        form = GroupForm(instance=group)

    return render(request, "groups/update_group.html", {'form': form, 'group': group})



# groups/views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Group

@require_POST
def delete_group(request):
    group_id = request.POST.get('group_id')
    try:
        group = get_object_or_404(Group, id=group_id)
        group.delete()
        return JsonResponse({'message': 'Group deleted successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

from django.shortcuts import render
from django.views import View
# views.py



class GroupChatView(View):
    template_name = 'groups/group_chat.html'

    def get(self, request, *args, **kwargs):
        group_id = kwargs.get('group_id')
        print("Group ID:", group_id)  # Check if group_id is being printed in the console
        return render(request, self.template_name, {'group_id': group_id})
    

def group_chats(request):
    if request.method == 'GET':
        group_chats=Group.objects.all()
        return render(request, "groups/group_chats.html",{"group_chats":group_chats})
