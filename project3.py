from PyPDF2 import PdfFileReader
from PIL import Image,ImageDraw,ImageFont
import img2pdf
import os
import datetime
from PyPDF2 import PdfFileMerger
from tkinter.filedialog import askopenfilename
now = datetime.datetime.now()
print str(now)
year = now.year
month = now.month
day = now.day
month_six_later = month + 6
date = '{}/{}/{}'.format(day,month,year)
date_six_later = '{}/{}/{}'.format(day,month_six_later,year)
print(date)

#infile = "Test-Sheet-3.pdf"
infile = askopenfilename()
pdf_reader = PdfFileReader(open(infile, "rb"))

dictionary = pdf_reader.getFormTextFields() # returns a python dictionary
dictionary_2  = pdf_reader.getFields(tree=None, retval=None)

patient_last_name = str(dictionary['Pat_LastName'])
patient_first_name = str(dictionary['Pat_FirstName'])
patient_name = '{} {}'.format(patient_first_name,patient_last_name)
#patient_gender = str(dictionary['Pat_Gender'])
patient_DOB = str(dictionary['Pat_DOB'])

patient_gender = str(dictionary_2['Pat_Gender'])

if patient_gender[102] == 'F':
    patient_gender = 'Female'
elif patient_gender[102]  == 'M':
    patient_gender = 'Male'

knee_for_analysis = str(dictionary_2['Pat_Side'])

if knee_for_analysis[100] == 'L':
    knee_for_analysis = 'Left'
elif knee_for_analysis[100]  == 'R':
    knee_for_analysis = 'Right'

femoral = False
femoral_component = str(dictionary_2['OP50_FemGuide'])
print(femoral_component[9])
if femoral_component[9] == 'Y':
    femoral = True
    femoral_component = 'Femur'
#elif femoral_component[9] == 'N':
tibial = False
tibial_component = str(dictionary_2['OP50_TibGuide'])
if tibial_component[9] == 'Y':
    tibial = True
    tibial_component = 'Tibia'

patella = False
patella_component = str(dictionary_2['OP50_PatGuide'])

if patella_component[9] == 'Y':
    patella = True
    patella_component = 'Patella'


#Knee for analysis
date_of_surgery= str(dictionary['DOS'])
Hospital_name = str(dictionary['Hospital'])
implant_brand= str(dictionary['Imp_Brand'])
implant_model = str(dictionary['Imp_Model'])
femoral_number = str(dictionary['OP40_femcmp_1'])
tibial_number = str(dictionary['OP40_tibcmp_1'])
patella_number  = str(dictionary['OP40_patcmp_1'])
surgeon_name = str(dictionary['Surgeon'])

femur_guide1 = '1507-0300-00 Femur Guide'
femur_guide2 = '1507-0500-00 Trial Distal Femur'
femur_guide3 = '1811-0800-00 Femur Drop Rod Attachment'

tibia_guide1 = '1507-0400-00 Tibia Guide'
tibia_guide2 = '1507-0600-00 Trial Proximal Tibia'
tibia_guide3 = '1811-0700-00 Tibia Drop Rod Attachment'

patella_guide1 = '1507-0100-00 Patella Guide'
patella_guide2 = '1507-0200-00 Trial Patella'

Job_ID_no = str(dictionary['Job_ID'])

image_back = Image.open('/Users/mingxiaotu/Desktop/back_2.png')
font_type = ImageFont.truetype('Arial.ttf',22)
draw  = ImageDraw.Draw(image_back)
draw.text(xy=(280,210),text = patient_name,fill = (0,0,0),font = font_type)
draw.text(xy=(280,242),text = patient_DOB,fill = (0,0,0),font = font_type)
draw.text(xy=(280,277),text = patient_gender,fill = (0,0,0),font = font_type)
draw.text(xy=(280,362),text = Hospital_name,fill = (0,0,0),font = font_type)
draw.text(xy=(280,395),text = surgeon_name,fill = (0,0,0),font = font_type)
draw.text(xy=(280,430),text = date_of_surgery,fill = (0,0,0),font = font_type)
draw.text(xy=(780,208),text = knee_for_analysis,fill = (0,0,0),font = font_type)
draw.text(xy=(780,275),text = implant_brand,fill = (0,0,0),font = font_type)
draw.text(xy=(855,275),text = implant_model,fill = (0,0,0),font = font_type)
if femoral == True:
    draw.text(xy=(780,243),text = femoral_component,fill = (0,0,0),font = font_type)
    draw.text(xy=(845,243),text = femoral_number,fill = (0,0,0),font = font_type)
