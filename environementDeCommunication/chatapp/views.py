from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room,Message
from .forms import RoomForm
from django.shortcuts import render, redirect, get_object_or_404

def rooms(request):
    if request.method == 'GET':
        rooms=Room.objects.all()
        return render(request, "rooms.html",{"rooms":rooms})

def room(request,id_room):
    room_name=Room.objects.get(id=id_room).name     
    messages=Message.objects.filter(room=Room.objects.get(id=id_room))    
    return render(request, "room.html",{"room_name":room_name,"id_room":id_room,'messages':messages})


@login_required
def room_group(request,id_room, group_id):
    var = group_id
    room = Room.objects.get(id=id_room ,group_id = group_id).id
    room_name = Room.objects.get(id=id_room ,group_id = group_id).name    
    messages = Message.objects.filter(room=room)
    return render(request, 'room.html', {"room":room,"id":id,'messages':messages , 'var':var, 'room_name':room_name})


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RoomForm

@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.admin = request.user
            room.save()
            return redirect('chatapp:rooms')  
    else:
        form = RoomForm()

    return render(request, "create_room.html", {'form': form})


@login_required
def update_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('chatapp:rooms')  # Change 'room_list' to your desired URL name
    else:
        form = RoomForm(instance=room)

    return render(request, "update_room.html", {'form': form, 'room': room})

@login_required
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id, admin=request.user)
    print(room)

    if request.method == 'POST':
        room.delete()
        return redirect('chatapp:rooms')  # Change 'room_list' to your desired URL name

    return render(request, 'delete_room.html', {'room': room})