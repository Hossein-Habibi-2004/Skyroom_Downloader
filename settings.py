import os

# Path
join_path = os.path.join
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = join_path(BASE_DIR, "Data")
if os.path.exists(join_path(BASE_DIR, "Files")) == False:
    os.mkdir(join_path(BASE_DIR, "Files"))
FILES_DIR = join_path(BASE_DIR, "Files")

# File
Gui_Font_Vazir = join_path(DATA_DIR, "Vazir-Black.ttf")
Gui_Font_RobotoMono = join_path(DATA_DIR, "RobotoMono-Regular.ttf")
Gui_StyleSheet = join_path(DATA_DIR, "GUI.qss")
