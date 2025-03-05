import pandas as pd
import random

num_responses = 70
# Adjusting dataset generation to better align with Champaign-Urbana's demographics and economic landscape

# Setting probabilities based on known city characteristics:
# - Higher student population and young professionals
# - Significant percentage of households earning below the national average
# - Healthcare and education are major employment sectors
# - High demand for childcare services with limited evening care availability

# Define weighted choices
parent_guardian_weights = [0.85, 0.1, 0.05]  # More likely to be parents
household_structure_weights = [0.3, 0.4, 0.2, 0.05, 0.05]  # Majority are single or married
income_level_weights = [0.3, 0.25, 0.2, 0.15, 0.1]  # Significant lower-middle income population
occupation_weights = [0.3, 0.25, 0.15, 0.1, 0.1, 0.1]  # More in healthcare and education
work_hours_weights = [0.5, 0.2, 0.2, 0.1]  # Most people work 9-5, some shift work

# Generate refined dataset
data_refined = {
    "Parent/Guardian": random.choices(["Parent", "Guardian", "Other"], weights=parent_guardian_weights, k=num_responses),
    "Household Structure": random.choices(
        ["Single", "Married", "Two adult household", "Extended family living together", "Prefer not to say"], 
        weights=household_structure_weights, 
        k=num_responses
    ),
    "Number of Children": random.choices(range(1, 5), weights=[0.5, 0.3, 0.15, 0.05], k=num_responses),
    "Income Level": random.choices(
        ["Below $30K", "$30K-$50K", "$50K-$75K", "$75K-$100K", "Above $100K"], 
        weights=income_level_weights, 
        k=num_responses
    ),
    "Occupation": random.choices(
        ["Healthcare", "Education", "Retail", "Manufacturing", "IT/Tech", "Self-Employed"], 
        weights=occupation_weights, 
        k=num_responses
    ),
    "Work Hours": random.choices(
        ["9 AM - 5 PM", "Shift Work (Rotating)", "Evening/Night Shifts", "Flexible/Remote"], 
        weights=work_hours_weights, 
        k=num_responses
    ),
    "Evening Childcare Available": random.choices(["Yes", "No"], weights=[0.3, 0.7], k=num_responses),  # Limited availability
    "Evening Childcare Type": random.choices(
        ["Family/Friend", "Babysitter", "Daycare", "None"], weights=[0.4, 0.2, 0.1, 0.3], k=num_responses
    ),
    "Daycare Closing Time": random.choices(["5 PM", "6 PM", "7 PM", "8 PM"], weights=[0.3, 0.4, 0.2, 0.1], k=num_responses),
    "Emergency Childcare Use": random.choices(["Yes", "No"], weights=[0.4, 0.6], k=num_responses),
    "Emergency Childcare Reason": random.choices(["Unavailable Services", "Last-Minute Emergency"], weights=[0.6, 0.4], k=num_responses),
    "Childcare Needs Beyond Regular Hours": random.choices(
        ["Rarely", "Sometimes", "Often", "Very Often"], 
        weights=[0.4, 0.3, 0.2, 0.1], 
        k=num_responses
    ),
    "Most Important Features in Childcare": [
        random.sample(["Safety", "Qualified Staff", "Education", "Affordability", "Flexibility"], 5) 
        for _ in range(num_responses)
    ],
    "Willingness to Pay Per Hour": random.choices(["$5-$10", "$10-$15", "$15-$20", "Above $20"], weights=[0.4, 0.3, 0.2, 0.1], k=num_responses),
    "Interest in After-Hours Childcare": random.choices(["Yes", "No"], weights=[0.5, 0.5], k=num_responses),
}

# Create refined DataFrame
df_refined = pd.DataFrame(data_refined)

# # Display the updated dataset
# tools.display_dataframe_to_user(name="Refined Childcare Survey Dataset", dataframe=df_refined)


df_refined.to_csv("./data/childcare_survey_dataset.csv", index=False)