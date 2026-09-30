# %% [markdown]
# # Module_1: Team ELMQVIST 7
# 
# ## Team Members:
# Jane Wyatt
# Risad Ilham
# 
# ## Project Title:
# ### Evaluating Years Spent in Education as Mediator for Symptom Onset-age
# 
# 

# %% [markdown]
# ## Project Goal:
# 

# %% [markdown]
# Neuroscientists have found that learning can physically alter the brain. A study by Asano, Taki, Hashizume et al. (2014) conducted a longitudinal study of 229 healthy children in Japan between the ages of 5 and 18. They aimed to see whether the amount of time children studied at home was related to the amount of white and gray matter. They did an MRI scan of every participant at the beginning of the study and one at the end, 3 years later. They found a positive correlation between studying 1+ hour a night and increased white matter in the right precuneus and right superior temporal gyrus. Furthermore, they found a positive correlation with change in gray matter in the right precuneus and the right inferior parietal lobe (Asano, Taki, Hashizume et al. 2014). Other neuroscientists have found that the right superior frontal gyrus is known to play an important role in memory. Furthermore, increased white and gray matter is known to be a sign of an increased number of axons. Therefore, we hypothesize that if learning increases the number of axons in the areas of the brain that are important for memory, the memory loss symptom of Alzieherms (dementia) will be delayed, and the age at onset will be larger.
# This article inspired us to investigate whether the number of years of education a patient had impacted the age at which their Alzheimer's symptoms started. This can be determined by comparing the years spent in education and age of onset for each patient. We are also curious if this relationship would change depending on the patient’s genetic predisposition. We can investigate this by creating subgroups filtered by the patient’s version of the apolipoprotein E (APOE) gene. The 3 variants of APOE are Ɛ2, Ɛ3, and Ɛ4. Every human has two of these variants, making 6 possible combinations: 2/2, 2/3, 2/4, 3/3, 3/4, and 4/4. Individuals with an Ɛ4 allele have a higher risk of getting AD, and patients with two Ɛ4 alleles (4/4) are at the highest risk.
# 
# 

# %% [markdown]
# ### Research questions: 
# #### 1) Does the length of time (years) an individual spends being educated impact the age at which their Alzheimer’s symptoms begin? 
# 
# #### 2) Does the length of time (years) an individual spends being educated play a different role in onset symptoms depending on the individual's genetic predisposition? 
# 

# %% [markdown]
# ## Disease Background: 
# 
# 

# %% [markdown]
# ### Prevalence and Incidence — United States
# 

# %% [markdown]
# 
# **Prevalence** is the number of people living with a disease at a given time.  
# **Incidence** is the number of new cases that occur over a specific period.
# 
# #### Prevalence
# - **About 7.4 million** Americans age 65 and older are living with Alzheimer’s disease (AD), according to the estimate in our notes.
# - The number of Americans living with AD is projected to reach **13.8 million by 2060**.
# 
# #### Incidence
# - Our notes report approximately **900,000 adults diagnosed with Alzheimer’s annually**. Confirm the source, year, and population covered; incidence is best described as *new cases per year*, rather than an incidence rate unless a population denominator is provided.
# 
# #### Related mortality statistic
# - Our notes report a **142% increase in deaths among people with AD** while deaths from other diseases declined. Add the comparison years and verify the statistic before including it as a finding.
# 
# **Sources:** [Alzheimer’s Association — Facts and Figures](https://www.alz.org/alzheimers-dementia/facts-figures); [PubMed Central article](https://pmc.ncbi.nlm.nih.gov/articles/PMC13098189/)
# 
# **AI use:** Gemini & Google AI helped find credible sources and polish this section. The VS Code agent helped format it.
# 
#  

# %% [markdown]
# ### Economic Burden
# 

