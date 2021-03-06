# !/usr/bin/env python
# -*- coding: utf-8 -*-
from os import mkdir as pathMkdir
from os.path import exists as pathExists
import sys
import os

menuFileName = "MENU.C"
fileEncoding = 'UTF-8'

# Delets every char that follows a comment in that line
# argv's should look like this:
# commentsDeleter.py -cpp "file 1" "file 2" "ect..."
# NOTE: Currently only language flags are working, also you cant choose directory to save files to

#TODO - auto.

#TODO think on re-naming comments

class Language:
	def __init__(self,name,flag,singleLineComment,multiLineComment,fileExtensions):
		self.name = name
		self.flag = flag
		self.singleLineComment = singleLineComment
		self.multiLineComment = multiLineComment
		self.fileExtensions = fileExtensions

languages = []
languages.append( Language( 'C++',    	'-cpp',    	['//',], [('/*', '*/'),],       ('.cpp', '.h', '.hpp', '.c') ) )
languages.append( Language( 'JAVA',   	'-java',   	['//',], [('/*', '*/'),],       ('') ) )
languages.append( Language( 'Delphi', 	'-delphi', 	['//',], [('{', '}'),],         ('') ) )
languages.append( Language( 'Python', 	'-python', 	['#',],  [('"""', '"""'),],     ('.py') ) )
languages.append( Language( 'Ruby',   	'-ruby',   	['#',],  [('=begin', '=end'),], ('.rb') ) )


flags = ["-auto", # gives a key depending on file extension
         "-all"]  # deletes comments for all the languages


def deleteSingleLineComments(text, singleComment):#TODO Rewrite coz this is veeeery bad solutuion for big files ( calles copy for the whole text for each comment )

	while singleComment in text :
		commentBeginIndex = text.find(singleComment)
		commentEndIndex = text.find('\n',commentBeginIndex)

		# copy  everything except commented text
		if commentEndIndex == -1:
			# this could happen if comment is at the last line of the file and there is no \n ending this line
			text = text[:commentBeginIndex]
		else:
			text = text[:commentBeginIndex] + text[commentEndIndex:]
	return text


def deleteMultiLineComments(text, comment):
	# this is an endless loop with an exit condition
	while True :
		commentBeginIndex = text.find(comment[0])
		commentEndIndex = text.find(comment[1], commentBeginIndex + len(comment[1])) # TODO mb len(comment[0]) needed?
		# copy  everything except commented text
		if (commentBeginIndex != -1) and (commentEndIndex != -1):
			# only if both comments were found
			text = text[:commentBeginIndex] + \
		    	   text[commentEndIndex + len(comment[1]):]
		else:
			#if one of the comments were not found - break the loop
			break
	return text


def deleteSpaceLine(text):
	spaceEndIndex = 0
	textTmp = ""

	while True:
		spaceBeginIndex = spaceEndIndex
		spaceEndIndex = text.find('\n',spaceBeginIndex+1)
		if spaceEndIndex==-1:
			if not text[spaceBeginIndex:].isspace():
				textTmp = textTmp+text[spaceBeginIndex:]
			break
		else:
			if not text[spaceBeginIndex:spaceEndIndex].isspace():
				textTmp = textTmp+text[spaceBeginIndex:spaceEndIndex]

	return textTmp

def deleteComments(text, comments):
	#NOTE: deleting single line comments first we may suddenly delete end of a multiline comment
	newText = text

	for comment in comments[1]:
		#for all multi-line comments
		newText = deleteMultiLineComments(newText, comment)

	for comment in comments[0]:
		#for all single Line Comments
		newText = deleteSingleLineComments(newText, comment)

	newText = deleteSpaceLine(newText)
	return newText


def getTextFromFile(filename):
	fileRelativePath = "./"
	f = open(fileRelativePath+filename, 'r', encoding=fileEncoding)
	text = f.read()
	f.close()
	return text


def saveTextToFile(dirName, filename, text):
	if not os.path.isdir(dirName):
		#if directory does not exist - create it
		os.mkdir(dirName)
	f = open(dirName + "\\" + filename, 'w', encoding=fileEncoding)
	f.write(text)
	f.close()


def getCommentsFromUser():
	print("No flag was specified")
	singleLineComment = input("Input single line comment:")
	multiLineCommentBegin = input("Input begin of multi-line comment:")
	multiLineCommentEnd = input("Input end if multi-line comment:")
	return [[singleLineComment,], [(multiLineCommentBegin, multiLineCommentEnd),]]


def getComments(flag):
	if flag == "":
		# if flag was not specified from console
		return getCommentsFromUser()
	elif flag == "-all":
		singleLineComments = []
		multiLineComments = []
		for language in languages:
			for comment in language.singleLineComment:
				if comment not in singleLineComments:
					singleLineComments.append(comment)
			for comment in language.multiLineComment:
				if comment not in multiLineComments:
					multiLineComments.append(comment)
		return [singleLineComments, multiLineComments]
	else:
		#check if flag is from languages
		for language in languages:
			if flag == language.flag:
				return [language.singleLineComment, language.multiLineComment]

		#if flag is not known
		print("Wrong flag\nKnown flags:")
		for language in languages:
			print ("{0} for {1}".format(language.flag, language.name))
		print("")
		print("-all for all languages together")
		#print("-auto to auto-detect comments from file extension")
		exit(0)


"""def main():
	files = [] # stores files that need to be cleaned
	flag = "" # stores flag passed as an argument
	if len(sys.argv) > 1:
		if (sys.argv[1][0] == '-') and (( len(sys.argv) > 2)):
			#if first argument is a flag AND There are files after the flag
			flag = sys.argv[1]
			files = sys.argv[2:]
		else:
			#flag was not specified
			flag = ""
			files = sys.argv[1:]
	else:
		# if no arguments were passed
		print("Expected: commentsDeleter.py -language 'file 1' 'file 2' 'ect...'")
		exit(0)

	flag = "-cpp"
	files = ["MENU.C"]
	comments = getComments(flag)
	for filename in files:
		text = getTextFromFile(filename)
		newText = deleteComments(text, comments)
		dirName = "withoutComments"
		saveTextToFile(dirName, filename, newText)

if __name__ == '__main__':
	main()"""

def filePreDeal(files=["MENU.C"], flag = "-cpp"):
	comments = getComments(flag)
	dirNames = []
	for filename in files:
		text = getTextFromFile(filename)
		newText = deleteComments(text, comments)
		dirName = "."
		saveFilename = 'tmp'+filename
		saveTextToFile(dirName, saveFilename, newText)
		dirNames.append(saveFilename)
	return dirNames

""" if __name__=="__main__":
	# os.chdir('.\\'+'src')
	fileNames = filePreDeal()
	print(fileNames) """