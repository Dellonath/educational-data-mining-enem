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
    'B': 'Less than 1 minimum wage',
    'C': 'Between 1-1.5 minimum wages',
    'D': 'Between 1.5-2 minimum wages',
    'E': 'Between 2-2.5 minimum wages',
    'F': 'Between 2.5-3 minimum wages',
    'G': 'Between 3-4 minimum wages',
    'H': 'Between 4-5 minimum wages',
    'I': 'Between 5-6 minimum wages',
    'J': 'Between 6-7 minimum wages',
    'K': 'Between 7-8 minimum wages',
    'L': 'Between 8-9 minimum wages',
    'M': 'Between 9-10 minimum wages',
    'N': 'Between 10-12 minimum wages',
    'O': 'Between 12-15 minimum wages',
    'P': 'Between 15-20 minimum wages',
    'Q': 'More than 20 minimum wages'
  },

  'qty_label': {
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
    'TP_ESCOLA': 'school_type',
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
    'Q009': 'bedrooms_qty',
    'Q010': 'cars_qty',
    'Q019': 'television_qty',
    'Q022': 'phones_qty',
    'Q024': 'computer_qty',
    'Q025': 'internet_access'
  }
}