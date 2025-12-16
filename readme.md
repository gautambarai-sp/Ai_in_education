# AI in Education: Interactive Research Dashboard

## 📊 Project Overview

This dashboard presents a comprehensive multi-institution research study on AI adoption in education, analyzing data from **40 professors** and **100 students** across **4 years (2022-2025)**, containing **560+ synthetic data points**.

### 🎯 Research Focus

**For Professors (As AI Facilitators):**
- Lesson planning & PowerPoint creation efficiency
- Automated grading with personal professor touch
- Administrative task automation (attendance, scheduling, reports)
- Student performance analytics & early intervention

**For Students (Learning AI Skills):**
- AI literacy, responsible use & skill acquisition while preserving creativity
- AI tool adoption & usage patterns
- Study efficiency & time management
- Diverse learning outcomes by learning style
- AI skill development pathway
- Collaboration & communication using AI

**Comparative Analysis:**
- Before AI adoption (2022) vs During AI adoption (2024-2025)
- Full Adoption vs Partial Restriction vs Full Restriction impact
- Future projections for 2026-2027

---

## 📁 Project Structure

```
.
├── ai_education_professor_data.csv          # 40 professors × 4 years = 160 records
├── ai_education_student_data.csv            # 100 students × 4 years = 400 records
├── ai_education_combined_data.csv           # Combined dataset
├── streamlit_app.py                         # Main dashboard application
├── generate_data.py                         # Data generation script
├── requirements.txt                         # Python dependencies
└── README.md                                # This file
```

---

## 🚀 Quick Start Guide

### Option 1: Local Deployment (Recommended for Development)

**Step 1: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 2: Run the Dashboard**
```bash
streamlit run streamlit_app.py
```

The dashboard will open in your default browser at `http://localhost:8501`

---

### Option 2: Cloud Deployment (Production)

#### **A. Deploy on Streamlit Cloud (Free & Easiest)**

1. **Push your code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "AI in Education Dashboard"
   git push origin main
   ```

2. **Deploy to Streamlit Cloud:**
   - Go to https://streamlit.io/cloud
   - Click "New app"
   - Select your GitHub repo, branch, and file (`streamlit_app.py`)
   - Click "Deploy"

3. **Share your dashboard URL** - That's it! ✅

#### **B. Deploy on Heroku**

1. **Create Heroku account** at https://www.heroku.com

2. **Create `Procfile`:**
   ```
   web: streamlit run streamlit_app.py --logger.level=error
   ```

3. **Create `setup.sh`:**
   ```bash
   mkdir -p ~/.streamlit/
   echo "[server]
   headless = true
   port = $PORT
   enableXsrfProtection = false
   [logger]
   level = error" > ~/.streamlit/config.toml
   ```

4. **Deploy:**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

#### **C. Deploy on AWS/Google Cloud/Azure**

Use Docker containerization:

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "streamlit_app.py"]
```

Then push to your cloud provider.

---

## 📊 Dashboard Features

### 5 Main Pages:

1. **Overview Dashboard**
   - Key metrics (40 professors, 100 students, 4 years)
   - Year-over-year adoption growth
   - 3 critical insights (efficiency, performance, literacy)

2. **Professor Analytics**
   - Lesson planning efficiency (hours saved trend)
   - PPT content creation volume
   - Automated grading quality & time reduction
   - Administrative task automation impact
   - Student monitoring & intervention success

3. **Student Analytics**
   - AI literacy & responsible use evolution
   - Creativity preservation scores
   - Tool adoption patterns (brainstorming, assessment, collaboration)
   - Study efficiency metrics
   - Learning outcomes by style (Visual, Auditory, Reading-Writing, Kinesthetic)
   - Skill development funnel
   - Language barrier reduction

4. **AI Restriction Impact**
   - Comparative analysis: Full Adoption vs Partial Restriction vs Full Restriction
   - Professor efficiency differences
   - Student outcome differences
   - Creativity preservation in restricted environments

5. **Future Projections & Insights**
   - Linear projections to 2026-2027
   - Strategic recommendations for institutions, professors, students
   - Risk mitigation strategies
   - Critical findings summary

### Visualizations:
- ✅ Line charts (trends over time)
- ✅ Bar charts (comparisons)
- ✅ Pie charts (distribution)
- ✅ Funnel charts (skill progression)
- ✅ Multi-series charts (adoption patterns)
- ✅ Interactive Plotly charts (hover for details)

---

## 📈 Key Statistics

### Data Characteristics:
- **Total Records**: 560 (160 professor + 400 student records)
- **Time Period**: 2022-2025 (4 years of monthly aggregations)
- **Professors**: 40 unique individuals with unique characteristics
  - Departments: CS, Business, Engineering, Liberal Arts, Data Science
  - Tenure: 2-25 years
  - Tech Adoption Levels: Early Adopter (35%), Moderate (45%), Traditional (20%)
  - AI Restrictions: Full Adoption (60%), Partial (25%), Full (15%)

- **Students**: 100 unique individuals with unique characteristics
  - Years of Study: Year 1, 2, 3, 4
  - Learning Styles: Visual, Auditory, Reading-Writing, Kinesthetic
  - Majors: CS, Business, Engineering, Liberal Arts, Data Science
  - AI Restrictions: Full Adoption (70%), Partial (20%), Full (10%)

### Key Findings:
- **60% professor time savings** on lesson planning (2022→2025)
- **14% GPA improvement** with AI adoption
- **92% student AI adoption rate** by 2025
- **81% intervention success rate** for at-risk students
- **55-75% language barrier reduction** for international collaboration
- **Visual learners show +15% performance improvement** (best outcome)

---

## 🔧 Customization

