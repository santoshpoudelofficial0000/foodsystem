import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Vata Ayurvedic & Modern Nutrition System",
    page_icon="🍲",
    layout="wide"
)

st.title("🌿 Vata Ayurvedic & Modern Nutrition Food System")
st.subheader("Greensboro, NC Ritucharya • 6 Tastes Matrix • Walmart Budget Ledger")
st.markdown("""
*Designed strictly according to **Ashtanga Hridayam** guidelines for Vata dosha pacification integrated with modern nutritional science.*
""")

st.sidebar.header("🧭 Navigation & Filters")
season = st.sidebar.selectbox("Select Season (Greensboro, NC)", [
    "Fall / Early Winter (Sep – Dec)",
    "Winter (Dec – Feb)",
    "Spring (Mar – May)",
    "Summer (Jun – Sep)"
])

meal_set = st.sidebar.radio("Select Weekly Meal Set", ["Meal Set 1", "Meal Set 2", "Meal Set 3", "Meal Set 4"])

st.sidebar.markdown("---")
st.sidebar.markdown("### ⏱️ Cooking Schedule")
st.sidebar.info("""
- **Sunday Night**: Batch cook Lunch & Dinner for Mon–Wed.
- **Wednesday Night**: Batch cook Lunch & Dinner for Thu–Sun.
- **Daily Breakfast**: Freshly prepared in **15 minutes or less**.
""")

# DATA DEFINITIONS
matrix_df = pd.DataFrame([
    {"Taste": "Sweet (Madhura)", "Ayurvedic Potency": "Heating/Sweet", "Protein": "Moong Dal, Tofu, Eggs, Almonds", "Fats": "Ghee, Sesame Oil, Coconut", "Carbs & Fibre": "Basmati Rice, Oats, Sweet Potatoes", "Minerals/Vitamins": "Magnesium, Potassium, B-Complex", "Vata Proportion": "70% (Primary Pacifier)"},
    {"Taste": "Sour (Amla)", "Ayurvedic Potency": "Heating/Sour", "Protein": "Cultured Yogurt (Warmed)", "Fats": "Sesame Oil, Ghee", "Carbs & Fibre": "Fermented Dosa/Idli, Sourdough", "Minerals/Vitamins": "Vitamin C, Bioflavonoids", "Vata Proportion": "15% (Agni Kindler)"},
    {"Taste": "Salty (Lavana)", "Ayurvedic Potency": "Heating/Sweet", "Protein": "Kelp, Sea Vegetables", "Fats": "Ghee", "Carbs & Fibre": "Mineralised Grains", "Minerals/Vitamins": "Sodium, Iodine, Saindhava Salt", "Vata Proportion": "10% (Fluid Balancer)"},
    {"Taste": "Pungent (Katu)", "Ayurvedic Potency": "Heating/Pungent", "Protein": "Peanuts, Pumpkin Seeds", "Fats": "Mustard Oil, Ghee", "Carbs & Fibre": "Spiced Whole Grains", "Minerals/Vitamins": "Zinc, Iron, Gingerol, Piperine", "Vata Proportion": "2% (Circulation)"},
    {"Taste": "Bitter (Tikta)", "Ayurvedic Potency": "Cooling/Pungent", "Protein": "Cooked Spinach, Methi", "Fats": "Ghee (Carrier)", "Carbs & Fibre": "Cooked Kale, Greens", "Minerals/Vitamins": "Folate, Vitamin K, Calcium", "Vata Proportion": "1.5% (Detoxification)"},
    {"Taste": "Astringent (Kashaya)", "Ayurvedic Potency": "Cooling/Pungent", "Protein": "Red Lentils, Chickpeas", "Fats": "Sesame Oil", "Carbs & Fibre": "Green Beans, Stewed Apples", "Minerals/Vitamins": "Iron, Potassium, Pectin", "Vata Proportion": "1.5% (Tissue Toning)"}
])

# MAIN LAYOUT TABS
tab_ledger, tab_matrix, tab_rules = st.tabs(["📅 Seasonal Meal Ledger & Recipes", "📊 6-Taste x Nutrient Matrix", "⚠️ Viruddha Ahara Rules"])

