from django.shortcuts import render
from .models import Post
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import BlogPost

# Create your views here.

def blog_list(request):
   post = Post.objects.all()
   context = {

       'blog_list':post
   }
   return render(request, "blog/blog_list.html",context)

def blog_detail(request,id):
    each_post= Post.objects.get(id=id)
    context = {
        'blog_detail':each_post
    }
    return render(request, "blog/blog_detail.html",context)
    

def blog_delete(request,id):
    each_post = Post.objects.get(id=id)
    each_post.delete()
    return HttpResponseRedirect('/posts/')
    
def blog_create(request):
    form= PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/posts/')    
    context = {
        'form':form,
        
    }
    return render(request, "blog/blog_create.html",context)

def blog_update(request,id):
    post = Post.objects.get(id=id)
    form= PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/posts/')    
    context = {
        'form':form,
        'form_type': 'Create'
    }
    return render(request, "blog/blog_create.html",context)







@csrf_exempt
def like_post(request, id):
    if request.method == 'POST':
        try:
            post = BlogPost.objects.get(id=id)
            post.likes += 1
            post.save()
            return JsonResponse({'likes': post.likes, 'dislikes': post.dislikes}, status=200)
        except BlogPost.DoesNotExist:
            return JsonResponse({'error': 'Post not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def dislike_post(request, post_id):
    if request.method == 'POST':
        post = BlogPost.objects.get(id=post_id)
        post.dislikes += 1
        post.save()
        return JsonResponse({'likes': post.likes, 'dislikes': post.dislikes})
