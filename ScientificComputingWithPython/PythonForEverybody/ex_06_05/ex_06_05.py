print("PY4E - Exercise 6.5")

str = 'X-DSPAM-Confidence: 0.8475'
str_colon = str.find(':')
print('position str_colon:', str_colon)
extracted_str = (str[str_colon + 1:]).lstrip()
print("Extracted string 1:",extracted_str)
print("Extracted string 1 type:", type(extracted_str))
extracted_str = float(extracted_str)
print("Extracted string final:",extracted_str)
print("Extracted string final type:", type(extracted_str))