if tibial == True:
    draw.text(xy=(870,243),text = tibial_component,fill = (0,0,0),font = font_type)
    draw.text(xy=(920,243),text = tibial_number,fill = (0,0,0),font = font_type)
if patella == True:
    draw.text(xy=(935,243),text = patella_component,fill = (0,0,0),font = font_type)
    draw.text(xy=(970,243),text = patella_number,fill = (0,0,0),font = font_type)


font_type2 = ImageFont.truetype('Arial.ttf',14)
image_front = Image.open('/Users/mingxiaotu/Desktop/front_2.png')
font_type = ImageFont.truetype('Arial.ttf',22)
draw  = ImageDraw.Draw(image_front)
draw.text(xy=(350,190),text = patient_name,fill = (0,0,0),font = font_type)

draw.text(xy=(350,120),text = Job_ID_no,fill = (0,0,0),font = font_type)
draw.text(xy=(90,400),text = date,fill = (0,0,0),font = font_type)
draw.text(xy=(90,480),text = date_six_later,fill = (0,0,0),font = font_type)
if femoral == True:
    draw.text(xy=(320,320),text = femur_guide1,fill = (0,0,0),font = font_type2)
    draw.text(xy=(320,340),text = femur_guide2,fill = (0,0,0),font = font_type2)
    draw.text(xy=(320,360),text = femur_guide3,fill = (0,0,0),font = font_type2)
if tibial == True:
    draw.text(xy=(600,320),text = tibia_guide1,fill = (0,0,0),font = font_type2)
    draw.text(xy=(600,340),text = tibia_guide2,fill = (0,0,0),font = font_type2)
    draw.text(xy=(600,360),text = tibia_guide3,fill = (0,0,0),font = font_type2)
if patella == True:
    draw.text(xy=(320,380),text = patella_guide1,fill = (0,0,0),font = font_type2)
    draw.text(xy=(600,380),text = patella_guide2,fill = (0,0,0),font = font_type2)

#image_front.show()
#image_back.show()

img_path = '/Users/mingxiaotu/Desktop/address.png'
pdf_path = '/Users/mingxiaotu/Desktop/address.pdf'
image = Image.open(img_path)

if image.mode == 'RGBA':
    image = image.convert('RGB')
pdf_path = '/Users/mingxiaotu/Desktop/address.pdf'
if not os.path.exists(pdf_path):
    image.save(pdf_path,"PDF",resolution  = 100.0)

if image_back.mode == 'RGBA':
    image_back = image_back.convert('RGB')
pdf_path = '/Users/mingxiaotu/Desktop/back_2.pdf'
if not os.path.exists(pdf_path):
    image_back.save(pdf_path,"PDF",resolution  = 100.0)

if image_front.mode == 'RGBA':
    image_front = image_front.convert('RGB')
pdf_path = '/Users/mingxiaotu/Desktop/front_2.pdf'
if not os.path.exists(pdf_path):
    image_front.save(pdf_path,"PDF",resolution  = 100.0)

path = "/Users/mingxiaotu/Desktop/"
pdf_files = ['address.pdf','front_2.pdf','back_2.pdf','front_2.pdf','back_2.pdf']
merger = PdfFileMerger()
for files in pdf_files:
    merger.append(path+files)
if not os.path.exists(path+'merger.pdf'):
    merger.write(path+'merger.pdf')
merger.close()

os.remove('back_2.pdf')
os.remove('address.pdf')
os.remove('front_2.pdf')
