import xml.etree.cElementTree as ET
import lxml.etree as etree
import numpy as np
from xml.dom import minidom
from itertools import cycle


# =======CLASSES TO USE LATER=============

class Note:
    letter = ''
    Octave = ''
    duration = ''
    typeOfNote = ''  # type of note
    alter = 'not_altered'  # sharp or not
    string = ''
    fret = ''


    def __init__(self, letter, Octave):
        self.letter = letter
        self.Octave = Octave

    def setDuration(self, duration):
        self.duration = duration

    def setTypeOfNote(self, typeOfNote):
        self.typeOfNote = typeOfNote

    def isChord(self):
        return False

    def getType(self):
        return self.typeOfNote

    def setAlter(self):
        self.alter = 1

    def getAlter(self):
        return self.alter

    def setString(self, string):
        self.string = string

    def setFret(self, fret):
        self.fret = fret

def whatOctave(string, fret):
    tempoctave = 0
    if string == 5:
        if fret <= 7:  # indexed E = 0 and b = 7 for me -alp: kalin e teli bu
            tempoctave = 2
        else:
            tempoctave = 3
    elif string == 4:  # A
        if fret <= 3:
            tempoctave = 2
        else:
            tempoctave = 3
    elif string == 3:  # D
        if fret <= 9:
            tempoctave = 3
        else:
            tempoctave = 4
    elif string == 2:
        if fret <= 4:
            tempoctave = 3
        else:
            tempoctave = 4
    elif string == 1:
        if fret == 0:
            tempoctave = 3
        elif fret <= 12:
            tempoctave = 4
        else:
            tempoctave = 5
    elif string == 0:
        if fret <= 7:
            tempoctave = 4
        else:
            tempoctave = 5
    else:
        print("String input might be wrong")
    return str(tempoctave)

# function for type calculation and selection gonna do something later
def totalTime(timeSelection):
    if timeSelection == '4/4':
        return 4
    elif timeSelection == '3/4':
        return 3

# ======== GONNA CHANGE IT LATER
def noteTypeHelper(note, whatType):
    typeOfNotes = ["16th", "eighth", "quarter", "half", "whole"]

    if whatType <= 0.25:
        note.setTypeOfNote(typeOfNotes[0])  # 1th
    elif whatType <= 0.5:
        note.setTypeOfNote(typeOfNotes[1])  # eight
    elif whatType <= 1:
        note.setTypeOfNote(typeOfNotes[2])  # quarter
    elif whatType <= 2:
        note.setTypeOfNote(typeOfNotes[3])  # half
    elif whatType <= 4:
        note.setTypeOfNote(typeOfNotes[4])  # whole



def noteTypeCalculator(arrOfNotes, lengthOfBar):
    typeOfNotes = ["16th", "eighth", "quarter", "half", "whole"]
    # trying something out here with the length
    tempLength = lengthOfBar - 1


    for j in range(0, len(arrOfNotes)):
        totalQuarterNoteTime = totalTime("4/4")  # it takes 4 quarter notes to play
        notePosition = arrOfNotes[j][1]
        note = arrOfNotes[j][0]

        if j != len(arrOfNotes) - 1:
            nextNotePosition = arrOfNotes[j + 1][1]
        else:
            nextNotePosition = lengthOfBar
        # variables are set for comparison
        difference = (nextNotePosition - notePosition)
        how_much_ratio = float(difference) / tempLength
        whatType = how_much_ratio * totalQuarterNoteTime
        if len(arrOfNotes[j]) > 2:
            for i in range(0, len(arrOfNotes[j]) - 1, 2):
                min = whatType
            for i in range(0, len(arrOfNotes[j]) - 1, 2): # need to increment by 2 for chords because i am sleepy and i fucked up

                noteTypeHelper(arrOfNotes[j][i], whatType)
        else:
            noteTypeHelper(note, whatType)









f = open("music.txt", "r")
text = f.read().split()
textarr = []



# Python3 program to Split string into characters
for t in text:
    textarr.append(list(t))

numpy_array = np.array(textarr)
transpose = numpy_array.T
transpose_list = transpose.tolist()




def duration(fret):  # find the next occurence of a number
    dur = 0

    for i in range(fret, len(transpose_list)):
        if transpose_list[i][0] == "-" and len(
                set(transpose_list[i])) == 1:  # if the first "|" occurs, then the first measure starts
            dur += 1
        else:
            break
    if dur > 8:
        return 8
    else:
        return dur


durations = []
for i in range(len(transpose_list)):
    durations.append(duration(i))

notes = []


##function gets the name of the note that was played
def noteFun(_string, fret):
    enote = ["F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E"]

    enote = ["F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E"]

    switcher = {  # default tuning mapping based of string.
        0: ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E"],
        1: ["B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"],
        2: ["G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G"],
        3: ["D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D"],
        4: ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A"],
        5: ["E", "F", "F#", "G", "G#", "A", "A#", "B", "C", "C#", "D", "D#", "E"],
    }

    return switcher.get(_string)[fret]


def isChord(fret):
    if len(set(fret)) > 2:
        return True
    else:
        return False


def isNum(x):
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "13", "14"]
    return x in num


def numToString(n):
    letters = ["E", "A", "D", "G", "B", "E"]
    return letters[n]


score_partwise = ET.Element("score-partwise", version="3.1")
part_list = ET.SubElement(score_partwise, "part-list")

score_part = ET.SubElement(part_list, "score-part", id="P1")

part_name = ET.SubElement(score_part, "part-name").text = "Classical Guitar"  # input part name here from user

part = ET.SubElement(score_partwise, "part", id="P1")

tree = ET.ElementTree(score_partwise)

m = 1  # number of measures

# the current fret we are on.
currFret = 0

