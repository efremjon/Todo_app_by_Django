from contextlib import nullcontext
from distutils.command.upload import upload
from django.db import models
from ckeditor.fields import RichTextField

class Cataory(models.Model):
    name=models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.name
class Coures(models.Model):
    cours_name=models.CharField(max_length=300)
    img=models.ImageField(upload_to='pics')
    catagory=models.ForeignKey(Cataory,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.cours_name
class Tutoris(models.Model):
    cours=models.ForeignKey(Coures,on_delete=models.CASCADE)
    titel=models.CharField(max_length=300)
    def __str__(self) -> str:
        return self.titel + '|' + str(self.cours)
class Bodycors(models.Model):
    select_cours=models.ForeignKey(Coures,on_delete=models.CASCADE)
    select_titel=models.ForeignKey(Tutoris,on_delete=models.CASCADE)
    body=RichTextField(blank=True,null=True)
    def __str__(self) -> str:
        return str(self.select_titel)+ '|' + str(self.select_cours)

