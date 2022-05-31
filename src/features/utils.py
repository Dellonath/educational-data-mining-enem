def convert_string_interval(income_interval):
    
  '''
  converts the income interval to a per capita income interval based on the number of persons in a family
  '''

  if income_interval == 'No income': return [0]
  elif income_interval == 'Less than BRL 1.045,00': return [1045.00]
  elif income_interval == 'More than BRL 20.900,00': return [20900.00]
  return list(map(float, income_interval.replace('BRL ', '').replace('.', '').replace(',', '.').split(' to ')))
  
def income_per_person(data):

  '''
  function for converter or range of income into a range of average per capita income
  '''

  income_interval = convert_string_interval(data.renda_familiar)
  num_persons = data.qtd_moradores

  income_interval = list(map(lambda x: round(x / num_persons, 2), income_interval))
  
  return sum(income_interval) / len(income_interval)

def age_label(age):

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