# %% [markdown]
# Alzheimer’s disease (AD) creates costs for families, caregivers, and the health care system.
# 
# - In **2025**, about **12 million** caregivers provided **19.2 billion hours** of unpaid care to people with dementia.
# - Unpaid care for people with AD was valued at **$413.5 billion in 2024**.
# - Health care, long-term care, and hospice services for people with dementia cost an estimated **$384 billion in 2025**.
# - Caregiving can also affect caregivers’ physical and mental health.
# 
# **Source:** [Alzheimer’s Association — Facts and Figures](https://www.alz.org/alzheimers-dementia/facts-figures)
# 
# **AI use:** Gemini & Google AI helped find credible sources and polish this section. The VS Code agent helped format it.

# %% [markdown]
# ### Risk factors (genetic, lifestyle)
# 

# %% [markdown]
# Factors associated with a higher risk of Alzheimer’s disease include:
# 
# - **Physical health:** Physical inactivity, obesity, high blood pressure, and diabetes.
# - **Lifestyle:** Smoking and excessive alcohol use.
# - **Mental and sensory health:** Depression and hearing loss.
# - **Genetics and demographics:** Family history and sex; women have higher rates of Alzheimer’s.
# 
# These factors may increase risk, but they do not mean someone will develop Alzheimer’s disease.
# 
# **Source:** [Alzheimer’s Association — Causes and Risk Factors](https://www.alz.org/alzheimers-dementia/what-is-alzheimers/causes-and-risk-factors)
# 
# **AI use:** Gemini & Google AI helped find credible sources and polish this section. The VS Code agent helped format it.

# %% [markdown]
# ### Societal determinants
# 

# %% [markdown]
# Social and environmental conditions can affect brain health and access to dementia care. These include:
# 
# - **Socioeconomic factors:** Education, income, and access to health care.
# - **Neighborhood factors:** Air pollution and access to healthy food.
# - **Social factors:** Discrimination and other barriers to care.
# 
# **Sources:** [CDC](https://www.cdc.gov/alzheimers-dementia/php/sdoh/index.html) · [DC Brain Health](https://brainhealth.dc.gov/page/social-determinants-health-and-dementia) · [Research article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12301702/)
# 
# **AI use:** Gemini & Google AI helped find credible sources and polish this section. The VS Code agent helped format it.
# 

# %% [markdown]
# ### Symptoms
# 

# %% [markdown]
# Common symptoms of Alzheimer’s disease include:
# 
# - **Memory loss** that disrupts daily life.
# - **Difficulty planning or solving problems**, such as following familiar tasks or working with numbers.
# - **Visual and spatial difficulties**, including trouble judging distance or knowing where you are.
# 
# **Source:** [CDC — Signs and Symptoms of Alzheimer’s Disease](https://www.cdc.gov/alzheimers-dementia/signs-symptoms/alzheimers.html)
# 
# **AI use:** Gemini & Google AI helped find credible sources and polish this section. The VS Code agent helped format it.

# %% [markdown]
# ### Diagnosis
# 

# %% [markdown]
# Alzheimer’s disease is diagnosed through a medical evaluation. This may include:
# 
# - **Medical history and cognitive tests** to assess memory and thinking.
# - **Physical and neurological exams** to check for other possible causes of symptoms.
# - **Lab tests and brain scans**, such as MRI, CT, or PET scans.
# - **Biomarker tests**, including tests of cerebrospinal fluid, when appropriate.
# 
# **Source:** [National Institute on Aging — How Is Alzheimer’s Disease Diagnosed?](https://www.nia.nih.gov/health/alzheimers-symptoms-and-diagnosis/how-alzheimers-disease-diagnosed)
# 
# **AI use:** Gemini & Google AI helped find credible sources and polish this section. The VS Code agent helped format it.

# %% [markdown]
# ### Standard Treatments and Coverage
# 

