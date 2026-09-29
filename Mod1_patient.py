#File to create the class constructor and methods that will be used in the main python file 
 
#importing data set file 
import csv

#making the class that will organize the patient data 
class Patient:
    #this list is the directory for every following method, once the data points are added by the constructor the other methods can refer to it for thier functions 
    all_patients = []
    #Constructor builds objects and assign the values age of onset, gender, gene type, and years of education to them for later use
    def __init__(self, age_of_onset, gender, gene_type, years_of_education):
        self.age_of_onset = age_of_onset
        self.gender = gender
        self.gene_type = gene_type
        self.years_of_education = years_of_education
        Patient.all_patients.append(self)

    #The str and repr methods format the objects created in the constructor so they display the values stored in the object for easy reading
    def __str__(self):
        return f"Gender: {self.gender}, Age of Onset: {self.age_of_onset}, Gene Type: {self.gene_type}"
    def __repr__(self):
        #according to class TA this is just for programmers to easily identify the objects and their values 
        return f" gender='{self.gender}', Patient(age_of_onset={self.age_of_onset}, gene_type='{self.gene_type}')"
    @classmethod 
    # We need a method that can organize the patient data from the CSV file into values the constructor can use 
    # We used the built in AI to help me with this portion 
    def instantiate_from_csv(cls, filename: str):

        #the code below will open the .csv file and go through row by row, pulling the assigned columns and assigning them to the values that the constructor will use 
        # in this process it is also calling the constructor and creating these objects by calling the class Patient 
        
        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)

        
            for row in rows_of_patients:
                    Patient(
                    gender = row['Sex'],
                    age_of_onset = (
                        int(row['Age of onset cognitive symptoms'])
                        if row['Age of onset cognitive symptoms'].strip()
                        else None
                    ),
                    gene_type = row['APOE Genotype'],
                    years_of_education = (
                        int(row['Years of education'])
                        if row['Years of education'].strip()
                        else None
                    ),
                    )
    @classmethod
    #We used the built in AI to help me with the code because we weren't sure how to sort the values by age of onset. 
    # this code sorts the patients with the e4 by age of onset  
    #When i call it from main it goes through the list of all patients and returns only those with the specified gene type 
    def get_patients_with_4_4_gene(cls, gene_type):
         matching_patients = [
             patient
             for patient in cls.all_patients
             if patient.gene_type == gene_type
         ]
         return sorted(
             matching_patients,
             key=lambda patient: (
                 patient.age_of_onset is not None,
                 patient.age_of_onset or 0,
             ),
             reverse=True,
         )
    @classmethod
    #This block of code is the same as 54-67 but for the 3_4 gene type 
    def get_patients_with_3_4_gene(cls, gene_type):
        matching_patients = [
            patient
                for patient in cls.all_patients
                if patient.gene_type == gene_type
        ]
        return sorted(
            matching_patients,
            key=lambda patient: (
                patient.age_of_onset is not None,
                patient.age_of_onset or 0,
            ),
            reverse=True,
            )
    @classmethod 
    #This block of code is the same as 54-67 but for the 2_4 gene type 
    def get_patients_with_2_4_gene(cls, gene_type):
        matching_patients = [
            patient
                for patient in cls.all_patients
                if patient.gene_type == gene_type
        ]
        return sorted(
            matching_patients,
            key=lambda patient: (
                patient.age_of_onset is not None,
                patient.age_of_onset or 0,
            ),
            reverse=True,
            )
    @classmethod 
    #This block of code is the same as 54-67 but for the 3_3 gene type 
    def get_patients_with_3_3_gene(cls, gene_type):
        matching_patients = [
            patient
                for patient in cls.all_patients
                if patient.gene_type == gene_type
        ]
        return sorted(
            matching_patients,
            key=lambda patient: (
                patient.age_of_onset is not None,
                patient.age_of_onset or 0,
            ),
            reverse=True,
            )
    @classmethod 
    #This block of code is the same as 54-67 but for the 3_2 gene type 
    def get_patients_with_3_2_gene(cls, gene_type):
            matching_patients = [
                patient
                    for patient in cls.all_patients
                    if patient.gene_type == gene_type
            ]
            return sorted(
                matching_patients,
                key=lambda patient: (
                    patient.age_of_onset is not None,
                    patient.age_of_onset or 0,
                ),
                reverse=True,
                )
    @classmethod
    #This method filters patients based of the range of ages provided when the method is called  
    def get_patients_number_of_years_educated(cls, minimum_years, maximum_years):
        for patient in cls.all_patients:
            if (#this conditional makes sure that there is data values for the number of years of education and that the data point falls within the requested range 
                patient.years_of_education is not None
                and minimum_years <= patient.years_of_education < maximum_years
            ):
                yield patient
