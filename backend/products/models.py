from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=9.99)

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def __str__(self):
        return f"{self.title}"

    def get_discount(self):
        if len(self.title) > 10:
            return "%.2f" % (float(self.price) * 0.7)
        else:
            return "%.2f" % (float(self.price) * 0.75)
