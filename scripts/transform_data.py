import pandas as pd
import os

INPUT_DIR = 'data/cleaned'
OUTPUT_DIR = 'data/transformed'
os.makedirs(OUTPUT_DIR, exist_ok=True)

students = pd.read_csv(os.path.join(INPUT_DIR, 'student_data.csv'))
logins = pd.read_csv(os.path.join(INPUT_DIR, 'student_logins.csv'))
assignment = pd.read_csv(os.path.join(INPUT_DIR, 'assignment_data.csv'))
grades = pd.read_csv(os.path.join(INPUT_DIR, 'assignment_submissions.csv'))
courses = pd.read_csv(os.path.join(INPUT_DIR, 'course_data.csv'))
content = pd.read_csv(os.path.join(INPUT_DIR, 'content_access.csv'))

# ================ STUDENT LEVEL AGGREGATION ===========================
login_count = logins.groupby('student_id').size().reset_index(name='login_count')
avg_grades = grades.groupby('student_id')['points'].mean().reset_index(name='avg_grade')
content_access_count = content.groupby('student_id')
access_count = content_access_count.size().reset_index(name='content_access_count')
total_minutes = content_access_count['time_spent_minutes'].sum().reset_index()

total_minutes['total_hours_spent'] = (total_minutes['time_spent_minutes'] / 60).round(2)
total_minutes = total_minutes.drop(columns='time_spent_minutes')
# import ipdb; ipdb.set_trace()

# Merge to form student-level engagement summary
engagement = pd.merge(students, login_count, on='student_id', how='left')
engagement = pd.merge(engagement, avg_grades, on='student_id', how='left')
engagement = pd.merge(engagement, access_count, on='student_id', how='left')
engagement = pd.merge(engagement, total_minutes, on='student_id', how='left')

engagement.to_csv(os.path.join(OUTPUT_DIR, 'student_engagment_summary.csv'), index=False)
print("Student-Level data saved.")

# =============== COURSE LEVEL AGGREGRATION ============================

assignment_activity = pd.merge(grades, assignment[['assignment_id', 'course_id']], 
                            on='assignment_id', how='left')

assignment_status_counts = (assignment_activity.groupby(['course_id', 'assignment_id', 'status'])['student_id']
                                .nunique().reset_index(name='student_count'))

assignment_summary = assignment_status_counts.pivot_table(
    index=['course_id', 'assignment_id'],
    columns='status',
    values='student_count',
    fill_value=0
).reset_index()

assignment_summary.to_csv(os.path.join(OUTPUT_DIR, 'course_assignment_status_summary.csv'), index=False)
print("Course-level assignment submission summary data saved.")

# =============== DEPARTMENT LEVEL AGGREGRATION =======================

students = students.rename(columns={'program': 'department'})
grades_with_dept = pd.merge(grades, students[['student_id', 'department']], on='student_id', how='left')

total_students = students.groupby('department')['student_id'].nunique().reset_index(name='total_students')

avg_grade_per_student = grades_with_dept.groupby(['student_id', 'department'])['points'].mean().reset_index(name='avg_grade')

top_students = avg_grade_per_student.sort_values(['department', 'avg_grade'], ascending=[True, False])
top_students_per_dept = top_students.groupby('department').first().reset_index()
top_students_per_dept = top_students_per_dept.rename(columns={
    'student_id': 'top_student_id',
    'avg_grade': 'top_student_grade'
})

department_summary = pd.merge(total_students, top_students_per_dept, on='department', how='left')
department_summary.to_csv(os.path.join(OUTPUT_DIR, 'department_top_students.csv'), index=False)
print("Department-level top student summary saved.")