# %% [markdown]
# 
# Treatment depends on the stage of Alzheimer’s disease. Medicines may help manage symptoms or slow decline; they do not cure the disease.
# 
# | Treatment | Use | Common risks or side effects |
# |---|---|---|
# | **Donepezil, galantamine, rivastigmine** | Help manage symptoms; galantamine and rivastigmine are generally used for mild to moderate disease. Donepezil may be used at different stages. | Nausea, diarrhea, or loss of appetite |
# | **Memantine** | Helps manage symptoms in moderate to severe disease. | Dizziness, headache, or constipation |
# | **Lecanemab and donanemab** | For some people with early Alzheimer’s disease; may slow cognitive decline. | Brain swelling or bleeding (ARIA); MRI monitoring is needed |
# | **Brexpiprazole** | May treat agitation associated with Alzheimer’s disease. | Drowsiness, dizziness, or restlessness |
# 
# **Coverage:** Insurance coverage and out-of-pocket costs vary by medication and plan. Check with the insurer and health care provider about eligibility and costs.
# 
# **Sources:** [National Institute on Aging — Alzheimer’s Disease Treatment](https://www.nia.nih.gov/health/alzheimers-treatment/how-alzheimers-disease-treated) · [CMS — Medicare Coverage of Alzheimer’s Drugs](https://www.cms.gov/medicare/coverage/evidence/alzheimers-disease)
# 
# **AI use:** Gemini & Google AI helped find credible sources and polish this section. The VS Code agent helped format it.
# 

# %% [markdown]
# ### Disease progression & prognosis

# %% [markdown]
# 
# Alzheimer’s disease progresses differently for each person. On average, people live about **8 years after symptoms begin**, though some live for **20 years or longer**. Early-onset Alzheimer’s is rare and can begin as early as a person’s 30s or 40s.
# 
# The stages of progression include:
# 
# 1. **Preclinical stage:** Brain changes begin before noticeable symptoms appear.
# 2. **Early stage:** Mild memory and thinking problems may affect daily activities.
# 3. **Middle stage:** Symptoms worsen, and the person may need more help with daily activities.
# 4. **Late stage:** Severe changes in memory and physical abilities may require full-time care.
# 
# **Source:** [Johns Hopkins Medicine — Stages of Alzheimer’s Disease](https://www.hopkinsmedicine.org/health/conditions-and-diseases/alzheimers-disease/stages-of-alzheimer-disease)
# 
# **AI Use**: Gemini & Google AI helped find credible sources and polish this section. The VS Code agent helped format it.
# 

# %% [markdown]
# ### Continuum of Care Providers
# 

# %% [markdown]
# 
# People with Alzheimer’s may need different types of support as their needs change. Care options can include:
# 
# - **In-home services:** Help with daily activities and personal care while living at home.
# - **Assisted living:** Housing with support for daily activities, meals, and medication routines.
# - **Memory care:** Specialized support in a setting designed for people with memory conditions.
# - **Long-term care:** Ongoing assistance for people who need substantial help. It may be provided at home or in a residential facility.
# 
# Care needs vary, so people may move between services or use more than one type of care.
# 
# **Sources:** [Understanding the Continuum of Care](https://www.edenseniorhc.com/from-independent-living-to-memory-care-understanding-the-continuum-of-care/) · [LCCA — Continuum of Care](https://lcca.com/blog/Continuum-of-Care)
# 
# 
# **AI Use**: Gemini & Google AI helped find credible sources and polish this section. The VS Code agent helped format it.
# 

# %% [markdown]
# ### Biological mechanisms (anatomy, organ physiology, cell & molecular physiology)
# 

