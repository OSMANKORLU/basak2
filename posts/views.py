from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from .models import Post
from .forms import PostForm,CommentForm
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.db.models import Q 

# Create your views here.

def post_index(request):
	posts=Post.objects.all()


	query = request.GET.get('q')
	if query:
		posts = posts.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)
		).distinct()




	paginator = Paginator(posts, 4)

	sayfa = request.GET.get('sayfa')

	posts = paginator.get_page(sayfa)

	return render(request,'post/index.html',{'posts':posts})


def post_detail(request,slug):
	post = get_object_or_404(Post,slug=slug)

	form = CommentForm(request.POST or None)
	if form.is_valid():
		comment =form.save(commit = False)
		comment.post = post
		comment.save()

		return HttpResponseRedirect(post.get_absolute_url())

	context = {
		'post':post,
		'form':form,
	}
	return render(request,'post/detail.html',context)


def post_create(request):
	if not request.user.is_authenticated:
		raise Http404()


	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		post =form.save(commit = False)
		post.user = request.user
		post.save()

		messages.success(request,'Başarılı Bir şekilde Oluşturdunuz ')
		return HttpResponseRedirect(post.get_absolute_url())

	context = {
		'form':form,
	}

	return render(request,'post/form.html',context)

def post_update(request,slug):

	if not request.user.is_authenticated:
		raise Http404()

	post = get_object_or_404(Post,slug=slug)
	form = PostForm(request.POST or None,request.FILES or None, instance=post)
	if form.is_valid():
		form.save()
		messages.success(request,'Başarılı Bir şekilde güncellediniz ')

		return HttpResponseRedirect(post.get_absolute_url())

	context = {
		'form':form,
	}

	return render(request,'post/form.html',context)	

def post_delete(request,slug):

	if not request.user.is_authenticated:
		raise Http404()

	post = get_object_or_404(Post,slug=slug)
	post.delete()


	return redirect('post:index')