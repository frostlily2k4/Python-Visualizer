from visualizer.executor import run_python_code
import streamlit as st
import base64

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(
    page_title="Python Visualizer",
    page_icon="🐍",
    layout="wide"
)

# ----------------------------------------------------
# LOAD BACKGROUND IMAGE
# ----------------------------------------------------
def get_base64(file_path):
    with open(file_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img = get_base64("assets/cat_bg.jpg")

# ----------------------------------------------------
# CUSTOM CSS
# ----------------------------------------------------
st.markdown(f"""
<style>

/* Background */
.stApp {{
    background-image: url("data:image/jpeg;base64,{img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

/* Hide Streamlit header */
header {{
    visibility: hidden;
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
    background: rgba(0,0,0,0);
}}

/* Title */
.main-title {{
    font-size:48px;
    font-weight:bold;
    color:white;
    text-align:center;
    margin-bottom:0;
    text-shadow:2px 2px 8px black;
}}

.subtitle {{
    text-align:center;
    color:#F8F8F8;
    font-size:20px;
    margin-bottom:30px;
}}

/* Glass Cards */
.glass {{
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(12px);
    border-radius:20px;
    padding:20px;
    border:1px solid rgba(255,255,255,0.2);
    box-shadow:0px 8px 20px rgba(0,0,0,0.3);
}}

/* Buttons */
.stButton > button {{
    width:100%;
    background:#D86A63;
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-size:16px;
    font-weight:bold;
}}

.stButton > button:hover {{
    background:#C9544F;
}}

textarea {{
    border-radius:15px !important;
}}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# HEADER
# ----------------------------------------------------
st.markdown("""
<div class='main-title'>
🐍 Python Visualizer
</div>

<div class='subtitle'>
Learn Python Visually • Step by Step
</div>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# CODE EDITOR
# ----------------------------------------------------
code = st.text_area(
    "Python Code",
    value="""x = 5
y = x + 2
name = "Lily"

print(y)
""",
    height=320,
    label_visibility="collapsed"
)

# ----------------------------------------------------
# BUTTONS
# ----------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    run = st.button("▶ Run Code")

with col2:
    st.button("⏮ Previous", disabled=True)

with col3:
    st.button("⏭ Next", disabled=True)

# ----------------------------------------------------
# EXECUTE CODE
# ----------------------------------------------------
success = False
result = ""
variables = {}

if run:
    success, result, variables = run_python_code(code)

# ----------------------------------------------------
# MAIN LAYOUT
# ----------------------------------------------------
left, right = st.columns([2, 1])

# ---------------- LEFT : OUTPUT ----------------
with left:

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    st.subheader("📤 Output Console")

    if run:

        if success:

            if result.strip():
                st.code(result, language="text")
            else:
                st.success("Program executed successfully.")

        else:
            st.error(result)

    else:
        st.code("Click ▶ Run Code to execute your program.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- RIGHT : MEMORY ----------------
with right:

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    st.subheader("🧠 Memory")

    if run:

        if success:

            if variables:

                for key, value in variables.items():
                    st.success(f"{key} → {value}")

            else:
                st.info("No variables created.")

        else:
            st.warning("Execution failed.")

    else:

        st.info("Variables will appear here after execution.")

    st.markdown("</div>", unsafe_allow_html=True)