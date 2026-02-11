import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Page Config
st.set_page_config(
    page_title="AI in Education Analytics",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🎓"
)

# Load Data
@st.cache_data
def load_data():
    try:
        prof_df = pd.read_csv('data/ai_education_professor_data.csv')
        student_df = pd.read_csv('data/ai_education_student_data.csv')
    except:
        try:
            prof_df = pd.read_csv('/mnt/user-data/outputs/ai_education_professor_data.csv')
            student_df = pd.read_csv('/mnt/user-data/outputs/ai_education_student_data.csv')
        except:
            prof_df = pd.read_csv('ai_education_professor_data.csv')
            student_df = pd.read_csv('ai_education_student_data.csv')
    return prof_df, student_df

prof_df, student_df = load_data()

# Enhanced Custom CSS
st.markdown("""
<style>
    /* Main container styling */
    .main {
        padding-top: 1rem;
    }

    /* Hide default Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Custom header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
    }

    .main-header h1 {
        color: white;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }

    .main-header p {
        color: rgba(255,255,255,0.9);
        font-size: 1.1rem;
        margin-top: 0.5rem;
    }

    /* KPI Card Styling */
    .kpi-container {
        display: flex;
        gap: 1rem;
        margin-bottom: 2rem;
    }

    .kpi-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9ff 100%);
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border: 1px solid rgba(102, 126, 234, 0.1);
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        flex: 1;
    }

    .kpi-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.2);
    }

    .kpi-icon {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }

    .kpi-value {
        font-size: 2.2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .kpi-label {
        color: #666;
        font-size: 0.9rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .kpi-delta {
        font-size: 0.85rem;
        padding: 0.25rem 0.5rem;
        border-radius: 20px;
        display: inline-block;
        margin-top: 0.5rem;
    }

    .kpi-delta.positive {
        background: rgba(34, 197, 94, 0.1);
        color: #22c55e;
    }

    .kpi-delta.negative {
        background: rgba(239, 68, 68, 0.1);
        color: #ef4444;
    }

    /* Metric Card (Gradient) */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
        transition: transform 0.3s ease;
    }

    .metric-card:hover {
        transform: scale(1.02);
    }

    .metric-card h3 {
        font-size: 2.5rem;
        margin: 0;
        font-weight: 700;
    }

    .metric-card p {
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
        font-size: 0.95rem;
    }

    /* Insight Box */
    .insight-box {
        background: linear-gradient(135deg, #f8f9ff 0%, #ffffff 100%);
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }

    .insight-box h4 {
        color: #667eea;
        margin: 0 0 0.5rem 0;
        font-weight: 600;
    }

    /* Section Headers */
    .section-header {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin: 2rem 0 1.5rem 0;
        padding-bottom: 0.75rem;
        border-bottom: 2px solid #f0f2f6;
    }

    .section-header h2 {
        margin: 0;
        font-size: 1.5rem;
        color: #1a1a2e;
    }

    .section-number {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        width: 32px;
        height: 32px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.9rem;
    }

    /* Stats Grid */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
        margin: 1.5rem 0;
    }

    .stat-item {
        background: white;
        padding: 1.25rem;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        border: 1px solid #f0f2f6;
    }

    .stat-item .label {
        color: #666;
        font-size: 0.85rem;
        margin-bottom: 0.25rem;
    }

    .stat-item .value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1a1a2e;
    }

    /* Comparison Cards */
    .comparison-card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin-bottom: 1rem;
    }

    .comparison-card.full-adoption {
        border-top: 4px solid #22c55e;
    }

    .comparison-card.partial {
        border-top: 4px solid #f97316;
    }

    .comparison-card.restricted {
        border-top: 4px solid #ef4444;
    }

    /* Info Cards */
    .info-card {
        background: linear-gradient(135deg, #e0e7ff 0%, #f0f4ff 100%);
        border-radius: 12px;
        padding: 1.25rem;
        border: 1px solid rgba(102, 126, 234, 0.2);
    }

    .info-card.success {
        background: linear-gradient(135deg, #dcfce7 0%, #f0fdf4 100%);
        border-color: rgba(34, 197, 94, 0.2);
    }

    .info-card.warning {
        background: linear-gradient(135deg, #fef3c7 0%, #fffbeb 100%);
        border-color: rgba(249, 115, 22, 0.2);
    }

    /* Sidebar Styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8f9ff 0%, #ffffff 100%);
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f8f9ff 0%, #ffffff 100%);
    }

    [data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }

    /* Chart container */
    .chart-container {
        background: white;
        border-radius: 16px;
        padding: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }

    /* Executive Summary Card */
    .exec-summary {
        background: linear-gradient(135deg, #1a1a2e 0%, #2d2d44 100%);
        color: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1.5rem 0;
    }

    .exec-summary h3 {
        color: #667eea;
        margin-top: 0;
    }

    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: #f8f9ff;
        border-radius: 8px;
        padding: 8px 16px;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }

    /* Download button */
    .download-btn {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        font-weight: 500;
    }

    /* Divider */
    .custom-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
        margin: 2rem 0;
        border: none;
    }

    /* Footer */
    .custom-footer {
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        background: linear-gradient(135deg, #f8f9ff 0%, #ffffff 100%);
        border-radius: 16px;
        border: 1px solid #f0f2f6;
    }

    .custom-footer p {
        color: #666;
        margin: 0.25rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Color Palette
COLORS = {
    'primary': '#667eea',
    'secondary': '#764ba2',
    'success': '#22c55e',
    'warning': '#f97316',
    'danger': '#ef4444',
    'info': '#3b82f6',
    'dark': '#1a1a2e',
    'light': '#f8f9ff'
}

CHART_COLORS = ['#667eea', '#764ba2', '#f97316', '#22c55e', '#3b82f6', '#ef4444']

# ============================================================================
# SIDEBAR - Navigation & Filters
# ============================================================================

with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <h2 style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0;">🎓 AI Education</h2>
        <p style="color: #666; font-size: 0.85rem;">Research Dashboard</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Navigation
    page = st.radio(
        "📍 Navigation",
        ["🏠 Executive Overview",
         "👨‍🏫 Professor Analytics",
         "👨‍🎓 Student Analytics",
         "⚖️ Restriction Impact",
         "🔮 Future Insights"],
        label_visibility="collapsed"
    )

    st.markdown("---")

    # Filters
    st.markdown("### 🎛️ Filters")

    # Year filter
    years = sorted(prof_df['Year'].unique())
    selected_years = st.multiselect(
        "📅 Select Years",
        options=years,
        default=years,
        help="Filter data by year"
    )

    # Department filter (for professors)
    if 'Department' in prof_df.columns:
        departments = ['All'] + sorted(prof_df['Department'].unique().tolist())
        selected_dept = st.selectbox(
            "🏛️ Department",
            options=departments,
            help="Filter professors by department"
        )
    else:
        selected_dept = 'All'

    # Restriction status filter
    restrictions = ['All'] + sorted(prof_df['AI_Restriction_Status'].unique().tolist())
    selected_restriction = st.selectbox(
        "🚦 Restriction Status",
        options=restrictions,
        help="Filter by AI restriction status"
    )

    # Learning style filter (for students)
    if 'Learning_Style' in student_df.columns:
        learning_styles = ['All'] + sorted(student_df['Learning_Style'].unique().tolist())
        selected_style = st.selectbox(
            "📚 Learning Style",
            options=learning_styles,
            help="Filter students by learning style"
        )
    else:
        selected_style = 'All'

    st.markdown("---")

    # Data export
    st.markdown("### 📥 Export Data")

    col1, col2 = st.columns(2)
    with col1:
        st.download_button(
            label="📊 Professors",
            data=prof_df.to_csv(index=False),
            file_name="professor_data.csv",
            mime="text/csv",
            use_container_width=True
        )
    with col2:
        st.download_button(
            label="🎓 Students",
            data=student_df.to_csv(index=False),
            file_name="student_data.csv",
            mime="text/csv",
            use_container_width=True
        )

# Apply filters
filtered_prof_df = prof_df[prof_df['Year'].isin(selected_years)]
filtered_student_df = student_df[student_df['Year'].isin(selected_years)]

if selected_dept != 'All' and 'Department' in prof_df.columns:
    filtered_prof_df = filtered_prof_df[filtered_prof_df['Department'] == selected_dept]

if selected_restriction != 'All':
    filtered_prof_df = filtered_prof_df[filtered_prof_df['AI_Restriction_Status'] == selected_restriction]
    filtered_student_df = filtered_student_df[filtered_student_df['AI_Restriction_Status'] == selected_restriction]

if selected_style != 'All' and 'Learning_Style' in student_df.columns:
    filtered_student_df = filtered_student_df[filtered_student_df['Learning_Style'] == selected_style]

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def create_gauge_chart(value, title, max_val=100, suffix=""):
    """Create a modern gauge chart"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        number={'suffix': suffix, 'font': {'size': 40, 'color': COLORS['dark']}},
        title={'text': title, 'font': {'size': 16, 'color': '#666'}},
        gauge={
            'axis': {'range': [0, max_val], 'tickwidth': 1, 'tickcolor': "#ddd"},
            'bar': {'color': COLORS['primary'], 'thickness': 0.75},
            'bgcolor': "white",
            'borderwidth': 0,
            'steps': [
                {'range': [0, max_val*0.33], 'color': 'rgba(239, 68, 68, 0.2)'},
                {'range': [max_val*0.33, max_val*0.66], 'color': 'rgba(249, 115, 22, 0.2)'},
                {'range': [max_val*0.66, max_val], 'color': 'rgba(34, 197, 94, 0.2)'}
            ],
            'threshold': {
                'line': {'color': COLORS['secondary'], 'width': 4},
                'thickness': 0.75,
                'value': value
            }
        }
    ))
    fig.update_layout(
        height=250,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'family': 'Inter, sans-serif'}
    )
    return fig

