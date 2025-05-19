import pandas as pd
import matplotlib.pyplot as plt
import os


INPUT_FILE = 'data/transformed/student_engagment_summary.csv'
OUTPUT_DIR = 'outputs/visualizations'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# import ipdb; ipdb.set_trace()
df = pd.read_csv(INPUT_FILE)

plt.figure(figsize=(10, 6))
plt.scatter(df['login_count'], df['avg_grade'], alpha=0.6)
plt.title('Login Count vs Average Grade')
plt.xlabel('Login Count')
plt.ylabel('Average Grade')
plt.grid(True)
plt.savefig(os.path.join(OUTPUT_DIR, 'login_vs_grade.png'))

print("Visualization saved.")