# %% [markdown]
# 
# Alzheimer’s disease causes changes in the brain that damage neurons and disrupt their connections. Two key changes are:
# 
# - **Amyloid plaques:** Amyloid-beta proteins build up between neurons.
# - **Tau tangles:** Tau proteins accumulate inside neurons, disrupting their function.
# 
# As the damage spreads, neurons lose connections and die. This can lead to shrinkage in affected brain areas and problems with memory, thinking, and other abilities. The exact sequence of changes is still being studied.
# 
# **Sources:** [National Institute on Aging — What Happens to the Brain in Alzheimer’s Disease?](https://www.nia.nih.gov/health/alzheimers-causes-and-risk-factors/what-happens-brain-alzheimers-disease) · [YouTube video](https://www.youtube.com/watch?v=YxjFyDUYT5k&t=32s)
# 
# **AI Use**: Gemini & Google AI helped find credible sources and polish this section. The VS Code agent helped format it.
# 

# %% [markdown]
# ### Clinical Trials/next-gen therapies
# 

# %% [markdown]
# 
# Clinical trials evaluate potential Alzheimer’s treatments for safety and effectiveness. Newer therapies aim to do more than ease symptoms; some target processes involved in disease progression. Researchers continue to study who may benefit, how well treatments work, and what risks they carry. A treatment discussed in an article is not necessarily approved or proven effective—check its current trial status and consult reliable medical sources.
# 
# **Sources:** [Scientific American — A New Generation of Alzheimer’s Treatments, Explained in Graphics](https://www.scientificamerican.com/article/a-new-generation-of-alzheimers-treatments-explained-in-graphics/) · [Cromos Pharma — Is Clinical Research Ready for the Next Era of Alzheimer’s Trials?](https://cromospharma.com/world-alzheimer-s-day-2026-is-clinical-research-ready-for-the-next-era-of-alzheimer-s-trials/)
# 
# **AI Use**: Gemini & Google AI helped find credible sources and polish this section. The VS Code agent helped format it.

# %% [markdown]
# ## Data-Set: 
# *(Describe the data set(s) you will analyze. Cite the source(s) of the data. Describe how the data was collected -- What techniques were used? What units are the data measured in? Etc.)*
# 
# The data set we were provided in class combine 2 data sets created by Seatle alzherimer diseass brain cell atlas (SEA-AD)

# %% [markdown]
# ## Data Analysis: 
# 

# %% [markdown]
# ### 1. Import models to caculate statistical test and generate graphs 

# %%
#importing the constructors and class made in Mod1_patient
from Mod1_patient import Patient

#import the proper packages for creating the plots and standard deviation 
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics
import pandas as pd
from sklearn.linear_model import LinearRegression

# %% [markdown]
# ### 2. Create list that will hold the values needed to compare the age of onset syptoms to years of education for each specific gene version 

# %%
#These list will be used to create the scatter plots and bar graph 
age_of_onset_4_4 = []
age_of_onset_3_4 = []
age_of_onset_2_4 = []
age_of_onset_3_3 = []
age_of_onset_3_2 = []
years_of_education_4_4 = []
years_of_education_3_4 = []
years_of_education_2_4 = []
years_of_education_3_3 = []
years_of_education_3_2 = []

# %% [markdown]
# ### 3. Call method from Mod1_patient.py that will read through the imported CSV file and creates objects according to the constructor in class Patient 

# %%
#this calls the method created in the patient.py file that opens the CSV file and goes through the data according to the following methods 
filename = "/Users/janewyatt/Desktop/BME 2315 /Module 1/BME2315_Module1_Project/Metadata and Protein Data for Module 1.csv"
Patient.instantiate_from_csv(filename)

#display a sample of the data file with rows and columns 
df = pd.read_csv(
    "/Users/janewyatt/Desktop/BME 2315 /Module 1/BME2315_Module1_Project/Metadata and Protein Data for Module 1.csv"
)
df.head()

# %% [markdown]
# ### 4. Call the methods from Mod1_patient.py that sort through the patients in the data file and returns only the ones with the requested gene combination. Adds these patient data points to the previously created list. 

