from django.db import models


class Good (models.Model):
    title = models.CharField(
                            verbose_name=u"Название",
                            max_length=255
    )

    add_date = models.DateTimeField(
                                    verbose_name=u"Дата поступления"
    )

    price = models.PositiveIntegerField(
        verbose_name=u'Цена',
        default=0
    )

    units = models.CharField(
        verbose_name=u"Ед. измерения",
        max_length=255
    )

    supplier_name = models.CharField(
                    verbose_name=u"Имя поставщика",
                    max_length=255
    )

