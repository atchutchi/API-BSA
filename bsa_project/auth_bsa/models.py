from django.db import models
from django.conf import settings

class Domain(models.Model):
    # O nome do domínio, como 'example.gw'
    name = models.CharField(max_length=255, unique=True)
    # Status do domínio, pode ser 'ativo', 'bloqueado', etc.
    status = models.CharField(max_length=50)
    # Data de criação do domínio
    created_at = models.DateTimeField(auto_now_add=True)
    # Data da última atualização do domínio
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class BlockOrder(models.Model):
    # Relacionamento com o usuário que criou a ordem de bloqueio
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # Relacionamento com o domínio a ser bloqueado
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    # Razão para o bloqueio
    reason = models.TextField()
    # Data de criação da ordem de bloqueio
    created_at = models.DateTimeField(auto_now_add=True)
    # Indica se a ordem está ativa ou foi revogada
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Block Order for {self.domain.name} by {self.user.username}"

class Report(models.Model):
    # Relacionamento com o domínio reportado
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    # Detalhes do relatório
    details = models.TextField()
    # Data de criação do relatório
    created_at = models.DateTimeField(auto_now_add=True)
    # Indica se o relatório foi resolvido
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Report for {self.domain.name}"