def create_trend_chart(df, x_col, y_col, title, color=COLORS['primary'], fill=True):
    """Create a modern trend line chart"""
    data = df.groupby(x_col)[y_col].mean().reset_index()

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=data[x_col],
        y=data[y_col],
        mode='lines+markers',
        line=dict(color=color, width=3, shape='spline'),
        marker=dict(size=10, color=color, line=dict(width=2, color='white')),
        fill='tozeroy' if fill else None,
        fillcolor=f'rgba{tuple(list(int(color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)) + [0.1])}' if fill else None,
        hovertemplate=f'<b>{title}</b><br>Year: %{{x}}<br>Value: %{{y:.2f}}<extra></extra>'
    ))

    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color=COLORS['dark'])),
        xaxis=dict(title='', gridcolor='#f0f2f6', showgrid=True),
        yaxis=dict(title='', gridcolor='#f0f2f6', showgrid=True),
        hovermode='x unified',
        height=350,
        margin=dict(l=40, r=40, t=60, b=40),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'family': 'Inter, sans-serif'}
    )
    return fig

def create_bar_chart(df, x_col, y_col, title, colors=None, horizontal=False):
    """Create a modern bar chart"""
    data = df.groupby(x_col)[y_col].mean().reset_index()

    if colors is None:
        colors = CHART_COLORS[:len(data)]

    fig = go.Figure()

    if horizontal:
        fig.add_trace(go.Bar(
            y=data[x_col],
            x=data[y_col],
            orientation='h',
            marker=dict(color=colors, cornerradius=8),
            text=data[y_col].round(2),
            textposition='outside',
            hovertemplate=f'<b>%{{y}}</b><br>{y_col}: %{{x:.2f}}<extra></extra>'
        ))
    else:
        fig.add_trace(go.Bar(
            x=data[x_col],
            y=data[y_col],
            marker=dict(color=colors, cornerradius=8),
            text=data[y_col].round(2),
            textposition='outside',
            hovertemplate=f'<b>Year: %{{x}}</b><br>{y_col}: %{{y:.2f}}<extra></extra>'
        ))

    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color=COLORS['dark'])),
        xaxis=dict(title='', gridcolor='#f0f2f6'),
        yaxis=dict(title='', gridcolor='#f0f2f6'),
        height=350,
        margin=dict(l=40, r=40, t=60, b=40),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        font={'family': 'Inter, sans-serif'}
    )
    return fig

def create_comparison_chart(data, categories, values, title):
    """Create a comparison bar chart for restriction analysis"""
    colors = [COLORS['success'], COLORS['warning'], COLORS['danger']]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=categories,
        y=values,
        marker=dict(color=colors, cornerradius=10),
        text=[f'{v:.2f}' for v in values],
        textposition='outside',
        textfont=dict(size=14, color=COLORS['dark'])
    ))

    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color=COLORS['dark'])),
        xaxis=dict(title='', tickangle=0),
        yaxis=dict(title='', gridcolor='#f0f2f6'),
        height=350,
        margin=dict(l=40, r=40, t=60, b=60),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        font={'family': 'Inter, sans-serif'}
    )
    return fig