# %%
#Calling the method get_patients_with_4_4_gene to sort the patients in the CSV file into only patients with 4_4 gene 
print("\nList of All Patients with 4_4 Gene sorted by age of onset:\n")
for patient in Patient.get_patients_with_4_4_gene("4_4"):
    if patient.age_of_onset is not None and patient.years_of_education is not None:
        #this condition checks to make sure the patient has both age of onset and years of education data 
        age_of_onset_4_4.append(patient.age_of_onset)
        years_of_education_4_4.append(patient.years_of_education)
        #these append functions add the values that meet the condition into the proper list
    print(patient)
    #Printing the patients with 4_4 gene to keep the data organize 

#This block of the code does the same thing as the one from lines 30-39 but for the 3_4 gene 
print ("\nList of All Patients with 3_4 Gene sorted by age of onset:\n")
for patient in Patient.get_patients_with_3_4_gene("3_4"):
    if patient.age_of_onset is not None and patient.years_of_education is not None:
        age_of_onset_3_4.append(patient.age_of_onset)
        years_of_education_3_4.append(patient.years_of_education)
    print(patient)

#This block of the code does the same thing as the one from lines 30-39 but for the 2_4 gene 
print ("\nList of All Patients with 2_4 Gene sorted by age of onset:\n")
for patient in Patient.get_patients_with_2_4_gene("2_4"):
    if patient.age_of_onset is not None and patient.years_of_education is not None:
        age_of_onset_2_4.append(patient.age_of_onset)
        years_of_education_2_4.append(patient.years_of_education)
    print(patient)

#This block of the code does the same thing as the one from lines 30-39 but for the 3_3 gene 
print ("\nList of All Patients with 3_3 Gene sorted by age of onset:\n")
for patient in Patient.get_patients_with_3_3_gene("3_3"):
    if patient.age_of_onset is not None and patient.years_of_education is not None:
        age_of_onset_3_3.append(patient.age_of_onset)
        years_of_education_3_3.append(patient.years_of_education)
    print(patient)

#This block of the code does the same thing as the one from lines 30-39 but for the 3_2 gene 
print ("\nList of All Patients with 3_2 Gene sorted by age of onset:\n")
for patient in Patient.get_patients_with_3_2_gene("3_2"):
    if patient.age_of_onset is not None and patient.years_of_education is not None:
        age_of_onset_3_2.append(patient.age_of_onset)
        years_of_education_3_2.append(patient.years_of_education)
    print(patient)

if len(years_of_education_3_2) < 2:
    print("Unfortunately there is not enough data for a 3_2 regression.")
    #While writing the code we realized that there aren't any patients in the data set with a 3_2 gene and a recorded length of years spent in school or onset age 


# %% [markdown]
# ### 5. Create the scatter plots using the previously created list and converting them into arrays. Apply a linear regression analysis using the imported model.  

# %%
#------------------------------------------------------------------------------------
#Creating the scatter plots using the the list in lines 15-24

#This is the scatter plot of 4_4 gene 
#At AI's reccommendation we converted the data list into numpy arrays because the array assist in reformating the data to make it easier to plot with the scikit-learn (the model that is performing the linear regression)
X = np.array(years_of_education_4_4).reshape(-1, 1)
y = np.array(age_of_onset_4_4)

#this tells python wich data sets to use for the x and y values for the line in the graph 
model = LinearRegression()
model.fit(X, y)

#these statistics model caculate the slope, intercept, and R-squared value
slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X, y)

equation = f"y = {slope:.2f}x + {intercept:.2f}\nR² = {r2:.2f}"

#the following block of code displays the graph and the regression equation
plt.scatter(X[:, 0], y, color="blue")
plt.plot(X[:, 0], model.predict(X), color="red")
plt.text(
    #this formatting was generated by AI to keep the equation from being cut off when the graph was generated
    0.05,
    0.95,
    equation,
    transform=plt.gca().transAxes,
    color="red",
    verticalalignment="top",
    bbox={"facecolor": "white", "alpha": 0.8, "edgecolor": "none"},
)
plt.xlabel("Years of Education")
plt.ylabel("Age of Onset")
plt.title("4_4: Years of Education vs Age of Onset")
plt.show()

