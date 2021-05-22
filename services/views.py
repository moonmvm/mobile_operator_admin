from django.shortcuts import render

from . import services


def display_charts(request):
    top_tariffs = services.get_tariff_chart_data('tariff__title', 'tariff')
    top_filials = services.get_tariff_chart_data('filial__name', 'filial')
    connections_by_date = services.get_tariff_chart_data('date', 'date')

    data_to_render = {
        'connections_by_date': connections_by_date,
        'top_tariffs': top_tariffs,
        'top_filials': top_filials,
    }
    return render(request, 'charts.html', data_to_render)
