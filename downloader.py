import os
import img2pdf
import requests
from glob import glob

join_path = os.path.join
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if os.path.exists(join_path(DATA_DIR, self.name)) == False:
    os.mkdir(join_path(BASE_DIR, "Files"))
DATA_DIR = join_path(BASE_DIR, "Files")

class Skyroom_Downloader:
    def __init__(self, url: str, name: str, last_page: int):
        self.url = url
        self.name = name
        self.last_page = last_page

        if os.path.exists(join_path(DATA_DIR, self.name)) == False:
            os.mkdir(join_path(DATA_DIR, self.name))
    
    def download_images(self) -> bool:
        for page in range(1, self.last_page+1):
            page = str(page).zfill(len(str(self.last_page)))
            self.__download_img(page)
            print(f'Page:{page}')
        return True
    
    def convert_to_pdf(self):
        folder_path = join_path(DATA_DIR, self.name)
        pdf_path = join_path(DATA_DIR, self.name, self.name+'.pdf')
        imagelist = self.__list_of_photos(folder_path)
        with open(pdf_path, 'wb') as f:
            f.write(img2pdf.convert(imagelist))
        return True
    
    def __download_img(self, page: str) -> bool:
        url = self.url + f"/images/P-{page}.jpg"
        name = f"{page}.jpg"
        with open(join_path(DATA_DIR, self.name, name), 'wb') as download_file:
            response = requests.get(url, stream=True)
            total_length = response.headers.get('content-length')
            if total_length is None:  # no content length header
                download_file.write(response.content)
                return False
            else:
                for data in response.iter_content(chunk_size=4096):
                    download_file.write(data)
                return True
    
    def __list_of_photos(self, folder_path, suffix='jpg'):
        return glob(f'{folder_path}/*.{suffix}')
