import streamlit as st
import random
from typing import List, Dict, Optional

st.set_page_config(page_title="Torneo FISI 2025", page_icon="⚽", layout="wide")
st.markdown("""
    <style>
        body {
            background-color: #f4f6f8;
            color: #2c3e50;
        }
        .block-container {
            padding: 2rem 3rem;
        }
        h1 {
            text-align: center;
        }
        h2, h3, h4 {
            color: #2c3e50;
        }
        div.stButton > button {
            font-size: 18px;
            padding: 12px 24px;
        }
        .floating-sorteo-box {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: white;
            border: 2px solid #ccc;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            padding: 20px 30px;
            z-index: 1000;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

def get_teams_data() -> List[Dict]:
    return [
        {'base': '22', 'team_name': 'Infieles F.C.', 'captain': ' Tineo, Christian Torres'},
        {'base': '24', 'team_name': 'Manchester FISI', 'captain': 'Saccaco oscco, Christopher'},
        {'base': '23', 'team_name': 'Sporting Mostaza FC', 'captain': 'Quispe Arango, Paolo'},
        {'base': '24', 'team_name': 'La Vecindad FC', 'captain': 'Salazar Ruiz, Angel'},
        {'base': '21', 'team_name': 'FC BARCELONA', 'captain': 'Contreras Guardia, Gorka'},
        {'base': '23', 'team_name': 'FisiBayern B23', 'captain': 'Ñahuis Arostegui, Jose'},
        {'base': '20', 'team_name': 'Toque Fino', 'captain': 'Chavez Torres, Diego'},
        {'base': '22', 'team_name': 'Sport Mottazoide', 'captain': 'Dioses Bellota, Angel'},
        {'base': '20', 'team_name': 'León XIV F. C', 'captain': 'Guevara Sánchez, Sandro'},
        {'base': '23', 'team_name': 'Los Migajeros', 'captain': 'Vasquez Pelaez, Francess'},
        {'base': '25', 'team_name': 'Fisichulones fc', 'captain': 'Cerna Pariona, Fabrizio'},
        {'base': '25', 'team_name': 'Creeper FC', 'captain': 'Marin Yachachin, Fabio'},
        {'base': '25', 'team_name': 'Los Galácticos de la FISI', 'captain': 'Cisneros Garavito, Sebastian'},
        {'base': '25', 'team_name': 'DarkGWolves', 'captain': 'Marina Mitma, Rafael'},
        {'base': '23', 'team_name': 'F++', 'captain': 'Tataje Rodríguez, Anderson'},
        {'base': '22', 'team_name': 'Los operadores', 'captain': 'Zavaleta Gavilán, Jack'},
    ]

def sort_next_team(teams: List[Dict], bracket_positions: List[Optional[Dict]]) -> List[Optional[Dict]]:
    sorted_teams = [pos for pos in bracket_positions if pos is not None]
    sorted_names = [team['team_name'] for team in sorted_teams]
    available = [team for team in teams if team['team_name'] not in sorted_names]
    if not available:
        return bracket_positions
    for i, pos in enumerate(bracket_positions):
        if pos is None:
            bracket_positions[i] = random.choice(available)
            break
    return bracket_positions

def create_team_card(team):
    if not team:
        return """
        <div style="padding: 10px; border-radius: 8px; background-color: #f5f5f5; border: 1px solid #ccc; margin-bottom:4px; height: 80px; display: flex; justify-content: center; align-items: center;">
            <strong style="color: #999;">Por definir</strong>
        </div>
        """
    return f"""
        <div style="
            padding: 10px;
            border-radius: 8px;
            background-color: #e3f2fd;
            border: 1px solid #90caf9;
            margin-bottom: 4px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 80px;
        ">
            <strong style="font-size: 24px; margin: 0;">{team['team_name']}</strong>
            <strong style="margin: 0;">B{team['base']} - {team['captain']}</strong>
        </div>
    """

def create_bracket_ui(bracket_positions):
    st.markdown("<h2 style='text-align: center;'>🏆 Bracket del Torneo</h2>", unsafe_allow_html=True)
    # (omitido por brevedad, igual al tuyo…)

def main():
    st.title(":soccer: Sorteo Interbases FISI 2025")
    teams = get_teams_data()
    if 'bracket_positions' not in st.session_state:
        st.session_state.bracket_positions = [None] * 16
    if 'all_sorted' not in st.session_state:
        st.session_state.all_sorted = False

    col_izq, col_der = st.columns(2)
    with col_izq:
        cols_izq = st.columns(4)
        for i in range(8):
            team = teams[i]
            with cols_izq[i % 4]:
                st.markdown(f"""
                <div style='background:#f9fbe7; border:1px solid #dce775; padding:10px; margin:8px 0; border-radius:5px;'>
                    <strong>{team['team_name']} - B{team['base']}</strong><br>
                    <small>Capitán: {team['captain']}</small>
                </div>
                """, unsafe_allow_html=True)

    with col_der:
        cols_der = st.columns(4)
        for i in range(8, 16):
            team = teams[i]
            with cols_der[i % 4]:
                st.markdown(f"""
                <div style='background:#f9fbe7; border:1px solid #dce775; padding:10px; margin:8px 0; border-radius:5px;'>
                    <strong>{team['team_name']} - B{team['base']}</strong><br>
                    <small>Capitán: {team['captain']}</small>
                </div>
                """, unsafe_allow_html=True)

    # Sorteo flotante
    st.markdown("<div class='floating-sorteo-box'>", unsafe_allow_html=True)
    st.markdown("<h3>🎲 Sorteo</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎯 Sortear equipo"):
            st.session_state.bracket_positions = sort_next_team(teams, st.session_state.bracket_positions)
            st.session_state.all_sorted = all(pos is not None for pos in st.session_state.bracket_positions)
    with col2:
        if st.button("🔄 Reiniciar sorteo"):
            st.session_state.bracket_positions = [None] * 16
            st.session_state.all_sorted = False
    st.markdown("</div>", unsafe_allow_html=True)

    create_bracket_ui(st.session_state.bracket_positions)

if __name__ == "__main__":
    main()
