import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style='whitegrid')

TRANSFORMED_DIR = 'data/transformed'
OUTPUT_DIR = 'outputs/visualizations'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ================= STUDENT LEVEL VISUALS ===================
student_df = pd.read_csv(os.path.join(TRANSFORMED_DIR, 'student_engagment_summary.csv'))

# Scatter: login count vs avg grade
plt.figure(figsize=(8, 6))
sns.scatterplot(data=student_df, x='login_count', y='avg_grade', hue='program')
plt.title('Login Count vs Average Grade')
plt.xlabel('Login Count')
plt.ylabel('Average Grade')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'student_login_vs_grade.png'))
plt.close()

# Scatter: total_hours_spent vs avg grade
plt.figure(figsize=(8, 6))
sns.scatterplot(data=student_df, x='total_hours_spent', y='avg_grade', hue='program')
plt.title('Total Hours Spent vs Average Grade')
plt.xlabel('Total Hours Spent')
plt.ylabel('Average Grade')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'student_hours_vs_grade.png'))
plt.close()

# Bar chart: content access count by student
top_students = student_df.sort_values(by='content_access_count', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(data=top_students, x='student_id', y='content_access_count', hue='program')
plt.title('Top 10 Students by Content Access Count')
plt.xlabel('Student ID')
plt.ylabel('Content Access Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'top10_students_content_access.png'))
plt.close()

# ================= COURSE LEVEL VISUALS ===================
course_df = pd.read_csv(os.path.join(TRANSFORMED_DIR, 'course_assignment_status_summary.csv'))

# Melt for stacked bar plot
melted_course = course_df.melt(id_vars=['course_id', 'assignment_id'], 
                               var_name='status', value_name='count')

plt.figure(figsize=(12, 6))
sns.barplot(data=melted_course, x='assignment_id', y='count', hue='status')
plt.title('Assignment Submission Status by Assignment ID')
plt.xlabel('Assignment ID')
plt.ylabel('Number of Students')
plt.xticks(rotation=45)
plt.legend(title='Status')
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'course_assignment_submission_status.png'))
plt.close()

# ================= DEPARTMENT LEVEL VISUALS ===================
dept_df = pd.read_csv(os.path.join(TRANSFORMED_DIR, 'department_top_students.csv'))

# Bar chart: total students per department
plt.figure(figsize=(8, 6))
sns.barplot(data=dept_df, x='department', y='total_students')
plt.title('Total Students per Department')
plt.xlabel('Department')
plt.ylabel('Total Students')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'department_total_students.png'))
plt.close()

# Bar chart: top student grade per department
plt.figure(figsize=(8, 6))
sns.barplot(data=dept_df, x='department', y='top_student_grade')
plt.title('Top Student Grade per Department')
plt.xlabel('Department')
plt.ylabel('Top Student Grade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, 'department_top_student_grade.png'))
plt.close()

print("All visualizations generated and saved to outputs/visualizations/")