with tab_ledger:
    st.header(f"📍 {season} — {meal_set}")
    st.caption("Each meal in this set covers all 6 tastes and key modern macronutrients/micronutrients while strictly avoiding incompatible combinations.")
    
    col_b, col_l, col_d = st.columns(3)
    
    with col_b:
        st.markdown("### 🌅 Breakfast (Max 15 Min)")
        st.success("⏱️ Fresh Daily Prep • Warm & Unctuous")
        st.write("**Meal**: Warm Cinnamon Steel-Cut Oats w/ Ghee, Stewed Pears & Almonds")
        st.write("**6 Tastes**: Sweet, Pungent, Astringent")
        st.write("**Modern Nutrients**: Complex Carbs, Healthy Lipids, Fibre, Magnesium")
        st.write("**Walmart Ingredients**: Great Value Oats, Ghee, Bartlett Pears, Almonds")
        
        with st.expander("📖 Step-by-Step Recipe"):
            st.markdown("""
            1. **Heat**: Add 1 tsp Ghee to a small saucepan over medium heat.
            2. **Spice**: Add a pinch of cinnamon and cardamom; sizzle for 10 seconds.
            3. **Stew**: Add diced pear and 2 tbsp water. Cover and steam for 4 minutes until soft.
            4. **Oats**: Stir in 1/2 cup quick steel-cut oats and 1 cup warm water/almond milk. Simmer 5 mins.
            5. **Finish**: Top with sliced almonds and 1 extra tsp Ghee. Serve hot.
            """)

    with col_l:
        st.markdown("### ☀️ Lunch (Batch Cooked)")
        st.info("🍲 Batch Cooked Sun/Wed • Heavy & Grounding")
        st.write("**Meal**: Yellow Moong Dal Khichdi w/ Roasted Sweet Potatoes & Cumin Ghee")
        st.write("**6 Tastes**: Sweet, Salty, Pungent, Sour (with a lemon squeeze at table)")
        st.write("**Modern Nutrients**: Complete Protein, Beta-Carotene, Potassium, Carbs")
        st.write("**Walmart Ingredients**: Moong Dal, Basmati Rice, NC Sweet Potatoes, Ghee, Cumin")
        
        with st.expander("📖 Step-by-Step Recipe"):
            st.markdown("""
            1. **Prep**: Rinse 1 cup Yellow Moong Dal and 1 cup Basmati Rice together.
            2. **Sauté**: Melt 2 tbsp Ghee in an instant pot or heavy pot. Add 1 tsp cumin seeds and pinch of hing (asafoetida).
            3. **Vegetables**: Add 1 cup cubed NC Sweet Potatoes and sauté for 2 minutes.
            4. **Cook**: Add rinsed dal/rice + 6 cups water + 1 tsp Saindhava Rock Salt + 1/2 tsp turmeric. Pressure cook 12 mins (or pot boil 25 mins).
            5. **Portion**: Divide into 3.5 glass meal prep containers for Sun–Wed lunches. Reheat with 1 tsp fresh Ghee.
            """)

    with col_d:
        st.markdown("### 🌙 Dinner (Batch Cooked)")
        st.warning("🌙 Batch Cooked Sun/Wed • Warm & Light Digestible")
        st.write("**Meal**: Warm Spiced Chickpea & Butternut Squash Stew w/ Basmati Rice")
        st.write("**6 Tastes**: Sweet, Salty, Pungent, Bitter (via turmeric/spinach)")
        st.write("**Modern Nutrients**: Plant Protein, Iron, Zinc, Dietary Fibre")
        st.write("**Walmart Ingredients**: Canned Organic Chickpeas, Butternut Squash, Basmati Rice")
        
        with st.expander("📖 Step-by-Step Recipe"):
            st.markdown("""
            1. **Base**: Warm 1.5 tbsp Ghee in a pot. Add ginger paste, cumin, coriander, and turmeric.
            2. **Stew**: Add 2 cups cubed Butternut Squash and 1 can rinsed Organic Chickpeas.
            3. **Simmer**: Add 3 cups vegetable broth/water. Cover and simmer 20 mins until squash is fork-tender.
            4. **Finish**: Stir in a handful of finely chopped baby spinach and rock salt.
            5. **Serve**: Serve hot over warm Basmati Rice.
            """)

    st.markdown("---")
    st.subheader("🛒 Walmart Grocery & Budget Checklist for this Set")
    st.markdown("""
    | Item Category | Walmart Item | Approx Cost | Cheaper Bulk Alternative |
    |---|---|---|---|
    | **Grains** | Great Value White Basmati Rice (5 lb) | $4.98 | Bulk Indian Grocery Store Basmati ($3.50/5lb) |
    | **Lentils/Protein** | Great Value Organic Yellow Moong Dal / Red Lentils | $2.48 | Indian Grocery Bulk 10lb Bag |
    | **Fats** | Carrington Farms Organic Ghee (12 oz) | $8.98 | Homemade Ghee from Great Value Unsalted Butter ($3.88) |
    | **Produce** | NC Local Sweet Potatoes & Butternut Squash | $2.50 | Seasonal Produce Stand / Farmer's Market |
    | **Spices** | Great Value Ground Cumin, Turmeric, Cinnamon | $1.50/ea | Spitia Bulk Spice Aisle |
    """)

with tab_matrix:
    st.header("Shad Rasa (6 Tastes) x Modern Nutritional Matrix")
    st.dataframe(matrix_df, use_container_width=True)

with tab_rules:
    st.header("⚠️ Viruddha Ahara (Incompatible Food Combinations)")
    st.error("The following combinations cause digestive toxin (Ama) formation and must NEVER be used in your meals:")
    st.markdown("""
    - ❌ **Milk + Acids**: Milk with Lemon, Lime, Tomatoes, Sour Berries, or Yogurt.
    - ❌ **Milk + Proteins/Salts**: Milk with Fish, Meat, Eggs, or Salt.
    - ❌ **Honey Heating**: Heating Honey above 104°F (40°C) or mixing equal weights of Honey & Ghee.
    - ❌ **Melons**: Melons eaten with ANY other food (must be eaten 100% alone).
    - ❌ **Leftover Heating**: Reheating food more than once (batch cooked food must be reheated exactly once upon serving).
    """)
