'''
Module to transform the dataset. To use, run the following command:
- python3 make_features.py <path of raw data> [<columns>]

Example:
- python3 make_features.py 'data/raw/v0-enem-raw-20220531.parquet' 'age' 'marital_status'
or to transform all columns of this dataset:
- python3 make_features.py 'data/raw/v0-enem-raw-20220531.parquet' 'all_columns' 

The output dataset will be in data/processed directory with same name but enem-processed
'''

import pandas as pd
from labels import labels
from datetime import date
import sys
import os

class MakeFeatures():

    def __init__(self):
        self.__labels = labels

    def label(self, label):

        '''
        get label dictionary
        '''

        return self.__labels[label]

    def transform(self, column, label):

        ''' 
        transform the colum values using the label dictionary
        '''

        return column.replace(self.label(label))

    def age_label(self, age):

        '''
        method to correct the age discrete variable to categorical data
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

    def income_per_person(self, family_income, qty_members):

        '''
        method for converter or range of income into a range of average per capita income
        '''

        income_interval = self.__convert_string_to_interval(family_income)
        num_persons = qty_members

        income_interval = list(map(lambda income: round(income / num_persons, 2), income_interval))
        len_income_interval = len(income_interval)
        
        return sum(income_interval) / len_income_interval

    def __convert_string_to_interval(self, income_interval):
    
        '''
        converts the income interval to a per capita income interval based on the number of persons in a family
        '''

        if income_interval == 'No income': return [0]
        elif income_interval == 'Less than BRL 1.045,00': return [1045.00]
        elif income_interval == 'More than BRL 20.900,00': return [20900.00]

        transformed_string = income_interval.replace('BRL ', '').replace('.', '').replace(',', '.').split(' to ')

        return list(map(float, transformed_string))


if __name__ == '__main__':

    
    raw_directory = sorted(os.listdir('data/raw'), reverse = True)[0]
    raw_directory = f'data/raw/{raw_directory}'

    # reading raw data to be transformed
    to_transform_data = pd.read_parquet(raw_directory)
    columns_to_transform = to_transform_data.columns

    MK = MakeFeatures()
    
    for column in columns_to_transform:

        try:
            if 'qty' in column:
                to_transform_data.loc[:, column] = MK.transform(to_transform_data.loc[:, column], 'qty_label')
            else:
                to_transform_data.loc[:, column] = MK.transform(to_transform_data.loc[:, column], column + '_label')
        except:
            print(f'Something went wrong with the column: {column}')

    # creating dataset name
    NUM_PROCESSED_DATA_FILES = len(list(filter(lambda file: 'parquet' in file, os.listdir(f'data/processed'))))
    date_now = date.today().strftime('%Y%m%d')
    OUTPUT_PATH = f'data/processed/v{NUM_PROCESSED_DATA_FILES}-enem-processed-{date_now}'

    # saving transformed data
    to_transform_data.to_parquet(OUTPUT_PATH + '.parquet', engine = 'fastparquet')
            