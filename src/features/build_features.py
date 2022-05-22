def convert_string_interval(income_interval):
    
  '''
  converts the income interval to a per capita income interval based on the number of persons in a family
  '''

  if income_interval == 'Nenhuma Renda': return [0]
  elif income_interval == 'Até R$ 1.045,00': return [1045.00]
  elif income_interval == 'Acima de R$ 20.900,00': return [20900.00]
  return list(map(float, income_interval.replace('De ', '').replace('R$ ', '').replace('.', '').replace(',', '.').split(' até ')))
  
def income_per_person(data):

  '''
  function for converter or range of income into a range of average per capita income
  '''

  income_interval = convert_string_interval(data.renda_familiar)
  num_persons = data.qtd_moradores

  income_interval = list(map(lambda x: round(x / num_persons, 2), income_interval))
  
  return sum(income_interval) / len(income_interval)

def TP_FAIXA_ETARIA_label(age):

  '''
  function to correct the age discrete variable to categorical data
  '''

  if age < 17: return 1
  elif age == 17: return 2
  elif age == 18: return 3
  elif age == 19: return 4
  elif age == 20: return 5
  elif age == 21: return 6
  elif age == 22: return 7
  elif age == 23: return 8
  elif age == 24: return 9
  elif age == 25: return 10
  elif age <= 30: return 11
  elif age <= 35: return 12
  elif age <= 40: return 13
  elif age <= 45: return 14
  elif age <= 50: return 15
  elif age <= 55: return 16
  elif age <= 60: return 17
  elif age <= 65: return 18
  elif age <= 70: return 19
  else: return 20

NU_IDADE2020_label = {
  1: 'Menor de 17 anos',
  2: '17 anos',
  3: '18 anos',
  4: '19 anos',
  5: '20 anos',
  6: '21 anos',
  7: '22 anos',
  8: '23 anos',
  9: '24 anos',
  10: '25 anos',
  11: 'Entre 26 e 30 anos',
  12: 'Entre 31 e 35 anos',
  13: 'Entre 36 e 40 anos',
  14: 'Entre 41 e 45 anos',
  15: 'Entre 46 e 50 anos',
  16: 'Entre 51 e 55 anos',
  17: 'Entre 56 e 60 anos',
  18: 'Entre 61 e 65 anos',
  19: 'Entre 66 e 70 anos',
  20: 'Maior de 70 anos'
}

TP_ESTADO_CIVIL_label= {0: 'Não informado', 1: 'Solteiro(a)', 2: 'Casado(a)/Mora com companheiro(a)', 3: 'Divorciado(a)', 4: 'Viúvo(a)'}

TP_COR_RACA_label = {0: 'Não declarado', 1: 'Branca', 2: 'Preta', 3: 'Parda', 4: 'Amarela', 5: 'Indígena'}

TP_ST_CONCLUSAO_label = {
  1: 'Já concluí o Ensino Médio', 
  2: 'Estou cursando e concluirei neste ano', 
  3: 'Estou cursando e concluirei o Ensino Médio no ano seguinte', 
  4: 'Não concluí e não estou cursando o Ensino Médio'
}
  
TP_ESCOLA_label = {1: 'Não respondeu', 2: 'Pública', 3: 'Privada', 4: 'Exterior'}

TP_PRESENCA_label = {0: 'Faltou à prova', 1: 'Presente na prova', 2: 'Eliminado na prova'}

Q001_Q002_label = {
  'A': 'Nunca estudou',
  'B': 'Não completou o Ensino Fundamental',
  'C': 'Não completou o Ensino Fundamental',
  'D': 'Completou o Ensino Fundamental',
  'E': 'Completou o Ensino Médio',
  'F': 'Completou a Faculdade',
  'G': 'Completou a Pós-graduação',
  'H': 'Não sei'
}

Q003_Q004_label = {
  'A': 'Grupo A',
  'B': 'Grupo B',
  'C': 'Grupo C',
  'D': 'Grupo D',
  'E': 'Grupo E',
  'F': 'Grupo F'
}

