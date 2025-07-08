import os
import time

#change to your required folder
# eg. C:\Users\name\some_folder_with_lots_of_files
folder = 'any_path'

os.chdir(folder)

contents = os.listdir()
files[]
Videos = ['mp4','mkv']
Audios = ['mp3','wav','ogg']
Images = ['jpg','jpeg','png','gif','webp','svg']
Docs = ['pdf','doc','docx','txt','ppt','pptx','xls','xlsx','csv']

print('Welcome to The File Classifier')
print('The program is running in: ')
print(3)
time.sleep(1000)
print(2)
time.sleep(1000)
print(1)
time(sleep)

for name in contents:
    if os.path.isfile(name):
        files.append(name)

for filename in files:
    if filename.split('.')[-1] in Videos:
        os.mkdir('Videos')
        source = os.path.join(folder, filename)
        destination = os.path.join(folder, 'Videos')
        os.rename(source, destination)
                          
    elif filename.split('.')[-1] in Audios:
        os.mkdir('Audios')
        source = os.path.join(folder, filename)
        destination = os.path.join(folder, 'Audios')
        os.rename(source, destination)
        
    elif filename.split('.')[-1] in Images:
        os.mkdir('Images')
        source = os.path.join(folder, filename)
        destination = os.path.join(folder, 'Images')
        os.rename(source, destination)
        
    elif filename.split('.')[-1] in Docs:
        os.mkdir('Docs')
        source = os.path.join(folder, filename)
        destination = os.path.join(folder, 'Docs')
        os.rename(source, destination)
        
    else:
        os.mkdir('Misc')
        source = os.path.join(folder, filename)
        destination = os.path.join(folder, 'Misc')
        os.rename(source, destination)


print('Operation Completed')
print('Files moved successfully')




    
