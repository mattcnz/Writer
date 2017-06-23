from django.shortcuts import render
from books.models import Book, User, Library
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from datetime import datetime
from django.utils import timezone
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from books.forms import NewBookForm


##Homepage
def directory(request):

	if request.user.is_authenticated:
		return render(request, 'directory.html', {'books' : request.user.books.all})
	else:
		return render(request, 'directory.html')

##Show some misc info, some tables with all data
def display_some_info(request):
	libraries = Library.objects.all()
	books = Book.objects.all()
	users = User.objects.all()

	return render(request,  'info.html', {'books' : books, 'users' : users, 'libraries':libraries})


##Show a book
def book_viewer(request, id):

	#Retrieve the book in question
	obj = Book.objects.get(id=id)

	#Figure out how long is left for that book
	timeleft = timezone.now() - obj.created_at
	seconds = (obj.time_total) - timeleft.seconds
	periodsleft, timeleft_in_period =  divmod(seconds, obj.timePeriod) 

	#Edge case for timeleft where we're checking right on 00
	if timeleft_in_period == 0:
		timeleft_in_period = obj.timePeriod

	#Get the book obj and return it in the response.
	if request.method != 'POST' and request.user.id == obj.author_id:
		obj = Book.objects.get(id=id)
		return render(request, 'home.html', {'book' : obj, 'id' : id, 'seconds' : seconds, 'timeleft_in_period' : timeleft_in_period})

	#If the book is finished, save it, make it so user can copy/paste. 
	if request.POST.get("finished", "") == 'true':
		updated = request.POST.get("writing", "")
		obj = Book.objects.get(id=id)
		obj.content = updated
		obj.is_finished =  True
		obj.save()
		return render(request, 'home.html', {'book' : obj, 'id' : id, 'seconds' : seconds, 'timeleft_in_period' : timeleft_in_period})

	#If all else fails (ie they're trying to access the wrong book), send them to the home page.
	else:
		return render(request, 'directory.html')



#Get the book, make it non-editable and destroy the user's hard work.
def out_of_time(request, id):
	obj = Book.objects.get(id=id)
	obj.content = 'Uh oh! Your book was deleted because you ran out of time'
	obj.editable = False
	obj.out_of_time = True
	obj.save()
	return HttpResponseRedirect('/book_viewer/'+str(id)+'/')

#Create a new book and then redirect the user to said book.
def new_book_bs(request):
	title = request.POST.get('book_name', '')
	words_pp = int(request.POST.get('words_req', ''))
	words_goal = int(request.POST.get('words_total', ''))
	time_period_h = int(request.POST.get('hours', ''))
	time_period_m = int(request.POST.get('minutes', ''))

	time_period_s = time_period_m*60 + time_period_h*60*60

	time_total = (words_goal / words_pp ) * time_period_s

	newBook = Book.objects.create(title=title, author=request.user, content='Your New Book', goal=words_goal, wordsPerPeriod=words_pp, timePeriod=time_period_s,
		time_total = time_total)

	return HttpResponseRedirect('/book_viewer/'+str(newBook.id)+'/')


#Save progress. Need's error handling.
def save_ajax(request, id, new=False):

	updated = request.POST.get("writing", "")
	obj = Book.objects.get(id=id)
	obj.content = updated

	obj.save()
	response = {}
	response['result'] = 'success'
	
	return JsonResponse(response)

