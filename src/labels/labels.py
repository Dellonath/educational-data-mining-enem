labels = {
  'age_label': {
  1: 'Less than 17 years-old',
  2: '17 years-old',
  3: '18 years-old',
  4: '19 years-old',
  5: '20 years-old',
  6: '21 years-old',
  7: '22 years-old',
  8: '23 years-old',
  9: '24 years-old',
  10: '25 years-old',
  11: 'Between 26 and 30 years-old',
  12: 'Between 31 and 35 years-old',
  13: 'Between 36 and 40 years-old',
  14: 'Between 41 and 45 years-old',
  15: 'Between 46 and 50 years-old',
  16: 'Between 51 and 55 years-old',
  17: 'Between 56 and 60 years-old',
  18: 'Between 61 and 65 years-old',
  19: 'Between 66 and 70 years-old',
  20: 'More than 70 years-old'
  },

  'marital_status_label': {
    0: 'Unknown', 
    1: 'Single', 
    2: 'Married', 
    3: 'Divorced', 
    4: 'Widower'
  },

  'color_race_label': {
    0: 'Unknown', 
    1: 'White', 
    2: 'Black', 
    3: 'Brown', 
    4: 'Yellow', 
    5: 'Indigenous'
  },

  'high_school_status_label': {
    1: 'Completed High School', 
    2: 'Ends in the current year', 
    3: 'Will complete High School the following year', 
    4: 'Did not complete and is not attending High School'
  },
    
  'school_type_label': {
    1: 'Unknown', 
    2: 'Public', 
    3: 'Private', 
    4: 'Foreign'
  },

  'presence_label': {
    0: 'Missed', 
    1: 'Present', 
    2: 'Eliminated'
  },

  'father_schooling_label': {
    'A': 'Never studied',
    'B': 'Didn\'t complete Elementary School',
    'C': 'Didn\'t complete Elementary School',
    'D': 'Completed Elementary School',
    'E': 'Completed High School',
    'F': 'Completed College',
    'G': 'Completed Graduate',
    'H': 'Unknown'
  },

  'mother_schooling_label': {
    'A': 'Never studied',
    'B': 'Didn\'t complete Elementary School',
    'C': 'Didn\'t complete Elementary School',
    'D': 'Completed Elementary School',
    'E': 'Completed High School',
    'F': 'Completed College',
    'G': 'Completed Graduate',
    'H': 'Unknown'
  },

  'father_profession_group_label': {
    'A': 'Group A',
    'B': 'Group B',
    'C': 'Group C',
    'D': 'Group D',
    'E': 'Group E',
    'F': 'Group F'
  },

  'mother_profession_group_label': {
    'A': 'Group A',
    'B': 'Group B',
    'C': 'Group C',
    'D': 'Group D',
    'E': 'Group E',
    'F': 'Group F'
  },

  'family_income_label': {
    'A': 'No income',
    'B': 'Less than BRL 1.045,00',
    'C': 'BRL 1.045,01 to BRL 1.567,50',
    'E': 'BRL 2.090,01 to BRL 2.612,50',
    'D': 'BRL 1.567,51 to BRL 2.090,00',
    'F': 'BRL 2.612,51 to BRL 3.135,00',
    'G': 'BRL 3.135,01 to BRL 4.180,00',
    'H': 'BRL 4.180,01 to BRL 5.225,00',
    'I': 'BRL 5.225,01 to BRL 6.270,00',
    'J': 'BRL 6.270,01 to BRL 7.315,00',
    'K': 'BRL 7.315,01 to BRL 8.360,00',
    'L': 'BRL 8.360,01 to BRL 9.405,00',
    'M': 'BRL 9.405,01 to BRL 10.450,00',
    'N': 'BRL 10.450,01 to BRL 12.540,00',
    'O': 'BRL 12.540,01 to BRL 15.675,00',
    'P': 'BRL 15.675,01 to BRL 20.900,00',
    'Q': 'More than BRL 20.900,00'
  },

  'number_label': {
    'A': 'No',
    'B': 'One',
    'C': 'Two',
    'D': 'Three',
    'E': 'Four or more'
  },

  'internet_access_label': {
    'A': 'No', 
    'B': 'Yes'
  },

  'columns': {
    'NU_INSCRICAO': 'id',
    'NU_ANO': 'enem_year',
    'TP_FAIXA_ETARIA': 'age',
    'TP_SEXO': 'sex',
    'TP_ESTADO_CIVIL': 'marital_status',
    'TP_COR_RACA': 'color_race',
    'TP_ST_CONCLUSAO': 'high_school_status',
    'TP_ANO_CONCLUIU': 'year_completion_high_school',
    'TP_ESCOLA': 'type_school',
    'CO_MUNICIPIO_ESC': 'id_city_school',
    'NO_MUNICIPIO_ESC': 'city_school',
    'SG_UF_ESC': 'state_school',
    'CO_MUNICIPIO_PROVA': 'id_city_test',
    'NO_MUNICIPIO_PROVA': 'city_test',
    'SG_UF_PROVA': 'state_test',
    'TP_PRESENCA_LC': 'presence_day_1',
    'TP_PRESENCA_MT': 'presence_day_2',
    'NU_NOTA_CN': 'nature_science_score',
    'NU_NOTA_CH': 'human_sciences_score',
    'NU_NOTA_LC': 'languages_codes_score',
    'NU_NOTA_MT': 'mathematics_score',
    'NU_NOTA_COMP1': 'ortography_score',
    'NU_NOTA_COMP2': 'understanding_score',
    'NU_NOTA_COMP3': 'structuring_score',
    'NU_NOTA_COMP4': 'argumentation_score',
    'NU_NOTA_COMP5': 'proposal_score',
    'NU_NOTA_REDACAO': 'redaction_score',
    'Q001': 'father_schooling',
    'Q002': 'mother_schooling',
    'Q003': 'father_profession_group',
    'Q004': 'mother_profession_group',
    'Q005': 'family_members',
    'Q006': 'family_income',
    'Q009': 'bedrooms_number',
    'Q010': 'cars_number',
    'Q019': 'television_number',
    'Q022': 'phones_number',
    'Q024': 'computer_numbers',
    'Q025': 'internet_access'
  }
}