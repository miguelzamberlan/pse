from django import template
from django.template.defaultfilters import stringfilter
import locale
from validate_docbr import CPF

register = template.Library()


def maskcpf(value):

    cpf = CPF()

    cpfmascarado = cpf.mask(str(value))

    return str(cpfmascarado)

register.filter("maskcpf", maskcpf)