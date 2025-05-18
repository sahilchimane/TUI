import streamlit as st
from recommender import TravelRecommender

# Static itineraries (can move to itinerary_data.py)
itineraries = {
    "Paris": [
        "Day 1: Eiffel Tower, Seine Cruise",
        "Day 2: Louvre, Notre-Dame, Montmartre",
        "Day 3: Versailles & shopping"
    ],
    "Tokyo": [
        "Day 1: Shibuya, Meiji Shrine, Harajuku",
        "Day 2: Tsukiji, Akihabara",
        "Day 3: Mt. Fuji or Disneyland"
    ],
    "Goa": [
        "Day 1: Baga Beach & Shack",
        "Day 2: Fort Aguada, Old Goa",
        "Day 3: Spice farm & Dolphins"
    ],
    "Bali": [
        "Day 1: Uluwatu, Jimbaran",
        "Day 2: Ubud & Monkey Forest",
        "Day 3: Nusa Dua & Tanah Lot"
    ],
    "New York": [
        "Day 1: Statue of Liberty, Wall St.",
        "Day 2: Central Park, Broadway",
        "Day 3: MoMA & Times Square"
    ]
}

# Streamlit UI
st.set_page_config(page_title="Travel Chatbot", page_icon="🌍")
st.title("🧳 WanderWise Travel Planner")

with st.form("preferences_form"):
    st.write("Tell us what you love, and we'll plan your trip:")
    activities = st.selectbox(
        "What activities do you enjoy?",
        ["Beach", "Museums", "Food"]
    )
    budget = st.selectbox("Your Budget", ["Low", "Medium", "High"])
    companions = st.radio("Traveling With", ["Solo", "Partner", "Friends", "Family"])
    submitted = st.form_submit_button("Get My Itinerary")

if submitted:
    recommender = TravelRecommender("travel_data.csv")
    recommended = recommender.get_recommendations("new_user")

    st.subheader("🌟 Recommended Destinations")
    for dest in recommended:
        st.markdown(f"### 🗺️ {dest}")
        st.write("**Suggested Itinerary:**")
        for day in itineraries.get(dest, ["Itinerary unavailable."]):
            st.markdown(f"- {day}")
