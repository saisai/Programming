#!/bin/env python 

"""

Date Created: 7/29/2014
Date Modified: 7/30/2014
"""

import os
import re
import sys
import time
import shutil


class ModelBranches:
	
	l_allBranchDirs = []
	path = ""
	fileABProps = '/var/mobeus/srcache/ABSelector.properties'
	
	def __init__(self, path):
		self.path = path
		
	def verifyPath(self, path):
		"This return true if the path is a directory, false otherwise"
		if os.path.isdir(path) and os.path.islink(path) == False:
			return True
		else:
			return False
	
	def checkABSelectorPropsFile(self):
		"This checks if the A or B folder is being used by checking the ABSelector.properties"
		(filePath, propsFile) = os.path.split(self.fileABProps)
		
		folderLetter=""
		if self.verifyPath(filePath) and os.path.isfile(self.fileABProps):
			fh = open(self.fileABProps, "r")
			
			for line in fh:
				matchObj = re.match(r'^selection=(.*)', line)
				folderLetter = matchObj
				
			if folderLetter:
				fh.close()
				return (True, folderLetter.group(1))
			
			
		else:
			print "\nERROR: folder path ", filePath, " not found"
			print "or file: ", self.fileABProps, " doesn't exist"
			return (False, "")
		
	def getAllDirFromPath(self):
		"This returns all the subdirectories for a given path"
		
		if self.verifyPath(self.path) == False:
			print "\nERROR: ", self.path," is not found."
			sys.exit()
			
		tempDirList = os.listdir(self.path)  # get all the contents in the path

		for dir in tempDirList:
			tempPath = os.path.join(self.path, dir)
			
			if os.path.isdir(tempPath) == 1:
				tempTuple = (tempPath, os.path.getmtime(tempPath))
				self.l_allBranchDirs.append(tempTuple)		# add to main list

		return ModelBranches.l_allBranchDirs
				
	
	def printAllDir(self):
		"This prints all subdirectories for a given path"
		
		print "\nList of Subdirectories:"
		for d in self.l_allBranchDirs:
			print "\t", d[0]
	
	def cleanUpOldBranches(self):
		"This deletes all subdirectories except for two recently created"
		
		(bool, let) = self.checkABSelectorPropsFile()
		
		if bool == True:
			if let == 'A':
				self.path = '/var/mobeus/srcache/A/usr/local/mobeus/models/vlingo/branches/'
				print let ," folder was selected"
			else:
				self.path = '/var/mobeus/srcache/B/usr/local/mobeus/models/vlingo/branches/'
				print let," folder was selected"
		else:
			sys.exit()
			
		tempArr = self.getAllDirFromPath()
		sort_by_date = sorted(tempArr, key=lambda tup: tup[1])		#sort the list by date ascending order.
		
		if len(tempArr) == 0:
			print "\nThere are no subdirectories. Finished."
			sys.exit()
		elif len(tempArr) <= 2:
			print "\nThere are only 2 subdirectories in ", self.path," nothing will be deleted. Finished"
			sys.exit()
		
		self.printAllDir()			# Prints a list of all the subdirectories
		
		print "\nThe following directories will be permanently deleted: "
		for i in range(0, len(sort_by_date)-2):
			print "\t",sort_by_date[i][0], "...Time Stamp: ", time.ctime(sort_by_date[i][1])
			
		proceed = raw_input('Would you like to continue (y/n)? ')
		
		if proceed == 'y' or proceed == 'Y':
			for i in range(0, len(sort_by_date)-2):
			
				try:
					print "removing folder: ", sort_by_date[i][0], "...Time Stamp: ", time.ctime(sort_by_date[i][1])
					shutil.rmtree(sort_by_date[i][0])			# double matrices is the folder path because each element in array is a tuple
				except OSError, e:
					print ("Error: %s - %s." % (e.filename,e.strerror))
					
			print "\nRemaining directories are: \n","\t",sort_by_date[-1][0]
			print "\n","\t",sort_by_date[-2][0]
		else:
			print "Exiting script..."
			sys.exit()
		
		
		
##### MAIN PROGRAM #########
filePath='/var/mobeus/srcache/A/usr/local/mobeus/models/vlingo/branches/'

if filePath != '/var/mobeus/srcache/A/usr/local/mobeus/models/vlingo/branches/':
		print "\nWARNING: Path does not match branch path. Please enter the correct path"
		
		
#choice = raw_input("\nDelete all branch directories except the two latest? (y/n) ")

#if choice == 'y' or choice == 'Y':
models = ModelBranches(filePath)
models.cleanUpOldBranches()
#else:
sys.exit()
	

