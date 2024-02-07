from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model

User = get_user_model()

class Service(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class ContenuService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class Subject(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Formation(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='formation/')
    description = models.TextField()
    avantage = models.TextField()
    certification = models.TextField()
    auteur = models.CharField(max_length=100)
    duree = models.CharField(max_length=100)
    prix = models.CharField(max_length=100)
    souscrire = models.ManyToManyField(User, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class Domaine(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Emploi(models.Model):
    domaine = models.ForeignKey(Domaine, on_delete=models.SET_NULL, null=True)
    poste = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='emploi/')
    entreprise = models.CharField(max_length=100)
    lieu = models.CharField(max_length=100)
    description = models.TextField()
    tache = models.TextField()
    competence = models.TextField()
    postuler = models.ManyToManyField(User)
    cloture = models.DateField()
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.poste

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.poste)
        super().save(*args, **kwargs)


class Plateforme(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


LIVRAISON = (
    ('en cours', 'En cours'),
    ('livré', 'Livré'),
)

class Achat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plateforme = models.ForeignKey(Plateforme, on_delete=models.SET_NULL, null=True)
    lien = models.CharField(max_length=300)
    adresse = models.CharField(max_length=200)
    livraison = models.CharField(choices=LIVRAISON, default='en cours', max_length=15)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.plateforme}: {self.lien}'
