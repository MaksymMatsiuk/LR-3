from django.db import models

class Instrument(models.Model):
    INSTRUMENT_TYPES = [
        ("Гітара", "Гітара"),
        ("Фортепіано", "Фортепіано"),
        ("Скрипка", "Скрипка"),
        ("Барабани", "Барабани"),
        ("Флейта", "Флейта"),
    ]
    
    name = models.CharField(max_length=255, verbose_name="Назва")
    description = models.TextField(verbose_name="Опис")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    stock_quantity = models.IntegerField(verbose_name="Кількість на складі")
    instrument_type = models.CharField(max_length=50, choices=INSTRUMENT_TYPES, verbose_name="Тип інструменту")
    photo = models.ImageField(upload_to="instruments/", verbose_name="Фото", blank=True, null=True)
    
    def __str__(self):
        return f"{self.name} ({self.instrument_type})"


class Order(models.Model):
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE, verbose_name="Інструмент")
    quantity = models.IntegerField(verbose_name="Кількість")
    customer_name = models.CharField(max_length=255, verbose_name="Ім'я клієнта")
    customer_email = models.EmailField(verbose_name="Електронна пошта клієнта")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата замовлення")
    
    def __str__(self):
        return f"Замовлення {self.id} - {self.instrument.name} x {self.quantity}"