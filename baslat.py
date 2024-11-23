import os
import subprocess
import time

# Baslangicta bu mesaji veriyor isterseniz kaldirabilirsiniz
print("LorNapes tarafından kodlandırılmıştır, like atıp abone olabilirsin.")
time.sleep(5)

# Buraya acacaginiz yazilimlarin adresini yazin varsayilan olarak toplama toplama yerini degistirin
folder_path = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'toplama')

# Klasor var mi diye kontrol ediyor bu kisim onemli degistirmeyin
if os.path.exists(folder_path):
    try:
        
        for file in os.listdir(folder_path):
            if file.endswith(".exe"):  
                file_path = os.path.join(folder_path, file)
                print(f"Executing: {file_path}")
                subprocess.run([file_path], shell=True)  
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print(f"The folder does not exist: {folder_path}")
