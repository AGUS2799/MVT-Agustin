from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime, date
from django.template import loader
from app_desafio.models import Integrantes


def integrantes(self, name: str = 'Name', age: int = 'Age', date_of_birth: str = 'date_of_birth'):
    date_of_birth = datetime.strptime(date_of_birth, '%d-%m-%Y')
    
    template = loader.get_template('template.html')

    inte = Integrantes(name=name, age=age, date_of_birth=date_of_birth)
    inte.save()

    context_dict = {
        'integrantes': inte,
    }

    render = template.render(context_dict)
    return HttpResponse(render)
