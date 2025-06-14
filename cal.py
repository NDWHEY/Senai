def hora_normal(salario,carga):
    calculo  = salario/carga
    return calculo

def hora_extra(hora_normal):
    calculo = hora_normal * 1.5
    return calculo

def quantas_horas_extras(quantidade, hora_extra):
    calculo =  quantidade * hora_extra
    return calculo

def salario_total(salario, quantidade_extra):
    calculo =  salario + quantidade_extra
    return calculo

def sistema_sal():
    salario = float(input('Digite seu salario: '))
    carga = float(input('Digite sua carga: '))
    hora_colaborador  = hora_normal(salario,carga)
    print('R$', round(hora_colaborador,2) )
    hora_extra1 = hora_extra(hora_colaborador)
    print('R$', round(hora_extra1,2))
    quantidade_extra = float(input('Horas extras:  '))
    quantas = quantas_horas_extras(quantidade_extra, hora_extra1)
    print('R$', round(quantas,2))
    salario_total_ = salario_total(salario, quantas)
    print('R$', round(salario_total_,2))


sistema_sal()