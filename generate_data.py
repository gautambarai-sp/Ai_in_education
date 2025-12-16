import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# ============================================================================
# SECTION 1: PROFESSOR DATA (40 professors with unique characteristics)
# ============================================================================

professor_data = []

for prof_id in range(1, 41):
    # Unique characteristics for each professor
    tenure_years = np.random.randint(2, 25)
    tech_adoption_level = np.random.choice(['Early Adopter', 'Moderate', 'Traditional'], p=[0.35, 0.45, 0.20])
    ai_restriction = np.random.choice(['Full Adoption', 'Partial Restriction', 'Full Restriction'], p=[0.60, 0.25, 0.15])
    department = np.random.choice(['Computer Science', 'Business', 'Engineering', 'Liberal Arts', 'Data Science'])
    
    # 2022-2025 Timeline Data
    for year in range(2022, 2026):
        # Lesson Planning & Content Creation (hours saved per week)
        if year == 2022:  # Pre-AI adoption
            hours_saved_lesson_planning = np.random.uniform(0, 1)
            ppts_created_per_month = np.random.randint(2, 5)
        elif year == 2023:  # Early adoption
            hours_saved_lesson_planning = np.random.uniform(1, 3)
            ppts_created_per_month = np.random.randint(4, 8)
        elif year == 2024:  # Active adoption
            hours_saved_lesson_planning = np.random.uniform(3, 6)
            ppts_created_per_month = np.random.randint(7, 12)
        else:  # 2025
            hours_saved_lesson_planning = np.random.uniform(5, 8)
            ppts_created_per_month = np.random.randint(10, 15)
        
        # Adjust for AI restriction level
        if ai_restriction == 'Full Restriction':
            hours_saved_lesson_planning = hours_saved_lesson_planning * 0.1
            ppts_created_per_month = max(1, int(ppts_created_per_month * 0.2))
        elif ai_restriction == 'Partial Restriction':
            hours_saved_lesson_planning = hours_saved_lesson_planning * 0.5
            ppts_created_per_month = int(ppts_created_per_month * 0.6)
        
        # Automated Grading (assignments graded, quality score, time in hours)
        if year <= 2022:
            assignments_graded = np.random.randint(50, 100)
            grading_quality_score = np.random.uniform(0.75, 0.85)
            grading_time_hours = np.random.uniform(12, 16)
        elif year == 2023:
            assignments_graded = np.random.randint(80, 150)
            grading_quality_score = np.random.uniform(0.82, 0.90)
            grading_time_hours = np.random.uniform(8, 12)
        elif year == 2024:
            assignments_graded = np.random.randint(120, 200)
            grading_quality_score = np.random.uniform(0.88, 0.95)
            grading_time_hours = np.random.uniform(4, 8)
        else:  # 2025
            assignments_graded = np.random.randint(150, 250)
            grading_quality_score = np.random.uniform(0.92, 0.97)
            grading_time_hours = np.random.uniform(3, 6)
        
        # Administrative Task Automation (hours saved per week)
        if year <= 2022:
            hours_saved_admin = np.random.uniform(0, 0.5)
        elif year == 2023:
            hours_saved_admin = np.random.uniform(0.5, 2)
        elif year == 2024:
            hours_saved_admin = np.random.uniform(2, 4)
        else:  # 2025
            hours_saved_admin = np.random.uniform(3.5, 6)
        
        if ai_restriction == 'Full Restriction':
            hours_saved_admin = hours_saved_admin * 0.05
        elif ai_restriction == 'Partial Restriction':
            hours_saved_admin = hours_saved_admin * 0.4
        
        # Student Performance Analytics (students monitored, at-risk identified, intervention success)
        if year <= 2022:
            students_monitored = np.random.randint(20, 40)
            at_risk_identified = int(students_monitored * np.random.uniform(0.1, 0.2))
            intervention_success_rate = np.random.uniform(0.40, 0.55)
        elif year == 2023:
            students_monitored = np.random.randint(40, 80)
            at_risk_identified = int(students_monitored * np.random.uniform(0.15, 0.25))
            intervention_success_rate = np.random.uniform(0.55, 0.70)
        elif year == 2024:
            students_monitored = np.random.randint(70, 120)
            at_risk_identified = int(students_monitored * np.random.uniform(0.18, 0.30))
            intervention_success_rate = np.random.uniform(0.68, 0.80)
        else:  # 2025
            students_monitored = np.random.randint(100, 150)
            at_risk_identified = int(students_monitored * np.random.uniform(0.20, 0.35))
            intervention_success_rate = np.random.uniform(0.75, 0.88)
        
        if ai_restriction == 'Full Restriction':
            students_monitored = int(students_monitored * 0.3)
            at_risk_identified = int(at_risk_identified * 0.3)
            intervention_success_rate = intervention_success_rate * 0.7
        elif ai_restriction == 'Partial Restriction':
            students_monitored = int(students_monitored * 0.6)
            intervention_success_rate = intervention_success_rate * 0.85
        
        professor_data.append({
            'Entity_Type': 'Professor',
            'ID': f'PROF_{prof_id:03d}',
            'Department': department,
            'Tenure_Years': tenure_years,
            'Tech_Adoption_Level': tech_adoption_level,
            'AI_Restriction_Status': ai_restriction,
            'Year': year,
            'Hours_Saved_Lesson_Planning_Per_Week': round(hours_saved_lesson_planning, 2),
            'PPTs_Created_Per_Month': ppts_created_per_month,
            'Assignments_Graded_Per_Semester': assignments_graded,
            'Grading_Quality_Score': round(grading_quality_score, 3),
            'Grading_Time_Hours_Per_Semester': round(grading_time_hours, 2),
            'Hours_Saved_Admin_Per_Week': round(hours_saved_admin, 2),
            'Students_Monitored': students_monitored,
            'At_Risk_Students_Identified': at_risk_identified,
            'Intervention_Success_Rate': round(intervention_success_rate, 3)
        })

