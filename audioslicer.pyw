from tkeasy import TKeasy
from pydub import AudioSegment
import ffmpeg
import random

gui = TKeasy()

gui.Title("Audio Slicer")
gui.config(size="320x400", bg = "#fcc045")

bg_color = "#ffd7ae"

gui.frames (frame = "Tab of Audio Slicer", x= 20, y = 10,
            highlightbackground = "#108eda",
            background = "#108eda")

gui.label(text="Audio Slicer", font=("Arial", 16), fg = "white", bg = "#108eda", padx = 10)

gui.frames (frame = "Audio Slicer", x= 10, y = 40,
            highlightbackground = "#108eda",
            highlightthickness = 1,
            background = bg_color,
            padx = 10, pady = 10)

def detect_format(fileFormat,file):

    match fileFormat:
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

    return song


def slicefile():
    text = "" 

    file = gui.select_file()
    fileFormat = file.split(".")[-1]

    song = detect_format(fileFormat,file)

    unique_filename = str(random.random())[2:8]

    total = len(song)
    
    multi = int(gui.get_info("ent"))*1000
    end_of_seg = multi
    start_seg = 0
    seg = 1 

    while True:
        if end_of_seg > total:
            end_of_seg = total
        
        mixed = song[start_seg:end_of_seg]
        filename = unique_filename + "_" + str(seg)+".mp3"
        mixed.export(filename, format="mp3")
        
        text+= filename + " was created" + "\n"
        start_seg+= multi
        end_of_seg+= multi
        seg+= 1
        if start_seg > total:
            gui.msg_box_warning("Done",text)
            break            

def extract_audio(video_path, output_path):
    ffmpeg.input(video_path).output(output_path, format='wav').run()

def extractor():
    video_path = gui.select_file()
    name_song = str(video_path.split("/")[-1])
    gui.label(text=name_song,  bg = "#ead5ff", padx = 3, column = 1)
    name_song = name_song.split(".")[0]
    audio_output_path = name_song+"_"+str(random.random())[2:8] + '.wav'
    extract_audio(video_path, audio_output_path)

def combiner():
    file = gui.select_file()
    fileFormat = file.split(".")[-1]
    song = detect_format(fileFormat,file)
    total = len(song)
    
    from_slice1 = gui.get_info(name="slice 1")
    if ":" in from_slice1:
        end_of_start = from_slice1.split(":")
        end_of_start = (int(end_of_start[0])*60+int(end_of_start[1]))*1000
    else:
        end_of_start = int(from_slice1) * 1000
    
    from_slice2 = gui.get_info(name="slice 2")
    if ":" in from_slice2:
        start_of_end = from_slice2.split(":")
        start_of_end = (int(start_of_end[0])*60+int(start_of_end[1]))*1000
    else:
        start_of_end = int(from_slice2)*1000
        
    seg1 = song[0:end_of_start]
    seg2 = song[start_of_end:total]
    seg_mix = seg1+seg2

    unique_filename = str(random.random())[2:8] + ".wav"
    seg_mix.export(unique_filename, format="wav")


gui.label(text="Support mp3, wav, ogg, \naac, flv", sticky="e", bg = bg_color, justify = "left")
gui.button(text="Choose an audio file", command=slicefile, sticky="w", padx = 10, pady = 5, column=1)

gui.label(text="Specify the time interval \nin seconds for cut.", bg = bg_color,  sticky="e", justify = "left", row=1, column=0)
gui.entry(name="ent", sticky="w", width = 4, padx = 10, pady = 5, row=1, column=1)
text = "30"
gui.insert_text("ent", text,fg="grey")


gui.frames (frame = "YouTube", x= 20, y = 145,
            highlightbackground = "#108eda",
            background = "#108eda")

gui.label(text="Extractor", font=("Arial", 16), fg = "white", bg = "#108eda", padx = 10)

gui.frames (frame = "Extractor", x= 10, y = 175,
            highlightbackground = "#108eda",
            highlightthickness = 1,
            width = 500,
            height = 300,          
            background = bg_color,  
            padx = 10,
            pady = 10)

gui.label(text="The audio track will be extracted from the video file.", bg = bg_color)
gui.button(text="Choose mp4 video file", command=extractor, sticky="w", row = 1, pady = 5)

gui.frames (frame = "Trimmer tab", x= 20, y = 265,
            highlightbackground = "#108eda",
            background = "#108eda")

gui.label(text="Trimmer", font=("Arial", 16), fg = "white", bg = "#108eda", padx = 10)

gui.frames (frame = "Trimmer under", x= 10, y = 295,
            highlightbackground = "#108eda",
            highlightthickness = 1,
            background = bg_color,
            padx = 10,
            pady = 10)

gui.button(text="Choose a music file", command=combiner, sticky="w", padx = 10, pady = 5, row = 1)

gui.label(text="Delete audio segment & combine", bg = bg_color, sticky = "e", row = 0)
gui.entry(name="slice 1", sticky="w", width = 4, padx = 5, pady = 5, column=1, row = 0)

gui.label(text="To", bg = bg_color, column=2, row = 0)
gui.entry(name="slice 2", sticky="w", width = 4, padx = 5, pady = 5, column=3, row = 0)

gui.loop()