def create_radar_chart(categories, values, title):
    """Create a radar chart for multi-dimensional comparison"""
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],
        theta=categories + [categories[0]],
        fill='toself',
        fillcolor=f'rgba(102, 126, 234, 0.2)',
        line=dict(color=COLORS['primary'], width=2),
        marker=dict(size=8, color=COLORS['primary'])
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, max(values) * 1.2], gridcolor='#f0f2f6'),
            angularaxis=dict(gridcolor='#f0f2f6')
        ),
        title=dict(text=title, font=dict(size=16, color=COLORS['dark'])),
        height=400,
        margin=dict(l=80, r=80, t=80, b=80),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'family': 'Inter, sans-serif'}
    )
    return fig

def create_donut_chart(labels, values, title):
    """Create a modern donut chart"""
    colors = [COLORS['success'], COLORS['warning'], COLORS['danger']]

    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=values,
        hole=0.6,
        marker=dict(colors=colors, line=dict(color='white', width=3)),
        textinfo='label+percent',
        textposition='outside',
        textfont=dict(size=12)
    )])

    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color=COLORS['dark'])),
        height=350,
        margin=dict(l=40, r=40, t=80, b=40),
        paper_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        font={'family': 'Inter, sans-serif'},
        annotations=[dict(text='2025', x=0.5, y=0.5, font_size=20, showarrow=False)]
    )
    return fig

def create_heatmap(df, x_col, y_col, value_col, title):
    """Create a heatmap for correlation analysis"""
    pivot_df = df.pivot_table(index=y_col, columns=x_col, values=value_col, aggfunc='mean')

    fig = go.Figure(data=go.Heatmap(
        z=pivot_df.values,
        x=pivot_df.columns,
        y=pivot_df.index,
        colorscale=[[0, '#f8f9ff'], [0.5, '#667eea'], [1, '#764ba2']],
        hoverongaps=False,
        text=np.round(pivot_df.values, 2),
        texttemplate='%{text}',
        textfont=dict(size=12, color='white')
    ))

    fig.update_layout(
        title=dict(text=title, font=dict(size=16, color=COLORS['dark'])),
        height=400,
        margin=dict(l=100, r=40, t=60, b=60),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'family': 'Inter, sans-serif'}
    )
    return fig

# ============================================================================
# PAGE 1: EXECUTIVE OVERVIEW
# ============================================================================

if page == "🏠 Executive Overview":
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🎓 AI in Education: Research Dashboard</h1>
        <p>Comprehensive Analysis Across 40 Professors & 100 Students (2022-2025)</p>
    </div>
    """, unsafe_allow_html=True)

    # Key Metrics Row
    col1, col2, col3, col4 = st.columns(4)

    prof_count = filtered_prof_df['Professor_ID'].nunique() if 'Professor_ID' in filtered_prof_df.columns else 40
    student_count = filtered_student_df['Student_ID'].nunique() if 'Student_ID' in filtered_student_df.columns else 100
    data_points = len(filtered_prof_df) + len(filtered_student_df)

    with col1:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">👨‍🏫</div>
            <div class="kpi-value">{prof_count}</div>
            <div class="kpi-label">Professors</div>
            <div class="kpi-delta positive">↑ Active Participants</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">👨‍🎓</div>
            <div class="kpi-value">{student_count}</div>
            <div class="kpi-label">Students</div>
            <div class="kpi-delta positive">↑ Enrolled</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">📅</div>
            <div class="kpi-value">4</div>
            <div class="kpi-label">Years Tracked</div>
            <div class="kpi-delta positive">2022-2025</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-icon">📊</div>
            <div class="kpi-value">{data_points:,}</div>
            <div class="kpi-label">Data Points</div>
            <div class="kpi-delta positive">↑ Comprehensive</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Executive Summary
    st.markdown("""
    <div class="exec-summary">
        <h3>📋 Executive Summary</h3>
        <p>This dashboard presents findings from a 4-year longitudinal study examining AI integration in higher education.
        Key findings reveal <strong>significant efficiency gains</strong> for professors (6+ hours/week saved) and
        <strong>improved academic outcomes</strong> for students (19% GPA improvement). The data supports a
        <strong>balanced adoption approach</strong> that maintains academic integrity while leveraging AI benefits.</p>
    </div>
    """, unsafe_allow_html=True)

    # Gauge Charts Row
    st.markdown("### 🎯 Key Performance Indicators (2025)")

    col1, col2, col3, col4 = st.columns(4)

    # Calculate KPIs
    prof_2025 = filtered_prof_df[filtered_prof_df['Year'] == 2025] if 2025 in selected_years else filtered_prof_df
    student_2025 = filtered_student_df[filtered_student_df['Year'] == 2025] if 2025 in selected_years else filtered_student_df

    avg_hours_saved = prof_2025['Hours_Saved_Lesson_Planning_Per_Week'].mean() if len(prof_2025) > 0 else 0
    avg_gpa = student_2025['GPA'].mean() if len(student_2025) > 0 else 0
    avg_literacy = student_2025['AI_Literacy_Score'].mean() if len(student_2025) > 0 else 0
    intervention_rate = prof_2025['Intervention_Success_Rate'].mean() * 100 if len(prof_2025) > 0 else 0

    with col1:
        st.plotly_chart(create_gauge_chart(avg_hours_saved, "Hours Saved/Week", 10, " hrs"), use_container_width=True)

    with col2:
        st.plotly_chart(create_gauge_chart(avg_gpa, "Average GPA", 4.0, ""), use_container_width=True)

    with col3:
        st.plotly_chart(create_gauge_chart(avg_literacy, "AI Literacy Score", 100, ""), use_container_width=True)

    with col4:
        st.plotly_chart(create_gauge_chart(intervention_rate, "Intervention Success", 100, "%"), use_container_width=True)

    st.markdown("<hr class='custom-divider'>", unsafe_allow_html=True)

    # Adoption Trends
    st.markdown("### 📈 AI Adoption Trends Over Time")

    col1, col2 = st.columns(2)

    with col1:
        # Professor Adoption
        prof_adoption = []
        for year in sorted(filtered_prof_df['Year'].unique()):
            year_data = filtered_prof_df[filtered_prof_df['Year'] == year]
            full_adoption = len(year_data[year_data['AI_Restriction_Status'] == 'Full Adoption'])
            prof_adoption.append({'Year': year, 'Full_Adoption': full_adoption})

        adoption_df = pd.DataFrame(prof_adoption)
        fig = create_trend_chart(adoption_df, 'Year', 'Full_Adoption', '👨‍🏫 Professor AI Adoption Growth', COLORS['primary'])
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Student Adoption
        student_adoption = []
        for year in sorted(filtered_student_df['Year'].unique()):
            year_data = filtered_student_df[filtered_student_df['Year'] == year]
            full_adoption = len(year_data[year_data['AI_Restriction_Status'] == 'Full Adoption'])
            student_adoption.append({'Year': year, 'Full_Adoption': full_adoption})

        adoption_df = pd.DataFrame(student_adoption)
        fig = create_trend_chart(adoption_df, 'Year', 'Full_Adoption', '👨‍🎓 Student AI Adoption Growth', COLORS['secondary'])
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("<hr class='custom-divider'>", unsafe_allow_html=True)

    # Key Insights Cards
    st.markdown("### 🔍 Key Insights from 2022-2025")

    col1, col2, col3 = st.columns(3)

    # Calculate year-over-year changes
    if 2022 in selected_years and 2025 in selected_years:
        prof_2022 = filtered_prof_df[filtered_prof_df['Year'] == 2022]
        prof_2025 = filtered_prof_df[filtered_prof_df['Year'] == 2025]
        student_2022 = filtered_student_df[filtered_student_df['Year'] == 2022]
        student_2025 = filtered_student_df[filtered_student_df['Year'] == 2025]

        hours_2022 = prof_2022['Hours_Saved_Lesson_Planning_Per_Week'].mean() if len(prof_2022) > 0 else 0
        hours_2025 = prof_2025['Hours_Saved_Lesson_Planning_Per_Week'].mean() if len(prof_2025) > 0 else 0
        hours_growth = ((hours_2025 - hours_2022) / hours_2022 * 100) if hours_2022 > 0 else 0

        gpa_2022 = student_2022['GPA'].mean() if len(student_2022) > 0 else 0
        gpa_2025 = student_2025['GPA'].mean() if len(student_2025) > 0 else 0
        gpa_improvement = gpa_2025 - gpa_2022

        literacy_2022 = student_2022['AI_Literacy_Score'].mean() if len(student_2022) > 0 else 0
        literacy_2025 = student_2025['AI_Literacy_Score'].mean() if len(student_2025) > 0 else 0
        literacy_growth = ((literacy_2025 - literacy_2022) / literacy_2022 * 100) if literacy_2022 > 0 else 0
    else:
        hours_2022, hours_2025, hours_growth = 0, 0, 0
        gpa_2022, gpa_2025, gpa_improvement = 0, 0, 0
        literacy_2022, literacy_2025, literacy_growth = 0, 0, 0

    with col1:
        st.markdown(f"""
        <div class="insight-box">
            <h4>⏱️ Lesson Planning Efficiency</h4>
            <p><strong>2022:</strong> {hours_2022:.2f} hrs/week saved</p>
            <p><strong>2025:</strong> {hours_2025:.2f} hrs/week saved</p>
            <p style="color: #22c55e; font-weight: 600;">📈 Growth: +{hours_growth:.1f}%</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="insight-box">
            <h4>🎓 Student Academic Performance</h4>
            <p><strong>2022 Avg GPA:</strong> {gpa_2022:.2f}</p>
            <p><strong>2025 Avg GPA:</strong> {gpa_2025:.2f}</p>
            <p style="color: #22c55e; font-weight: 600;">📈 Improvement: +{gpa_improvement:.2f}</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="insight-box">
            <h4>🤖 AI Literacy Development</h4>
            <p><strong>2022:</strong> {literacy_2022:.1f}/100</p>
            <p><strong>2025:</strong> {literacy_2025:.1f}/100</p>
            <p style="color: #22c55e; font-weight: 600;">📈 Growth: +{literacy_growth:.1f}%</p>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# PAGE 2: PROFESSOR ANALYTICS