for fret in transpose_list:
    if fret[0] == "|" and len(set(fret)) == 1:  # if the first "|" occurs, then the first measure starts
        measure = ET.SubElement(part, "measure", number=str(m))  # place a measure
        if m == 1:
            attributes = ET.SubElement(measure, "attributes")
            divisions = ET.SubElement(attributes, "divisions").text = str(2)
            key = ET.SubElement(attributes, "key")
            fifths = ET.SubElement(key, "fifths").text = str(0)
            t = ET.SubElement(attributes, "time")
            _beats = ET.SubElement(t, "beats").text = str(4)
            beats_type = ET.SubElement(t, "beats_type").text = str(4)
            clef = ET.SubElement(attributes, "clef")
            sign = ET.SubElement(clef, "sign").text = "TAB"
            line = ET.SubElement(clef, "line").text = str(5)
            staff_details = ET.SubElement(attributes, "staff-details")
            staff_lines = ET.SubElement(staff_details, "staff-lines").text = "6"
            for i in range(6):
                staff_tuning_line = ET.SubElement(staff_details, "staff-tuning", line="{}".format((i + 1)))
                tuning_step = ET.SubElement(staff_tuning_line, "tuning-step").text = numToString(i)
                switcher = {  # default tuning mapping based of string.
                    0: "2",
                    1: "2",
                    2: "3",
                    3: "3",
                    4: "3",
                    5: "4",
                }
                tuning_octave = ET.SubElement(staff_tuning_line, "tuning-octave").text = switcher.get(i)

        m += 1

    currFret += 1
    for string in fret:

        if isNum(string):  # if the current fret is a note.

            ## logic for finding out what note is what ################################################
            #########################################################################################

            note = ET.SubElement(measure, "note")

            if isChord(fret):
                chord = ET.SubElement(note, "chord")

            pitch = ET.SubElement(note, "pitch")

            if noteFun(fret.index(string), int(string)) == "F#":
                step = ET.SubElement(pitch, "step").text = "F"
                alter = ET.SubElement(pitch, "alter").text = "1"
            elif noteFun(fret.index(string), int(string)) == "G#":
                step = ET.SubElement(pitch, "step").text = "G"
                alter = ET.SubElement(pitch, "alter").text = "1"
            elif noteFun(fret.index(string), int(string)) == "A#":
                step = ET.SubElement(pitch, "step").text = "A"
                alter = ET.SubElement(pitch, "alter").text = "1"
            elif noteFun(fret.index(string), int(string)) == "C#":
                step = ET.SubElement(pitch, "step").text = "C"
                alter = ET.SubElement(pitch, "alter").text = "1"
            elif noteFun(fret.index(string), int(string)) == "D#":
                step = ET.SubElement(pitch, "step").text = "D"
                alter = ET.SubElement(pitch, "alter").text = "1"
            else:
                step = ET.SubElement(pitch, "step").text = noteFun(fret.index(string), int(string))

            octave = ET.SubElement(pitch, "octave").text = whatOctave(fret.index(string), int(string))
            notations = ET.SubElement(pitch, "pitch")

            duration = ET.SubElement(note, "duration").text = str(durations[currFret])

            technical = ET.SubElement(note, "technical")
            _string = ET.SubElement(technical, "string").text = "{}".format((fret.index(string) + 1))
            _fret = ET.SubElement(technical, "fret").text = string

# place notes

def makeNote(letter, octave):
    return Note(letter, octave)


def isAlter(alterednote):
    arrOfAlter = ['F#', 'G#', 'A#', 'C#', 'D#']
    arrOfNonAlter = ['F', 'G', 'A', 'C', 'D']
    if alterednote in arrOfAlter:
        return arrOfNonAlter[arrOfAlter.index(alterednote)]
    else:
        return False

# function that takes one line until the '|' and sets everything for that line only, call a for loop later
def noteArrayMaker(transpose_list):
    notesAndChords = []
    position = -1
    length = 0
    for vertLine in transpose_list:
        if vertLine[0] != '|':
            position += 1
            length += 1
        tempList = []
        for string in vertLine:
            if isNum(string):
                if not isAlter(noteFun(vertLine.index(string), int(string))):
                    tempNote = makeNote(isAlter(noteFun(vertLine.index(string), int(string))), whatOctave(vertLine.index(string), int(string)))
                    tempNote.setString(vertLine.index(string))
                    tempNote.setFret(int(string))
                    tempNote.setAlter()
                    tempList.append(tempNote)
                else:
                    # makes a note with the parameter type (the letter) and the octave of that note which are set
                    tempNote = makeNote(isAlter(noteFun(vertLine.index(string), int(string))), whatOctave(vertLine.index(string), int(string)))
                    tempNote.setString(vertLine.index(string))
                    tempNote.setFret(int(string))
                    tempList.append(tempNote)
                tempList.append(position)
        if len(tempList) >= 1:
            notesAndChords.append(tempList)
    noteTypeCalculator(notesAndChords, length)
    return notesAndChords







# methods for object to xml
# for note in range(0, len(noteArrayMaker(transpose_list)[0]) - 1, 2):
    # print noteArrayMaker(transpose_list)[0][note].getType()



for lists in noteArrayMaker(transpose_list):
    print lists
    if len(lists) > 2:
        for k in range(0, len(lists) - 1, 2):
            note = lists[k]
            # note is the indiviudal note in a chord so we can put it in its thing
            # all notes have their properties
            # if u wanna check if its altered you do if note.alter == 'not_altered'
            print(note, 'chord notes')
    else:
        note = lists[0]
        print(note, 'note')




















xmlstr = minidom.parseString(ET.tostring(score_partwise)).toprettyxml(indent="   ")

tree.write("filename.xml")

with open("filename.xml", "w") as f:
    f.write(xmlstr)







