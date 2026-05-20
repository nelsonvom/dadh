import streamlit as st
import time
import random

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION & THE "BAT CAVE" MATRIC THEME
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Bat Cave Command Center",
    page_icon="🦇",
    layout="wide",
)

# Custom CSS for the Neon Blue & Charcoal Aesthetic
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0c10;
        color: #c5c6c7;
    }
    .house-box {
        background-color: #1f2833;
        border: 2px solid #45f3ff;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 0 15px #45f3ff;
        margin-bottom: 20px;
    }
    .house-title {
        color: #45f3ff;
        font-weight: bold;
        font-size: 24px;
    }
    .alert-box {
        background-color: #1f2833;
        border: 2px solid #ff0055;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 0 20px #ff0055;
        animation: blinker 1.5s linear infinite;
    }
    @keyframes blinker {
        50% { opacity: 0.3; }
    }
    .status-text {
        font-size: 18px;
        font-family: 'Courier New', Courier, monospace;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. STATE MANAGEMENT (Simulating Tuya API Streams for Vibe Coding)
# -----------------------------------------------------------------------------
if 'gate_closed' not in st.session_state:
    st.session_state.gate_closed = True
if 'python_detected' not in st.session_state:
    st.session_state.python_detected = False

# -----------------------------------------------------------------------------
# 3. HEADER
# -----------------------------------------------------------------------------
st.title("🦇 THE BAT CAVE TACTICAL RADAR")
st.write("**Location:** 275 Waterford Tamborine Rd, Waterford 4133")
st.write("Integrated Ecosystem: Kmart Genio x Temu Smart Life (Tuya Backend)")
st.markdown("---")

# -----------------------------------------------------------------------------
# 4. TACTICAL VISUAL MAP (GRID LAYOUT)
# -----------------------------------------------------------------------------
st.subheader("🌐 Property Layout Radar Map")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="house-box">
            <div class="house-title">🏠 HOUSE A (275A)</div>
            <p class="status-text" style="color: #66fcf1;">Occupants: Riste Junior & Unit</p>
            <p class="status-text">Perimeter Link: STABLE</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    if st.session_state.python_detected:
        st.markdown("""
            <div class="alert-box">
                <div class="house-title" style="color: #ff0055;">⚠️ HOUSE B (THE BLUE HOUSE)</div>
                <p class="status-text" style="color: #ff0055; font-weight: bold;">CRITICAL ALERT: MOTION DETECTED ON PATIO PATH!</p>
                <p class="status-text" style="color: #ffffff;">Check Kmart Spotlight Cameras Immediately</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="house-box" style="border-color: #66fcf1; box-shadow: 0 0 15px #66fcf1;">
                <div class="house-title" style="color: #66fcf1;">🔷 HOUSE B (THE BLUE HOUSE)</div>
                <p class="status-text" style="color: #66fcf1;">Occupants: Me & Shane</p>
                <p class="status-text" style="color: #00ffcc;">Status: SECURE & CLEAR</p>
            </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# -----------------------------------------------------------------------------
# 5. HARDWARE INTERACTION & CONTROLS
# -----------------------------------------------------------------------------
st.subheader("⚡ Motor Pool & Hardware Control")

c1, c2, c3 = st.columns([1, 1, 2])

with c1:
    st.write("### Front Gate Actuator")
    if st.session_state.gate_closed:
        st.error("Gate Status: LOCKED / CLOSED")
        if st.button("🔓 DISENGAGE FRONT GATE MOTOR", use_container_width=True):
            st.session_state.gate_closed = False
            st.rerun()
    else:
        st.success("Gate Status: OPEN / UNLOCKED")
        if st.button("🔒 ENGAGE FRONT GATE MOTOR", use_container_width=True):
            st.session_state.gate_closed = True
            st.rerun()

with c2:
    st.write("### Sentry Testing")
    # A quick toggle button so you can test how the visual dashboard looks when a snake trips the sensor
    if st.button("💥 Toggle Simulation Python Tripwire", use_container_width=True):
        st.session_state.python_detected = not st.session_state.python_detected
        st.rerun()

with c3:
    st.write("### Drop Zone Lockbox Vault")
    st.info("Delivery Drop Status: Securely Latched")
    st.caption("Pressing this bypasses the Kmart Doorbell request and unlocks the Temu internal cabinet latch for 15 seconds.")
    if st.button("🔑 Remote Unlock Hidden Delivery Shed"):
        with st.spinner("Unlatching Internal Latch via Tuya Relay..."):
            time.sleep(2)
        st.success("Shed Unlocked! Latch will automatically re-lock upon closure.")

st.markdown("---")

# -----------------------------------------------------------------------------
# 6. AI WILDLIFE LOG & NOCTURNAL RADAR FEED
# -----------------------------------------------------------------------------
st.subheader("🦎 AI Edge Night-Vision Wildlife Log")

# Simulated AI camera data streams
wildlife_logs = [
    {"Time": "02:14 AM", "Device": "Temu Starlight Fence Cam", "Detection": "Wallaby (Low/Horizontal Cluster)", "Confidence": "94%"},
    {"Time": "01:05 AM", "Device": "Kmart Advwin Patio Cam", "Detection": "Feral Cat (Acoustic Rustle Match)", "Confidence": "88%"},
    {"Time": "11:42 PM", "Device": "Temu Boundary Laser Beam", "Detection": "Solid Object Beam Interruption (Acreage Clear Line)", "Confidence": "100%"},
    {"Time": "09:15 PM", "Device": "Temu Driveway PIR", "Detection": "Vehicle (Incoming from House A)", "Confidence": "97%"}
]

st.table(wildlife_logs)
st.caption("AI Note: System filters out blowing debris and wind variables to prevent false triggers.")
