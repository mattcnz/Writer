# Writer

clone repository
create virtualenv
pip install -r requirements

and you should be good to go. Comes with a sqlite db, superuser: admin pw: greenapple, users: tony, paulie - password: greenapple (for both)

So this is a simple web app for motivating someone to write. The user chooses a word count goal, how many words they want to write per time period, and a words per time period goal. If they don’t meet the goals, the book gets deleted.

So you have three models - User (built in model), Book, Library. When a user signs in, they hit the directory page. From there, they enter the details of their new book (data is send to view: new_book_bs and a new book with foreign key that user is added to the database, a redirect to book_viewer then fires), or they select a book they’ve already made (request goes straight to book_viewer). When a user runs out of time, a request is sent to the view out_of_time and some of the book objects fields are updated, stopping writing and deleting the book. 

The Library class is something of an afterthought. Book objects can be added to multiple libraries. When you visit /info/ you can see what libraries books are in, as well as a few other things. This was really only added because the email mentioned having a many-to-many relationship in there somewhere (initially I tried making the books many-to-many with users, so that people could collaborate on books. I then used channels to enable “real time” collaboration. This sort of worked, but it was also very broken and I decided to cut my losses and revert back to one user per book. I think I’ll revisit this later though). 

You can add libraries/add books to libraries from the admin panel. 

#Flaws

-The New Book form should probably use django’s forms to validate it’s data.
-The book_viewer page runs the autosave function once every minute, even when nothing as changed. This doesn’t need to happen.
-Inconsistent variable naming standards.
-The user needs to find sufficient motivation to actually write something in the first place, in order to be motivated by the threat of losing their hard work. 
-Someone could just view source and copy from there. 
-User could change javascript variables to cheat. These should be hidden in an external script. 

#Merits

Conceptually intriguing.