prof_df = pd.DataFrame(professor_data)
print("✓ Professor Data Created:", prof_df.shape)

# ============================================================================
# SECTION 2: STUDENT DATA (100 students with unique characteristics)
# ============================================================================

student_data = []

for student_id in range(1, 101):
    # Unique characteristics for each student
    year_of_study = np.random.choice(['Year 1', 'Year 2', 'Year 3', 'Year 4'])
    learning_style = np.random.choice(['Visual', 'Auditory', 'Reading-Writing', 'Kinesthetic'])
    ai_restriction = np.random.choice(['Full Adoption', 'Partial Restriction', 'Full Restriction'], p=[0.70, 0.20, 0.10])
    major = np.random.choice(['Computer Science', 'Business', 'Engineering', 'Liberal Arts', 'Data Science'])
    
    # 2022-2025 Timeline Data
    for year in range(2022, 2026):
        # AI Literacy & Skill Acquisition (0-100 scale)
        if year == 2022:
            ai_literacy_score = np.random.uniform(20, 35)
            responsible_use_awareness = np.random.uniform(15, 30)
            creativity_preservation_score = np.random.uniform(75, 90)
        elif year == 2023:
            ai_literacy_score = np.random.uniform(35, 55)
            responsible_use_awareness = np.random.uniform(30, 50)
            creativity_preservation_score = np.random.uniform(70, 85)
        elif year == 2024:
            ai_literacy_score = np.random.uniform(55, 75)
            responsible_use_awareness = np.random.uniform(55, 75)
            creativity_preservation_score = np.random.uniform(65, 80)
        else:  # 2025
            ai_literacy_score = np.random.uniform(70, 90)
            responsible_use_awareness = np.random.uniform(75, 92)
            creativity_preservation_score = np.random.uniform(60, 78)
        
        # Adjust for AI restriction
        if ai_restriction == 'Full Restriction':
            ai_literacy_score = ai_literacy_score * 0.4
            responsible_use_awareness = responsible_use_awareness * 0.9
            creativity_preservation_score = np.min([creativity_preservation_score + 15, 95])
        elif ai_restriction == 'Partial Restriction':
            ai_literacy_score = ai_literacy_score * 0.7
            responsible_use_awareness = responsible_use_awareness * 0.95
        
        # AI Tool Adoption & Usage Patterns
        if year == 2022:
            ai_tool_adoption_rate = np.random.uniform(0.05, 0.15)
            uses_ai_for_brainstorming = np.random.uniform(0.02, 0.10)
            uses_ai_for_assessment = np.random.uniform(0.01, 0.08)
            uses_ai_for_collaboration = np.random.uniform(0.01, 0.05)
        elif year == 2023:
            ai_tool_adoption_rate = np.random.uniform(0.30, 0.50)
            uses_ai_for_brainstorming = np.random.uniform(0.25, 0.40)
            uses_ai_for_assessment = np.random.uniform(0.20, 0.35)
            uses_ai_for_collaboration = np.random.uniform(0.15, 0.30)
        elif year == 2024:
            ai_tool_adoption_rate = np.random.uniform(0.65, 0.82)
            uses_ai_for_brainstorming = np.random.uniform(0.55, 0.70)
            uses_ai_for_assessment = np.random.uniform(0.50, 0.65)
            uses_ai_for_collaboration = np.random.uniform(0.40, 0.55)
        else:  # 2025
            ai_tool_adoption_rate = np.random.uniform(0.85, 0.95)
            uses_ai_for_brainstorming = np.random.uniform(0.80, 0.92)
            uses_ai_for_assessment = np.random.uniform(0.75, 0.88)
            uses_ai_for_collaboration = np.random.uniform(0.65, 0.80)
        
        if ai_restriction == 'Full Restriction':
            ai_tool_adoption_rate = ai_tool_adoption_rate * 0.1
            uses_ai_for_brainstorming = uses_ai_for_brainstorming * 0.15
            uses_ai_for_assessment = uses_ai_for_assessment * 0.1
            uses_ai_for_collaboration = uses_ai_for_collaboration * 0.2
        elif ai_restriction == 'Partial Restriction':
            ai_tool_adoption_rate = ai_tool_adoption_rate * 0.5
            uses_ai_for_brainstorming = uses_ai_for_brainstorming * 0.6
            uses_ai_for_assessment = uses_ai_for_assessment * 0.5
            uses_ai_for_collaboration = uses_ai_for_collaboration * 0.7
        
        # Study Efficiency & Time Management
        if year == 2022:
            hours_per_assignment = np.random.uniform(8, 12)
            gpa = np.random.uniform(2.5, 3.5)
            assignment_completion_rate = np.random.uniform(0.75, 0.90)
        elif year == 2023:
            hours_per_assignment = np.random.uniform(6, 10)
            gpa = np.random.uniform(2.7, 3.7)
            assignment_completion_rate = np.random.uniform(0.82, 0.92)
        elif year == 2024:
            hours_per_assignment = np.random.uniform(4, 7)
            gpa = np.random.uniform(3.0, 3.8)
            assignment_completion_rate = np.random.uniform(0.88, 0.95)
        else:  # 2025
            hours_per_assignment = np.random.uniform(3, 5)
            gpa = np.random.uniform(3.2, 3.9)
            assignment_completion_rate = np.random.uniform(0.90, 0.97)
        
        if ai_restriction == 'Full Restriction':
            hours_per_assignment = hours_per_assignment * 1.3
            gpa = gpa * 0.95
            assignment_completion_rate = assignment_completion_rate * 0.90
        elif ai_restriction == 'Partial Restriction':
            hours_per_assignment = hours_per_assignment * 1.1
            gpa = gpa * 0.98
            assignment_completion_rate = assignment_completion_rate * 0.95
        
        # Diverse Learning Outcomes by Learning Style
        learning_style_multiplier = {
            'Visual': 1.15,
            'Auditory': 1.10,
            'Reading-Writing': 1.12,
            'Kinesthetic': 1.08
        }
        
        if year == 2022:
            performance_improvement = np.random.uniform(0, 5) * learning_style_multiplier[learning_style]
        elif year == 2023:
            performance_improvement = np.random.uniform(5, 12) * learning_style_multiplier[learning_style]
        elif year == 2024:
            performance_improvement = np.random.uniform(12, 22) * learning_style_multiplier[learning_style]
        else:  # 2025
            performance_improvement = np.random.uniform(18, 30) * learning_style_multiplier[learning_style]
        
        if ai_restriction == 'Full Restriction':
            performance_improvement = performance_improvement * 0.5
        elif ai_restriction == 'Partial Restriction':
            performance_improvement = performance_improvement * 0.75
        
        # AI Skill Development Pathway (proficiency level %)
        if year == 2022:
            skill_awareness_level = np.random.uniform(10, 25)
            skill_beginner_level = np.random.uniform(5, 15)
            skill_intermediate_level = np.random.uniform(2, 8)
            skill_advanced_level = np.random.uniform(0, 3)
        elif year == 2023:
            skill_awareness_level = np.random.uniform(50, 75)
            skill_beginner_level = np.random.uniform(30, 50)
            skill_intermediate_level = np.random.uniform(10, 25)
            skill_advanced_level = np.random.uniform(3, 10)
        elif year == 2024:
            skill_awareness_level = np.random.uniform(75, 95)
            skill_beginner_level = np.random.uniform(55, 75)
            skill_intermediate_level = np.random.uniform(30, 50)
            skill_advanced_level = np.random.uniform(10, 25)
        else:  # 2025
            skill_awareness_level = np.random.uniform(90, 98)
            skill_beginner_level = np.random.uniform(75, 90)
            skill_intermediate_level = np.random.uniform(50, 70)
            skill_advanced_level = np.random.uniform(25, 45)
        
        if ai_restriction == 'Full Restriction':
            skill_awareness_level = skill_awareness_level * 0.3
            skill_beginner_level = skill_beginner_level * 0.2
            skill_intermediate_level = skill_intermediate_level * 0.1
            skill_advanced_level = skill_advanced_level * 0.05
        elif ai_restriction == 'Partial Restriction':
            skill_awareness_level = skill_awareness_level * 0.6
            skill_beginner_level = skill_beginner_level * 0.5
            skill_intermediate_level = skill_intermediate_level * 0.4
            skill_advanced_level = skill_advanced_level * 0.3
        
        # Collaboration & Communication Using AI
        if year == 2022:
            uses_ai_collaboration_tools = np.random.uniform(0.02, 0.10)
            language_barrier_reduction = np.random.uniform(0, 5)
            team_project_success_rate = np.random.uniform(0.65, 0.80)
        elif year == 2023:
            uses_ai_collaboration_tools = np.random.uniform(0.25, 0.45)
            language_barrier_reduction = np.random.uniform(10, 25)
            team_project_success_rate = np.random.uniform(0.75, 0.85)
        elif year == 2024:
            uses_ai_collaboration_tools = np.random.uniform(0.55, 0.70)
            language_barrier_reduction = np.random.uniform(30, 50)
            team_project_success_rate = np.random.uniform(0.82, 0.92)
        else:  # 2025
            uses_ai_collaboration_tools = np.random.uniform(0.75, 0.88)
            language_barrier_reduction = np.random.uniform(55, 75)
            team_project_success_rate = np.random.uniform(0.88, 0.97)
        
        if ai_restriction == 'Full Restriction':
            uses_ai_collaboration_tools = uses_ai_collaboration_tools * 0.2
            language_barrier_reduction = language_barrier_reduction * 0.3
            team_project_success_rate = team_project_success_rate * 0.90
        elif ai_restriction == 'Partial Restriction':
            uses_ai_collaboration_tools = uses_ai_collaboration_tools * 0.6
            language_barrier_reduction = language_barrier_reduction * 0.65
            team_project_success_rate = team_project_success_rate * 0.95
        
        student_data.append({
            'Entity_Type': 'Student',
            'ID': f'STU_{student_id:03d}',
            'Major': major,
            'Year_of_Study': year_of_study,
            'Learning_Style': learning_style,
            'AI_Restriction_Status': ai_restriction,
            'Year': year,
            'AI_Literacy_Score': round(ai_literacy_score, 2),
            'Responsible_Use_Awareness': round(responsible_use_awareness, 2),
            'Creativity_Preservation_Score': round(creativity_preservation_score, 2),
            'AI_Tool_Adoption_Rate': round(ai_tool_adoption_rate, 3),
            'Uses_AI_For_Brainstorming': round(uses_ai_for_brainstorming, 3),
            'Uses_AI_For_Assessment': round(uses_ai_for_assessment, 3),
            'Uses_AI_For_Collaboration': round(uses_ai_for_collaboration, 3),
            'Hours_Per_Assignment': round(hours_per_assignment, 2),
            'GPA': round(gpa, 2),
            'Assignment_Completion_Rate': round(assignment_completion_rate, 3),
            'Performance_Improvement_Percent': round(performance_improvement, 2),
            'Skill_Awareness_Level': round(skill_awareness_level, 2),
            'Skill_Beginner_Level': round(skill_beginner_level, 2),
            'Skill_Intermediate_Level': round(skill_intermediate_level, 2),
            'Skill_Advanced_Level': round(skill_advanced_level, 2),
            'Uses_AI_Collaboration_Tools': round(uses_ai_collaboration_tools, 3),
            'Language_Barrier_Reduction_Percent': round(language_barrier_reduction, 2),
            'Team_Project_Success_Rate': round(team_project_success_rate, 3)
        })

student_df = pd.DataFrame(student_data)
print("✓ Student Data Created:", student_df.shape)

# Save to output directory
prof_df.to_csv('/mnt/user-data/outputs/ai_education_professor_data.csv', index=False)
student_df.to_csv('/mnt/user-data/outputs/ai_education_student_data.csv', index=False)

# Create combined dataset for dashboard
combined_df = pd.concat([prof_df, student_df], ignore_index=True)
combined_df.to_csv('/mnt/user-data/outputs/ai_education_combined_data.csv', index=False)

print("\n✓ All synthetic data files created successfully!")
print(f"  - Professor records: {len(prof_df)}")
print(f"  - Student records: {len(student_df)}")
print(f"  - Total combined records: {len(combined_df)}")
