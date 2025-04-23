import streamlit as st
import matplotlib.pyplot as plt

def pensioen_simulatie(
    kapitaal,
    pensioen_maand,
    gewenste_maand_inkomen,
    start_leeftijd,
    eind_leeftijd,
    inflatie,
    rendement
):
    jaren = list(range(start_leeftijd, eind_leeftijd + 1))
    saldo = kapitaal
    historiek = []

    for jaar in jaren:
        jaarlijkse_behoefte = (gewenste_maand_inkomen - pensioen_maand) * 12
        jaarlijkse_behoefte *= (1 + inflatie) ** (jaar - start_leeftijd)

        jaarlijkse_rente = saldo * rendement
        opname = jaarlijkse_behoefte

        saldo = saldo + jaarlijkse_rente - opname
        historiek.append(saldo)

        if saldo < 0:
            st.warning(f"⚠️ Kapitaal op rond leeftijd {jaar}!")
            break

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(jaren[:len(historiek)], historiek, marker='o')
    ax.set_title("Evolutie pensioenkapitaal")
    ax.set_xlabel("Leeftijd")
    ax.set_ylabel("Kapitaal (€)")
    ax.grid(True)
    st.pyplot(fig)

# Streamlit UI
st.title("💰 Pensioen Simulatie")

kapitaal = st.number_input("Startkapitaal (€)", value=500000, step=1000)
pensioen_maand = st.number_input("Maandelijks wettelijk pensioen (€)", value=1200, step=100)
gewenste_maand_inkomen = st.number_input("Gewenst totaal maandinkomen (€)", value=2200, step=100)
start_leeftijd = st.slider("Startleeftijd pensioen", min_value=55, max_value=70, value=65)
eind_leeftijd = st.slider("Verwachte levensduur (leeftijd)", min_value=75, max_value=100, value=90)
inflatie = st.slider("Inflatie (%)", min_value=0.0, max_value=0.05, value=0.02, step=0.005)
rendement = st.slider("Gemiddeld jaarlijks rendement (%)", min_value=0.0, max_value=0.08, value=0.03, step=0.005)

if st.button("📊 Simuleer"):
    pensioen_simulatie(
        kapitaal=kapitaal,
        pensioen_maand=pensioen_maand,
        gewenste_maand_inkomen=gewenste_maand_inkomen,
        start_leeftijd=start_leeftijd,
        eind_leeftijd=eind_leeftijd,
        inflatie=inflatie,
        rendement=rendement
    )

