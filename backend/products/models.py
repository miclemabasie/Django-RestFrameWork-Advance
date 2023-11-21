from django.db import models
from django.urls import reverse
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Product(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=9.99)
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"Product-> {self.title}"

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

    def get_url(self):
        return f"/api/products/{self.id}"


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"category-{self.name}"

    def get_all_products(self):
        products = Product.objects.all(category=self.category)
