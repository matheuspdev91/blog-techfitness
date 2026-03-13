from django import template
import math


register = template.Library()

@register.filter
def tempo_leitura(texto):
    if not texto:
        return "1 min de leitura"
    
    palavras = len(texto.split())
    minutos = math.ceil(palavras / 200) 
    return f"{minutos} min de leitura"