from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


class Edicao(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="edicoes_criadas")
    data = models.DateField(unique=True)

    class Meta:
        verbose_name_plural = "Edicoes"

    def clean(self):
        super().clean()
        if (self.data > timezone.localdate()):
            raise ValidationError("A data da edição não pode ser posteiror à atual.")

    def __str__(self):
        return f'{self.data}'

class Noticia(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="noticias_criadas_autor")
    edicao = models.ForeignKey(Edicao, on_delete=models.CASCADE, related_name="noticias_criadas_edicao")
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()

    def clean(self):
        super().clean()
        if (len(self.titulo) < 10):
            raise ValidationError("O título da notícia deve possuir no mínimo 10 caracteres.")
        if (len(self.titulo) > 255):
            raise ValidationError("O título da notícia não deve possuir mais do que 255 caracteres.")
        if (len(self.conteudo) < 100):
            raise ValidationError("O conteúdo da notícia deve possuir no mínimo 100 caracteres.")

    def __str__(self):
        titulo = self.titulo
        if (len(titulo) > 45):
            titulo = f'{titulo[:45]}...'
        return titulo

class Comentario(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comentarios_criados_autor")
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE, related_name="comentarios_criados_noticia")
    data = models.DateTimeField(auto_now_add=True)
    conteudo = models.TextField()

    def clean(self):
        super().clean()
        if (not self.conteudo or self.conteudo.isspace()):
            raise ValidationError("O comentário não pode estar vazio.")

    def __str__(self):
        return f'{self.autor.username} - {self.data}'
