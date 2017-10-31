from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return "{}:({})".format(self.name, self.age)

    def my_property(self):
        return self.name + " haha"

    #用来显示非字段内容
    my_property.short_description = "Full name of the person"
    full_name = property(my_property)