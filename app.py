import streamlit as st
import math

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Textile Fabric Production Calculator",
    page_icon="🧵",
    layout="wide"
)

# ---------------------------------------------------------
# Title
# ---------------------------------------------------------
st.title("🧵 Textile Fabric Production Rate Calculator")
st.markdown(
    """
    Calculate the estimated production rate of fabric using
    machine speed, fabric width, machine efficiency, operating
    hours, and fabric GSM.
    """
)

st.divider()

# ---------------------------------------------------------
# Sidebar - Inputs
# ---------------------------------------------------------
st.sidebar.header("Production Parameters")

machine_type = st.sidebar.selectbox(
    "Machine Type",
    [
        "Weaving Machine",
        "Knitting Machine"
    ]
)

machine_speed = st.sidebar.number_input(
    "Machine Speed",
    min_value=0.1,
    value=500.0,
    step=10.0,
    help="For weaving: picks/min. For knitting: machine speed can be entered according to your production standard."
)

fabric_width = st.sidebar.number_input(
    "Fabric Width (meters)",
    min_value=0.01,
    value=1.60,
    step=0.01
)

efficiency = st.sidebar.number_input(
    "Machine Efficiency (%)",
    min_value=0.0,
    max_value=100.0,
    value=85.0,
    step=1.0
)

operating_hours = st.sidebar.number_input(
    "Operating Hours per Day",
    min_value=0.1,
    value=24.0,
    step=0.5
)

gsm = st.sidebar.number_input(
    "Fabric GSM",
    min_value=0.1,
    value=150.0,
    step=1.0,
    help="Grams per square meter"
)

machines = st.sidebar.number_input(
    "Number of Machines",
    min_value=1,
    value=1,
    step=1
)

# ---------------------------------------------------------
# Calculation
# ---------------------------------------------------------
def calculate_production(
    speed,
    width,
    efficiency_percent,
    hours,
    fabric_gsm,
    number_of_machines
):
    """
    Calculate fabric production.

    Assumption:
    Speed represents fabric production speed in meters/minute.

    If using a weaving machine where speed is in picks/minute,
    a separate construction-based calculation should be used.
    """

    efficiency_decimal = efficiency_percent / 100

    # Production length per minute
    meters_per_minute = speed * efficiency_decimal

    # Production per hour
    meters_per_hour = meters_per_minute * 60

    # Production per day for one machine
    meters_per_day_single = meters_per_hour * hours

    # Total production for all machines
    total_meters_per_day = meters_per_day_single * number_of_machines

    # Fabric weight calculation
    # Weight (kg) = Length (m) × Width (m) × GSM / 1000
    kg_per_meter = (width * fabric_gsm) / 1000

    total_kg_per_day = total_meters_per_day * kg_per_meter

    return (
        meters_per_minute,
        meters_per_hour,
        total_meters_per_day,
        kg_per_meter,
        total_kg_per_day
    )


if st.sidebar.button("Calculate Production", type="primary"):

    (
        meters_per_minute,
        meters_per_hour,
        total_meters_per_day,
        kg_per_meter,
        total_kg_per_day
    ) = calculate_production(
        machine_speed,
        fabric_width,
        efficiency,
        operating_hours,
        gsm,
        machines
    )

    # -----------------------------------------------------
    # Results
    # -----------------------------------------------------
    st.subheader("📊 Production Results")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Production / Minute",
            f"{meters_per_minute:,.2f} m"
        )

    with col2:
        st.metric(
            "Production / Hour",
            f"{meters_per_hour:,.2f} m"
        )

    with col3:
        st.metric(
            "Production / Day",
            f"{total_meters_per_day:,.2f} m"
        )

    with col4:
        st.metric(
            "Weight / Day",
            f"{total_kg_per_day:,.2f} kg"
        )

    st.divider()

    # -----------------------------------------------------
    # Detailed Calculation
    # -----------------------------------------------------
    st.subheader("📋 Calculation Details")

    results = {
        "Machine Type": machine_type,
        "Machine Speed": f"{machine_speed:,.2f}",
        "Fabric Width": f"{fabric_width:,.2f} m",
        "Machine Efficiency": f"{efficiency:,.2f}%",
        "Operating Hours": f"{operating_hours:,.2f} hours",
        "Number of Machines": f"{machines}",
        "Fabric GSM": f"{gsm:,.2f} g/m²",
        "Fabric Weight per Meter": f"{kg_per_meter:,.4f} kg/m",
        "Production per Minute": f"{meters_per_minute:,.2f} m",
        "Production per Hour": f"{meters_per_hour:,.2f} m",
        "Total Production per Day": f"{total_meters_per_day:,.2f} m",
        "Total Weight per Day": f"{total_kg_per_day:,.2f} kg"
    }

    for key, value in results.items():
        col1, col2 = st.columns([2, 2])

        with col1:
            st.write(f"**{key}**")

        with col2:
            st.write(value)

    # -----------------------------------------------------
    # Formula Explanation
    # -----------------------------------------------------
    st.divider()
    st.subheader("🧮 Formula Used")

    st.latex(
        r"""
        Effective\ Speed =
        Machine\ Speed \times \frac{Efficiency}{100}
        """
    )

    st.latex(
        r"""
        Production/hour =
        Effective\ Speed \times 60
        """
    )

    st.latex(
        r"""
        Production/day =
        Production/hour \times Operating\ Hours
        \times Number\ of\ Machines
        """
    )

    st.latex(
        r"""
        Fabric\ Weight\ (kg) =
        \frac{Length\ (m) \times Width\ (m) \times GSM}{1000}
        """
    )

else:
    st.info(
        "Enter your textile production parameters in the sidebar "
        "and click **Calculate Production**."
    )

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.divider()

st.caption(
    "Textile Fabric Production Calculator | Built with Streamlit"
)
