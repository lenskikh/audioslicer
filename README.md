# Audio Slicer
The application slices the audio track into parts. 

# Before start

1. Please make sure to have ffmpeg installed
https://ffmpeg.org/download.html
2. Download the codec ffmpeg and edit path in your system
It would be great if you could watch this video https://youtu.be/IECI72XEox0
3. If you have a windows operating system, you can download audioslicer.zip and unzip to the folder with the same name, and run audioslicer.exe Be sure that the logo2.png file is present with the program


By default, it is sliced into 30-second chunks. The new version will allow you to specify the exact size.
![Screenshot](/screenshots/scr3.png)

# Audio Slicer Ru

Программа имеет три функции:
1. Нарезка аудиофайла на ровные отрезки. Укажите отрезок в секундах. 
2. Извлечение аудиодорожки из видеофайла формата mp4, по умолчанию сохраниться в wav формате
3. Извлечение отрезка из аудиофайла и комбинирование mp3 файла. Например, вы хотите удалить короткий разговор из аудиоклипа. Укажите в секундах, где начинается разговор и когда заканчивается, именно этот отрывок будет удален и создан новый mp3 файл без этого отрывка. 

# Установка

1. Поставьте язык python любой версии
2. Перед запуском установите кодек ffmpeg, нужно просто скачать exe и прописать к нему путь, как показано на этом видео https://youtu.be/IECI72XEox0
3. Установите две библиотеки: 
pip install pydub
pip install ffmpeg

Если у вас Windows, то можете просто скачать архив audioslicer.zip и распаковать его в директорию. 