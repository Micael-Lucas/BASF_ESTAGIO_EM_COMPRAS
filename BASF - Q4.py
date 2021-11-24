import math

alt_med = 3
comp_casas = math.sqrt(75)
comp_edgrandes = math.sqrt(1000)
larg_tij = 0.15

tam_portas = 2
tam_janelas = 1.5*1.5 

qtd_med_portas_edPeqMed = 5
qtd_med_jan_edPeqMed = 3
qtd_med_portas_Gnd = 20
qtd_med_jan_edGnd = 12

per_interno_casas = alt_med*4*comp_casas
per_interno_edgrandes = alt_med*4*comp_edgrandes
per_externo_casas = alt_med*(comp_casas+2*larg_tij)
per_externo_edgrandes = alt_med*(comp_edgrandes+2*larg_tij)

per_tot_med_edPeqMed = per_interno_casas + per_externo_casas + (2* per_interno_casas)/3
per_tot_med_edGnd = per_externo_edgrandes + per_interno_edgrandes + (2* per_interno_edgrandes)/3

rend_tinta = 7
tam_med_galao_tinta = 10

continua = True

while(continua):
    qtdContru_PqMed = int(input("Digite a quantidade de Construções de Pequeno/Médio porte no Brasil: "))
    porce_pintadas_mes_peq = int(input("Quantos desses são pintados no mês? Digite uma porcentagem de (0 a 100): "))

    qtdContru_gnd = int(input("Digite a quantidade de Construções de grande porte no Brasil: "))
    porce_pintadas_mes_gnd = int(input("Quantos desses são pintados no mês? Digite uma porcentagem de (0 a 100): "))

    per_tot = ((qtdContru_PqMed * porce_pintadas_mes_peq/100 * per_tot_med_edPeqMed) - (qtd_med_jan_edPeqMed*tam_janelas + qtd_med_portas_edPeqMed*tam_portas)) + ((qtdContru_gnd * porce_pintadas_mes_gnd/100 * per_tot_med_edGnd) - (qtd_med_jan_edGnd*tam_janelas + qtd_med_portas_Gnd*tam_portas))
    
    qtd_Litros = float(per_tot)/float(rend_tinta)
    qtd_vend = qtd_Litros/float(tam_med_galao_tinta)

    print("\nA quantidade média de galões vendidos seguindo os parametros passados foi:", qtd_vend,"\nA area pintada em M^2 foi de:", per_tot, "\n")
    desejo = input("Deseja testar novos valores? S/N\n")

    if desejo != 'S':
        continua = False

print("Obrigado por testar o programa!\n")