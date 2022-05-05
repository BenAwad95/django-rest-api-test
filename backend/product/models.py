from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    title = models.CharField(_("product title"), max_length=50)
    content = models.TextField(_("product content"))
    price = models.DecimalField(_("product price"), max_digits=6, decimal_places=2, default=99.99)

    @property
    def ten_sales(self):
        return f'{float(self.price)*0.9:.2f}'
