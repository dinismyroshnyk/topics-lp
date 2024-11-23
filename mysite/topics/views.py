from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib import messages
from .models import Topic, Comment
from .forms import CommentForm, TopicForm

def topic_list(request):
    topics = Topic.objects.annotate(
        comment_count=Count('comments')
    ).order_by('-created_at')
    return render(request, 'topics/topic_list.html', {'topics': topics})

def topic_detail(request, topic_id):
    topic = get_object_or_404(Topic.objects.annotate(
        comment_count=Count('comments')), pk=topic_id)
    comments = topic.comments.order_by('created_at')
    comment_form = CommentForm()
    return render(request, 'topics/topic_detail.html', {
        'topic': topic,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def add_comment(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.topic = topic
            comment.save()
            messages.success(request, 'Comment added successfully!')
    return redirect('topic_detail', topic_id=topic.id)

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, 'You can only delete your own comments!')
        return redirect('topic_detail', topic_id=comment.topic.id)

    topic_id = comment.topic.id
    comment.delete()
    messages.success(request, 'Comment deleted successfully!')
    return redirect('topic_detail', topic_id=topic_id)

@login_required
def edit_topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.user != topic.author:
        messages.error(request, 'You can only edit your own topics!')
        return redirect('topic_detail', topic_id=topic.id)

    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            messages.success(request, 'Topic updated successfully!')
            return redirect('topic_detail', topic_id=topic.id)
    else:
        form = TopicForm(instance=topic)
    return render(request, 'topics/edit_topic.html', {'form': form, 'topic': topic})

@login_required
def delete_topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.user != topic.author:
        messages.error(request, 'You can only delete your own topics!')
        return redirect('topic_detail', topic_id=topic.id)

    if request.method == 'POST':
        topic.delete()
        messages.success(request, 'Topic deleted successfully!')
        return redirect('topic_list')
    return render(request, 'topics/delete_topic.html', {'topic': topic})

@login_required
def create_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            messages.success(request, 'Topic created successfully!')
            return redirect('topic_detail', topic_id=topic.id)
    else:
        form = TopicForm()
    return render(request, 'topics/create_topic.html', {'form': form})