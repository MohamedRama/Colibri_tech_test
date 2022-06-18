from django.http import HttpResponse
from operations.models import Employee
import datetime
import numpy as np
import pandas as pd

def get_df():
    employees = Employee.objects.all()
    employees_values = employees.values()
    df = pd.DataFrame(employees_values)
    return df

def avg_age_industry(request):
    df = get_df()
    
    # caluclate age from date_of_birth
    now = pd.Timestamp('now')
    df_date_of_birth = pd.to_datetime(df['date_of_birth'])
    df_date_of_birth = df_date_of_birth.where(df_date_of_birth < now, df_date_of_birth -  np.timedelta64(100, 'Y'))
    df['age'] = (now - df_date_of_birth).astype('<m8[Y]')    # set age datetype to years

    df = df.groupby('industry').age.mean()
    data = df.to_json(indent=2)
    return HttpResponse(data, content_type='application/json')

def avg_salary_industry(request):
    df = get_df()

    df = df.groupby('industry').salary.mean()
    data = df.to_json(indent=2)
    return HttpResponse(data, content_type='application/json')

def avg_salary_exp(request):
    df = get_df()

    df = df.groupby('years_of_experience').salary.mean()
    data = df.to_json(indent=2)
    return HttpResponse(data, content_type='application/json')

def gender_pct_select_company(request, company):
    df = get_df()

    gender_grp = df.groupby('gender')
    genders = df['gender'].value_counts()
    gender_company = gender_grp['email'].apply(lambda x: x.str.contains(f'@{company}').sum()) # get company from email
    concat_df = pd.concat([genders, gender_company], axis='columns', sort=False)
    concat_df.rename(columns={'gender': 'gender_count', 'email': 'gender_per_selected_company'}, inplace=True)
    concat_df['percentage'] = (concat_df['gender_per_selected_company']/concat_df['gender_count']) * 100

    data = concat_df.to_json(indent=2)
    return HttpResponse(data, content_type='application/json')
