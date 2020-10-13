from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from student.models import Posts, Topics, Categories
from student.forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def community(request):
    categories = Categories.objects.all()
    topics = Topics.objects.all().order_by('-topic_posts')
    posts = Posts.objects.all()
    return render(request, 
                    'community/latest.html', 
                    {
                        'categories': categories,
                        'topics': topics,
                        'posts': posts
                    }
                )

# This view is for topic.html page which shows a particular thread
def topic(request, pk):
    if request.method == 'POST' and request.user.is_anonymous == False:
        topic = Topics.objects.get(pk=pk)
        post_content = request.POST.get('content')
        post_by = request.user
        post_topic = topic
        post = Posts.objects.create(post_content=post_content, post_by=post_by, post_topic=post_topic)
        topic.topic_posts += 1
        topic.save()
        post.save()
        return redirect('showTopic', topic.pk)
    topic = Topics.objects.get(pk=pk)
    posts = Posts.objects.filter(post_topic=topic).order_by('-post_date')
    form = PostForm()
    return render(request, 'community/topic.html', {'topic': topic, 'posts': posts, 'form': form})

# This view is for forumList.html which shows all threads available
def topicList(request):
    forums_list = Topics.objects.all().order_by('-topic_date')
    page = request.GET.get('page')
    paginator = Paginator(forums_list, 7)
    forums = paginator.get_page(page)
    return render(request, 'community/forumList.html', {'forums': forums})


def createTopic(request):
    if request.method == 'POST':
        topic_content = request.POST.get('content')
        topic_by = request.user
        topic_name = request.POST.get('name')
        topic_cat = request.POST.get('cat')
        cat = Categories.objects.get(cat_name=topic_cat)
        topic = Topics.objects.create(topic_desc=topic_content, topic_by=topic_by, topic_name=topic_name, topic_cat=cat)
        cat.cat_topics += 1
        cat.save()
        topic.save()
        return redirect('threads')
    cats = Categories.objects.all()
    return render(request, 'community/createTopic.html', {'cats': cats})

def search(request):
    return HttpResponse("Hello Forum")

#  Forum Suggestions Views
def suggestions(request):
    return HttpResponse("Hello Forum")

# Forum Members Views
def members(request):
    return HttpResponse("Hello Forum")