Q006_label = {
  'A': 'Nenhuma Renda',
  'B': 'Até R$ 1.045,00',
  'C': 'De R$ 1.045,01 até R$ 1.567,50',
  'D': 'De R$ 1.567,51 até R$ 2.090,00',
  'E': 'De R$ 2.090,01 até R$ 2.612,50',
  'F': 'De R$ 2.612,51 até R$ 3.135,00',
  'G': 'De R$ 3.135,01 até R$ 4.180,00',
  'H': 'De R$ 4.180,01 até R$ 5.225,00',
  'I': 'De R$ 5.225,01 até R$ 6.270,00',
  'J': 'De R$ 6.270,01 até R$ 7.315,00',
  'K': 'De R$ 7.315,01 até R$ 8.360,00',
  'L': 'De R$ 8.360,01 até R$ 9.405,00',
  'M': 'De R$ 9.405,01 até R$ 10.450,00',
  'N': 'De R$ 10.450,01 até R$ 12.540,00',
  'O': 'De R$ 12.540,01 até R$ 15.675,00',
  'P': 'De R$ 15.675,01 até R$ 20.900,00',
  'Q': 'Acima de R$ 20.900,00'
}

Q011_Q019_label = {
  'A': 'Não',
  'B': 'Uma',
  'C': 'Duas',
  'D': 'Três',
  'E': 'Quatro ou mais'
}

Q009_Q010_Q022_Q024_label = {
  'A': 'Não',
  'B': 'Um',
  'C': 'Dois',
  'D': 'Três',
  'E': 'Quatro ou mais'
}

Q025_label = {'A': 'Não', 'B': 'Sim'}

boolean_label = {0: 'Não', 1: 'Sim'}

columns = {
  'NU_INSCRICAO': 'id',
  'NU_ANO': 'enem',
  'NU_IDADE': 'idade',
  'TP_SEXO': 'sexo',
  'TP_ESTADO_CIVIL': 'estado_civil',
  'TP_COR_RACA': 'cor_raca',
  'TP_ST_CONCLUSAO': 'status_ensino_medio',
  'TP_ANO_CONCLUIU': 'ano_conclusao_ensino_medio',
  'TP_ESCOLA': 'tipo_escola',
  'CO_MUNICIPIO_ESC': 'id_municipio_escola',
  'NO_MUNICIPIO_ESC': 'municio_escola',
  'SG_UF_ESC': 'uf_escola',
  'CO_MUNICIPIO_PROVA': 'id_municipio_prova',
  'NO_MUNICIPIO_PROVA': 'municio_prova',
  'SG_UF_PROVA': 'uf_prova',
  'TP_PRESENCA_LC': 'presenca_dia_1',
  'TP_PRESENCA_MT': 'presenca_dia_2',
  'NU_NOTA_CN': 'nota_ciencias_natureza',
  'NU_NOTA_CH': 'nota_ciencias_humanas',
  'NU_NOTA_LC': 'nota_linguagens_codigos',
  'NU_NOTA_MT': 'nota_matematica',
  'NU_NOTA_COMP1': 'nota_ortografia',
  'NU_NOTA_COMP2': 'nota_entendimento',
  'NU_NOTA_COMP3': 'nota_estruturacao',
  'NU_NOTA_COMP4': 'nota_argumentacao',
  'NU_NOTA_COMP5': 'nota_proposta',
  'NU_NOTA_REDACAO': 'nota_redacao',
  'Q001': 'escolariade_pai',
  'Q002': 'escolariade_mae',
  'Q003': 'grupo_ocupacao_pai',
  'Q004': 'grupo_ocupacao_mae',
  'Q005': 'qtd_moradores',
  'Q006': 'renda_familiar',
  'Q009': 'qtd_quartos',
  'Q010': 'qtd_carros',
  'Q019': 'qtd_televisao',
  'Q022': 'qtd_celular',
  'Q024': 'qtd_computador',
  'Q025': 'possui_internet'
}
