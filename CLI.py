from downloader import Skyroom_Downloader

def main():
    main_url = input("Enter Sample Url: ")
    lesson_name = input("Enter Lesson Name: ")
    last_page = int(input("Enter Last Page Number: "))
    pdf = input("Are You Want Convert To PDF? [Y/N]")
    
    downloader = Skyroom_Downloader(main_url, lesson_name, last_page, PrintValue)
    downloader.download_images()
    print("Download Images: 100%")
    if pdf.lower() == "y":
        downloader.convert_to_pdf()
        print("Convert To Pdf: 100%")
    input("Please [Enter] To Exit :)")

def PrintValue(v):
    print(f"Page: {v}")

if __name__ == '__main__':
    main()
