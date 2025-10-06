from django.db import models

class Library(models.Model):
  title = models.CharField(max_length=20)
  author = models.CharField(max_length=20)
  publish_date = models.IntegerField(max_length=10)
  borrowed = models.BooleanField(default=False)

  def __str__(self):
    return self.title
  

class UserBook(models.Model):
  user = models.ForeignKey("user.User", related_name="borrowed_books", on_delete=models.CASCADE)
  book = models.ForeignKey(Library, related_name="borrowers", on_delete=models.CASCADE)
  returned = models.BooleanField(default=False)

