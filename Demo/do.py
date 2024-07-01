# class ClassName:
#     def __init__(self, patient_name, patient_number, hospital_name):
#         self.patient_name = patient_name
#         self.patient_number = patient_number
#         self.hospital_name = hospital_name
#     def __str__(self):
#         return f'Patient Name: {self.patient_name}, Patient Number: {self.patient_number}, Hospital Name: {self.hospital_name}'
        
#     def records(self):
#         print('records')
        
# ObjectName = ClassName('Juma', 21, 'Safaricom')
# print(ObjectName)   
# ObjectName.records()

# class Class2(ClassName):   
#     super(ClassName).__init__(self,age, country, id_no):
        
# def getKeys(formatString):
    
#     """formatString is a format string with embedded dictionary keys.
#     Return a list containing all the keys from the format string. """
#     keyList = list()
#     end = 0
#     repetitions = formatString.count("{")
#     for i in range(repetitions):
#         start = formatString.find("{", end) + 1
#         end = formatString.find("}", start)
#         key = formatString[start : end]
#         keyList.append(key)
#     return keyList     
    
# originalStory = """
# Once upon a time, deep in an ancient jungle,
# there lived a {animal}. This {animal}
# liked to eat {food}, but the jungle had
# very little {food} to offer. One day, an
# explorer found the {animal} and discovered
# it liked {food}. The explorer took the
# {animal} back to {city}, where it could
# eat as much {food} as it wanted. However,
# the {animal} became homesick, so the
# explorer brought it back to the jungle,
# leaving a large supply of {food}.
# The End
# """
# print(getKeys(originalStory))   
import xml.etree.ElementTree as ET

data = '''
<person>
<name>Chuck</name>
<phone type="intl">
+1 734 303 4456
</phone>
<email hide="yes" />
</person>'''

tree= ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
print('Phone:', tree.find('phone').text)