# ============================================================================

elif page == "👨‍🏫 Professor Analytics":
    st.markdown("""
    <div class="main-header">
        <h1>👨‍🏫 Professor Analytics</h1>
        <p>AI as a Teaching Facilitator: Efficiency, Grading & Student Support</p>
    </div>
    """, unsafe_allow_html=True)

    # Section 1: Lesson Planning
    st.markdown("""
    <div class="section-header">
        <div class="section-number">1</div>
        <h2>Lesson Planning & Content Creation</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        fig = create_trend_chart(
            filtered_prof_df, 'Year', 'Hours_Saved_Lesson_Planning_Per_Week',
            '⏱️ Hours Saved Per Week on Lesson Planning',
            COLORS['primary'], fill=True
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = create_bar_chart(
            filtered_prof_df, 'Year', 'PPTs_Created_Per_Month',
            '📊 Average PPTs Created Per Month',
            CHART_COLORS
        )
        st.plotly_chart(fig, use_container_width=True)

    # Section 2: Grading
    st.markdown("""
    <div class="section-header">
        <div class="section-number">2</div>
        <h2>Automated Grading with Personal Touch</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        fig = create_bar_chart(
            filtered_prof_df, 'Year', 'Assignments_Graded_Per_Semester',
            '📝 Assignments Graded/Semester',
            [COLORS['primary']] * 4
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = create_trend_chart(
            filtered_prof_df, 'Year', 'Grading_Quality_Score',
            '⭐ Grading Quality Score (0-1)',
            COLORS['secondary'], fill=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col3:
        fig = create_bar_chart(
            filtered_prof_df, 'Year', 'Grading_Time_Hours_Per_Semester',
            '⏰ Grading Time (Hours/Semester)',
            [COLORS['warning']] * 4
        )
        st.plotly_chart(fig, use_container_width=True)

    # Section 3: Admin Tasks
    st.markdown("""
    <div class="section-header">
        <div class="section-number">3</div>
        <h2>Administrative Task Automation</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        fig = create_bar_chart(
            filtered_prof_df, 'Year', 'Hours_Saved_Admin_Per_Week',
            '🗂️ Hours Saved Per Week on Admin Tasks',
            CHART_COLORS
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h4 style="color: #667eea; margin-top: 0;">📋 Tasks Automated</h4>
            <ul style="margin: 0; padding-left: 1.2rem;">
                <li>📋 Attendance Tracking</li>
                <li>📅 Class Scheduling</li>
                <li>📄 Report Generation</li>
                <li>✉️ Email Drafting</li>
                <li>📊 Grade Analytics</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # Quick stats
        admin_2025 = filtered_prof_df[filtered_prof_df['Year'] == 2025]['Hours_Saved_Admin_Per_Week'].mean() if 2025 in selected_years else 0
        st.metric("Hours Saved (2025)", f"{admin_2025:.1f} hrs/week", f"+{admin_2025*52:.0f} hrs/year")

    # Section 4: Student Performance
    st.markdown("""
    <div class="section-header">
        <div class="section-number">4</div>
        <h2>Student Performance Analytics & Early Intervention</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        fig = create_trend_chart(
            filtered_prof_df, 'Year', 'Students_Monitored',
            '👥 Students Monitored Per Professor',
            COLORS['info'], fill=False
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Intervention success rate as percentage
        intervention_df = filtered_prof_df.copy()
        intervention_df['Intervention_Rate_Pct'] = intervention_df['Intervention_Success_Rate'] * 100

        fig = create_bar_chart(
            intervention_df, 'Year', 'Intervention_Rate_Pct',
            '🎯 At-Risk Student Intervention Success Rate (%)',
            [COLORS['success']] * 4
        )
        st.plotly_chart(fig, use_container_width=True)

    # Department Analysis (if available)
    if 'Department' in filtered_prof_df.columns:
        st.markdown("""
        <div class="section-header">
            <div class="section-number">5</div>
            <h2>Department-Level Analysis</h2>
        </div>
        """, unsafe_allow_html=True)

        dept_summary = filtered_prof_df.groupby('Department').agg({
            'Hours_Saved_Lesson_Planning_Per_Week': 'mean',
            'Grading_Quality_Score': 'mean',
            'Intervention_Success_Rate': 'mean'
        }).reset_index()

        if 'Learning_Style' in filtered_student_df.columns:
            fig = create_heatmap(
                filtered_prof_df, 'Year', 'Department',
                'Hours_Saved_Lesson_Planning_Per_Week',
                '🏛️ Hours Saved by Department Over Time'
            )
            st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# PAGE 3: STUDENT ANALYTICS
# ============================================================================

elif page == "👨‍🎓 Student Analytics":
    st.markdown("""
    <div class="main-header">
        <h1>👨‍🎓 Student Analytics</h1>
        <p>Learning with AI: Literacy, Performance & Skill Development</p>
    </div>
    """, unsafe_allow_html=True)

    # Section 1: AI Literacy & Skills
    st.markdown("""
    <div class="section-header">
        <div class="section-number">1</div>
        <h2>AI Literacy, Responsible Use & Creativity</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        fig = create_trend_chart(
            filtered_student_df, 'Year', 'AI_Literacy_Score',
            '🤖 AI Literacy Score',
            COLORS['primary'], fill=True
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = create_trend_chart(
            filtered_student_df, 'Year', 'Responsible_Use_Awareness',
            '⚖️ Responsible AI Use Awareness',
            COLORS['secondary'], fill=True
        )
        st.plotly_chart(fig, use_container_width=True)

    with col3:
        fig = create_trend_chart(
            filtered_student_df, 'Year', 'Creativity_Preservation_Score',
            '🎨 Creativity Preservation Score',
            COLORS['warning'], fill=True
        )
        st.plotly_chart(fig, use_container_width=True)

    # Section 2: Tool Adoption
    st.markdown("""
    <div class="section-header">
        <div class="section-number">2</div>
        <h2>AI Tool Adoption & Usage Patterns</h2>
    </div>
    """, unsafe_allow_html=True)

    # Multi-line adoption chart
    adoption_cols = ['AI_Tool_Adoption_Rate', 'Uses_AI_For_Brainstorming',
                     'Uses_AI_For_Assessment', 'Uses_AI_For_Collaboration']
    adoption_names = ['Overall Adoption', 'Brainstorming', 'Assessment', 'Collaboration']

    fig = go.Figure()

    for col, name, color in zip(adoption_cols, adoption_names, CHART_COLORS):
        if col in filtered_student_df.columns:
            data = filtered_student_df.groupby('Year')[col].mean() * 100
            fig.add_trace(go.Scatter(
                x=data.index,
                y=data.values,
                mode='lines+markers',
                name=name,
                line=dict(width=3),
                marker=dict(size=10)
            ))

    fig.update_layout(
        title=dict(text='📱 Student AI Tool Usage by Purpose (%)', font=dict(size=18, color=COLORS['dark'])),
        xaxis=dict(title='Year', gridcolor='#f0f2f6'),
        yaxis=dict(title='Adoption Rate (%)', gridcolor='#f0f2f6'),
        height=400,
        hovermode='x unified',
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'family': 'Inter, sans-serif'}
    )
    st.plotly_chart(fig, use_container_width=True)

    # Section 3: Study Efficiency
    st.markdown("""
    <div class="section-header">
        <div class="section-number">3</div>
        <h2>Study Efficiency & Academic Performance</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        # Hours per assignment (showing decrease is good)
        time_data = filtered_student_df.groupby('Year')['Hours_Per_Assignment'].mean().reset_index()

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=time_data['Year'],
            y=time_data['Hours_Per_Assignment'],
            marker=dict(
                color=[COLORS['danger'], COLORS['warning'], COLORS['success'], COLORS['success']],
                cornerradius=8
            ),
            text=time_data['Hours_Per_Assignment'].round(1),
            textposition='outside'
        ))
        fig.update_layout(
            title=dict(text='⏱️ Average Hours Per Assignment', font=dict(size=16, color=COLORS['dark'])),
            xaxis=dict(title='Year'),
            yaxis=dict(title='Hours'),
            height=350,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        completion_df = filtered_student_df.copy()
        completion_df['Completion_Pct'] = completion_df['Assignment_Completion_Rate'] * 100

        fig = create_trend_chart(
            completion_df, 'Year', 'Completion_Pct',
            '✅ Assignment Completion Rate (%)',
            COLORS['success'], fill=True
        )
        st.plotly_chart(fig, use_container_width=True)

    # Section 4: Learning Styles
    st.markdown("""
    <div class="section-header">
        <div class="section-number">4</div>
        <h2>Learning Outcomes by Learning Style</h2>
    </div>
    """, unsafe_allow_html=True)

    if 'Learning_Style' in filtered_student_df.columns:
        # Radar chart for learning styles
        learning_styles = filtered_student_df['Learning_Style'].unique()
        style_performance = []

        for style in ['Visual', 'Auditory', 'Reading-Writing', 'Kinesthetic']:
            if style in learning_styles:
                perf = filtered_student_df[
                    (filtered_student_df['Learning_Style'] == style) &
                    (filtered_student_df['Year'] == max(selected_years))
                ]['Performance_Improvement_Percent'].mean()
                style_performance.append(perf if not pd.isna(perf) else 0)
            else:
                style_performance.append(0)

        col1, col2 = st.columns([1, 1])

        with col1:
            fig = create_radar_chart(
                ['Visual', 'Auditory', 'Reading-Writing', 'Kinesthetic'],
                style_performance,
                '📚 Performance Improvement by Learning Style (%)'
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Performance trend by learning style
            fig = go.Figure()
            style_colors = {'Visual': COLORS['primary'], 'Auditory': COLORS['secondary'],
                           'Reading-Writing': COLORS['warning'], 'Kinesthetic': COLORS['success']}

            for style in learning_styles:
                style_data = filtered_student_df[filtered_student_df['Learning_Style'] == style]
                perf_by_year = style_data.groupby('Year')['Performance_Improvement_Percent'].mean()

                fig.add_trace(go.Scatter(
                    x=perf_by_year.index,
                    y=perf_by_year.values,
                    mode='lines+markers',
                    name=style,
                    line=dict(width=3, color=style_colors.get(style, COLORS['info'])),
                    marker=dict(size=8)
                ))

            fig.update_layout(
                title=dict(text='📈 Performance Trends by Learning Style', font=dict(size=16)),
                xaxis=dict(title='Year'),
                yaxis=dict(title='Improvement (%)'),
                height=400,
                hovermode='x unified',
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig, use_container_width=True)

    # Section 5: Skill Development
    st.markdown("""
    <div class="section-header">
        <div class="section-number">5</div>
        <h2>AI Skill Development Pathway</h2>
    </div>
    """, unsafe_allow_html=True)

    skill_cols = ['Skill_Awareness_Level', 'Skill_Beginner_Level',
                  'Skill_Intermediate_Level', 'Skill_Advanced_Level']

    if all(col in filtered_student_df.columns for col in skill_cols):
        latest_year = max(selected_years)
        skill_data = filtered_student_df[filtered_student_df['Year'] == latest_year]

        skills = ['Awareness', 'Beginner', 'Intermediate', 'Advanced']
        values = [skill_data[col].mean() for col in skill_cols]

        col1, col2 = st.columns([1, 1])

        with col1:
            # Funnel chart
            fig = go.Figure(go.Funnel(
                y=skills,
                x=values,
                textposition="inside",
                textinfo="value+percent initial",
                marker=dict(color=[COLORS['primary'], COLORS['secondary'],
                                   COLORS['warning'], COLORS['success']])
            ))
            fig.update_layout(
                title=dict(text=f'🎯 AI Skill Development Funnel ({latest_year})',
                          font=dict(size=16, color=COLORS['dark'])),
                height=400,
                paper_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Skill progression over time
            fig = go.Figure()

            for skill, col, color in zip(skills, skill_cols, CHART_COLORS):
                skill_trend = filtered_student_df.groupby('Year')[col].mean()
                fig.add_trace(go.Scatter(
                    x=skill_trend.index,
                    y=skill_trend.values,
                    mode='lines+markers',
                    name=skill,
                    line=dict(width=3, color=color),
                    marker=dict(size=8)
                ))

            fig.update_layout(
                title=dict(text='📊 Skill Level Progression Over Time', font=dict(size=16)),
                xaxis=dict(title='Year'),
                yaxis=dict(title='Average Level'),
                height=400,
                hovermode='x unified',
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig, use_container_width=True)

    # Section 6: Collaboration
    st.markdown("""
    <div class="section-header">
        <div class="section-number">6</div>
        <h2>Collaboration & Communication</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if 'Uses_AI_Collaboration_Tools' in filtered_student_df.columns:
            collab_df = filtered_student_df.copy()
            collab_df['Collab_Pct'] = collab_df['Uses_AI_Collaboration_Tools'] * 100

            fig = create_bar_chart(
                collab_df, 'Year', 'Collab_Pct',
                '🤝 AI Collaboration Tool Adoption (%)',
                [COLORS['primary']] * 4
            )
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        if 'Language_Barrier_Reduction_Percent' in filtered_student_df.columns:
            fig = create_bar_chart(
                filtered_student_df, 'Year', 'Language_Barrier_Reduction_Percent',
                '🌍 Language Barrier Reduction (%)',
                [COLORS['success']] * 4
            )
            st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# PAGE 4: AI RESTRICTION IMPACT
# ============================================================================

elif page == "⚖️ Restriction Impact":
    st.markdown("""
    <div class="main-header">
        <h1>⚖️ AI Restriction Impact Analysis</h1>
        <p>Comparing Full Adoption, Partial Restriction & Full Restriction Outcomes</p>
    </div>
    """, unsafe_allow_html=True)

    # Introduction
    st.markdown("""
    <div class="info-card">
        <h4 style="margin-top: 0; color: #667eea;">📋 Restriction Categories</h4>
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem;">
            <div style="text-align: center; padding: 1rem; background: rgba(34, 197, 94, 0.1); border-radius: 8px;">
                <strong style="color: #22c55e;">Full Adoption</strong>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.85rem;">Unrestricted AI usage</p>
            </div>
            <div style="text-align: center; padding: 1rem; background: rgba(249, 115, 22, 0.1); border-radius: 8px;">
                <strong style="color: #f97316;">Partial Restriction</strong>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.85rem;">Limited AI with guidelines</p>
            </div>
            <div style="text-align: center; padding: 1rem; background: rgba(239, 68, 68, 0.1); border-radius: 8px;">
                <strong style="color: #ef4444;">Full Restriction</strong>
                <p style="margin: 0.5rem 0 0 0; font-size: 0.85rem;">Minimal or no AI allowed</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Distribution Charts
    st.markdown("### 📊 Restriction Status Distribution (2025)")

    col1, col2 = st.columns(2)

    latest_year = max(selected_years)

    with col1:
        prof_restriction = filtered_prof_df[filtered_prof_df['Year'] == latest_year]['AI_Restriction_Status'].value_counts()
        fig = create_donut_chart(
            prof_restriction.index.tolist(),
            prof_restriction.values.tolist(),
            '👨‍🏫 Professor Distribution'
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        student_restriction = filtered_student_df[filtered_student_df['Year'] == latest_year]['AI_Restriction_Status'].value_counts()
        fig = create_donut_chart(
            student_restriction.index.tolist(),
            student_restriction.values.tolist(),
            '👨‍🎓 Student Distribution'
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("<hr class='custom-divider'>", unsafe_allow_html=True)

    # Professor Impact Analysis
    st.markdown("### 👨‍🏫 Professor Impact Analysis")

    restrictions = ['Full Adoption', 'Partial Restriction', 'Full Restriction']

    prof_metrics = []
    for restriction in restrictions:
        subset = filtered_prof_df[
            (filtered_prof_df['AI_Restriction_Status'] == restriction) &
            (filtered_prof_df['Year'] == latest_year)
        ]
        if len(subset) > 0:
            prof_metrics.append({
                'Restriction': restriction,
                'Hours_Saved': subset['Hours_Saved_Lesson_Planning_Per_Week'].mean(),
                'Grading_Quality': subset['Grading_Quality_Score'].mean(),
                'Admin_Hours': subset['Hours_Saved_Admin_Per_Week'].mean(),
                'Intervention_Success': subset['Intervention_Success_Rate'].mean() * 100
            })

    if prof_metrics:
        prof_metrics_df = pd.DataFrame(prof_metrics)

        col1, col2, col3 = st.columns(3)

        with col1:
            fig = create_comparison_chart(
                prof_metrics_df, restrictions,
                prof_metrics_df['Hours_Saved'].tolist(),
                '⏱️ Hours Saved (Lesson Planning)'
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            fig = create_comparison_chart(
                prof_metrics_df, restrictions,
                prof_metrics_df['Grading_Quality'].tolist(),
                '⭐ Grading Quality Score'
            )
            st.plotly_chart(fig, use_container_width=True)

        with col3:
            fig = create_comparison_chart(
                prof_metrics_df, restrictions,
                prof_metrics_df['Admin_Hours'].tolist(),
                '🗂️ Admin Hours Saved'
            )
            st.plotly_chart(fig, use_container_width=True)

    st.markdown("<hr class='custom-divider'>", unsafe_allow_html=True)

    # Student Impact Analysis
    st.markdown("### 👨‍🎓 Student Impact Analysis")

    student_metrics = []
    for restriction in restrictions:
        subset = filtered_student_df[
            (filtered_student_df['AI_Restriction_Status'] == restriction) &
            (filtered_student_df['Year'] == latest_year)
        ]
        if len(subset) > 0:
            student_metrics.append({
                'Restriction': restriction,
                'AI_Literacy': subset['AI_Literacy_Score'].mean(),
                'GPA': subset['GPA'].mean(),
                'Creativity': subset['Creativity_Preservation_Score'].mean(),
                'Hours_Per_Assignment': subset['Hours_Per_Assignment'].mean()
            })

    if student_metrics:
        student_metrics_df = pd.DataFrame(student_metrics)

        col1, col2, col3 = st.columns(3)

        with col1:
            fig = create_comparison_chart(
                student_metrics_df, restrictions,
                student_metrics_df['AI_Literacy'].tolist(),
                '🤖 AI Literacy Score'
            )
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            fig = create_comparison_chart(
                student_metrics_df, restrictions,
                student_metrics_df['GPA'].tolist(),
                '🎓 Average GPA'
            )
            st.plotly_chart(fig, use_container_width=True)

        with col3:
            fig = create_comparison_chart(
                student_metrics_df, restrictions,
                student_metrics_df['Creativity'].tolist(),
                '🎨 Creativity Preservation'
            )
            st.plotly_chart(fig, use_container_width=True)

    # Key Findings
    st.markdown("<hr class='custom-divider'>", unsafe_allow_html=True)

    st.markdown("### 💡 Key Findings")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="info-card success">
            <h4 style="margin-top: 0; color: #22c55e;">✅ Benefits of Full Adoption</h4>
            <ul style="margin: 0.5rem 0 0 0; padding-left: 1.2rem;">
                <li>40% higher efficiency gains vs. full restriction</li>
                <li>Higher student GPA improvement</li>
                <li>Better intervention success rates</li>
                <li>Increased collaboration capabilities</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card warning">
            <h4 style="margin-top: 0; color: #f97316;">⚖️ Partial Restriction Trade-offs</h4>
            <ul style="margin: 0.5rem 0 0 0; padding-left: 1.2rem;">
                <li>Maintains 75% of AI benefits</li>
                <li>95%+ academic integrity preserved</li>
                <li>Balanced approach for most institutions</li>
                <li>Similar creativity preservation scores</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# PAGE 5: FUTURE PROJECTIONS & INSIGHTS
# ============================================================================

elif page == "🔮 Future Insights":
    st.markdown("""
    <div class="main-header">
        <h1>🔮 Future Projections & Strategic Insights</h1>
        <p>Trend Analysis, 2026-2027 Projections & Recommendations</p>
    </div>
    """, unsafe_allow_html=True)

    # Projections
    st.markdown("### 📈 Projected Trends: 2026-2027")

    col1, col2 = st.columns(2)

    # Professor hours saved projection
    with col1:
        prof_trend = filtered_prof_df.groupby('Year')['Hours_Saved_Lesson_Planning_Per_Week'].mean()
        years_hist = np.array(prof_trend.index)
        values_hist = prof_trend.values

        # Linear projection
        z = np.polyfit(years_hist, values_hist, 1)
        p = np.poly1d(z)

        future_years = np.array([2026, 2027])
        future_values = p(future_years)

        fig = go.Figure()

        # Historical data
        fig.add_trace(go.Scatter(
            x=years_hist, y=values_hist,
            mode='lines+markers',
            name='Historical Data',
            line=dict(color=COLORS['primary'], width=3),
            marker=dict(size=10, color=COLORS['primary'], line=dict(width=2, color='white'))
        ))

        # Projection
        fig.add_trace(go.Scatter(
            x=np.concatenate([[years_hist[-1]], future_years]),
            y=np.concatenate([[values_hist[-1]], future_values]),
            mode='lines+markers',
            name='Projection',
            line=dict(color=COLORS['primary'], width=3, dash='dash'),
            marker=dict(size=10, symbol='diamond', color=COLORS['primary'])
        ))

        fig.update_layout(
            title=dict(text='👨‍🏫 Projected Professor Hours Saved', font=dict(size=16)),
            xaxis=dict(title='Year', gridcolor='#f0f2f6'),
            yaxis=dict(title='Hours/Week', gridcolor='#f0f2f6'),
            height=400,
            hovermode='x unified',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5)
        )
        st.plotly_chart(fig, use_container_width=True)

    # Student GPA projection
    with col2:
        gpa_trend = filtered_student_df.groupby('Year')['GPA'].mean()
        years_hist = np.array(gpa_trend.index)
        values_hist = gpa_trend.values

        z = np.polyfit(years_hist, values_hist, 1)
        p = np.poly1d(z)

        future_values = p(future_years)

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=years_hist, y=values_hist,
            mode='lines+markers',
            name='Historical Data',
            line=dict(color=COLORS['secondary'], width=3),
            marker=dict(size=10, color=COLORS['secondary'], line=dict(width=2, color='white'))
        ))

        fig.add_trace(go.Scatter(
            x=np.concatenate([[years_hist[-1]], future_years]),
            y=np.concatenate([[values_hist[-1]], future_values]),
            mode='lines+markers',
            name='Projection',
            line=dict(color=COLORS['secondary'], width=3, dash='dash'),
            marker=dict(size=10, symbol='diamond', color=COLORS['secondary'])
        ))

        fig.update_layout(
            title=dict(text='👨‍🎓 Projected Student Average GPA', font=dict(size=16)),
            xaxis=dict(title='Year', gridcolor='#f0f2f6'),
            yaxis=dict(title='GPA', gridcolor='#f0f2f6'),
            height=400,
            hovermode='x unified',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='center', x=0.5)
        )
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("<hr class='custom-divider'>", unsafe_allow_html=True)

    # Strategic Insights
    st.markdown("### 💡 Strategic Insights & Key Takeaways")

    # Calculate dynamic insights
    if len(filtered_prof_df) > 0 and len(filtered_student_df) > 0:
        latest_year = max(selected_years)
        earliest_year = min(selected_years)

        prof_latest = filtered_prof_df[filtered_prof_df['Year'] == latest_year]
        prof_earliest = filtered_prof_df[filtered_prof_df['Year'] == earliest_year]
        student_latest = filtered_student_df[filtered_student_df['Year'] == latest_year]
        student_earliest = filtered_student_df[filtered_student_df['Year'] == earliest_year]

        hours_growth = ((prof_latest['Hours_Saved_Lesson_Planning_Per_Week'].mean() -
                        prof_earliest['Hours_Saved_Lesson_Planning_Per_Week'].mean()) /
                       prof_earliest['Hours_Saved_Lesson_Planning_Per_Week'].mean() * 100) if len(prof_earliest) > 0 else 0

        gpa_growth = ((student_latest['GPA'].mean() - student_earliest['GPA'].mean()) /
                     student_earliest['GPA'].mean() * 100) if len(student_earliest) > 0 else 0

        literacy_growth = ((student_latest['AI_Literacy_Score'].mean() -
                           student_earliest['AI_Literacy_Score'].mean()) /
                          student_earliest['AI_Literacy_Score'].mean() * 100) if len(student_earliest) > 0 else 0
    else:
        hours_growth = gpa_growth = literacy_growth = 0

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>+{hours_growth:.0f}%</h3>
            <p>📚 Time Savings Growth</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);">
            <h3>+{gpa_growth:.1f}%</h3>
            <p>🎓 GPA Improvement</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card" style="background: linear-gradient(135deg, #22c55e 0%, #3b82f6 100%);">
            <h3>+{literacy_growth:.0f}%</h3>
            <p>🤖 AI Literacy Growth</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Recommendations
    st.markdown("### 🎓 Key Findings & Recommendations")

    tabs = st.tabs(["🏛️ For Institutions", "👨‍🏫 For Professors", "👨‍🎓 For Students", "🔮 Future Outlook"])

    with tabs[0]:
        st.markdown("""
        1. **Wide Adoption Benefits**: Full AI adoption shows 40% improvement in professor efficiency vs. full restriction
        2. **Learning Style Matters**: Visual learners benefit most (+15% performance), kinesthetic learners benefit least (+8%)
        3. **Balanced Approach Effective**: Partial restriction maintains 95%+ academic integrity while preserving most AI benefits
        4. **Quality Over Quantity**: Grading quality improves (0.85→0.95) while time decreases—AI enhances professor judgment
        5. **Creativity Preservation**: Full adoption institutions maintain 65-78 creativity scores (similar to restricted)
        """)

    with tabs[1]:
        st.markdown("""
        1. **Time Investment Pays Off**: 5-8 hours/week saved in lesson planning = 260-400 hours/year per professor
        2. **Administrative Burden Reduced**: Attendance, scheduling, reports automated—frees time for teaching
        3. **Grading Enhanced, Not Automated**: Personal touch + AI assistance = 60% faster, 10% higher quality
        4. **Early Intervention Works**: 81% success rate in identifying & helping at-risk students (2025)
        5. **Professional Development**: AI-fluent professors most effective at both teaching & learning facilitation
        """)

    with tabs[2]:
        st.markdown("""
        1. **AI Literacy is Critical**: 70-90 score needed for competitiveness in 2027 job market
        2. **Responsible Use Awareness**: Despite 92% AI use, only 75-92% understand ethical guidelines—requires curriculum update
        3. **Time is Freed, Not Wasted**: Hours/assignment drop 60%+ but completion rates & GPA increase → AI enables deeper learning
        4. **Learning Style Adaptation**: Institutions should provide AI tools tailored to learning styles
        5. **Collaboration Barrier Breaker**: 55-75% language barrier reduction = major equity improvement for international students
        """)

    with tabs[3]:
        st.markdown("""
        ### Forward Projection (2026-2027)
        - **Professor hours saved**: 8.5-9.5 hours/week (up from 6.5 in 2025)
        - **Student average GPA**: 3.75-3.85 (up from 3.45 in 2025)
        - **AI adoption rate**: 85-95% across all institutions
        - **Creativity concern**: Minimal (preservation scores stable at 60-78)

        ### Risks & Mitigations
        - **Over-reliance**: Require AI-free assignments (20-30% of curriculum)
        - **Plagiarism Accusations**: Implement clear AI use policies & detection tools
        - **Equity Issues**: Ensure all students access AI literacy training
        - **Data Privacy**: Implement privacy-first AI tools
        """)

    st.markdown("<hr class='custom-divider'>", unsafe_allow_html=True)

    # Critical Considerations
    st.markdown("### ⚠️ Critical Considerations")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="info-card warning">
            <h4 style="margin-top: 0; color: #f97316;">🚨 Risks to Monitor</h4>
            <ul style="margin: 0.5rem 0 0 0; padding-left: 1.2rem;">
                <li>30% of students may become overly dependent on AI</li>
                <li>33% of students face plagiarism accusations</li>
                <li>AI grading may perpetuate biases</li>
                <li>Data privacy concerns with AI systems</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card success">
            <h4 style="margin-top: 0; color: #22c55e;">✅ Mitigation Strategies</h4>
            <ul style="margin: 0.5rem 0 0 0; padding-left: 1.2rem;">
                <li>Require 20-30% AI-free assignments</li>
                <li>Clear AI use policies & detection tools</li>
                <li>Professor review of all AI grades</li>
                <li>Privacy-first AI tool implementation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("""
<div class="custom-footer">
    <p><strong>📊 AI in Education: Research Dashboard</strong></p>
    <p>Data: 40 Professors × 100 Students × 4 Years = 560+ Synthetic Data Points</p>
    <p style="font-size: 0.85rem; color: #999;">Dashboard Enhanced with Modern UI • Last Updated: 2025</p>
</div>
""", unsafe_allow_html=True)
