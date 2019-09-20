from moto import Moto

estado_moto = int(input('Digite 8 para ligar moto: '))
estado_marcha = int(input('Digite qual macha você deseja:\n (0) Neutro, (1) Primeira marcha, (2) Segunda marcha, (3) Terceira macha :'))

moto1 = Moto('Honda', 'R1', 'Azul', estado_marcha, estado_moto)

moto1.ligar()
moto1.marcha_acima()
moto1.imprimir()
moto1.marcha_abaixo()
moto1.imprimir()