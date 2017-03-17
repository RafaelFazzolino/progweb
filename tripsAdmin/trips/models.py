from django.db import models

# Create your models here.
class Trip(models.Model):
    title = models.CharField('Nome', max_length=40)
    slug = models.SlugField()
    description = models.TextField('Descrição')
    date = models.DateField('Data')
    image = models.ImageField(upload_to='trips/images', verbose_name='Imagem', null=True, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)#Atualiza sempre que for criado
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('trips:details', (), {'slug':self.slug})

    class Meta:
        #Fazer com que o django trabalhe com singular e plural e jogo
        verbose_name = 'Viagem'
        verbose_name_plural = 'Viagens'

        #Ordenar por nome na listagem
        ordering = ['title'] #Descrescente é só -name
