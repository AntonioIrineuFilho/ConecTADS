from django.core.exceptions import ValidationError
from ..models import Noticia


class News:

    @staticmethod
    def createNews(_autor_id, _edicao_id, _titulo, _conteudo):
        try:
            news = Noticia(autor_id=_autor_id, edicao_id=_edicao_id, titulo=_titulo, conteudo=_conteudo)
            news.full_clean()
            news.save()
            return news
        except ValidationError as error:
            raise ValidationError(error)

    @staticmethod
    def getNews(_edicao_id):
        news = Noticia.objects.filter(edicao_id=_edicao_id)
        return list(news)
    
    @staticmethod
    def getOne(news_id):
        try:
            return Noticia.objects.get(id=news_id)
        except Noticia.DoesNotExist as error:
            raise ValueError(error)