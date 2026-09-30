import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# =========================
# NATION DATA
# =========================

nation_data = pd.read_excel("網路APP檔案.xlsx")

countries = sorted(
    nation_data["Country"]
    .dropna()
    .astype(str)
    .str.strip()
    .tolist()
)

# =========================
# PAGE SETUP
# =========================
st.set_page_config(
    page_title="MY NET ZERO | GNPA",

    layout="wide"
)


# =========================
# HERO VIDEO
# =========================
if st.session_state.get("hero_visible", True):
    st.video(
        "hero.mp4",
        autoplay=True,
        muted=True,
        loop=False
    )

# =========================
# COLORS / STYLE
# =========================
st.markdown("""
<style>

.stApp {
    background-color: #FAFAF7;
}

.block-container {
    max-width: 1150px;
    padding-top: 45px;
    padding-bottom: 80px;
}

.gnpa {
    color: #2F765D;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 3px;
}

.agency {
    color: #68757D;
    font-size: 15px;
    margin-top: 5px;
}

.main-title {
    color: #123047;
    font-size: 70px;
    font-weight: 750;
    letter-spacing: -3px;
    margin-top: 55px;
    margin-bottom: 5px;
}

.world-title {
    color: #2F765D;
    font-size: 18px;
    font-weight: 700;
    letter-spacing: 4px;
    margin-bottom: 70px;
}

.small-title {
    color: #68757D;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.formula {
    color: #123047;
    font-size: 42px;
    font-weight: 650;
    margin-top: 10px;
    margin-bottom: 35px;
}

.divider {
    height: 1px;
    background-color: #D9DEDB;
    margin-top: 25px;
    margin-bottom: 50px;
}

.diet-title {
    color: #123047;
    font-size: 32px;
    font-weight: 750;
    letter-spacing: 3px;
}

.number-title {
    color: #68757D;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 2px;
}

.big-number {
    color: #123047;
    font-size: 43px;
    font-weight: 700;
}

.small-number {
    color: #68757D;
    font-size: 14px;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================
# GNPA
# =========================
st.markdown(
    '<div style="font-size:24px; font-weight:800; color:#2F765D; '
    'letter-spacing:6px; margin-top:28px; margin-bottom:6px;">'
    'GNPA'
    '</div>'
    '<div style="font-size:14px; font-weight:600; color:#123047; '
    'letter-spacing:1.6px; text-transform:uppercase; margin-bottom:34px;">'
    'Global Nature & Plant-based Diet Shift Agency'
    '</div>',
    unsafe_allow_html=True
)


# =========================
# MY NET ZERO
# =========================
st.markdown(
    '<div class="main-title">MY NET ZERO</div>',
    unsafe_allow_html=True
)

# =========================
# MAIN NAVIGATION
# =========================

nav1, nav2, nav3, nav4 = st.columns(4)

with nav1:
    for_me = st.button(
        "FOR ME",
        use_container_width=True
    )

with nav2:
    my_nation = st.button(
        "MY NATION",
        use_container_width=True
    )

with nav3:
    our_world = st.button(
        "OUR WORLD",
        use_container_width=True
    )

with nav4:
    beyond_net_zero = st.button(
        "BEYOND NET ZERO",
        use_container_width=True
    )


# =========================
# MY NATION SELECTOR
# =========================

# =========================
# PAGE SELECTION
# =========================

if "show_nation" not in st.session_state:
    st.session_state.show_nation = False

if "show_for_me" not in st.session_state:
    st.session_state.show_for_me = False

if "show_beyond" not in st.session_state:
    st.session_state.show_beyond = False

if "hero_visible" not in st.session_state:
    st.session_state.hero_visible = True

if for_me:
    st.session_state.show_for_me = True
    st.session_state.show_nation = False
    st.session_state.show_beyond = False
    st.session_state.hero_visible = False

if my_nation:
    st.session_state.show_for_me = False
    st.session_state.show_nation = True
    st.session_state.show_beyond = False
    st.session_state.hero_visible = False

if our_world:
    st.session_state.show_for_me = False
    st.session_state.show_nation = False
    st.session_state.show_beyond = False
    st.session_state.hero_visible = False

if beyond_net_zero:
    st.session_state.show_for_me = False
    st.session_state.show_nation = False
    st.session_state.show_beyond = True
    st.session_state.hero_visible = False

# =========================
# PAGE BACKGROUND
# =========================

if st.session_state.show_for_me:
    page_bg = "#FCECEF"

elif st.session_state.show_nation:
    page_bg = "#F6F0DF"

elif st.session_state.show_beyond:
    page_bg = "#EAF5ED"

else:
    page_bg = "#EAF4F8"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {page_bg};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# BEYOND NET ZERO
# =========================

if st.session_state.show_beyond:

    st.markdown(
        '<div style="font-size:48px; font-weight:750; color:#123047; '
        'margin-top:55px; letter-spacing:-1px;">'
        'BEYOND NET ZERO'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="font-size:30px; font-weight:700; color:#2F765D; '
        'margin-top:8px; margin-bottom:35px;">'
        'A THRIVING FUTURE'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="font-size:21px; line-height:1.8; color:#123047; '
        'max-width:850px; margin-bottom:50px;">'
        'Changing an unsustainable system is not about giving up the future.<br>'
        'It is about unlocking a future more abundant, more advanced, '
        'and more exciting than we imagined.'
        '</div>',
        unsafe_allow_html=True
    )

    future1, future2, future3, future4 = st.columns(4)

    with future1:
        st.markdown("### FOOD SECURITY")

    with future2:
        st.markdown("### A RESTORED PLANET")

    with future3:
        st.markdown("### CLIMATE STABILITY")

    with future4:
        st.markdown("### HUMAN ADVANCEMENT")
     
# =========================
# FOR ME
# =========================

if st.session_state.show_for_me:

    st.markdown(
        '<div style="font-size:32px; font-weight:700; color:#123047; '
        'margin-top:30px;">FOR ME</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:#2F765D; font-size:15px; font-weight:700; '
        'letter-spacing:2px; margin-top:25px;">MY NET ZERO INDEX</div>',
        unsafe_allow_html=True
    )

    if "diet_choice" not in st.session_state:
        st.session_state.diet_choice = "ANIMAL-BASED"

    if st.session_state.diet_choice == "PLANT-BASED":
        my_net_zero_index = -6
    else:
        my_net_zero_index = 10

    st.markdown(
        f'<div style="font-size:64px; font-weight:750; color:#123047; '
        f'margin-top:5px; margin-bottom:30px;">{my_net_zero_index}</div>',
        unsafe_allow_html=True
    )
    

    personal1, personal2 = st.columns(2)

    with personal1:
        st.markdown(
            '<div class="number-title">EVERYDAY LIFE</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size:46px; font-weight:700; color:#123047; '
            'margin-top:10px;">2</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="small-number">'
            'Energy · Transport · Cooking · Appliances'
            '</div>',
            unsafe_allow_html=True
        )

    with personal2:

        st.markdown(
            '<div class="number-title">FOOD</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div style="font-size:46px; font-weight:700; color:#123047; '
            'margin-top:10px;">8</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="small-number">'
            'Animal-based food system'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<div style="height:35px;"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:#2F765D; font-size:15px; font-weight:700; '
        'letter-spacing:2px;">YOUR DIET</div>',
        unsafe_allow_html=True
    )

    diet1, diet2 = st.columns(2)

    if "diet_choice" not in st.session_state:
        st.session_state.diet_choice = "ANIMAL-BASED"

    with diet1:
        plant_based = st.button(
            "PLANT-BASED",
            use_container_width=True
        )

        if plant_based:
            st.session_state.diet_choice = "PLANT-BASED"
            st.rerun()

    with diet2:
        animal_based = st.button(
            "ANIMAL-BASED",
            use_container_width=True
        )

        if animal_based:
            st.session_state.diet_choice = "ANIMAL-BASED"
            st.rerun()

  
    if st.session_state.diet_choice == "PLANT-BASED":

        st.markdown(
            '<div style="height:35px;"></div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div style="color:#2F765D; font-size:15px; font-weight:700; '
            'letter-spacing:2px; margin-bottom:20px;">WHAT CHANGES?</div>',
            unsafe_allow_html=True
        )

        # FIRST ROW
        change1, change2, change3 = st.columns(3)

        with change1:
            st.markdown(
                '<div class="number-title">METHANE REDUCTION</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:27px; font-weight:700; color:#123047; '
                'margin-top:10px;">REDUCED</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">livestock-related methane emissions</div>',
                unsafe_allow_html=True
            )

        with change2:
            st.markdown(
                '<div class="number-title">LAND RELEASED</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:32px; font-weight:700; color:#123047; '
                'margin-top:10px;">78%</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">of global agricultural land</div>',
                unsafe_allow_html=True
            )

        with change3:
            st.markdown(
                '<div class="number-title">FOREST RECOVERY</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:32px; font-weight:700; color:#123047; '
                'margin-top:10px;">41%</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">of tropical deforestation linked to beef production</div>',
                unsafe_allow_html=True
            )

        # SPACE BETWEEN TWO ROWS
        st.markdown(
            '<div style="height:30px;"></div>',
            unsafe_allow_html=True
        )

        # SECOND ROW
        change4, change5, change6 = st.columns(3)

        with change4:
            st.markdown(
                '<div class="number-title">NATURAL CO₂ ABSORPTION</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:27px; font-weight:700; color:#123047; '
                'margin-top:10px;">RESTORED</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">through ecosystem recovery</div>',
                unsafe_allow_html=True
            )

        with change5:
            st.markdown(
                '<div class="number-title">OCEAN DEAD ZONE RECOVERY</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:32px; font-weight:700; color:#123047; '
                'margin-top:10px;">80%</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">dead zones recover and coastal marine forests resume CO₂ absorption</div>',
                unsafe_allow_html=True
            )

        with change6:
            st.markdown(
                '<div class="number-title">FOSSIL ENERGY REDUCTION</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div style="font-size:32px; font-weight:700; color:#123047; '
                'margin-top:10px;">41%</div>',
                unsafe_allow_html=True
            )
            st.markdown(
                '<div class="small-number">attributed to livestock-system energy use</div>',
                unsafe_allow_html=True
            )

if st.session_state.show_nation:
    selected_country = st.selectbox(
        "SELECT YOUR NATION",
        countries
    )

    selected_row = nation_data[
        nation_data["Country"].astype(str).str.strip() == selected_country
    ].iloc[0]

    selected_region = selected_row["Groups"]

    st.markdown(
        f'<div style="font-size:32px; font-weight:700; color:#123047; '
        f'margin-top:25px;">{selected_country.upper()}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div style="font-size:16px; color:#68757D; '
        f'margin-top:5px;">{selected_region}</div>',
        unsafe_allow_html=True
    )
    
     
    co2_impact = selected_row["Cow's CO2  impact "]
    gdp_impact = selected_row["COW's GDP impacts"]

    result1, result2 = st.columns(2)

    with result1:
        st.markdown(
            '<div class="number-title">LIVESTOCK CO₂ IMPACT</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div style="font-size:38px; font-weight:700; '
            f'color:#123047; margin-top:10px;">{co2_impact*100:,.0f}%</div>',
            unsafe_allow_html=True
        )

    with result2:
        st.markdown(
            '<div class="number-title">LIVESTOCK GDP IMPACT</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div style="font-size:38px; font-weight:700; '
            f'color:#123047; margin-top:10px;">{gdp_impact*100:,.0f}%</div>',
            unsafe_allow_html=True
        )

    regional_co2 = selected_row["Livestock CO2 Region"]
    regional_gdp = selected_row["Livestock GDP Region"]

    st.markdown(
        f'<div style="font-size:15px; font-weight:700; color:#2F765D; '
        f'letter-spacing:2px; margin-top:35px;">'
        f'{selected_region.upper()} — REGIONAL COMPARISON</div>',
        unsafe_allow_html=True
    )

    region1, region2 = st.columns(2)

    with region1:
        st.markdown(
            '<div class="number-title">REGIONAL CO₂ IMPACT</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div style="font-size:30px; font-weight:700; color:#123047; '
            f'margin-top:8px;">{regional_co2 * 100:,.0f}%</div>',
            unsafe_allow_html=True
        )

    with region2:
        st.markdown(
            '<div class="number-title">REGIONAL GDP IMPACT</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div style="font-size:30px; font-weight:700; color:#123047; '
            f'margin-top:8px;">{regional_gdp * 100:,.0f}%</div>',
            unsafe_allow_html=True
        )


    # =========================
    # CALCULATION BASIS
    # =========================

    st.markdown(
        '<div style="height:25px;"></div>',
        unsafe_allow_html=True
    )

    basis1, basis2 = st.columns(2)

    with basis1:
        st.markdown(
            '<div style="border:1px solid #D9DEDB; border-radius:8px; padding:20px 24px; min-height:250px;">'
            '<div style="color:#123047; font-size:15px; font-weight:700; letter-spacing:1.5px; margin-bottom:18px;">CO₂ IMPACT — CALCULATION BASIS</div>'
            '<div style="color:#68757D; font-size:15px; line-height:2;">Methane emissions<br>Grazing land<br>Deforestation<br>Energy use<br>Fossil fuels</div>'
            '</div>',
            unsafe_allow_html=True
        )

    with basis2:
        st.markdown(
            '<div style="border:1px solid #D9DEDB; border-radius:8px; padding:20px 24px; min-height:250px;">'
            '<div style="color:#123047; font-size:15px; font-weight:700; letter-spacing:1.5px; margin-bottom:18px;">GDP IMPACT — CALCULATION BASIS</div>'
            '<div style="color:#68757D; font-size:15px; line-height:2;">Methane emissions<br>Water<br>Soil erosion<br>Deforestation<br>Feed crops</div>'
            '</div>',
            unsafe_allow_html=True
        )

    st.markdown(
        '<div style="color:#68757D; font-size:13px; margin-top:12px;">'
        'Results are calculated using the MY NET ZERO research model.'
        '</div>',
        unsafe_allow_html=True
    )
    
    # =========================
    # KEY NATIONAL MESSAGE
    # =========================

    national_message = selected_row["Key national message"]

    st.markdown(
        '<div style="height:30px;"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="color:#2F765D; font-size:14px; font-weight:700; '
        'letter-spacing:2px;">KEY NATIONAL MESSAGE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div style="color:#123047; font-size:20px; line-height:1.7; '
        f'margin-top:12px; margin-bottom:20px;">{national_message}</div>',
        unsafe_allow_html=True
    )



st.markdown(
    '<div class="world-title">WORLD NET ZERO</div>',
    unsafe_allow_html=True
)


# =========================
# NET ZERO FORMULAS
# =========================
col1, col2 = st.columns(2)

with col1:

    st.markdown(
        '<div class="small-title">'
        'Conventional Net Zero'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="formula">'
        '1 − 1 = 0'
        '</div>',
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        '<div class="small-title">'
        'Actual Net Zero Gap'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '''
        <div style="
            color:#123047;
            font-size:34px;
            font-weight:600;
            margin-top:10px;
            line-height:1.25;
            white-space:nowrap;
        ">
            Net Zero = 1 − (0.25 − 11.87)
        </div>

        <div style="
            color:#123047;
            font-size:58px;
            font-weight:750;
            letter-spacing:-2px;
            margin-top:12px;
            margin-bottom:25px;
        ">
            = 12.62
        </div>
        ''',
        unsafe_allow_html=True
    )

  


# =========================
# WHY
# =========================
with st.expander("WHY?"):

    st.image(
        "net_zero_gap.png.png",
        caption="Figure 1.1. Measurement of the distance from the present to climate success.",
        use_container_width=True
    )

    st.markdown("""
### THE NET ZERO GAP

**Atmospheric CO₂ gap**

426 ppm − 350 ppm ≈ **76 ppm**

**CO₂ equivalent**

76 ppm × 7.81 GtCO₂/ppm ≈ **593 GtCO₂**

**Equivalent years of global emissions**

593 GtCO₂ ÷ 50 GtCO₂/year ≈ **11.87 years**

**MY NET ZERO model**

1 − (0.25 − 11.87) ≈ **12.62**

*Conversion basis: Poljak (2023), where each atmospheric CO₂ ppm ≈ 7.81 GtCO₂.*
""")

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)


# =========================
# DIET SHIFT
# =========================
st.markdown(
    '<div class="diet-title">DIET SHIFT</div>',
    unsafe_allow_html=True
)


diet_shift = st.slider(
    "Diet Shift",
    0,
    100,
    0,
    1,
    label_visibility="collapsed"
)


# =========================
# CALCULATION
# =========================

MAX_CO2 = 643.0

START_PPM = 426.0
TARGET_PPM = 350.0

co2_reduced = MAX_CO2 * diet_shift / 100

co2_remaining = MAX_CO2 - co2_reduced

current_ppm = (
    START_PPM
    - (START_PPM - TARGET_PPM)
    * diet_shift / 100
)

ppm_reduced = START_PPM - current_ppm


# =========================
# RESULTS
# =========================
col3, col4 = st.columns(2)

with col3:

    st.markdown(
        '<div class="number-title">'
        'CO₂ REDUCED'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="big-number">'
        f'{co2_reduced:.1f} GtCO₂'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="small-number">'
        f'{co2_remaining:.1f} GtCO₂ remaining'
        f'</div>',
        unsafe_allow_html=True
    )


with col4:

    st.markdown(
        '<div class="number-title">'
        'ATMOSPHERIC CO₂'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="big-number">'
        f'{current_ppm:.1f} ppm'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="small-number">'
        f'426 → {current_ppm:.1f} ppm'
        f'</div>',
        unsafe_allow_html=True
    )


# =========================
# CHART DATA
# =========================

x = np.arange(0, 101)

carbon_curve = MAX_CO2 * (1 - x / 100)

ppm_curve = (
    START_PPM
    - (START_PPM - TARGET_PPM)
    * x / 100
)


# =========================
# CHART 1
# =========================

chart1, chart2 = st.columns(2)


with chart1:

    fig1 = go.Figure()

    fig1.add_trace(
        go.Scatter(
            x=x,
            y=carbon_curve,
            mode="lines",
            line=dict(
                color="#123047",
                width=4
            )
        )
    )

    fig1.add_trace(
        go.Scatter(
            x=[diet_shift],
            y=[co2_remaining],
            mode="markers",
            marker=dict(
                size=13,
                color="#2F765D"
            )
        )
    )

    fig1.update_layout(
        title="CO₂ GAP",
        height=330,
        showlegend=False,
        paper_bgcolor="#FAFAF7",
        plot_bgcolor="#FAFAF7",
        xaxis_title="Diet Shift (%)",
        yaxis_title="GtCO₂ remaining",
        margin=dict(
            l=20,
            r=20,
            t=55,
            b=30
        )
    )

    st.plotly_chart(
        fig1,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )


# =========================
# CHART 2
# =========================

with chart2:

    fig2 = go.Figure()

    fig2.add_trace(
        go.Scatter(
            x=x,
            y=ppm_curve,
            mode="lines",
            line=dict(
                color="#2F765D",
                width=4
            )
        )
    )

    fig2.add_trace(
        go.Scatter(
            x=[diet_shift],
            y=[current_ppm],
            mode="markers",
            marker=dict(
                size=13,
                color="#123047"
            )
        )
    )

    fig2.update_layout(
        title="ATMOSPHERIC CO₂",
        height=330,
        showlegend=False,
        paper_bgcolor="#FAFAF7",
        plot_bgcolor="#FAFAF7",
        xaxis_title="Diet Shift (%)",
        yaxis_title="ppm",
        margin=dict(
            l=20,
            r=20,
            t=55,
            b=30
        )
    )

    st.plotly_chart(
        fig2,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )

# =========================
# KEY IMPACTS
# =========================

st.markdown(
    '<div class="divider"></div>',
    unsafe_allow_html=True
)

impact1, impact2, impact3 = st.columns(3)

with impact1:
    st.markdown(
        '<div class="number-title">LAND RELEASED</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="font-size:32px; font-weight:700; color:#123047; '
        'margin-top:12px; white-space:nowrap;">37 million km²</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="small-number">78% of global agricultural land</div>',
        unsafe_allow_html=True
    )

with impact2:
    st.markdown(
        '<div class="number-title">GHG REDUCTION</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="font-size:32px; font-weight:700; color:#123047; '
        'margin-top:12px;">166%</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="small-number">of 2020 global GHG</div>',
        unsafe_allow_html=True
    )

with impact3:
    st.markdown(
        '<div class="number-title">ECONOMIC COST REDUCTION</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div style="font-size:32px; font-weight:700; color:#123047; '
        'margin-top:12px;">163%</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="small-number">of 2020 world GDP</div>',
        unsafe_allow_html=True
    )

# =========================
# SECOND WHY
# =========================

with st.expander(
    "WHY DOES DIET SHIFT CHANGE CO₂?"
):

    st.markdown(
        '<div style="font-size:22px; font-weight:700; color:#123047; '
        'margin-bottom:15px;">DATA MODEL</div>',
        unsafe_allow_html=True
    )

    st.image(
        "data model.png",
        caption="MY NET ZERO research data model",
        use_container_width=True
    )


    st.markdown(
        '<div style="font-size:22px; font-weight:700; color:#123047; '
        'margin-top:35px; margin-bottom:15px;">'
        'RESEARCH STRUCTURE'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
**CHAPTER 3 — DATA AND METHODOLOGY**  
Research framework · Data · Variables · Equations · Nature Restoration Model

**CHAPTER 4 — EMISSIONS AND NATURE'S CO₂ ABSORPTION**  
Model validity · Forecasting · Sensitivity analysis · Climate scenarios

**CHAPTER 5 — EXTERNAL COSTS OF FOSSIL FUELS AND LIVESTOCK**  
Livestock externalities · Energy · Economic costs

**CHAPTER 6 — CO₂ RESPONSIBILITY OF FOSSIL FUELS AND LIVESTOCK**  
Emissions · CO₂ removal loss · Energy consumption · Land and forest sensitivity analysis · Adjusted responsibility

**CHAPTER 7 — APPLICATION AND NATURE RESTORATION MODEL**  
U.S. · China · Global climate policy · Nature restoration
        """
    )

    st.caption(
        "Detailed methodology, calculations, sensitivity analyses and "
        "underlying data are documented in the full research."
    )



    st.markdown(
        '<div style="font-size:22px; font-weight:700; color:#123047; '
        'margin-top:40px; margin-bottom:15px;">'
        'CALCULATION BASIS'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
**ENERGY — 41%**

**SOURCE DATA**  
Global meat consumption by meat type · Energy requirements by meat type · Global population · Global electricity consumption

**MY NET ZERO CALCULATION**  
Meat consumption × energy requirement by meat type × global population  
→ estimated global meat-industry electricity consumption  
→ compared with total global electricity consumption

**RESULT**  
Estimated meat-industry electricity consumption = **41% of global electricity consumption**
        """
    )

    st.caption(
        "Derived indicator calculated by the MY NET ZERO research model "
        "from underlying source data."
    )

    st.markdown(
        """
**METHANE — 31%**

**SOURCE DATA**  
Cattle population · Annual methane emissions per cow

**MY NET ZERO MODEL ASSUMPTION**  
Methane = **100× CO₂-equivalent** to represent its strong near-term warming impact

**MY NET ZERO CALCULATION**  
Cattle population × methane emissions per cow × 100 CO₂-equivalent  
→ approximately **15.2 GtCO₂-equivalent**

**RESULT**  
15.2 GtCO₂-eq. ÷ 50 GtCO₂-eq. global annual emissions  
→ **≈ 31%**
        """
    )

    st.caption(
        "The 100× methane factor is a MY NET ZERO model assumption. "
        "It is not the conventional 100-year GWP factor."
    )
 
    st.markdown(
        """
**LAND — 11%**

**SOURCE DATA**  
Livestock land use = **37 million km²**

**MY NET ZERO CALCULATION**  
37 million km² × estimated CO₂ absorption capacity of released land  
→ approximately **5.17 GtCO₂ per year**

**RESULT**  
5.17 GtCO₂ ÷ 50 GtCO₂ global annual emissions  
→ **≈ 11%**
        """
    )

    st.caption(
        "The 37 million km² livestock land-use estimate is source data. "
        "The 11% indicator is derived by the MY NET ZERO research model."
    )

    st.markdown(
        """
**FOREST — 91%**

**MODEL BOUNDARY**  
Conservative estimate using cattle in **Amazon nations and one Congo Basin country**, rather than global cattle populations

**MY NET ZERO CALCULATION**  
Cattle population in the selected tropical-forest regions × forest area impact × estimated tropical-forest CO₂ absorption capacity  
→ approximately **45.34 GtCO₂ per year**

**RESULT**  
45.34 GtCO₂ ÷ 50 GtCO₂ global annual emissions  
→ **≈ 91%**
        """
    )

    st.caption(
        "The forest estimate uses a deliberately restricted tropical-forest "
        "boundary to avoid applying one CO₂ absorption rate to forests "
        "across different climatic regions."
    )

    st.markdown(
        """
**TOTAL LIVESTOCK CO₂ RESPONSIBILITY — 166%**

**ENERGY REALLOCATION**  
Meat-industry energy use = **41%** of global electricity  
Applied to the **78% fossil-fuel baseline**  
→ 78% × 41% ≈ **32%**

**MY NET ZERO INTEGRATED CALCULATION**  
Methane **31%** + Land **11%** + Forest **91%** + Energy **32%**

**RESULT**  
31% + 11% + 91% + 32% ≈ **166%**
        """
    )

    st.caption(
        "The 166% result is an integrated MY NET ZERO research-model "
        "estimate relative to the 50 GtCO₂-eq. annual global emissions baseline."
    )


    st.markdown(
        '<div style="font-size:22px; font-weight:700; color:#123047; '
        'margin-top:40px; margin-bottom:15px;">'
        'SOURCES'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
**CORE DATA SOURCES**

**FAO / UNFAO**  
Livestock, food consumption and agricultural land-use data

**Energypedia**  
Energy requirements within food and agricultural value chains

**U.S. Energy Information Administration (EIA)**  
Global energy and electricity data

**IPCC**  
Conventional greenhouse-gas accounting and climate assessment framework
        """
    )

    st.caption(
        "Source data are used as inputs. Calculations, integration and "
        "derived indicators are produced by the MY NET ZERO research model."
    )
    st.markdown(
        """
**VIEW ORIGINAL SOURCES**

[FAO / FAOSTAT — Global Food & Agriculture Data](https://www.fao.org/faostat/)

[Energypedia — Energy within Food and Agricultural Value Chains](https://energypedia.info/wiki/Energy_within_Food_and_Agricultural_Value_Chains)

[U.S. Energy Information Administration (EIA) — Electricity Data](https://www.eia.gov/electricity/data.php)

[Gatti et al. (2021), Nature — Amazonia as a carbon source linked to deforestation and climate change](https://www.nature.com/articles/s41586-021-03629-6)
        """
    )
