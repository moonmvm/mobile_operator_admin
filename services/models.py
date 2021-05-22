from django.db import models


class Tariff(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return f'Tariff: {self.title}. Price: {self.price}'


class Tv(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Телевидения'

    def __str__(self):
        return f'TV: {self.title}. Price: {self.price}'


class ConnectedTariff(models.Model):
    filial = models.ForeignKey('operators.Filial', on_delete=models.PROTECT, related_name='tariffs')
    tariff = models.ForeignKey(Tariff, on_delete=models.PROTECT, related_name='connected_tariffs')
    client = models.ForeignKey('clients.Client', on_delete=models.PROTECT, related_name='tariffs')
    # date = models.DateField(auto_now_add=True)
    date = models.DateField()

    class Meta:
        unique_together = ('filial', 'tariff', 'client')
        verbose_name_plural = 'Подключенные тарифы'

    def __str__(self):
        return f'Tariff: {self.tariff.title}. Filial: {self.filial.name}.'


class ConnectedTv(models.Model):
    filial = models.ForeignKey('operators.Filial', on_delete=models.PROTECT, related_name='tvs')
    tv = models.ForeignKey(Tv, on_delete=models.PROTECT, related_name='connected_tvs')
    client = models.ForeignKey('clients.Client', on_delete=models.PROTECT, related_name='tvs')
    # date = models.DateField(auto_now_add=True)
    date = models.DateField()

    class Meta:
        unique_together = ('filial', 'tv', 'client')
        verbose_name_plural = 'Подключенные телевидения'

    def __str__(self):
        return f'Tv: {self.tv.title}. Filial: {self.filial.name}. Client: {self.client}'
