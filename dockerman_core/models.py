from django.db import models
import uuid

# Create your models here.
class Server(models.Model):
    name = models.CharField(max_length=255)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    ssh_key = models.CharField(
        max_length=3000,
        default=None,
        null=True,
        blank=True,
    )
    hostname = models.CharField(
        max_length=255,
        default=None,
        null=True,
        blank=True,
    )
    status =  models.CharField(
        max_length=255,
        default="Inactive",
        null=True,
        blank=True,
    ) 
    last_heartbeat = models.DateTimeField()

    def __str__(self):
        return f"{self.name}"




class DockerContainer(models.Model):
    server = models.ForeignKey(Server,on_delete=models.CASCADE)
    container_id = models.CharField(max_length=1024)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255) 
    created = models.DateTimeField(max_length=255) 
    started = models.DateTimeField(max_length=255) 
    finished = models.DateTimeField(max_length=255) 
    args = models.CharField(max_length=255) 
    port_bindings =models.CharField(max_length=2000)
    mounts =models.CharField(max_length=2000)

    def __str__(self):
        return f"Server: {self.server.name} name:{self.name}"






