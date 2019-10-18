from django.db import models
from django.urls import reverse
import uuid
from datetime import date
from django.contrib.auth.models import User


class Book(models.Model):
    """Model represent a book"""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summery = models.TextField(max_length=1000, help_text="Enter detail of a book")
    isbn = models.CharField('ISBN', max_length=13, help_text="13 charecter isbn number.")
    genre = models.ManyToManyField('Genre', help_text="Select a genre.")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """Representing the model object"""
        self.title
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    """Model represnt a specific copy of book"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='unique id')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprient = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Availble'),
        ('r', 'Resserve'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availablity',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """Representing the model object"""
        return f' {self.id} ({self.book.title}) '


class Author(models.Model):
    """Representing a author."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['first_name', 'last_name']
    
    def get_asoulate_url(self):
        return reverse('author-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Genre(models.Model):
    """this model represent a book genre"""
    name = models.CharField(max_length=200, help_text="Enter a book genre")

    def __str__(self):
        """string for representing the model object"""
        return self.name


class Language(models.Model):
    """Represent the book language"""
    name = models.CharField(max_length=100, help_text="book language.")

    def __str__(self):
        return self.name