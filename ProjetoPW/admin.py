from django.contrib import admin
from .models import Usuario
from .models import Usuario, Quiz, Pergunta, Resposta, Resultados


# Register your models here.
admin.site.register(Usuario)
admin.site.register(Quiz)
admin.site.register(Resultados)

class RespostaInline(admin.TabularInline):
    model = Resposta

class PerguntaAdmin(admin.ModelAdmin):
    inlines = [RespostaInline]

admin.site.register(Pergunta, PerguntaAdmin)
admin.site.register(Resposta)