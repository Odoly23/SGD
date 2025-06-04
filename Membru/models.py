from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import FileExtensionValidator
from django.views import View
from custom.models import Municipality,AdministrativePost,Village, \
	  Kategoria, Subkategoria, Pozisaun, Status, Year, ActiveManager, SubVillage
from Config.utils import membru_foto

# Create your models here.
class Membru(models.Model):
	id_membru = models.CharField(max_length=10, null=True, verbose_name="ID Membru")
	name = models.CharField(max_length=200, null=True, blank=False, verbose_name="Naran")
	pob = models.CharField(max_length=100, null=True, blank=True, verbose_name="Fatin Moris")
	dob = models.DateField(null=True, blank=True, verbose_name="Data Moris")
	sex = models.CharField(choices=[('Mane','Mane'),('Feto','Feto')], max_length=10, null=True, verbose_name="Sexu")
	pos = models.ForeignKey(Pozisaun, on_delete=models.CASCADE, null=True, verbose_name="Pozisaun")
	cat = models.ForeignKey(Kategoria, on_delete=models.CASCADE, null=True, verbose_name="Kategoria")
	subcat = models.ForeignKey(Subkategoria, on_delete=models.CASCADE, null=True, verbose_name="Grau")
	literaria = models.CharField(max_length=200, null=True, blank=True, verbose_name="Habilitasaun Literaria")
	year = models.ForeignKey(Year, on_delete=models.CASCADE, null=True, verbose_name="Tinan Envolve")
	status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, verbose_name="Status")
	phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Nu. Telfone")
	nu_electoral = models.CharField(max_length=15, null=True, blank=True, verbose_name="Nu. Kartaun Eleitoral")
	municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Municipiu")
	administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Postu Administrativu")
	village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Suku")
	subvillage = models.ForeignKey(SubVillage, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Suku")
	image = models.FileField(upload_to=membru_foto, null=True, blank=True,\
			validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jpeg'])], verbose_name="Imajen")
	is_active = models.BooleanField(default=False)
	datetime = models.DateTimeField(null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	hashid = models.CharField(max_length=32, null=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="membrucreatedby")
	created_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="membruupdatedby")
	update_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="membrudeletedby")
	deleted_at = models.DateTimeField(auto_created=True, null=True, blank=True)

	def __str__(self):
		template = '{0.id_membru} - {0.name}'
		return template.format(self)
	
	def soft_delete(self, user):
		self.deleted_at = str(timezone.now())
		self.deleted_by = user
		self.save()

	def undelete(self):
		self.deleted_at = None
		self.deleted_by = None
		self.save()
		
	def hard_delete(self):
		super().delete()
		
	objects = models.Manager()
	active_objects = ActiveManager()
	
	class Meta:
		verbose_name_plural = "Dadus Membru"

class ControlMembru(models.Model):
	memebru = models.OneToOneField(Membru, on_delete=models.CASCADE, null=True, related_name='controlmembru')
	is_active = models.BooleanField(default=True, null=True)
	is_coloc = models.BooleanField(default=False, null=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="controlcreatedby")
	created_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="controlupdatedby")
	update_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="controldeletedby")
	deleted_at = models.DateTimeField(auto_created=True, null=True, blank=True)

	def __str__(self):
		template = '{0.memebru.name}'
		return template.format(self)
	
	def soft_delete(self, user):
		self.deleted_at = str(timezone.now())
		self.deleted_by = user
		self.save()

	def undelete(self):
		self.deleted_at = None
		self.deleted_by = None
		self.save()
		
	def hard_delete(self):
		super().delete()
		
	objects = models.Manager()
	active_objects = ActiveManager()
	
	class Meta:
		verbose_name_plural = "Dadus Controlo Membru"


class MembruUser(models.Model):
	membru = models.OneToOneField(Membru, on_delete=models.CASCADE, related_name="memeberuser")
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="memusercreatedby")
	created_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="memuserupdatedby")
	update_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="memuserdeletedby")
	deleted_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	
	def __str__(self):
		template = '{0.membru} - {0.user}'
		return template.format(self)
	
	def soft_delete(self, user):
		self.deleted_at = str(timezone.now())
		self.deleted_by = user
		self.save()

	def undelete(self):
		self.deleted_at = None
		self.deleted_by = None
		self.save()
		
	def hard_delete(self):
		super().delete()
		
	objects = models.Manager()
	active_objects = ActiveManager()
	
	class Meta:
		verbose_name_plural = "Dadus User Membru"