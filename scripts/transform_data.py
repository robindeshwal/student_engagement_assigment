import pandas as pd
import os

INPUT_DIR = 'data/cleaned'
OUTPUT_DIR = 'data/transformed'
os.makedirs(OUTPUT_DIR, exist_ok=True)

students = pd.read_csv(os.path.join(INPUT_DIR, 'student_data.csv'))
logins = pd.read_csv(os.path.join(INPUT_DIR, 'student_logins.csv'))
grades = pd.read_csv(os.path.join(INPUT_DIR, 'assignment_submissions.csv'))

login_count = logins.groupby('student_id') \
                    .size() \
                    .reset_index(name='login_count')

# import ipdb; ipdb.set_trace()
# print("Columns in Assignment_Submissions.csv:", grades.columns.tolist())
avg_grades = grades.groupby('student_id')['points'] \
                    .mean() \
                    .reset_index(name='avg_grade')


engamement = pd.merge(students, 
                      login_count,
                      on='student_id',
                      how='left')

engamement = pd.merge(engamement,
                      avg_grades,
                      on='student_id',
                      how='left')

engamement.to_csv(os.path.join(OUTPUT_DIR,
                               'student_engagment_summary.csv'))
print("Transfromed data saved.")
