import streamlit as st
import requests
import streamlit as st
import requests



st.title("🚢 Prédiction de survie - Titanic")
st.write("Remplis les informations ci-dessous :")

# 🎚️ 1. Age interactif
age = st.slider("Âge", min_value=0, max_value=100, value=30, step=1)

# 🧍‍♂️ 2. Sexe
sex = st.radio("Sexe", ["Homme", "Femme"])
sex_encoded = 1 if sex == "Homme" else 0

# 🎓 3. Classe
pclass = st.selectbox("Classe du billet", [1, 2, 3])

# 👨‍👩‍👧 4. Nombre de frères/soeurs + parents/enfants
sibsp = st.number_input("Nombre de frères/soeurs à bord", 0, 10, step=1)
parch = st.number_input("Nombre de parents/enfants à bord", 0, 10, step=1)

# 💰 5. Prix du billet
fare = st.slider("Tarif du billet ($)", min_value=0.0, max_value=600.0, value=50.0, step=0.5)

# 📍 6. Port d'embarquement
embarked = st.selectbox("Port d'embarquement", ["C", "Q", "S"])
embarked_map = {"C": 0, "Q": 1, "S": 2}
embarked_encoded = embarked_map[embarked]

# 🔢 7. Construire les features
features = [pclass, sex_encoded, age, sibsp, parch, fare, embarked_encoded]

if st.button("🔍 Prédire"):
    url = "http://localhost:8000/predict"  # modifie si ton API tourne ailleurs
    response = requests.post(url, json={"features": features})

    if response.status_code == 200:
        result = response.json()["prediction"]
        if result == 1:
            st.success("🎉 Cette personne aurait survécu.")
        else:
            st.error("❌ Cette personne n’aurait pas survécu.")
    else:
        st.warning("⚠️ Erreur lors de la requête à l’API.")

