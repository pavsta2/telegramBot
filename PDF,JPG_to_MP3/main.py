from gtts import gTTS
import pdfplumber
from pathlib import Path
import pytesseract
from PIL import Image
from art import tprint


class ConvertPDFToMP3:
    """
    Класс для конвертации файлов PDF и JPG в файлы MP3 ...
    """

    def jpg_to_mp3(self, file_path: str, lang: str) -> None:
        """метод конвертирует JPG в MP3 (пока только на английском)"""

        # проверяем путь к файлу и формат файла
        if Path(file_path).is_file() and Path(file_path).suffix == '.jpg':
            tprint('jpg to mp3', font='bulbhead')
            # выводим в консоль сообщение о начале работы программы
            print('Processing...')
            # открываем картинку
            image = Image.open(file_path)
            # инициализируем путь к приложению tesseract
            pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
            # распознаем картинку и конвертируем в текст
            text = pytesseract.image_to_string(image)

            # with open("text3.txt", "w") as file:
            #     file.write(text)
            #     print('текст3 записан')

            # создаем аудио файл
            my_audio = gTTS(text, lang=lang)
            # читаем имя файла, из которого брали картинку
            file_name = Path(file_path).stem
            # записываем аудиофайл с этим же именем
            my_audio.save(f'{file_name}.mp3')

            print(f'File {file_name} created')

        else:
            print('File not exists!')

    def pdf_to_mp3(self, file_path: str, lang: str) -> None:
        """метод конвертирует PDF в MP3"""

        # проверяем путь к файлу и формат файла
        if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
            tprint('pdf to mp3', font='bulbhead')
            print('Processing...')
            # открываем файл, читаем и формируем список с текстами страниц
            with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
                pages = [page.extract_text() for page in pdf.pages]
            # склеиваем все страницы в один текст
            text = ''.join(pages)
            # убираем из текста переносы
            text = text.replace('\n', '')

            my_audio = gTTS(text, lang=lang)
            file_name = Path(file_path).stem
            my_audio.save(f'{file_name}.mp3')

            print(f'File {file_name} created')

        else:
            print('File not exists!')


if __name__ == '__main__':
    a = ConvertPDFToMP3()
    # a.pdf_to_mp3("/Users/darinastarshinova/pavel/Test.pdf", 'ru')
    a.jpg_to_mp3("//Mac/Home/Desktop/test2.jpg", 'en')

