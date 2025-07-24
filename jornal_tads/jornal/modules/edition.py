from django.core.exceptions import ValidationError
from ..models import Edicao

class Edition:

    @staticmethod
    def createEdition(_autor, _data):
        try:
            ed = Edicao(autor=_autor, data=_data)
            ed.full_clean()
            ed.save()
            return ed
        except ValidationError as error:
            raise ValidationError(error)
    
    @staticmethod
    def getEditions():
        eds = Edicao.objects.all().order_by("-data")
        return list(eds)
    
    @staticmethod
    def getOne(_id):
        try:
            ed = Edicao.objects.get(id=_id)
            return ed
        except Edicao.DoesNotExist as error:
            raise ValueError(error) 



