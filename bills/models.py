from django.db import models


class Bill(models.Model):
    """ Модель счета """
    client_name = models.CharField(max_length=128, blank=False, null=False)
    client_org = models.CharField(max_length=256, blank=False, null=False)
    bill_number = models.IntegerField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    sum = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    service = models.TextField(blank=False)

    def __str__(self):
        return f"{self.client_name} - {self.client_org}"
