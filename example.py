def get_vat(payment):
    try:
        vat = payment / 100 * 18
        return round(vat, 2)
    except(TypeError, ValueError):
        print('проверьте воодимые данные')

result = get_vat('rere')
print('Сумма НДС: {}'.format(result))