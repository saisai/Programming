#!/usr/bin/env python 

"""
Date Created: 8/1/2014
Date Modified: 8/4/2014

Purpose: This script cleans up logs in the specified directory. The user has
the option of entering how many of the most recent logs they would 
like to keep and which WebApp logs they would like to clean up.
"""

import os
import re
import sys
import time
import optparse


class LogCleanUp:

	appName = ""
	logDirectory = '' 	#'/var/log/vlingo/ a list of tuples (log_file, modified_date, web_app)
	l_allLogs = []

	def __init__(self, app, directory):
		self.logDirectory = directory
		self.appName = app
		
	def verifyPath(self, path):
		"This return true if the path is a directory, false otherwise"
		
		if os.path.isdir(path) and os.path.islink(path) == False:
			return True
		else:
			return False
	
	def isWebAppLog(self, fileName):
		matchObj = re.match(r'(.*)_daily.log(.*)',fileName, re.I)
			
		if matchObj:
			return (True, matchObj.group(1))
		else:
			return (False, "none")
			
	def getLogList(self):
		l_temp = os.listdir(self.logDirectory)
		
		for item in l_temp:
			tempPath = os.path.join(self.logDirectory, item)
			
			if os.path.isfile(tempPath) and os.path.islink(tempPath) == False:
				(isWebApp, webApp) = self.isWebAppLog(item)
				
				if isWebApp == True and self.appName == webApp:
					tempTuple = (tempPath, os.path.getmtime(tempPath), webApp)
					self.l_allLogs.append(tempTuple)
					#print tempTuple
				
		return self.l_allLogs
		
	def keepNMostRecentLogs(self, num):
		
		l_logs = self.getLogList()
		size = len(l_logs)
		
		if size == 0:
			print "No logs founds."
			sys.exit()
		elif size <= num:
			print "There are exactly ", size," log(s). Nothing will be deleted."
			sys.exit()	
		elif num <= 0:
			print "Error: -n option cannot be set to zero or less. Must retain at least one log file"
			sys.exit()
		
		l_logs_sorted = sorted(l_logs, key=lambda tup: tup[1])		#sort list by date modified in ascending order.
		
		for i in range(0, len(l_logs_sorted) - num):
			
			try:
				print "Removing %s" % (l_logs_sorted[i][0])
				os.remove(l_logs_sorted[i][0])				#remove file
			except OSError, e:
				print ("Error: %s - %s" % (e.filename, e.strerror))
		
			
########## MAIN PROGRAM ############
logDir = '/var/log/vlingo/' 				

parser = optparse.OptionParser()
parser.add_option('-w', '--webapp', dest='webapp', help='WebApp Name')
parser.add_option('-n', '--num', dest='number', help='Number of most recent logs to keep, set to 30 by default', type=int)

(options, args) = parser.parse_args()

if options.webapp is None:
	print "WebApps List: asr, lmtt, localsearch, vvs, opworker, location, submitter, op, tts, nluservice"
	print "USAGE: sudo ./cleanup_log_files.py -w asr -n 15\n"
	options.webapp = raw_input('Enter WebApp (ex. asr, lmtt): ');
	
	if options.number is None:
		options.number = raw_input('Number of logs to keep: ');
		
elif options.webapp and options.number is None:
	options.number = 30
	
logC = LogCleanUp(options.webapp,logDir)
logC.keepNMostRecentLogs(int(options.number))