#-------------------
# Scatter plot for data points with gene 3_4 
#the following code is the same as for lines 80-112 but for the 3_4 gene

X = np.array(years_of_education_3_4).reshape(-1, 1)
y = np.array(age_of_onset_3_4)

model = LinearRegression()
model.fit(X, y)

slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X, y)

equation = f"y = {slope:.2f}x + {intercept:.2f}\nR² = {r2:.2f}"

plt.scatter(X[:, 0], y, color="blue")
plt.plot(X[:, 0], model.predict(X), color="red")
plt.text(
    0.05,
    0.95,
    equation,
    transform=plt.gca().transAxes,
    color="red",
    verticalalignment="top",
    bbox={"facecolor": "white", "alpha": 0.8, "edgecolor": "none"},
)
plt.xlabel("Years of Education")
plt.ylabel("Age of Onset")
plt.title("3_4: Years of Education vs Age of Onset")
plt.show()
#-------------------
# Scatter plot for data points with gene 2_4 
#the following code is the same as for lines 80-112 but for the 2_4 gene

X = np.array(years_of_education_2_4).reshape(-1, 1)
y = np.array(age_of_onset_2_4)

model = LinearRegression()
model.fit(X, y)

slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X, y)

equation = f"y = {slope:.2f}x + {intercept:.2f}\nR² = {r2:.2f}"

plt.scatter(X[:, 0], y, color="blue")
plt.plot(X[:, 0], model.predict(X), color="red")
plt.text(
    0.05,
    0.95,
    equation,
    transform=plt.gca().transAxes,
    color="red",
    verticalalignment="top",
    bbox={"facecolor": "white", "alpha": 0.8, "edgecolor": "none"},
)
plt.xlabel("Years of Education")
plt.ylabel("Age of Onset")
plt.title("2_4: Years of Education vs Age of Onset")
plt.show()
#-------------------
# Scatter plot for data points with gene 3_3 
#the following code is the same as for lines 80-112 but for the 3_3 gene

X = np.array(years_of_education_3_3).reshape(-1, 1)
y = np.array(age_of_onset_3_3)

model = LinearRegression()
model.fit(X, y)

slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X, y)

equation = f"y = {slope:.2f}x + {intercept:.2f}\nR² = {r2:.2f}"

plt.scatter(X[:, 0], y, color="blue")
plt.plot(X[:, 0], model.predict(X), color="red")
plt.text(
    0.05,
    0.95,
    equation,
    transform=plt.gca().transAxes,
    color="red",
    verticalalignment="top",
    bbox={"facecolor": "white", "alpha": 0.8, "edgecolor": "none"},
)
plt.xlabel("Years of Education")
plt.ylabel("Age of Onset")
plt.title("3_3: Years of Education vs Age of Onset")
plt.show()
#-------------------
# Scatter plot for data points with gene 3_2
# the following code is the same as for lines 80-112 but for the 3_2 gene

X = np.array(years_of_education_3_2).reshape(-1, 1)
y = np.array(age_of_onset_3_2)

if len(X) >= 2: #this conditional checks if there are at least 2 data points in the group because if its not 2 points or more the linear regression method will not work 
    model = LinearRegression()
    model.fit(X, y)

    slope = model.coef_[0]
    intercept = model.intercept_
    r2 = model.score(X, y)

    equation = f"y = {slope:.2f}x + {intercept:.2f}\nR² = {r2:.2f}"

    plt.scatter(X[:, 0], y, color="blue")
    plt.plot(X[:, 0], model.predict(X), color="red")
    plt.text(
        0.05,
        0.95,
        equation,
        transform=plt.gca().transAxes,
        color="red",
        verticalalignment="top",
        bbox={"facecolor": "white", "alpha": 0.8, "edgecolor": "none"},
    )
    plt.xlabel("Years of Education")
    plt.ylabel("Age of Onset")
    plt.title("3_2: Years of Education vs Age of Onset")
    plt.show()


