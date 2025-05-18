from recommender import TravelRecommender

# Static sample itinerary data (could be replaced with dynamic data or API)
itinerary_data = {
    "Paris": [
        "Day 1: Visit Eiffel Tower, Seine River Cruise, and dinner at Le Jules Verne.",
        "Day 2: Louvre Museum, Notre-Dame Cathedral, and explore Montmartre.",
        "Day 3: Versailles Day Trip and shopping at Champs-Élysées."
    ],
    "Tokyo": [
        "Day 1: Explore Shibuya Crossing, Meiji Shrine, and Harajuku.",
        "Day 2: Tsukiji Market, Tokyo Tower, and Akihabara gaming district.",
        "Day 3: Day trip to Mt. Fuji or Disneyland Tokyo."
    ],
    "Goa": [
        "Day 1: Relax on Baga Beach and enjoy beach shacks in the evening.",
        "Day 2: Explore Fort Aguada and Old Goa churches.",
        "Day 3: Visit spice plantations and go on a dolphin-watching tour."
    ],
    "Bali": [
        "Day 1: Visit Uluwatu Temple and relax at Jimbaran Beach.",
        "Day 2: Explore Ubud, rice terraces, and monkey forest.",
        "Day 3: Water sports at Nusa Dua and sunset at Tanah Lot Temple."
    ],
    "New York": [
        "Day 1: Statue of Liberty, Wall Street, and One World Observatory.",
        "Day 2: Central Park, 5th Avenue, and a Broadway show.",
        "Day 3: Museums (MoMA or MET) and Times Square night lights."
    ]
}

def get_user_preferences():
    print("👋 Welcome to WanderWise — Your Smart Travel Planner!")
    activities = input("What activities do you enjoy? (e.g., beach, museums, food): ").strip().lower().split(',')
    budget = input("What's your travel budget? (low / medium / high): ").strip().lower()
    companions = input("Who are you traveling with? (solo / partner / friends / family): ").strip().lower()
    return {"activities": activities, "budget": budget, "companions": companions}

def show_itinerary(destination):
    print(f"\n🗺️  Sample 3-Day Itinerary for {destination}:")
    days = itinerary_data.get(destination, ["Itinerary details unavailable."])
    for day in days:
        print(f"• {day}")

def main():
    recommender = TravelRecommender("travel_data.csv")
    prefs = get_user_preferences()

    print("\n🔍 Finding destinations loved by travelers with similar tastes...\n")
    recommendations = recommender.get_recommendations(user_id="new_user")

    print("🎯 Top Travel Picks for You:")
    for i, dest in enumerate(recommendations, start=1):
        print(f"{i}. {dest}")

    for dest in recommendations:
        show_itinerary(dest)

    print("\n🧳 Ready to start booking? We’re here to help anytime!")

if __name__ == "__main__":
    main()
