'''import pandas as pd
import random
from faker import Faker
from datetime import timedelta, datetime

fake= Faker()
random.seed(1)
departments = ['HR', 'Finance', 'IT', 'Marketing' 'Technician', 'Operations', 'Customer Service', 'Administration',
              'Legal', 'Procurement', 'Research and Development'],
job_titles = {
    'HR':['HR Assistance', 'HR Manager'],
    'Finance':['Accountant', 'Financial Analyst'],
    'IT':['Developer', 'System Admin'],
    'Marketing':['Marketing Executive', 'Content Specialist'],
    'Technician':['Equipment Maintenance', 'Hardware % Software Troubleshooting'],
    'Operations':['Operations Analyst', 'Logistical Coordinator'],
    'Customer Service':['Customer Inquiries',],
    'Administration':['Office Management', 'Administraive Support', 'Facilities Management'],
    'Legal':['Contract Management', 'Compliance', 'Legal counsel',],
    'Procurement':['Sourcing', 'Purchasing'],
    'Research and Development':['Product development', 'Innovation', 'Research']
}
locations = ['Lagos', 'Abuja', 'Kano', 'Rivers', 'Edo', 'Delta', 'Imo', 'Abia', 'Ogun', 'Osun',
             'Adamawa', 'Jos', 'Anambra', 'Akwa ibom', 'Cross river','Kaduna', 'Yobe', 'Benue']
benefit_types = ['Health Insurance', 'Transport Allowance', 'Housing', 'Gym Membership', 'None']
career_goals = ['Manager', 'Team lead', 'Specialist', 'Consultant']
mentorship_status = ['Assign', 'None']
diversity_groups = ['None', 'Minority', 'Female', 'Veteran', 'Disable']
engagement_levels =['High', 'Medium', 'Low']

def calculate_tax(salary):
    if salary<=40000:
        return round(salary * 0.10, 2)
    elif salary<=80000:
        return round(salary * 0.15, 2)
    else:
        return round(salary * 0.20, 2)
def calculate_allowance(job_title, salary):
    if 'Manager' in job_title or 'Analyst' in job_title:
        return round(salary * random.uniform(0.15, 0.20), 2)
    else:
        return round(salary * random.uniform(0.05, 0.10), 2)
def generate_hr_data(n=1000):
    data = []
    for i in range(1, n + 1):
        gender = random.choice(['Male', 'Female'])
        name = fake.name_male() if gender == 'Male' else fake.name_female()
        age = random.randint(25,60)
        hy = random.choice(departments)
        job = random.choice(job_titles[hy])
        salary = round(random.uniform(25000,120000), 2)
        hire_date = fake.date_between(start_date='-10y', end_date='today')
        years_experience = max(0,round((datetime.now().date() - hire_date).days / 365 + random.uniform(-2, 2), 1))
        performance_rating = random.randint(1, 5)
        marital_status = random.choice(['Single', 'Married', 'Divorced', 'Widowed'])
        location = random.choice(locations)
        tax = calculate_tax(salary)
        allowance = calculate_allowance(job_titles, salary)
        benefits = random.sample(benefit_types, k = random.randint(1, 3))
        training_completed = random.choice(['Yes', 'No'])
        goal = random.choice(career_goals)
        mentorship = random.choice(mentorship_status)
        engagement_score = random.randint(40, 100)
        diversity = random.choice(diversity_groups)
        succession_plan = random.choice(['Yes', 'No'])
        compensation_score = round(salary/1000+performance_rating*2,2)
        alltrition_risk = ('High' if performance_rating<=2 and engagement_score<60 else 'Medium' if engagement_score
                           <75 else 'Low')
        data.append({
            'Employee ID': f'EMP{i:04}',
            'Name': name,
            'Age': age,
            'Department':departments,
            'Job Title': job_titles,
            'Location': locations,
            'Salary': salary,
            'Tax': tax,
            'Allowance': allowance,
            'Net pay': round(salary - tax + allowance, 2),
            'Hire Date': hire_date,
            'Years of Experience': years_experience,
            'Performance rating': performance_rating,
            'Marital Status': marital_status,
            'Benefits': ", ".join(benefits),
            'Training Completed': training_completed,
            'Career Goal': goal,
            'Mentorship': mentorship,
            'Engagement Score': engagement_score,
            'Diversity Group': diversity,
            'Succession Plan': succession_plan,
            'Compensation Score': compensation_score,
            'Attrition Risk': alltrition_risk})
        return pd.DataFrame(data)

df= generate_hr_data(1000)
print(hr_data.head())'''
#from tkinter.font import names

import numpy as np
import pandas as pd
import numpy as np
import random
from faker import Faker

