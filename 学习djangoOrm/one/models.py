from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    qq = models.CharField(max_length=10)
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    content = models.TextField(null=True)
    score = models.IntegerField(null=True)
    tags = models.ManyToManyField("Tag")

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