# %% [markdown]
# ### 6. Create the empty list to store the data points of patients that have been educated within the required range of years 

# %%
#-------------------------------------------------------------------

#Code that groups the patients by length of time they were educated 

#First create the empty lists to store the data needed for the bar graph 

patients_0_13_years_educated_age_onset = []
patients_13_16_years_educated_age_onset = []
patients_16_20_years_educated_age_onset = []
patients_20_plus_years_educated_age_onset = []

# %% [markdown]
# ### 7. Call methods created in Mod1_main.py that sort through CSV file and filter the patients with the requested range of years of education. The groups of education are 0-13 years, 13-16 years, 16-20 years, 20+ 

# %%
#call the method made in the patient class that gets the number of patients with 0-13 years of education 
print("\nPatients with 0-13 years of education:\n")
for patient in Patient.get_patients_number_of_years_educated(0, 13):
    if patient.age_of_onset is not None:
        #this condition makes sure that only patients with a recorded age of onset is added to the sub data set for 0-13 years of education 
        patients_0_13_years_educated_age_onset.append(patient.age_of_onset)
    print(patient)

#this block of code is the same as 252-257 but for 13-16 years of education
print("\nPatients with 13-16 years of education:\n")
for patient in Patient.get_patients_number_of_years_educated(13, 16):
    if patient.age_of_onset is not None:
        patients_13_16_years_educated_age_onset.append(patient.age_of_onset)
    print(patient)

#this block of code is the same as 252-257 but for 16-20 years of education
print("\nPatients with 16-20 years of education:\n")
for patient in Patient.get_patients_number_of_years_educated(16, 20):
    if patient.age_of_onset is not None:
        patients_16_20_years_educated_age_onset.append(patient.age_of_onset)
    print(patient)

#this block of code is the same as 252-257 but for 20+ years of education
print("\nPatients with 20+ years of education:\n")
for patient in Patient.get_patients_number_of_years_educated(20, 100):
    if patient.age_of_onset is not None:
        patients_20_plus_years_educated_age_onset.append(patient.age_of_onset)
    print(patient)

# %% [markdown]
# ### 8. Reformat list into arrays to fit the proper format of the statistical models 

# %%

#Following the built in AIs Advice reformatting the list into arrays for the proper format for the statistics models 
x_patients_0_13_years_educated_age_onset = np.array(patients_0_13_years_educated_age_onset)
x_patients_13_16_years_educated_age_onset = np.array(patients_13_16_years_educated_age_onset)
x_patients_16_20_years_educated_age_onset = np.array(patients_16_20_years_educated_age_onset)
x_patients_20_plus_years_educated_age_onset = np.array(patients_20_plus_years_educated_age_onset)


# %% [markdown]
# ### 9. Find the mean age of onset in each group

# %%
#caculating the mean of each group using the np model for mean 
patients_0_13_years_educated_age_onset_mean = np.mean(x_patients_0_13_years_educated_age_onset)
patients_13_16_years_educated_age_onset_mean = np.mean(x_patients_13_16_years_educated_age_onset)
patients_16_20_years_educated_age_onset_mean = np.mean(x_patients_16_20_years_educated_age_onset)
patients_20_plus_years_educated_age_onset_mean = np.mean(x_patients_20_plus_years_educated_age_onset)

# %% [markdown]
# ### 10. Finding the standard deviation of each group 

# %%
#caculating the std of each group using the std model 
patients_0_13_years_educated_age_onset_std = np.std(x_patients_0_13_years_educated_age_onset)
patients_13_16_years_educated_age_onset_std = np.std(x_patients_13_16_years_educated_age_onset)
patients_16_20_years_educated_age_onset_std = np.std(x_patients_16_20_years_educated_age_onset)
patients_20_plus_years_educated_age_onset_std = np.std(x_patients_20_plus_years_educated_age_onset)

