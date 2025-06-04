from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(delete_at__isnull=True)

class Pozisaun(models.Model):
	name = models.CharField(max_length=200, null=True, blank=False)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Pozisauncreatedby")
	created_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Pozisaunupdatedby")
	update_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Pozisaundeletedby")
	deleted_at = models.DateTimeField(auto_created=True, null=True, blank=True)

	def __str__(self):
		template = '{0.name}'
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
		verbose_name_plural = "Dadus Pozisaun"
	
class Kategoria(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Kategoriacreatedby")
	created_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Kategoriaupdatedby")
	update_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Kategoriadeletedby")
	deleted_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	def __str__(self):
		template = '{0.name}'
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
		verbose_name_plural = "Dadus Kategoria"

class Subkategoria(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Subkategoriacreatedby")
	created_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Subkategoriaupdatedby")
	update_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Subkategoriadeletedby")
	deleted_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	def __str__(self):
		template = '{0.name}'
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
		verbose_name_plural = "Dadus SubKategoria"
	
class Status(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Statuscreatedby")
	created_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Statusupdatedby")
	update_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Statusdeletedby")
	deleted_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	def __str__(self):
		template = '{0.name}'
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
		verbose_name_plural = "Dadus Status"
	

class Municipality(models.Model):
	code = models.CharField(max_length=5, null=True)
	name = models.CharField(max_length=50, verbose_name="Naran")
	hckey = models.CharField(max_length=10, null=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Municipalitycreatedby")
	created_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Municipalityupdatedby")
	update_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Municipalitydeletedby")
	deleted_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	def __str__(self):
		template = '{0.name}'
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
		verbose_name_plural = "Dadus Munisipiu"

class AdministrativePost(models.Model):
	municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, null=True)
	name = models.CharField(max_length=100, verbose_name="Naran")
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Administrativeposcreatedby")
	created_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Administrativeposupdatedby")
	update_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Administrativeposdeletedby")
	deleted_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	def __str__(self):
		template = '{0.name}'
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
		verbose_name_plural = "Dadus Postu"

class Village(models.Model):
	administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE, null=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Villagecreatedby")
	created_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Villageupdatedby")
	update_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Villagedeletedby")
	deleted_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	name = models.CharField(max_length=100, verbose_name="Naran")
	
	def __str__(self):
		template = '{0.name}'
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
		verbose_name_plural = "Dadus Suku"

class SubVillage(models.Model):
	village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True)
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Subvillagecreatedby")
	created_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Subvillageupdatedby")
	update_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Subvillagedeletedby")
	deleted_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	name = models.CharField(max_length=100)
	def __str__(self):
		template = '{0.name}'
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
		verbose_name_plural = "Dadus Aldeia"

	
class Year(models.Model):
	name = models.CharField(max_length = 50 ,verbose_name='Tinan')
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Yearcreatedby")
	created_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Yearupdatedby")
	update_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Yeardeletedby")
	deleted_at = models.DateTimeField(auto_created=True, null=True, blank=True)
	def __str__(self):
		template = '{0.name}'
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
		verbose_name_plural = "Dadus Tinan"
