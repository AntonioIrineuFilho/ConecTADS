from ..models import Comentario
from django.core.exceptions import ValidationError

class Comment:

    @staticmethod
    def createComment(_autor_id, _noticia_id, _conteudo):
        try:
            comment = Comentario(autor_id=_autor_id, noticia_id=_noticia_id, conteudo=_conteudo)
            comment.full_clean()
            comment.save()
            return comment
        except ValidationError as error:
            raise ValidationError(error)
    
    @staticmethod
    def getComments(_noticia_id):
        comments = Comentario.objects.filter(noticia_id=_noticia_id).order_by("-data")
        return list(comments)