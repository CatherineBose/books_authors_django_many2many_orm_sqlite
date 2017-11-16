from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
  name = models.CharField(max_length=255)
  desc = models.TextField(default='No description')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __repr__(self):
      return "Book Object :: \n Name:{} \n Description : {}".format(self.name, self.desc)
class Author(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  notes = models.TextField(default='No notes for now')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  books = models.ManyToManyField(Book, related_name="authors")
  def __repr__(self):
      return "Author object:: \nfirst_name:{} \n last_name:  {} ".format(self.first_name, self.last_name)

'''
from apps.library.models import *
Book.objects.create(name="C sharp", desc="C sharp is a OOP language")
Book.objects.create(name="Python", desc="Python is a OOP language")
Book.objects.create(name="Java", desc="Java is a OOP language")
Book.objects.create(name="Ruby", desc="Ruby is a OOP language")
Book.objects.create(name="Swift", desc="Ruby is a OOP language")

Author.objects.create(first_name="Jaden", last_name="Jade", email="jjade@gmail.com",books = book1)
Traceback (most recent call last):
ValueError: "Author object:: Jaden Jade " needs to have a value for field "author" before this many-to-many relationship can be used.

Author.objects.create(first_name="Jaden", last_name="Jade", email="jjade@gmail.com
Author.objects.create(first_name="Jessica", last_name="Simpson", email="jessi@gmail.com")
Author.objects.create(first_name="Jacklyn", last_name="Fernandez", email="jacklyn@gmail.com")
Author.objects.create(first_name="Joshua", last_name="Seeps", email="josh@gmail.com")
Author.objects.create(first_name="Mary", last_name="Ann", email="mAnn@gmail.com")
# Binding statement
Author.objects.get(id = 1).books.add(Book.objects.get(id=1))
book1 = Book.objects.get(id=1)
book2 = Book.objects.get(id=2)
book3 = Book.objects.get(id=3)
book4 = Book.objects.get(id=4)
book5 = Book.objects.get(id=5)
author1 = Author.objects.get(id=1)
author2 = Author.objects.get(id=2)
author3 = Author.objects.get(id=3)
author4 = Author.objects.get(id=4)
author5 = Author.objects.get(id=5)
author2.books.add(book5)
author2.books.add(book1)
author2.books.add(book3)
author3.books.add(book3)
author3.books.add(book1)
author3.books.add(book2)


-----
Change the first_name of the 5th author to Ketul
author5 = Author.objects.get(id=5)
author5.first_name ="Ketul"
print author5.first_name
Ketul
----------
Assign the first author to the first 2 books
author1 = Author.objects.get(id=1)
author1.books.add(book1,book2)
author1.books.all()
<QuerySet [Book Object ::
 Name:C sharp
 DescriptionC sharp is a OOP language, Book Object ::
 Name:Python
 DescriptionPython is a OOP language]>

--------
Assign the second author to the first 3 books
author2 = Author.objects.get(id=2)
book1 = Book.objects.get(id=1)
book2 = Book.objects.get(id=2)
book3 = Book.objects.get(id=3)
author2.books.add(book1, book2,book3)
author2.books.all()
<QuerySet [Book Object ::
 Name:C sharp
 DescriptionC sharp is a OOP language, Book Object ::
 Name:Python
 DescriptionPython is a OOP language, Book Object ::
 Name:Java
 DescriptionJava is a OOP language, Book Object ::
 Name:Swift
 DescriptionRuby is a OOP language]>

-----
For the 3rd book, retrieve all the authors
 book3.authors.all()
<QuerySet [Author object::
first_name:Jessica
 last_name:  Simpson , Author object::
first_name:Jacklyn
 last_name:  Fernandez ]>

 ------
Find all the books that the 3rd author is part of
>>> author3 = Author.objects.get(id=3)
>>> author3.books.all()

------
For the 3rd book, remove the first author
book3 = Book.objects.get(id=3)
authorforbook3 = book3.authors.first()
book3.authors.remove(author1ForBook3)
'''