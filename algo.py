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
    </style>
""", unsafe_allow_html=True)

def get_teams_data() -> List[Dict]:
    return [
        {'base': '22', 'team_name': 'Infieles F.C.', 'captain': 'Christian Torres'},
        {'base': '24', 'team_name': 'Manchester FISI', 'captain': 'Christopher Saccaco'},
        {'base': '23', 'team_name': 'Sporting Mostaza FC', 'captain': 'Paolo Quispe'},
        {'base': '24', 'team_name': 'La Vecindad FC', 'captain': 'Angel Salazar'},
        {'base': '21', 'team_name': 'FC BARCELONA', 'captain': 'Gorka Contreras'},
        {'base': '23', 'team_name': 'FisiBayern B23', 'captain': 'Jose Ñahuis'},
        {'base': '20', 'team_name': 'Toque Fino', 'captain': 'Diego Chavez'},
        {'base': '22', 'team_name': 'Sport Mottazoide', 'captain': 'Angel Dioses'},
        {'base': '20', 'team_name': 'León XIV F. C', 'captain': 'Sandro Guevara'},
        {'base': '23', 'team_name': 'Los Migajeros', 'captain': 'Francess Vasquez'},
        {'base': '25', 'team_name': 'Fisichulones fc', 'captain': 'Fabrizio Cerna'},
        {'base': '25', 'team_name': 'Creeper FC', 'captain': 'Fabio Marin'},
        {'base': '25', 'team_name': 'Los Galácticos de la FISI', 'captain': 'Sebastian Cisneros'},
        {'base': '25', 'team_name': 'DarkGWolves', 'captain': 'Rafael Marina'},
        {'base': '23', 'team_name': 'F++', 'captain': 'Anderson Tataje'},
        {'base': '22', 'team_name': 'Los operadores', 'captain': 'Jack Zavaleta'},
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
    # Layout: 8vos (izq) - Cuartos (izq) - Semis (izq) - Final - Semis (der) - Cuartos (der) - 8vos (der)
    col_8vos_izq, col_cuartos_izq, col_semis_izq, col_final, col_semis_der, col_cuartos_der, col_8vos_der = st.columns([2,2,2,1.5,2,2,2], gap="small")

    # 8vos Izquierda (primeros 8 posiciones, partidos 1 a 4)
    with col_8vos_izq:
        st.markdown("<h3 style='text-align: center;'>8vos de Final</h3>", unsafe_allow_html=True)
        for i in range(0, 8, 2):
            team1 = create_team_card(bracket_positions[i])
            team2 = create_team_card(bracket_positions[i+1])
            st.markdown(f"""
                <div style='text-align:center; color:#1f77b4; font-weight:bold; margin-bottom: 4px;'>Partido {(i//2)+1}</div>
                {team1}
                {team2}
            """, unsafe_allow_html=True)

    # Cuartos Izquierda (partidos 1 y 2)
    with col_cuartos_izq:
        st.markdown("<h3 style='text-align: center;'>Cuartos de Final</h3>", unsafe_allow_html=True)
        # Espaciado superior para alinear con los 8vos
        st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
        for i in range(0, 4, 2):
            st.markdown(f"""
                <div style='background:#fff3e0; padding:10px; border-radius:8px; margin:135px auto; text-align:center; max-width: 200px;'>
                    <strong style='color:#ef6c00;'>Cuarto {(i//2)+1}</strong><br>
                    <small>Ganador Partido {i+1} vs Partido {i+2}</small>
                </div>
            """, unsafe_allow_html=True)

    # Semis Izquierda (partido 1)
    with col_semis_izq:
        st.markdown("<h3 style='text-align: center;'>Semifinales</h3>", unsafe_allow_html=True)
        # Espaciado superior para centrar verticalmente
        st.markdown("<div style='height: 120px;'></div>", unsafe_allow_html=True)
        st.markdown(f"""
            <div style='background:#e0f2f1; padding:12px; border-radius:8px; margin:250px auto; text-align:center; max-width: 200px;'>
                <strong style='color:#00796b;'>Semifinal 1</strong><br>
                <small>Ganador Cuarto 1 vs Cuarto 2</small>
            </div>
        """, unsafe_allow_html=True)

    # Final (centro)
    with col_final:
        st.markdown("<h3 style='text-align: center;'>Final</h3>", unsafe_allow_html=True)
        # Espaciado superior para centrar verticalmente
        st.markdown("<div style='height: 180px;'></div>", unsafe_allow_html=True)
        st.markdown("""
            <div style='background:#fff9c4; padding:16px; border-radius:8px; margin:185px auto; text-align:center; max-width: 200px;'>
                <strong style='color:#fbc02d;'>🏆 FINAL 🏆</strong><br>
                <small>Ganador SF1 vs Ganador SF2</small>
            </div>
        """, unsafe_allow_html=True)

    # Semis Derecha (partido 2)
    with col_semis_der:
        st.markdown("<h3 style='text-align: center;'>Semifinales</h3>", unsafe_allow_html=True)
        # Espaciado superior para centrar verticalmente
        st.markdown("<div style='height: 120px;'></div>", unsafe_allow_html=True)
        st.markdown(f"""
            <div style='background:#e0f2f1; padding:12px; border-radius:8px; margin:250px auto; text-align:center; max-width: 200px;'>
                <strong style='color:#00796b;'>Semifinal 2</strong><br>
                <small>Ganador Cuarto 3 vs Cuarto 4</small>
            </div>
        """, unsafe_allow_html=True)

    # Cuartos Derecha (partidos 3 y 4)
    with col_cuartos_der:
        st.markdown("<h3 style='text-align: center;'>Cuartos de Final</h3>", unsafe_allow_html=True)
        # Espaciado superior para alinear con los 8vos
        st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
        for i in range(4, 8, 2):
            st.markdown(f"""
                <div style='background:#fff3e0; padding:10px; border-radius:8px; margin:135px auto; text-align:center; max-width: 200px;'>
                    <strong style='color:#ef6c00;'>Cuarto {(i//2)+1}</strong><br>
                    <small>Ganador Partido {i+1} vs Partido {i+2}</small>
                </div>
            """, unsafe_allow_html=True)

    # 8vos Derecha (últimos 8 posiciones, partidos 5 a 8)
    with col_8vos_der:
        st.markdown("<h3 style='text-align: center;'>8vos de Final</h3>", unsafe_allow_html=True)
        for i in range(8, 16, 2):
            team1 = create_team_card(bracket_positions[i])
            team2 = create_team_card(bracket_positions[i+1])
            st.markdown(f"""
                <div style='text-align:center; color:#1f77b4; font-weight:bold; margin-bottom: 4px;'>Partido {(i//2)+1}</div>
                {team1}
                {team2}
            """, unsafe_allow_html=True)


def main():
    st.title(":soccer: Sorteo Interbases FISI 2025")
    teams = get_teams_data()
    if 'bracket_positions' not in st.session_state:
        st.session_state.bracket_positions = [None] * 16
    if 'all_sorted' not in st.session_state:
        st.session_state.all_sorted = False
    # Primera fila: Títulos alineados a centro en cada sector
    col_izq_t, col_centro_t, col_der_t = st.columns([4, 2, 4])
    with col_izq_t:
        st.markdown("<h3 style='text-align: center;'>📋 Equipos Registrados</h3>", unsafe_allow_html=True)
    with col_centro_t:
        st.markdown("<h3 style='text-align: center;'>🎲 Sorteo</h3>", unsafe_allow_html=True)
    with col_der_t:
        st.markdown("<h3 style='text-align: center;'>📋 Equipos Registrados</h3>", unsafe_allow_html=True)

    # Segunda fila: contenido (equipos a izq y der, sorteo al centro)
    col_izq, col_centro, col_der = st.columns([4, 2, 4])

    # Equipos izquierda (primeros 8) en 4 columnas
    with col_izq:
        cols_izq = st.columns(4)
        for i in range(8):
            team = teams[i]
            col_idx = i % 4
            with cols_izq[col_idx]:
                st.markdown(f"""
                <div style='background:#f9fbe7; border:1px solid #dce775; padding:10px; margin:8px 0; border-radius:5px;'>
                    <strong>{team['team_name']} - B{team['base']}</strong><br>
                    <small>Capitán: {team['captain']}</small>
                </div>
                """, unsafe_allow_html=True)

    # Sector central (sorteo)
    with col_centro:
        if st.button("🎯 Sortear", use_container_width=True, disabled=st.session_state.all_sorted):
            st.session_state.bracket_positions = sort_next_team(teams, st.session_state.bracket_positions)
            if all(st.session_state.bracket_positions):
                st.session_state.all_sorted = True
            st.rerun()

        if st.button("🔄 Reiniciar", use_container_width=True):
            st.session_state.bracket_positions = [None] * 16
            st.session_state.all_sorted = False
            st.rerun()

    # Equipos derecha (últimos 8) en 4 columnas
    with col_der:
        cols_der = st.columns(4)
        for i in range(8, len(teams)):
            team = teams[i]
            col_idx = (i - 8) % 4
            with cols_der[col_idx]:
                st.markdown(f"""
                <div style='background:#f9fbe7; border:1px solid #dce775; padding:10px; margin:8px 0; border-radius:5px;'>
                    <strong>{team['team_name']} - B{team['base']}</strong><br>
                    <small>Capitán: {team['captain']}</small>
                </div>
                """, unsafe_allow_html=True)
    # Bracket simétrico y centrado
    st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .element-container {
            padding: 0;
        }
    </style>
    """, unsafe_allow_html=True)
    create_bracket_ui(st.session_state.bracket_positions)
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()