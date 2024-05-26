import random
import matplotlib.pyplot as plt
import streamlit as st


# Define the Agent class
class Agent:
    def __init__(self, id, income, employment, family_status, relatives_abroad, children, education):
        self.id = id
        self.income = income
        self.employment = employment
        self.family_status = family_status
        self.relatives_abroad = relatives_abroad
        self.children = children
        self.education = education
        self.accommodation = None

    def choose_accommodation(self):
        if self.income > 500 and self.education in ['Undergraduate', 'Postgraduate']:
            self.accommodation = 'Luxury Apartment'
        elif 200 <= self.income <= 500:
            self.accommodation = 'Standard Apartment'
        elif self.income < 200 and (self.family_status == 'Single' or self.education in ['Primary', 'Secondary']):
            self.accommodation = 'Shared Housing'
        elif self.family_status == 'Family' and self.income >= 200:
            self.accommodation = 'House'
        elif self.income < 200 and (self.family_status == 'Family' or self.education in ['No Education', 'Primary']):
            self.accommodation = 'Public Housing'
        else:
            self.accommodation = 'Undefined'


# Function to create agents and plot results
def create_agents_and_plot(num_agents, high_income_prob, employed_prob, single_prob, relatives_abroad_prob,
                           children_prob, education_levels):
    agents = []
    for i in range(num_agents):
        income = random.choices([100, 350, 1000], [1 - high_income_prob, 0.4, high_income_prob])[0]
        employment = random.choices(['Employed', 'Unemployed'], [employed_prob, 1 - employed_prob])[0]
        family_status = random.choices(['Single', 'Family'], [single_prob, 1 - single_prob])[0]
        relatives_abroad = random.choices(['Yes', 'No'], [relatives_abroad_prob, 1 - relatives_abroad_prob])[0]
        children = random.choices(['Yes', 'No'], [children_prob, 1 - children_prob])[0]
        education = random.choices(
            ['No Education', 'Primary', 'Secondary', 'Technical', 'Undergraduate', 'Postgraduate'],
            education_levels
        )[0]
        agent = Agent(i, income, employment, family_status, relatives_abroad, children, education)
        agent.choose_accommodation()
        agents.append(agent)

    accommodation_counts = {
        'Luxury Apartment': 0,
        'Standard Apartment': 0,
        'Shared Housing': 0,
        'House': 0,
        'Public Housing': 0,
        'Undefined': 0
    }

    for agent in agents:
        accommodation_counts[agent.accommodation] += 1

    labels = list(accommodation_counts.keys())
    counts = list(accommodation_counts.values())

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(labels, counts, color=['blue', 'green', 'red', 'purple', 'orange', 'gray'])
    ax.set_xlabel('Accommodation Type')
    ax.set_ylabel('Number of People')
    ax.set_title(f'Accommodation Choices of {num_agents} Agents')
    st.pyplot(fig)


# Streamlit UI
st.title('Agent-Based Model: Accommodation Choices')

num_agents = st.slider('Number of Agents', min_value=1000, max_value=20000, step=1000, value=10000)
high_income_prob = st.slider('High Income Probability', min_value=0.0, max_value=1.0, step=0.05, value=0.1)
employed_prob = st.slider('Employed Probability', min_value=0.0, max_value=1.0, step=0.05, value=0.83)
single_prob = st.slider('Single Probability', min_value=0.0, max_value=1.0, step=0.05, value=0.51)
relatives_abroad_prob = st.slider('Relatives Abroad Probability', min_value=0.0, max_value=1.0, step=0.05, value=0.18)
children_prob = st.slider('Children Probability', min_value=0.0, max_value=1.0, step=0.05, value=0.667)

education_levels = [
    st.slider('No Education Probability', min_value=0.0, max_value=1.0, step=0.01, value=0.02),
    st.slider('Primary Education Probability', min_value=0.0, max_value=1.0, step=0.01, value=0.115),
    st.slider('Secondary Education Probability', min_value=0.0, max_value=1.0, step=0.01, value=0.515),
    st.slider('Technical Education Probability', min_value=0.0, max_value=1.0, step=0.01, value=0.13),
    st.slider('Undergraduate Education Probability', min_value=0.0, max_value=1.0, step=0.01, value=0.25),
    st.slider('Postgraduate Education Probability', min_value=0.0, max_value=1.0, step=0.01, value=0.03)
]

if st.button('Run Model'):
    create_agents_and_plot(num_agents, high_income_prob, employed_prob, single_prob, relatives_abroad_prob,
                           children_prob, education_levels)

 