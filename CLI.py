from downloader import Skyroom_Downloader

def main():
    main_url = input("Enter Sample Url: ")
    lesson_name = input("Enter Lesson Name: ")
    last_page = int(input("Enter Last Page Number: "))
    
    downloader = Skyroom_Downloader(main_url, lesson_name, last_page)
    downloader.download_images()
    print("Download Images: 100%")
    downloader.convert_to_pdf()
    print("Convert To Pdf: 100%")

if __name__ == '__main__':
    main()
