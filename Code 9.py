#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Patients:
    def __init__(self, name, age, gender, blood_pressure, temperature):
        self.name = name
        self.age = age
        self.gender = gender
        self.blood_pressure = blood_pressure
        self.temperature = temperature
        
    def display_patient_info(self):
        print(f"Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nBlood Pressure: {self.blood_pressure[0]} / {self.blood_pressure[1]}\nTemperature: {self.temperature}")
    
    def is_hypertensive(self):
        systolic, diastolic = self.blood_pressure
        return systolic >= 140 or diastolic >= 90
    
    def is_feverish(self):
        return self.temperature >= 37.5


# In[7]:


# defining data
patient1 = Patients("John Doe", 45, "Male", (140,85), 36.8 )
patient2 = Patients("Jane Smith", 32, "Female", (130,88), 37.6 )


# In[8]:


# display the patient information
patient1.display_patient_info()
patient2.display_patient_info()


# In[19]:


# check blood pressure
patient1.is_hypertensive()


# In[20]:


patient2.is_hypertensive()


# In[21]:


# check temperature
patient1.is_feverish()


# In[22]:


patient2.is_feverish()


# In[ ]:




