import streamlit as st
import pandas as pd
import joblib
from src.data_preprocessing import preprocess_data

# Load the trained model and feature names
try:
    model, feature_names = joblib.load('models/accident_model.pkl')
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Set page config
st.set_page_config(
    page_title="Accident Prediction System",
    page_icon="🚗",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #000000;
        color: #FFFFFF;
    }
    .stButton>button {
        background-color: #FF0000;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: bold;
    }
    .stSelectbox, .stTextInput {
        background-color: #1E1E1E;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #1E1E1E;
    }
    h1, h2, h3 {
        color: #FF0000;
    }
    .prediction-box {
        border: 2px solid #FF0000;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        background-color: #1E1E1E;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/1946/1946488.png",
    width=80,
    caption="Accident Predictor"
)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Welcome", "Accident Prediction"])

st.sidebar.markdown("---")
st.sidebar.subheader("About")
st.sidebar.info(
    "This app predicts the risk of road accidents using machine learning. "
    "Select a page to get started."
)
st.sidebar.markdown(
    "<small>Developed for SDG 11: Sustainable Cities and Communities</small>",
    unsafe_allow_html=True
)

# Welcome Page
if page == "Welcome":
    st.title("🚗 Road Accident Prediction System")
    st.markdown("---")
    
    col1, col2 = st.columns([3, 2])
    with col1:
        st.header("Addressing SDG 11: Sustainable Cities and Communities")
        st.write("""
        Sustainable Development Goal 11 aims to make cities inclusive, safe, resilient, and sustainable. 
        A critical aspect of this goal is improving road safety and reducing accidents in urban areas.
        """)
        
        st.subheader("The Global Road Safety Crisis")
        st.write("""
        - Approximately 1.3 million people die each year from road traffic crashes
        - Road traffic injuries are the leading cause of death for children and young adults aged 5-29
        - Over 90% of road fatalities occur in low- and middle-income countries
        - Traffic crashes cost most countries 3% of their gross domestic product
        """)
        
        st.subheader("Common Causes of Road Accidents")
        st.write("""
        - Speeding and reckless driving
        - Poor road infrastructure
        - Distracted driving (mobile phone use)
        - Driving under the influence of alcohol/drugs
        - Poor weather conditions
        - Vehicle malfunctions
        - Inadequate lighting
        """)
    
    with col2:
        st.image("https://images.unsplash.com/photo-1509822929063-6b6cfc9b42f2?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80", 
                 caption="Road safety is crucial for sustainable communities")
        st.image("https://images.unsplash.com/photo-1581093196277-1e31650a1c66?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=80",
                 caption="Modern cities need smart accident prevention systems")
    
    st.markdown("---")
    st.header("How Our System Helps")
    st.write("""
    Our Accident Prediction System uses machine learning to analyze various factors that contribute to road accidents. 
    By predicting high-risk scenarios, we can:
    - Help drivers make safer decisions
    - Enable city planners to identify dangerous areas
    - Support policymakers in implementing targeted safety measures
    - Potentially save lives by preventing accidents before they happen
    """)
    
    st.markdown("👉 Use the navigation sidebar to try our prediction system")

# Prediction Page
elif page == "Accident Prediction":
    st.title("🚦 Accident Risk Prediction")
    st.markdown("Fill in the details below to assess accident risk probability")
    st.markdown("---")
    
    with st.expander("📋 Form Input", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            # Time Input
            st.markdown("#### 🕒 Time Information")
            time_hour = st.select_slider(
            "Hour", options=[f"{i:02d}" for i in range(24)], value="08", help="Select hour of the day"
            )
            time_minute = st.select_slider(
            "Minute", options=[f"{i:02d}" for i in range(0, 60, 5)], value="30", help="Select minute (5-min steps)"
            )
            day_of_week = st.radio(
            "Day of the Week",
            ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            index=0,
            horizontal=True,
            help="Choose the day"
            )

            # Location Information
            st.markdown("#### 📍 Location Details")
            area_accident = st.selectbox(
            "Area of Accident",
            [
                '🏢 Office areas', '🏞️ Recreational areas', '🏠 Residential areas', '🏭 Industrial areas',
                '❓ Other', '⛪ Church areas', '🛒 Market areas', '🏡 Rural village areas', '🌄 Outside rural areas',
                '🏥 Hospital areas', '🏫 School areas', '❓ Unknown', '🏡 Rural village areasOffice areas'
            ],
            index=0,
            help="Where did the accident occur?"
            )

            lane_or_medians = st.selectbox(
            "Lane or Medians",
            [
                '🛣️ Undivided Two way', '❓ other', '🛤️ Double carriageway (median)', '➡️ One way',
                '🟡 Two-way (solid lines)', '⚪ Two-way (broken lines)', '❓ Unknown'
            ],
            index=0,
            help="Type of road lane or median"
            )

        with col2:
            # Vehicle Information
            st.markdown("#### 🚗 Vehicle Details")
            type_of_vehicle = st.selectbox(
            "Type of Vehicle",
            [
                '🚚 Lorry (41–100Q)', '🚌 Public (12 seats)', '🐎 Ridden horse', '🚛 Lorry (11–40Q)', '🚗 Turbo', '🚕 Taxi',
                '🚲 Bicycle', '🚙 Automobile', '❓ Other', '🛻 Pick up up to 10Q', '🚌 Public (13–45 seats)', '🚜 Special vehicle',
                '🚐 Stationwagen', '🚛 Long lorry', '🛺 Bajaj', '🚌 Public (> 45 seats)', '🏍️ Motorcycle'
            ],
            index=7,
            help="Select the vehicle type"
            )

            # Road Conditions
            st.markdown("#### 🛣️ Road Conditions")
            road_surface_type = st.selectbox(
            "Road Surface Type",
            [
                '🛣️ Asphalt roads', '🌱 Earth roads', '🪨 Gravel roads', '❓ Other', '🛣️ Asphalt (distressed)'
            ],
            index=0,
            help="Surface type of the road"
            )

            road_surface_conditions = st.selectbox(
            "Road Surface Conditions",
            [
                '🚦 No junction', '🔀 Y Shape', '✖️ Crossing', '⭕ O Shape', '❓ Other', '❓ Unknown', '🔱 T Shape', '❌ X Shape'
            ],
            index=0,
            help="Junction or crossing type"
            )

            light_conditions = st.radio(
            "Light Conditions",
            [
                '🌞 Daylight', '💡 Darkness - lights lit', '🌑 Darkness - no lighting', '💡 Darkness - lights unlit'
            ],
            index=0,
            horizontal=True,
            help="Lighting at the time"
            )

            weather_conditions = st.selectbox(
            "Weather Conditions",
            [
                '☀️ Normal', '🌧️ Raining', '🌧️💨 Raining and Windy', '☁️ Cloudy', '❓ Other', '💨 Windy', '❄️ Snow', '❓ Unknown', '🌫️ Fog or mist'
            ],
            index=0,
            help="Weather at the time"
            )

            sex_of_driver = st.radio(
            "Sex of Driver", ["♂️ Male", "♀️ Female"], index=0, horizontal=True, help="Driver's gender"
            )
    
    # Prediction button
    if st.button("🔮 Predict Accident Risk", key="predict_button"):
        try:
            # Combine time input
            time = f"{time_hour}:{time_minute}"

            # Convert input into DataFrame
            input_data = pd.DataFrame({
                'time': [time],
                'day_of_week': [day_of_week],
                'area_accident': [area_accident],
                'type_of_vehicle': [type_of_vehicle],
                'lane_or_medians': [lane_or_medians],
                'road_surface_type': [road_surface_type],
                'road_surface_conditions': [road_surface_conditions],
                'light_conditions': [light_conditions],
                'weather_conditions': [weather_conditions],
                'sex_of_driver': [sex_of_driver]
            })

            # Preprocess the input data
            input_data, _ = preprocess_data(input_data)

            # Ensure the input data columns match the feature names
            input_data = input_data[feature_names]

            # Make prediction
            prediction_proba = model.predict_proba(input_data)
            accident_chance = prediction_proba[0][1] * 100  # Probability of accident
            
            # Display prediction with visual feedback
            st.markdown("---")
            st.subheader("Prediction Results")
            
            if accident_chance > 70:
                risk_level = "🚨 High Risk"
                color = "#FF0000"
            elif accident_chance > 40:
                risk_level = "⚠️ Moderate Risk"
                color = "#FFA500"
            else:
                risk_level = "✅ Low Risk"
                color = "#00FF00"
            
            # Create a visually appealing prediction box
            accident_chance_display = accident_chance * 100
            st.markdown(f"""
            <div class="prediction-box">
                <h3 style="text-align: center;">{risk_level}</h3>
                <h2 style="text-align: center; color: {color};">{accident_chance_display:.2f}%</h2>
                <p style="text-align: center;">probability of accident</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Add safety tips based on prediction
            st.subheader("Safety Recommendations")
            if accident_chance > 70:
                st.warning("""
                - Consider delaying your trip if possible
                - Exercise extreme caution if you must travel
                - Reduce speed significantly
                - Increase following distance
                - Ensure all vehicle lights are working
                """)
            elif accident_chance > 40:
                st.info("""
                - Drive with increased awareness
                - Moderate your speed
                - Be prepared for sudden stops
                - Check weather conditions before departing
                """)
            else:
                st.success("""
                - Still maintain safe driving practices
                - Stay alert for unexpected hazards
                - Obey all traffic laws
                """)
                
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")