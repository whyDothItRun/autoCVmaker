from docx import Document


modules = ['Design and Experimentation', 'Prototyping and Development', 'Electronic Engineering Foundations',
           'Engineering Science',
           'Engineering Mathematics', 'Thermodynamics and Fluid Mechanics', 'Quality Engineering',
           'Engineering Materials', 'Solid Mechanics', 'Dynamics and Control Systems',
           'Design and Engineering for the User', 'Engineering for Industry', 'Advanced Thermodynamics and Fluids',
           'Heat Transfer and Turbo-Machinery', 'Energy Efficiency', 'Design Failure Analysis',
           'Advanced Dynamics and Control Systems', 'Advanced Systems Design',
           'Solid Mechanics and Finite Element Analysis', 'Engineering Design and the Environment']


fieldType = input("What field is this? \n" )

for i, item in enumerate(modules,1):            #this numbers the list above and with the \n puts it on each line
    print(i, '. ' + item, sep='',end='\n')



print("Which out of the following modules are relevant to this job? Choose 3: \n")
chosenModule1 = input("First \n")
chosenModule2 = input("Second \n")
chosenModule3 = input("Third \n")

chosenModule1 = modules[int(chosenModule1)]
chosenModule2 = modules[int(chosenModule2)]
chosenModule3 = modules[int(chosenModule3)]

chosenModules = chosenModule1 + ', ' + chosenModule2 + ', ' + chosenModule3 + '.'







doc = Document(r'C:\Users\Daniel\.PyCharmCE2019.3\config\scratches\CV_Template.docx')

Dictionary = {"chosenModules": "fieldType"}



for paragraph in doc.paragraphs:
    if 'chosenModules' in paragraph.text:
        print(paragraph.text)
        paragraph.text = "Modules include: " + chosenModules
    if 'fieldType' in paragraph.text:
        print(paragraph.text)
        paragraph.text = "Creative and innovative mechanical engineering graduate with extensive experience in teaching, seeking employment within the " + fieldType + ". Detail oriented with the ability to efficiently organise, problem solve and manage teams. Experience within customer service, consistently fulfilling client’s requests and increasing the efficiency of the team."

doc.save("CV_" + fieldType + ".docx")