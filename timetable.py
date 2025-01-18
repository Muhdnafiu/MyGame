# Importing required libraries
import matplotlib.pyplot as plt
import pandas as pd

# Data for the timetable
days = ['Monday', 'Wednesday', 'Saturday', 'Tuesday', 'Thursday', 'Friday', 'Sunday']
activities = [
    ["Fajr & Quran (30m)", "School Hours", "Lunch/Rest (1h)", "Homework (1-2h)", "Asr & Break (30m)", 
     "Reading (1h)", "Family/Personal (1h)", "Isha & Sleep Prep (50m)"],
    ["Fajr & Quran (30m)", "School Hours", "Lunch/Rest (1h)", "Homework (1-2h)", "Asr & Break (30m)", 
     "Reading (1h)", "Family/Personal (1h)", "Isha & Sleep Prep (50m)"],
    ["Fajr & Quran (30m)", "School Hours", "Lunch/Rest (1h)", "Homework (1-2h)", "Asr & Break (30m)", 
     "Reading (1h)", "Family/Personal (1h)", "Isha & Sleep Prep (50m)"],
    ["Fajr & Quran (30m)", "Exercise (30m)", "Focused Study (2h)", "Dhuhr & Relaxation (30m)", 
     "Skill Development (2h)", "Asr & Break (30m)", "Book Reading (1h)", "Isha & Sleep Prep (50m)"],
    ["Fajr & Quran (30m)", "Exercise (30m)", "Focused Study (2h)", "Dhuhr & Relaxation (30m)", 
     "Skill Development (2h)", "Asr & Break (30m)", "Book Reading (1h)", "Isha & Sleep Prep (50m)"],
    ["Fajr & Quran (30m)", "Exercise (30m)", "Focused Study (2h)", "Dhuhr & Relaxation (30m)", 
     "Skill Development (2h)", "Asr & Break (30m)", "Book Reading (1h)", "Isha & Sleep Prep (50m)"],
    ["Fajr & Quran (30m)", "Relax/Outdoor (1h)", "Focused Study (2h)", "Dhuhr & Rest (30m)", 
     "Family/Skill Building (2h)", "Asr & Break (30m)", "Reflection/Goals (30m)", "Early Sleep (1h)"]
]

# Create a dataframe for better visualization
df = pd.DataFrame(activities, index=days, columns=["Morning 1", "Morning 2", "Afternoon 1", "Afternoon 2", 
                                                   "Afternoon 3", "Evening 1", "Evening 2", "Night"])

# Plotting the timetable
fig, ax = plt.subplots(figsize=(12, 6))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, rowLabels=df.index, loc='center', cellLoc='center')

# Styling the table
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(df.columns))))

# Display the timetable
plt.title("Weekly Timetable", fontsize=14, fontweight='bold', pad=20)
plt.show()
