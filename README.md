Django application for HR system that returns JSON data. Data used is from the MOCK_DATA.json file provided with the test. 
* Operations on employees APIs:
    - read all (with ordering, filters & pagination as parameters): employee_all function view, http://127.0.0.1:8000/employee/all: 
        - django-filters for filtering the dataset results, usage examples: 
            - http://127.0.0.1:8000/employee/all?years_of_experience=4 , http://127.0.0.1:8000/employee/all?years_of_experience__gt=4, http://127.0.0.1:8000/employee/all?first_name__icontains=annmarie .. etc
        - ordering data: 
            - http://127.0.0.1:8000/employee/all?order_by=salary
        - pagination:
            - http://127.0.0.1:8000/employee/all?paginate_by=5
        http://127.0.0.1:8000/employee/all?years_of_experience=4&order_by=salary&paginate_by=5
        
    - read one: employee_one function view, http://127.0.0.1:8000/employee/id/<int:pk>/:
        - http://127.0.0.1:8000/employee/id/3/, will get one employee that has the id=3
    
    - update one: employee_update function view, update_emp.html template and EmployeeForm in froms.py, http://127.0.0.1:8000/employee/id/<int:pk>/update/:
        from the browser the form for the selected employee can be filled with the new data to be updated.
    
    - delete one: employee_delete function view and delete_emp.html, http://127.0.0.1:8000/employee/id/<int:pk>/delete/:
        the selected employee will be deleted and the you get redirected to all employees. 

* Pandas_stats APIs:
    - Average age per industry: avg_age_industry view, http://127.0.0.1:8000/stats/avg_age_industry/
    - Average salaries per industry: avg_salary_industry view, http://127.0.0.1:8000/stats/avg_salary_industry/
    - Average salaries per years of experience: avg_salary_exp view, http://127.0.0.1:8000/stats/avg_salary_exp/
    - Gender percentage per company: gender_pct_select_company view, http://127.0.0.1:8000/stats/gender_pct_select_company/<company>/
        this additional statistic for calculating the percentage of F/M in a specific company passed in the api as a parameter, ex:
            http://127.0.0.1:8000/stats/gender_pct_select_company/cisco/ 
