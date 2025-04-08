from django.db import models

class Table(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)  # Например, "Table 1"
    seats = models.IntegerField()  # Количество мест
    location = models.CharField(max_length=100, null=True, blank=True)  # Например, "зал у окна", "терраса"

    def __str__(self):
        return self.name


class Reservation(models.Model):
    customer_name = models.CharField(max_length=50, null=True, blank=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reservations')
    reservation_time = models.DateTimeField()
    duration_minutes = models.IntegerField()

    def __str__(self):
        return f'{self.customer_name} — {self.table.name} в {self.reservation_time}'