# %% [markdown]
# ### 11. Print each group and the mean +/- the standard deviation for that respective group 

# %%

#printing the results of the mean and standard deviation for each data group 
print(f'\nAge of onset for 0-13 years of education: {patients_0_13_years_educated_age_onset_mean} ± {patients_0_13_years_educated_age_onset_std}')
print(f'\nAge of onset for 13-16 years of education: {patients_13_16_years_educated_age_onset_mean} ± {patients_13_16_years_educated_age_onset_std}')
print(f'\nAge of onset for 16-20 years of education: {patients_16_20_years_educated_age_onset_mean} ± {patients_16_20_years_educated_age_onset_std}')
print(f'\nAge of onset for 20+ years of education: {patients_20_plus_years_educated_age_onset_mean} ± {patients_20_plus_years_educated_age_onset_std}')


# %% [markdown]
# ### 12. Organizing the values found in the previous block into the proper format for the bar graph model to run 

# %%

#Creating the column names for the bar chart
year_educating = ['0-13', '13-16', '16-20', '20+']
#creating the arrays for the bar chart
mean_age_onset = [
    patients_0_13_years_educated_age_onset_mean,
    patients_13_16_years_educated_age_onset_mean,
    patients_16_20_years_educated_age_onset_mean,
    patients_20_plus_years_educated_age_onset_mean,
]
#creating the arrays of standard deviations for the bar chart
stdev_age_onset = [patients_0_13_years_educated_age_onset_std, patients_13_16_years_educated_age_onset_std, patients_16_20_years_educated_age_onset_std, patients_20_plus_years_educated_age_onset_std]

#This line is copied from the class example. It creates an asymmetric error bar which is the standard devaition bar that extends above each group in the bar graph 
yerr = [np.zeros(len(mean_age_onset)), stdev_age_onset]


# %% [markdown]
# ### 13. Format and display the bar graph 

# %%

#This block of code formats the bar graph 
plt.bar(year_educating, mean_age_onset, yerr=yerr, capsize=10, color=["blue", "orange"])
plt.title("Average Age of Onset Mediated by Years of Education")
plt.xlabel("Years of Education")
plt.ylabel("Average Age of Onset (age)")

#This block of code performs the one-way ANOVA test to determine if there are significant differences between the groups that would indicate level of education plays a role in deffering symptoms 
f_stat, p_value = stats.f_oneway(x_patients_0_13_years_educated_age_onset, x_patients_13_16_years_educated_age_onset, x_patients_16_20_years_educated_age_onset, x_patients_20_plus_years_educated_age_onset)
print("\nF-statistic:", f_stat)
print("\np-value:", p_value)
plt.text(
    0.98,
    0.98,
    f"One-Way ANOVA: p = {p_value:.3f}",
    transform=plt.gca().transAxes,
    ha="right",
    va="top",
    fontsize=12,
)
plt.show()


# %% [markdown]
# ## Verify and validate your analysis: 
# *(Describe how you checked to see that your analysis gave you an answer that you believe (verify). Describe how your determined if your analysis gave you an answer that is supported by other evidence (e.g., a published paper).*

# %% [markdown]
# ## Conclusions and Ethical Implications: 
# *(Think about the answer your analysis generated, draw conclusions related to your overarching question, and discuss the ethical implications of your conclusions.*

# %% [markdown]
# ## Limitations and Future Work: 
# *(Think about the answer your analysis generated, draw conclusions related to your overarching question, and discuss the ethical implications of your conclusions.*

# %% [markdown]
# ## AI Usage Statement:
# The only AI used was the built in AI in VsCode. The AI was used to debugg the code, and help with formating the bar graphs and scatter plots. 

# %% [markdown]
# ## GitHub Repository Link:
# *Please provide the link to your shared GitHub repository that includes this notebook and any other scripts, notebooks, or data that you used for this project.*
# 


