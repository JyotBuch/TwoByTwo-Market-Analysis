import pandas as pd
import random

# Define potential responses based on the survey questions and context of Champaign-Urbana
num_responses = 70

# Generate synthetic dataset
data = {
    "Parent/Guardian": random.choices(["Parent", "Guardian", "Other"], k=num_responses),
    "Household Structure": random.choices(
        ["Single", "Married", "Two adult household", "Extended family living together", "Prefer not to say"], 
        k=num_responses
    ),
    "Number of Children": random.choices(range(1, 5), k=num_responses),
    "Income Level": random.choices(
        ["Below $30K", "$30K-$50K", "$50K-$75K", "$75K-$100K", "Above $100K"], 
        k=num_responses
    ),
    "Occupation": random.choices(
        ["Healthcare", "Education", "Retail", "Manufacturing", "IT/Tech", "Self-Employed", "Other"], 
        k=num_responses
    ),
    "Work Hours": random.choices(
        ["9 AM - 5 PM", "Shift Work (Rotating)", "Evening/Night Shifts", "Flexible/Remote"], 
        k=num_responses
    ),
    "Evening Childcare Available": random.choices(["Yes", "No"], k=num_responses),
    "Evening Childcare Type": random.choices(
        ["Family/Friend", "Babysitter", "Daycare", "None"], k=num_responses
    ),
    "Daycare Closing Time": random.choices(["5 PM", "6 PM", "7 PM", "8 PM"], k=num_responses),
    "Emergency Childcare Use": random.choices(["Yes", "No"], k=num_responses),
    "Emergency Childcare Reason": random.choices(["Unavailable Services", "Last-Minute Emergency"], k=num_responses),
    "Childcare Needs Beyond Regular Hours": random.choices(
        ["Rarely", "Sometimes", "Often", "Very Often"], 
        k=num_responses
    ),
    "Most Important Features in Childcare": [
        random.sample(["Safety", "Qualified Staff", "Education", "Affordability", "Flexibility"], 5) 
        for _ in range(num_responses)
    ],
    "Willingness to Pay Per Hour": random.choices(["$5-$10", "$10-$15", "$15-$20", "Above $20"], k=num_responses),
    "Interest in After-Hours Childcare": random.choices(["Yes", "No"], k=num_responses),
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the generated dataset
# import ace_tools as tools
# tools.display_dataframe_to_user(name="Childcare Survey Dataset", dataframe=df)

df.to_csv("./data/childcare_survey_dataset.csv", index=False)