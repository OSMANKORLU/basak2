from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.urls import reverse



class Home (models.Model):
	user = models.ForeignKey('auth.User',verbose_name='Yazar', on_delete=models.CASCADE, related_name='home')
	title = models.CharField(max_length=120, verbose_name='Başlık')
	category = models.CharField(max_length=120, verbose_name='Kategori',null=True)
	content = RichTextField(verbose_name='İçerik')
	publishing_date = models.DateTimeField(verbose_name='Yayımlanma Tarihi',auto_now_add=True)
	image = models.ImageField(null=True, blank=True)
	slug = models.SlugField(unique=True, editable=False, max_length=130)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('home:detail',kwargs={'slug':self.slug})

	def get_create_url(self):
		return reverse('home:create')

	def get_update_url(self):
		return reverse('home:update',kwargs={'slug':self.slug})

	def get_delete_url(self):
		return reverse('home:delete',kwargs={'slug':self.slug})

	def get_unique_slug(self):
		slug = slugify (self.title.replace('ı','i'))
		uniqu_slug = slug
		counter = 1
		while Home.objects.filter (slug=uniqu_slug).exists():
			uniqu_slug = '{}-{}'.format(slug,counter)
			counter += 1
		return uniqu_slug

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self.get_unique_slug()
		return super(Home, self).save(*args, **kwargs)

	class Meta:
		ordering = ['-publishing_date']



class Welcome (models.Model):
	user = models.ForeignKey('auth.User',verbose_name='Yazar', on_delete=models.CASCADE, related_name='welcome')
	title = models.CharField(max_length=120, verbose_name='Başlık')
	category = models.CharField(max_length=120, verbose_name='Kategori',null=True)
	content = RichTextField(verbose_name='İçerik')
	publishing_date = models.DateTimeField(verbose_name='Yayımlanma Tarihi',auto_now_add=True)
	image = models.ImageField(null=True, blank=True)
	slug = models.SlugField(unique=True, editable=False, max_length=130)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('home:detail',kwargs={'slug':self.slug})

	def get_create_url(self):
		return reverse('home:create')

	def get_update_url(self):
		return reverse('home:update',kwargs={'slug':self.slug})

	def get_delete_url(self):
		return reverse('home:delete',kwargs={'slug':self.slug})

	def get_unique_slug(self):
		slug = slugify (self.title.replace('ı','i'))
		uniqu_slug = slug
		counter = 1
		while Welcome.objects.filter (slug=uniqu_slug).exists():
			uniqu_slug = '{}-{}'.format(slug,counter)
			counter += 1
		return uniqu_slug

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = self.get_unique_slug()
		return super(Welcome, self).save(*args, **kwargs)

	class Meta:
		ordering = ['-publishing_date']


