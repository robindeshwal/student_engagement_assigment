import pandas as pd
import os

INPUT_DIR = 'data/cleaned'
OUTPUT_DIR = 'data/transformed'
os.makedirs(OUTPUT_DIR, exist_ok=True)

students = pd.read_csv(os.path.join(INPUT_DIR, 'student_data.csv'))
logins = pd.read_csv(os.path.join(INPUT_DIR, 'student_logins.csv'))
grades = pd.read_csv(os.path.join(INPUT_DIR, 'assignment_submissions.csv'))
courses = pd.read_csv(os.path.join(INPUT_DIR, 'course_data.csv'))

# ================ STUDENT LEVEL AGGREGATION ===========================
login_count = logins.groupby('student_id').size().reset_index(name='login_count')
avg_grades = grades.groupby('student_id')['points'].mean().reset_index(name='avg_grade')

# Merge to form student-level engagement summary
engamement = pd.merge(students, login_count, on='student_id', how='left')
engamement = pd.merge(engamement, avg_grades, on='student_id', how='left')

engamement.to_csv(os.path.join(OUTPUT_DIR, 'student_engagment_summary.csv'))
print("Transfromed data saved.")

# =============== COURSE LEVEL AGGREGRATION ============================

# Assume each student is linked to one course (based on student_data.csv having course_id)

# students_renamed = students.rename(columns={'program': 'course_id'})

# student_course = students_renamed[['student_id', 'course_id']]
# grades_sc = pd.merge(student_course, grades, on='student_id', how='inner')
# logins_sc = pd.merge(student_course, logins, on='student_id', how='inner')

# course_grades = grades_sc.groupby('course_id')['points'].mean().reset_index(name='avg_grade')
# course_logins = logins_sc.groupby('course_id').size().reset_index(name='total_logins')

# course_summary = pd.merge(course_grades, course_logins, on='course_id', how='outer')
# course_summary = pd.merge(course_summary, courses, on='course_id', how='left')

# course_summary.to_csv(os.path.join(OUTPUT_DIR, 'course_engagement_summary.csv'), index=False)
# print("Course-level engagement summary saved.")


# =============== DEPARTMENT LEVEL AGGREGRATION =======================
# Join student -> course -> department

# students_with_dept = pd.merge(students_renamed, courses, on='course_id', how='left')

# grades_sd = pd.merge(students_with_dept[['student_id', 'department']], grades, on='student_id', how='inner')
# logins_sd = pd.merge(students_with_dept[['student_id', 'department']], logins, on='student_id', how='inner')

# dept_grades = grades_sd.groupby('department')['points'].mean().reset_index(name='avg_grade')
# dept_logins = logins_sd.groupby('department').size().reset_index(name='total_logins')

# department_summary = pd.merge(dept_grades, dept_logins, on='department', how='outer')
# department_summary.to_csv(os.path.join(OUTPUT_DIR, 'department_engagement_summary.csv'), index=False)
# print("Department-level engagement summary saved.")
