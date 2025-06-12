def calculate_energy_consumption(power, hours, days):
    """
    Рассчитывает потребление электроэнергии за заданный период.
    :param power: мощность прибора в ваттах
    :param hours: количество часов использования в день
    :param days: количество дней использования
    :return: потребление электроэнергии в кВт*ч
    """
    return (power * hours * days) / 1000

def calculate_cost(energy_consumption, rate):
    """
    Рассчитывает стоимость использования прибора за заданный период.
    :param energy_consumption: потребление электроэнергии в кВт*ч
    :param rate: стоимость 1 кВт*ч
    :return: стоимость использования прибора
    """
    return energy_consumption * rate