info = []
age_info = []
symptom_info = []

def get_patient():  # Function to gather patient information.
    patient_number = 1
    while True:
        print(f'Patient #{patient_number}')
        first_name = input('What is your first name?: ')
        last_name = input('What is your last name?: ')
        while True:
            patient_id = input('Enter your ID?: ')
            if len(patient_id) == 6:
                break
        age = int(input('How old are you?: '))
        symptom = input('What symptom do you have?: ')
        status = input('More patient?(y/n): ')
        patient_info = [first_name, last_name, patient_id, age, symptom]
        info.append(patient_info)
        if status == 'y':
            patient_number += 1
            print('******')
        else:
            print('******')
            return info

def find_age_above(all_patient, age):  # Function to find patients with ages above a specified threshold.
    for i in range(len(all_patient)):
        if all_patient[i][3] > age:
            age_info.append(all_patient[i][2])
    return age_info

def print_patient(all_patient, patient_id):  # Function to print patient information based on patient IDs.
    for patient in patient_id:
        for j in range(len(all_patient)):
            if all_patient[j][2] == patient:
                print(f'ID:{patient} {all_patient[j][0]} {all_patient[j][1]}')

def find_symptoms(all_patient, symptom):  # Function to find patients with specific symptoms.
    for i in range(len(all_patient)):
        symptoms_list = all_patient[i][4].split(' and ')
        if symptom in symptoms_list:
            symptom_info.append(all_patient[i][2])
    return symptom_info

# Main part
# Fill in code for the main part below
info = get_patient()
age = int(input('Type Age: '))
print(f'Output the name of the patient with age more than {age}.')
patient_id = find_age_above(info, age)
print_patient(info, patient_id)
symptom = input('Type Symptoms: ')
print(f'Output the name of the patient with {symptom} symptoms.')
patient_id = find_symptoms(info, symptom)
print_patient(info, patient_id)