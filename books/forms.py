from django import forms
from books.models import Book, User

class NewBookForm(forms.Form):
	
	def check_user(self):
		usernameCollab = self.cleaned_data.get("collaborator")
		username = self.cleaned_data.get("username")
		dbuser = User.objects.filter(username=usernameCollab)
		

		if dbuser==False or dbuser==username:
			return False