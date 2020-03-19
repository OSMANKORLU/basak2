from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from home.models import Home
from home.models import Welcome

from .forms import HomeForm
from django.core.paginator import Paginator
from django.utils.text import slugify
from django.core.paginator import Paginator
from django.db.models import Q 

# Create your views here.


def welcome_index(request):



	welcome = Home.objects.all()



	return render(request,'home/index.html',{'welcome':welcome})




def welcome_detail(request,slug):
	welcome = get_object_or_404(Welcome,slug=slug)
	'''
		form = CommentForm(request.POST or None)
		if form.is_valid():
			comment =form.save(commit = False)
			comment.home = home
			comment.save()

			return HttpResponseRedirect(home.get_absolute_url())
	'''
	context = {
		'welcome':welcome,
		#'form':form,
	}
	return render(request,'home/welcome_detail.html',context)

def home_index(request):

	welcome = Home.objects.all()
	home=Home.objects.all()


	query = request.GET.get('q')
	if query:
		home = home.filter(
			Q(title__icontains=query)|
			Q(content__icontains=query)
		).distinct()

	paginator = Paginator(home, 4)

	sayfa = request.GET.get('sayfa')

	home = paginator.get_page(sayfa)

	return render(request,'home/index.html',{'home':home, 'welcome': welcome})

def home_detail(request,slug):
	home = get_object_or_404(Home,slug=slug)
	'''
		form = CommentForm(request.POST or None)
		if form.is_valid():
			comment =form.save(commit = False)
			comment.home = home
			comment.save()

			return HttpResponseRedirect(home.get_absolute_url())
	'''
	context = {
		'home':home,
		#'form':form,
	}
	return render(request,'home/detail.html',context)




def home_create(request):
	if not request.user.is_authenticated:
		raise Http404()


	form = HomeForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		home =form.save(commit = False)
		home.user = request.user
		home.save()

		messages.success(request,'Başarılı Bir şekilde Oluşturdunuz ')
		return HttpResponseRedirect(home.get_absolute_url())

	context = {
		'form':form,
	}

	return render(request,'home/form.html',context)



def home_update(request,slug):

	if not request.user.is_authenticated:
		raise Http404()

	home = get_object_or_404(Home,slug=slug)
	form = HomeForm(request.POST or None,request.FILES or None, instance=home)
	if form.is_valid():
		form.save()
		messages.success(request,'Başarılı Bir şekilde güncellediniz ')

		return HttpResponseRedirect(home.get_absolute_url())

	context = {
		'form':form,
	}

	return render(request,'home/form.html',context)	

def home_delete(request,slug):

	if not request.user.is_authenticated:
		raise Http404()

	home = get_object_or_404(Home,slug=slug)
	home.delete()


	return redirect('home:home')
