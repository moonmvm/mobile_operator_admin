from services.models import ConnectedTariff
from django.db.models import Count


def get_tariff_chart_data(field_name: str, field_for_count: str) -> dict:
    """
    Return labels and connections of every label by provided field_name.
    """
    labels = []
    connections = []

    queryset = ConnectedTariff.objects.values(field_name).annotate(connections=Count(field_for_count))

    for entry in queryset:
        labels.append(str(entry[field_name]))
        connections.append(entry['connections'])

    return {'labels': labels, 'connections': connections}
