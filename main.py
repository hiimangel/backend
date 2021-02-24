import xml.etree.cElementTree as ET
import numpy as np

f = open("music.txt", "r")
text = f.read().split()
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14]

arre_test = "-----------0-----"
arrb_test = "---------0---0---"
arrg_test = "-------1-------1-"
arrd_test = "-----------------"
arra_test = "---2-------------"
arrE_test = "-0---------------"



# for later use of the chords
chord1 = "-0---------------"
chord2 = "-0---------------"
chord3 = "-0---------------"
chord4 = "-0---------------"
chord5 = "-0---------------"






def isChord():
    return False


class Note:
    letter = ''
    Octave = ''
    duration = ''
    typeOfNote = ''  # type of note
    state = ''  # sharp or not

    def __init__(self, letter, Octave, State):
        self.letter = letter
        self.Octave = Octave
        self.state = State

    def setDuration(self, duration):
        self.duration = duration

    def setTypeOfNote(self, typeOfNote):
        self.typeOfNote = typeOfNote

    def isChord(self):
        return False

    def getType(self):
        return self.typeOfNote


class Chord:
    arrayOfNote = []

    def __init__(self):
        pass

    def addNotes(self, note):
        self.arrayOfNote.append(note)

    def isChord(self):
        return True


# =====FUNCTION MADE FOR LATER REGULAR USE=======

def whatNote(string, fret):
    string_E = ['E', 'F', 'G', 'A', 'B', 'C', 'D']
    string_B = ['B', 'C', 'D', 'E', 'F', 'G', 'A']
    string_G = ['G', 'A', 'B', 'C', 'D', 'E', 'F']
    string_D = ['D', 'E', 'F', 'G', 'A', 'B', 'C']
    string_A = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


def whatOctave(string, fret):
    pass

def isSharp(string, fret):
    pass

def makeNote(string, fret):
    return Note(whatNote(string, fret), whatOctave(string, fret), isSharp(string, fret))

def noteTypeCalculator(arrOfNotes, arrOfPositions, arrOfOneString):
    typeOfNotes = ["128th", "64th", "32nd", "16th", "eighth", "quarter", "half", "whole"]
    for i in range(0, len(arrOfNotes)):
        if arrOfNotes[i].isChord():
            # if arrOfNotes[i][0] type of thing
            pass  # set the duration of all the notes inside the chord
        else:
            # cant measure last one, array index out of bounds error, so hard coded it
            if (i + 1) == len(arrOfNotes):
                if (len(arrOfOneString) - arrOfPositions[i]) / len(arrOfOneString) == 1/8:
                    arrOfNotes[i].typeOfNote = "eighth"
                    print("YEY")
            else:
                if (arrOfPositions[i + 1] - arrOfPositions[i])/len(arrOfOneString) == 1/8:
                    arrOfNotes[i].typeOfNote = "eighth"
                    print("Yey")



def forEachSection(arre, arrb, arrg, arrd, arra, arrE):

    whereTheNotesAre = []
    listOfNotesAndChores = []
    for i in range(0, len(arre)):
        countOfNotesPress = 0
        noteList = []
        if arre[i] != '-':
            if arre[i + 1] != '-':
                # add another if statement for pull and stuff here later
                countOfNotesPress += 1
                noteList.append(makeNote('e', arre[i] + arre[i + 1]))
                whereTheNotesAre.append(i)
            elif arre[i + 1] == '-':
                countOfNotesPress += 1
                noteList.append(makeNote('e', arre[i]))
                whereTheNotesAre.append(i)

        if arrb[i] != '-':
            if arrb[i + 1] != '-':
                countOfNotesPress += 1
                noteList.append(makeNote('e', arrb[i] + arrb[i + 1]))
                whereTheNotesAre.append(i)
            elif arrb[i + 1] == '-':
                countOfNotesPress += 1
                noteList.append(makeNote('e', arrb[i]))
                whereTheNotesAre.append(i)

        if arrg[i] != '-':
            if arrg[i + 1] != '-':
                countOfNotesPress += 1
                noteList.append(makeNote('e', arrg[i] + arrg[i + 1]))
                whereTheNotesAre.append(i)
            elif arrg[i + 1] == '-':
                countOfNotesPress += 1
                noteList.append(makeNote('e', arrg[i]))
                whereTheNotesAre.append(i)

        if arrd[i] != '-':
            if arrd[i + 1] != '-':
                countOfNotesPress += 1
                noteList.append(makeNote('e', arrd[i] + arrd[i + 1]))
                whereTheNotesAre.append(i)
            elif arrd[i + 1] == '-':
                countOfNotesPress += 1
                noteList.append(makeNote('e', arrd[i]))
                whereTheNotesAre.append(i)

        if arra[i] != '-':
            if arra[i + 1] != '-':
                countOfNotesPress += 1
                noteList.append(makeNote('e', arra[i] + arra[i + 1]))
                whereTheNotesAre.append(i)
            elif arra[i + 1] == '-':
                countOfNotesPress += 1
                noteList.append(makeNote('e', arra[i]))
                whereTheNotesAre.append(i)

        if arrE[i] != '-':
            if arrE[i + 1] != '-':
                countOfNotesPress += 1
                noteList.append(makeNote('e', arrE[i] + arrE[i + 1]))
                whereTheNotesAre.append(i)
            elif arrE[i + 1] == '-':
                countOfNotesPress += 1
                noteList.append(makeNote('e', arrE[i]))
                whereTheNotesAre.append(i)

        if countOfNotesPress >= 2:
            tempChord = Chord()
            for note in noteList:
                tempChord.addNotes(note)
                listOfNotesAndChores.append(tempChord)
        elif countOfNotesPress == 1:
            listOfNotesAndChores.append(noteList[0])
        else:
            pass



    # printing out values for myself
    noteTypeCalculator(listOfNotesAndChores, whereTheNotesAre, arre)
    print(whereTheNotesAre)
    print(listOfNotesAndChores)


    # the function that runs the test
forEachSection(arre_test, arrb_test, arrg_test, arrd_test, arra_test, arrE_test)




root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "field1", name="blah").text = "some value1"
ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

tree = ET.ElementTree(root)
tree.write("filename.musicxml")