### Modify Data Generation:
Edit `generate_data.py` to adjust:
- Number of professors/students
- Time period
- Metric ranges
- Restriction distributions

```python
# Example: Increase professor count from 40 to 80
for prof_id in range(1, 81):  # Changed from 1, 41
    ...
```

### Modify Dashboard:
Edit `streamlit_app.py` to:
- Change colors (update hex codes in chart colors)
- Add/remove pages (modify `page` radio button)
- Change chart types (swap `go.Bar` for `go.Scatter`, etc.)
- Add new metrics (calculate from existing columns)

---

## 💾 Data Files Explained

### `ai_education_professor_data.csv`
**160 rows × 16 columns**

| Column | Description |
|--------|-------------|
| Entity_Type | "Professor" |
| ID | PROF_001 to PROF_040 (repeated 4× for each year) |
| Department | Computer Science, Business, Engineering, etc. |
| Tenure_Years | 2-25 years of teaching |
| Tech_Adoption_Level | Early Adopter / Moderate / Traditional |
| AI_Restriction_Status | Full Adoption / Partial Restriction / Full Restriction |
| Year | 2022, 2023, 2024, 2025 |
| Hours_Saved_Lesson_Planning_Per_Week | 0-8 hours |
| PPTs_Created_Per_Month | 1-15 presentations |
| Assignments_Graded_Per_Semester | 50-250 assignments |
| Grading_Quality_Score | 0.75-0.97 (quality metric) |
| Grading_Time_Hours_Per_Semester | 3-16 hours |
| Hours_Saved_Admin_Per_Week | 0-6 hours (attendance, scheduling, reports) |
| Students_Monitored | 10-150 students |
| At_Risk_Students_Identified | 2-50 students per professor |
| Intervention_Success_Rate | 0.40-0.88 (percentage) |

### `ai_education_student_data.csv`
**400 rows × 25 columns**

| Column | Description |
|--------|-------------|
| Entity_Type | "Student" |
| ID | STU_001 to STU_100 (repeated 4× for each year) |
| Major | Computer Science, Business, Engineering, etc. |
| Year_of_Study | Year 1, 2, 3, 4 |
| Learning_Style | Visual / Auditory / Reading-Writing / Kinesthetic |
| AI_Restriction_Status | Full Adoption / Partial Restriction / Full Restriction |
| Year | 2022, 2023, 2024, 2025 |
| AI_Literacy_Score | 20-90 (0-100 scale) |
| Responsible_Use_Awareness | 15-92 (0-100 scale) |
| Creativity_Preservation_Score | 60-95 (maintains creativity despite AI use) |
| AI_Tool_Adoption_Rate | 0.05-0.95 (% of students using AI) |
| Uses_AI_For_Brainstorming | 0.02-0.92 (% using for brainstorming) |
| Uses_AI_For_Assessment | 0.01-0.88 (% using for assignments) |
| Uses_AI_For_Collaboration | 0.01-0.80 (% using for group work) |
| Hours_Per_Assignment | 3-12 hours |
| GPA | 2.5-3.9 (0-4.0 scale) |
| Assignment_Completion_Rate | 0.75-0.97 (% of assignments completed) |
| Performance_Improvement_Percent | 0-30% improvement |
| Skill_Awareness_Level | 10-98 (% aware of AI skills) |
| Skill_Beginner_Level | 5-90 (% at beginner level) |
| Skill_Intermediate_Level | 2-70 (% at intermediate level) |
| Skill_Advanced_Level | 0-45 (% at advanced level) |
| Uses_AI_Collaboration_Tools | 0.02-0.88 (% using collaboration AI) |
| Language_Barrier_Reduction_Percent | 0-75 (% reduction in barriers) |
| Team_Project_Success_Rate | 0.65-0.97 (success rate) |

---

## 🎓 Use Cases

### For Presentations:
- Export charts as PNGs from Streamlit (⬇️ button on each chart)
- Use insights for conference presentations
- Share dashboard link with stakeholders

### For Academic Papers:
- Extract aggregated statistics from each page
- Use visualizations as figures
- Reference findings in literature review

### For Institutional Decision-Making:
- Inform AI adoption policies
- Guide technology investment decisions
- Plan professor training programs
- Design curriculum updates

### For Research Extensions:
- Modify data generation to model different scenarios
- Add new variables (cost analysis, student satisfaction, etc.)
- Compare across institutions
- Analyze specific department outcomes

---

## 🐛 Troubleshooting

### "Module not found" error
```bash
pip install --upgrade streamlit pandas numpy plotly
```

### Dashboard runs slow
- Dashboard caches data on first load
- Subsequent runs are instant
- For very large datasets, consider optimizing Plotly rendering

### Charts not showing
- Ensure Plotly is installed: `pip install plotly>=5.0`
- Clear browser cache and refresh

### Port 8501 already in use
```bash
streamlit run streamlit_app.py --server.port 8502
```

---

## 📞 Support & Questions

For issues or customizations:
1. Check Streamlit docs: https://docs.streamlit.io
2. Check Plotly docs: https://plotly.com/python
3. Review data generation script for custom fields

---

## 📜 License & Attribution

This research dashboard was created for an AI in Education exhibition presentation. 
- **Data**: Synthetic (created for research purposes)
- **Visualization**: Streamlit + Plotly
- **Created**: December 2025

---

## 🚀 Next Steps

1. **Customize the data** - Modify number of professors/students or metrics
2. **Add your branding** - Update colors, titles, logos
3. **Deploy online** - Use Streamlit Cloud, Heroku, or cloud provider
4. **Share the link** - Embed in presentations or websites
5. **Iterate** - Gather feedback and add new insights

---

**Happy exploring! 🎓📊**
