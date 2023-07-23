from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


@login_required
def chat_room(request, room_id):
    try:
    # извлечь обсуждение с заданным id, к которому
    # присоединился текущий пользователь
        room = request.user.rooms_joined.get(id=room_id)
    except:
    # пользователь не является участником обсуждения, либо
    # обсуждение не существует
        return HttpResponseForbidden()
    return render(request, 'chat/room.html', {'room': room})

def forum_pages(request):
    return render(request,
        'chat/forumpages.html',
        {'section': 'forum'})



from .models import Post, Replie, Profile


def forum(request):
    profile = Profile.objects.all()
    if request.method=="POST":
        user = request.user
        image = request.user.profile.image
        title = request.POST.get('title')
        content = request.POST.get('content','')
        post = Post(user=user, post_title=title, post_content=content, image=image)
        post.save()
        alert = True
        return render(request, "chat/forum.html", {'alert':alert})
    posts = Post.objects.filter().order_by('-timestamp')
    return render(request, "chat/forum.html", {'posts':posts})


def discussion(request, myid):
    post = Post.objects.filter(id=myid).first()
    replies = Replie.objects.filter(post=post)
    if request.method == "POST":
        user = request.user
        image = request.user.profile.image
        desc = request.POST.get('desc', '')
        post_id = request.POST.get('post_id', '')
        reply = Replie(user=user, reply_content=desc, post=post, image=image)
        reply.save()
        alert = True
        return render(request, "chat/room.html", {'alert': alert, 'post': post, 'replies': replies})
    return render(request, "chat/room.html", {'post': post, 'replies': replies})

#
# from django.views.generic.edit import FormView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import DiscussionJoinForm
# from django.urls import reverse_lazy
#
# class JoinRoomView(LoginRequiredMixin, FormView):
#     room = None
#     form_class = DiscussionJoinForm
#     def form_valid(self, form):
#         self.room = form.cleaned_data['room']
#         self.room.participants.add(self.request.user)
#         return super().form_valid(form)
#     def get_success_url(self):
#         return reverse_lazy('room_detail',
#                             args=[self.room.id])


# class CourseDetailView(DetailView):
#     model = Discussion
#     template_name = 'courses/course/detail.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['enroll_form'] = CourseEnrollForm(
#                 initial={'course':self.object})
#     return context