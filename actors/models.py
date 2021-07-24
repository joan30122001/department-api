from django.db import models
from django.db.models.fields import CharField
from users.models import User

# Create your models here.

class Niveau(models.Model):

    NIVEAU_CHOICES = (
        (INFOL1, 'INFOL1'),
        (INFOL2, 'INFOL2'),
        (INFOL3, 'INFOL3'),
        (INFO_M1, 'INFO_M1'),
        (INFO_M2, 'INFO_M2'),
        (ICTL1, 'ICTL1'),
        (ICTL2, 'ICTL2'),
        (ICTL3, 'ICTL3'),
        (MASTER_PRO, 'MASTER_PRO')
    )

    level = models.CharField(max_length=10, choices=NIVEAU_CHOICES, default='INFOL1')



class Etudiant(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length=250, unique=True)
    telephone = models.CharField(max_length = 9)
    matricule = models.CharField(max_length = 7)
    Niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)



class Ue(models.Model):
    code = models.CharField(max_length=255)
    intitule = models.CharField(max_length = 255)



class Enseignant(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length=250, unique=True)
    telephone = models.CharField(max_length = 9)
    type = models.CharField(max_length = 255)
    jury = models.CharField(max_length = 10, null = True)



class Enseignement(models.Model):
    ue = models.ForeignKey(Ue, on_delete=models.CASCADE)
    enseignant = models.ForeignKey(Enseignant, on_delete=models.CASCADE)
    annee = models.IntegerField()



class Requete(models.Model): 

    ATTACHMENT_CHOICES = (
        ('pdf', 'Pdf'),
        ('image', 'Image'),
    )

    contenu = models.TextField()
    type_fichier = models.FileField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    update_at = models.DateField(auto_now=False, auto_now_add=False) 
    status = models.CharField(max_length = 255)  