from pandas.io.pytables import performance_doc
fake = Faker()
np.random.seed(0)

num_employees = 10
employee_ids = [f"E{i:4d}" for i in range(1, num_employees+1)]
names =[fake.name_nonbinary() for _ in range(num_employees)]
departments = np.random.choice(['HR', 'Finance', 'IT', 'Marketing' 'Technician',
                                'Operations', 'Customer Service', 'Administration',
                                'Legal', 'Procurement', 'Research and Development'],num_employees)
job_titles = np.random.choice(['HR Assistance', 'HR Manager','Accountant', 'Financial Analyst',
                               'Developer', 'System Admin','Marketing Executive',
                               'Content Specialist','Equipment Maintenance',
                               'Hardware % Software Troubleshooting','Operations Analyst',
                               'Logistical Coordinator','Customer Inquiries','Office Management',
                               'Compliance', 'Legal counsel','Sourcing', 'Purchasing','Product development',
                               'Innovation', 'Research'],num_employees)
mentorship = np.random.choice(["Yes", "No"], num_employees)
ages = np.random.randint(25,60, num_employees)
genders = [fake.random_element(elements=('Male','Female')) for _ in range(num_employees)]
marital_status = np.random.choice(["Married", "Single", "Divorce"], num_employees)
locations = np.random.choice(['Lagos', 'Abuja', 'Kano', 'Rivers', 'Edo', 'Delta', 'Imo',
                              'Abia', 'Ogun', 'Osun','Adamawa', 'Jos', 'Anambra', 'Akwa ibom',
                              'Cross river','Kaduna', 'Yobe', 'Benue'],num_employees)
hire_dates = [f"{np.random.randint(2010, 2025)}-{np.random.randint(1,15):02d}" for _ in range(num_employees)]
years_experience = np.random.randint(1, 30, num_employees)
performance_ratings = np.round(np.random.uniform(1.0, 5.0, num_employees), 2)
career_goals = np.random.choice(['Manager', 'Specialist','Consultant','Team Lead'], num_employees)
training = np.random.choice(["Teachnical Skill", "Leadership Development", "Communication Skills"], num_employees)

diversity_inclusion = np.random.choice(["Yes", "No"], num_employees)
succession_planning = np.random.choice(["Potential Leader","Not Eligible"], num_employees)
compensation_analysis = np.random.choice(["Market-based", "Performance-based" ], num_employees)
predictive_analytics = np.random.choice(["High", "Low", "Medium" ], num_employees)
employee_engagement = np.round(np.random.uniform(1.0, 5.0, num_employees), 2)
salaries = np.random.randint(50000, 200000, num_employees)

benefits = []
allowances = np.zeros(num_employees)
for i in range(num_employees):
    num_benefits = np.random.randint(1, 4)
    employee_benefits = np.random.choice(["Health Insurance", "Transport Allowance",
                                      "Housing",  "Gym Membership"] )
    #benefit_str = ", ".join(employee_benefits)
    benefits.append(employee_benefits)


    #allowances = np.ra ndom.randint(5000, 20000)

    allowance = 0
    for benefit in employee_benefits:
        if benefit == "Health Insurance":
            allowance += np.random.randint(8000,10000, )
        elif benefit == "Transport Allowance":
            allowance += np.random.randint(3000, 5000,)
        elif benefit == "Housing":
            allowance += np.random.randint(6000,7500,)
        elif benefit == "Gym Membership":
            allowance += np.random.randint(1000,2000,)
       
        #  allowances.append(allowances)

    allowances[i] = allowance

print(benefits)

tax = np.round(salaries * 0.25, 2)
#tax = tax.tolist()
net_pay = np.round(salaries - tax + allowances, 2)
total_money_received = np.round(net_pay * 12, 2)


hr_data = pd.DataFrame({'Employee ID': employee_ids,
                        "Name": names,
                        "Department": departments,
                        "Job Title": job_titles,
                        "Age": ages,
                        "Gender": genders,
                        "Marital Status": marital_status,
                        "Location": locations,
                        "Hire Date": hire_dates,
                        "Year of Experience": years_experience,
                        "Career Goal": career_goals,
                        "Training": training,
                        "Succession Planning": succession_planning,
                        "Diversity Inclusion" : diversity_inclusion,
                        "Compensation Analysis": compensation_analysis,
                        "Predictive Analytics": predictive_analytics,
                        "Benefit": benefits,
                        "Employee Engagement": employee_engagement,
                        "Salary": salaries,
                        "Allowance": allowances,
                        "Tax": tax,
                        "Net Pay": net_pay,
                        "Wages": total_money_received,
                        "Performance Rating": performance_ratings})
print(hr_data.to_string())
