
import streamlit as st
import random
from datetime import datetime, timedelta

def generate_company():
    # Company name generation components
    adjectives = ['Global', 'Advanced', 'Innovative', 'Strategic', 'Dynamic', 'Premier', 'Elite', 'Next-Gen']
    nouns = ['Solutions', 'Technologies', 'Systems', 'Dynamics', 'Enterprises', 'Industries', 'Analytics', 'Ventures']
    suffixes = ['Inc.', 'Corp.', 'LLC', 'Group', 'International']
    
    company_name = f"{random.choice(adjectives)} {random.choice(nouns)} {random.choice(suffixes)}"
    
    # Generate random founding date between 1980 and 2020
    start_date = datetime(1980, 1, 1)
    end_date = datetime(2020, 12, 31)
    days_between = (end_date - start_date).days
    founding_date = start_date + timedelta(days=random.randint(0, days_between))
    
    # Generate random company details
    industries = ['Technology', 'Healthcare', 'Finance', 'Manufacturing', 'Energy', 'Consulting']
    employees = random.randint(50, 10000)
    revenue = random.randint(1, 500)
    
    return {
        'name': company_name,
        'founded': founding_date.strftime('%B %d, %Y'),
        'industry': random.choice(industries),
        'employees': employees,
        'revenue': revenue
    }

st.title('🏢 Fake Company Generator')

if st.button('Generate New Company'):
    company = generate_company()
    
    st.header(company['name'])
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Founded", company['founded'])
        st.metric("Industry", company['industry'])
    
    with col2:
        st.metric("Employees", f"{company['employees']:,}")
        st.metric("Annual Revenue", f"${company['revenue']}M")
    
    st.markdown("---")
    
    # Generate a fake company description
    st.subheader("About Us")
    description = f"""
    {company['name']} is a leading provider of innovative solutions in the {company['industry'].lower()} sector. 
    Since our founding in {company['founded']}, we have grown to employ over {company['employees']:,} professionals worldwide. 
    With annual revenue of ${company['revenue']}M, we continue to drive innovation and create value for our stakeholders.
    """
    st.write(description)

    # Generate mission statement
    mission_statements = [
        "Our mission is to revolutionize the {industry} landscape through cutting-edge innovation and sustainable practices.",
        "We strive to deliver exceptional value to our customers while maintaining the highest standards of excellence in {industry}.",
        "At {company}, we're committed to transforming {industry} through innovative solutions and customer-centric approaches.",
        "Our goal is to be the global leader in {industry}, driving positive change through technology and expertise."
    ]
    
    st.subheader("Mission Statement")
    st.write(random.choice(mission_statements).format(
        industry=company['industry'].lower(),
        company=company['name']
    ))
    
    # Generate key statistics
    st.subheader("Key Statistics")
    
    # Create metrics in 3 columns
    stat_col1, stat_col2, stat_col3 = st.columns(3)
    
    with stat_col1:
        st.metric("Global Offices", random.randint(3, 20))
        st.metric("Patents Filed", random.randint(10, 200))
    
    with stat_col2:
        st.metric("Client Satisfaction", f"{random.randint(90, 99)}%")
        st.metric("Market Share", f"{random.randint(5, 30)}%")
    
    with stat_col3:
        st.metric("R&D Investment", f"${random.randint(5, 50)}M")
        st.metric("Growth Rate", f"{random.randint(5, 25)}%")
    
    # Generate leadership team
    st.subheader("Leadership Team")
    
    # Fake executive titles and names
    titles = [
        "Chief Executive Officer",
        "Chief Financial Officer",
        "Chief Technology Officer",
        "Chief Operating Officer",
        "Chief Marketing Officer"
    ]
    
    first_names = ["John", "Sarah", "Michael", "Emma", "David", "Lisa", "Robert", "Jennifer"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
    
    # Display leadership in an expander
    with st.expander("View Leadership Team"):
        for title in titles:
            exec_name = f"{random.choice(first_names)} {random.choice(last_names)}"
            st.write(f"**{title}:** {exec_name}")
    
    # Generate company values
    st.subheader("Our Core Values")
    
    values = [
        "Innovation", "Integrity", "Excellence", "Collaboration", 
        "Sustainability", "Customer Focus", "Diversity"
    ]
    
    selected_values = random.sample(values, 4)
    values_cols = st.columns(4)
    
    for i, value in enumerate(selected_values):
        with values_cols[i]:
            st.markdown(f"### {value}")
            st.write(f"We believe in {value.lower()} as a fundamental principle of our success.")
    
    # Add social media presence
    st.subheader("Connect With Us")
    social_col1, social_col2, social_col3, social_col4 = st.columns(4)
    
    with social_col1:
        st.write("🔵 LinkedIn")
        st.write(f"{company['name']}")
    
    with social_col2:
        st.write("🐦 Twitter")
        st.write(f"@{company['name'].replace(' ', '')}")
    
    with social_col3:
        st.write("📘 Facebook")
        st.write(f"{company['name']}")
    
    with social_col4:
        st.write("📸 Instagram")
        st.write(f"@{company['name'].lower().replace(' ', '_')}")


        # Add a fun balloon animation effect
        st.balloons()
    
