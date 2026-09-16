import streamlit as st
from datetime import datetime

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Namma Kada",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "transactions" not in st.session_state:
    st.session_state.transactions = [
        {
            "customer": "Rifa",
            "amount": 5000.0,
            "type": "Credit",
            "date": datetime.now().strftime("%d %b %Y")
        }
    ]

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Main background */
.stApp {
    background: #f4f6fb;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #111827;
    min-width: 270px;
    max-width: 270px;
}

section[data-testid="stSidebar"] * {
    color: #f9fafb;
}

.sidebar-title {
    font-size: 27px;
    font-weight: 800;
    margin-top: 20px;
}

.sidebar-subtitle {
    color: #9ca3af !important;
    font-size: 14px;
    margin-top: 5px;
    margin-bottom: 35px;
}

.sidebar-item {
    padding: 13px 10px;
    font-size: 16px;
    border-radius: 10px;
    margin: 5px 0;
}

.sidebar-item:hover {
    background: #1f2937;
}

/* Main content */
.main-title {
    font-size: 32px;
    font-weight: 800;
    color: #111827;
    margin-bottom: 4px;
}

.main-subtitle {
    color: #6b7280;
    font-size: 15px;
    margin-bottom: 28px;
}

/* Metric cards */
.metric-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 24px;
    min-height: 145px;
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.05);
}

.metric-icon {
    font-size: 25px;
}

.metric-title {
    color: #6b7280;
    font-size: 15px;
    margin-top: 12px;
}

.metric-value {
    color: #111827;
    font-size: 30px;
    font-weight: 800;
    margin-top: 6px;
}

/* Section cards */
.section-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 25px;
    margin-top: 30px;
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.04);
}

.section-title {
    color: #111827;
    font-size: 22px;
    font-weight: 800;
}

.section-subtitle {
    color: #6b7280;
    font-size: 14px;
    margin-top: 5px;
}

/* Input labels */
label {
    color: #374151 !important;
    font-weight: 600 !important;
}

/* Buttons */
.stButton > button {
    background: #111827 !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 10px 22px !important;
    font-weight: 700 !important;
    min-height: 45px;
}

.stButton > button:hover {
    background: #374151 !important;
}

/* Table */
.customer-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
    background: white;
    border-radius: 12px;
    overflow: hidden;
}

.customer-table th {
    background: #181b24;
    color: #d1d5db;
    padding: 15px;
    text-align: left;
    font-weight: 500;
}

.customer-table td {
    padding: 15px;
    border-bottom: 1px solid #e5e7eb;
    color: #111827;
}

.status {
    color: #dc2626;
    font-weight: 700;
}

.credit {
    color: #dc2626;
    font-weight: 700;
}

.payment {
    color: #16a34a;
    font-weight: 700;
}

/* Voice box */
.voice-box {
    background: linear-gradient(135deg, #111827, #1f2937);
    border-radius: 18px;
    padding: 28px;
    margin-top: 30px;
    color: white;
}

.voice-title {
    font-size: 22px;
    font-weight: 800;
}

.voice-text {
    color: #d1d5db;
    margin-top: 7px;
}

/* Remove excessive top padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown(
        '<div class="sidebar-title">🛍️ Namma Kada</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">Smart Digital Khata</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-item">🏠 Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-item">👥 Customers</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-item">📒 Khata</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-item">🔔 Reminders</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-item">📊 Reports</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        '<div class="sidebar-item">⚙️ Settings</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.caption("Namma Kada v1.0")
    st.caption("Smart Business Assistant")


# --------------------------------------------------
# CALCULATIONS
# --------------------------------------------------

transactions = st.session_state.transactions

customers = {}

for t in transactions:

    name = t["customer"]
    amount = t["amount"]

    if name not in customers:
        customers[name] = 0

    if t["type"] == "Credit":
        customers[name] += amount
    else:
        customers[name] -= amount


outstanding = sum(
    max(balance, 0)
    for balance in customers.values()
)

customer_count = len(customers)
transaction_count = len(transactions)


# --------------------------------------------------
# MAIN HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">Good morning 👋</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'Manage your shop smarter with Namma Kada.'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# METRIC CARDS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-icon">💰</div>
            <div class="metric-title">Total Outstanding</div>
            <div class="metric-value">₹{outstanding:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-icon">👥</div>
            <div class="metric-title">Total Customers</div>
            <div class="metric-value">{customer_count}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-icon">🧾</div>
            <div class="metric-title">Transactions</div>
            <div class="metric-value">{transaction_count}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# ADD TRANSACTION
# --------------------------------------------------

st.markdown(
    """
    <div class="section-card">
        <div class="section-title">➕ Add New Transaction</div>
        <div class="section-subtitle">
            Record a customer credit or payment
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns([2.3, 1.1, 1.3, 0.9])

with col1:
    customer_name = st.text_input(
        "Customer",
        placeholder="e.g. Ravi",
        key="customer_input"
    )

with col2:
    amount = st.number_input(
        "Amount",
        min_value=0.0,
        step=100.0,
        key="amount_input"
    )

with col3:
    transaction_type = st.selectbox(
        "Transaction Type",
        ["Credit", "Payment"],
        key="type_input"
    )

with col4:
    st.markdown("<br>", unsafe_allow_html=True)

    add_button = st.button(
        "Add Transaction",
        use_container_width=True
    )


# --------------------------------------------------
# ADD BUTTON LOGIC
# --------------------------------------------------

if add_button:

    if customer_name.strip() == "":
        st.error("Please enter customer name.")

    elif amount <= 0:
        st.error("Please enter a valid amount.")

    else:

        st.session_state.transactions.append(
            {
                "customer": customer_name.strip().title(),
                "amount": amount,
                "type": transaction_type,
                "date": datetime.now().strftime("%d %b %Y")
            }
        )

        st.success(
            f"₹{amount:,.0f} {transaction_type.lower()} added for {customer_name.title()}."
        )

        st.rerun()


# --------------------------------------------------
# CUSTOMER BALANCES
# --------------------------------------------------

st.markdown(
    """
    <div class="section-card">
        <div class="section-title">👥 Customer Balances</div>
        <div class="section-subtitle">
            Track who owes you money
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


if customers:

    table_html = """
    <table class="customer-table">
        <tr>
            <th>Customer</th>
            <th>Balance</th>
            <th>Status</th>
        </tr>
    """

    for name, balance in customers.items():

        if balance > 0:

            table_html += f"""
            <tr>
                <td>{name}</td>
                <td class="credit">₹{balance:,.0f}</td>
                <td class="status">Outstanding</td>
            </tr>
            """

        elif balance < 0:

            table_html += f"""
            <tr>
                <td>{name}</td>
                <td class="payment">₹{abs(balance):,.0f}</td>
                <td class="payment">Advance</td>
            </tr>
            """

        else:

            table_html += f"""
            <tr>
                <td>{name}</td>
                <td>₹0</td>
                <td class="payment">Settled</td>
            </tr>
            """

    table_html += "</table>"

    st.markdown(table_html, unsafe_allow_html=True)

else:

    st.info("No customers yet. Add your first transaction.")


# --------------------------------------------------
# VOICE ENTRY
# --------------------------------------------------

st.markdown(
    """
    <div class="voice-box">
        <div class="voice-title">🎤 Smart Voice Entry</div>
        <div class="voice-text">
            Add transactions using your voice.
            Tamil and English voice support coming next.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)