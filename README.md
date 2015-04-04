# PyDownloadManager
Simple Download Manager developed using wxPython for GUI and urllib2 for downloading parallely 

You need to have the wxPython module installed for running this application. Place DownloadManager.py and gui.py in the same directory or adjust the import statement if you plan on keep them in separate places.

#BugToFix

The GUI hangs and becomes unresponsive when the download is taking place by the multiple processes, and is resumed only after the downloading task is finished. The GUI, in particular the StatusGauge, also gets updated at the very end of the download. A simple solution using subscriber events or something similar would solve the problem
