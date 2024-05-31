from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\d{9,15}$', message="El número de teléfono debe contener entre 9 y 15 dígitos.")
 
def valida_cedula(value):
    cedula_o_ruc = str(value)
    if not cedula_o_ruc.isdigit():
        raise ValidationError('La cédula o RUC debe contener solo números.')

    longitud = len(cedula_o_ruc)
    if longitud != 10 and longitud != 13:
        raise ValidationError('La cédula debe tener 10 dígitos o 13 si es RUC.')

    coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
    total = 0
    for i in range(9):
        digito = int(cedula_o_ruc[i])
        coeficiente = coeficientes[i]
        producto = digito * coeficiente
        if producto > 9:
            producto -= 9
        total += producto

    residuo = total % 10
    if residuo == 0:
        digito_verificador = 0
    else:
        digito_verificador = 10 - residuo

    if digito_verificador != int(cedula_o_ruc[9]):
        raise ValidationError('La cédula o RUC no es válido.')

    # Si es un RUC, verificar los últimos 3 dígitos
    if longitud == 13 and (cedula_o_ruc[10:] == '000' or not cedula_o_ruc[10:].isdigit()):
        raise ValidationError('El RUC no es válido.')

