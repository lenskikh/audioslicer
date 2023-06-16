from tkeasy import TKeasy
from pydub import AudioSegment
import random

gui = TKeasy()

gui.Title("Audio Slicer")
gui.config(size="325x380")

gui.frames (frame = "frame 1", x= 0, y = 0,
            highlightbackground = "black",
            background = "#fcc045",
            padx = 10,
            pady = 10)

def slicefile():
    try:
        file = gui.select_file()
        file_format = file.split(".")[-1]
        gui.text_area(name="info area",width=37,height=19,padx = 5, row=2)

        match file_format:
            case "mp3":
                song = AudioSegment.from_mp3(file)
            case "wav":
                song = AudioSegment.from_wav(file)
            case "flv":
                song = AudioSegment.from_flv(file)
            case "ogg":
                song = AudioSegment.from_ogg(file)
            case "aac":
                song = AudioSegment.from_file(file, "aac")                
        
        unique_filename = str(random.random())[2:8]

        total = len(song)
        counter = 30000
        i = 0
        seg = 1

        while i < total:
            mixed = song[i:counter]
            filename = unique_filename + "_" +str(seg)+".mp3"
            mixed.export(filename, format="mp3")
            text = filename + " was created" + "\n"
            gui.insert_text_area("info area", text)
            i+= 30000
            counter+= 30000
            seg+= 1
    except:
         gui.msg_box_warning("Nope","A file was not selected")

gui.label(text="Support mp3, wav, ogg, aac", bg = "#fcc045")
gui.button(text="Choose an audio file", command=slicefile, padx = 5, pady = 5, row=1, column=0)

#if logo-picture was deleted
try:
    gui.photo("logo2.png",row = 2)
except:
    pass

gui.loop()
