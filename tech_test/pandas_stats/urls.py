from django.urls import path
from . import views

urlpatterns = [
    path('stats/avg_age_industry/', views.avg_age_industry, name='avg-age-industry'),
    path('stats/avg_salary_industry/', views.avg_salary_industry, name='avg-salary-industry'),
    path('stats/avg_salary_exp/', views.avg_salary_exp, name='avg-salary-experience'),
    path('stats/gender_pct_select_company/<company>/', views.gender_pct_select_company, name='gender-pct-select-company'),
]