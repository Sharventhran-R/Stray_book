from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def search(request):
	title = 'Results'
	form = InfoSearchForm(request.POST or None)
	queryset = Info.objects.filter(name__icontains=form['name'].value(),
								   animal__icontains=form['animal'].value()
								   )
	context = {
		"title": title,
		"queryset": queryset,
		"form": form,
	}
	# if request.method == 'POST':
	# 	queryset = Info.objects.filter(name__icontains=form['name'].value(),
	# 									  animal__icontains=form['animal'].value()
	# 									  )
	# 	context = {
	# 		"form": form,
	# 		"title": title,
	# 		"queryset": queryset,
	# 	}

	return render(request, "search.html", context)

def home(request):
	title = 'Welcome: This is the Home Page'
	context = {
		"title": title,
	}
	return render(request, "home.html", context)

@login_required
def add(request):
	form = InfoForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('/search')
	context = {
		"form": form,
		"title": "New Entry",
	}
	return render(request, "entry.html", context)

@login_required
def update(request, pk):
	queryset = Info.objects.get(number=pk)
	form = InfoUpdateForm(instance=queryset)
	if request.method == 'POST':
		form = InfoUpdateForm(request.POST, instance=queryset)
		if form.is_valid():
			form.save()
			return redirect('/message')

	context = {
		'form': form,
	}
	return render(request, 'entry.html', context)

# @login_required
# def delete(request, pk):
# 	queryset = Info.objects.get(number=pk)
# 	if request.method == 'POST':
# 		queryset.delete()
# 		return redirect('/search')
# 	return render(request, 'delete_info.html')
#
# def message(request):
# 	return render(request, 'message.html')