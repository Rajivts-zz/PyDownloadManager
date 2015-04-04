from multiprocessing.dummy import Pool as ThreadPool
# from multiprocessing import Lock
# from multiprocessing import Semaphore
from urlparse import urlsplit
# from functools import partial
# from time import sleep

import wx
import gui
import urllib2
import time 
import os.path
import sys


class DownloadManager(gui.MainFrame):
     def __init__(self,parent):        
        gui.MainFrame.__init__(self,parent)
        self.parts = {}
        self.file_size_dl = 0
        self.file_name = ""
        self.file_size = 0
        self.block_sz = 8192*4
        self.url = ""
        self.func = None



     def download(self, start):
        try:                    
            req = urllib2.Request(self.url)
            req.headers['Range'] = 'bytes=%s-%s' % (start, (start+self.block_sz-1 if (start+self.block_sz < self.file_size) else self.file_size))
            # print start, (start+block_sz if (start+block_sz < self.file_size) else self.file_size)            
            f = urllib2.urlopen(req)
            self.parts[start] = f.read()    
            self.file_size_dl += len(self.parts[start])
            status = self.file_size_dl * 100. / self.file_size
            status = int(status)            
            # print self.StatusGauge.SetValue(status)                    
            wx.CallAfter(self.StatusGauge.SetValue, status)            
            # self.StatusGauge.SetValue(status)                  
        except KeyboardInterrupt:
            pass
         
     def StartDownload(self, event):
        self.DownloadButton.Enable( False )                
        # url = "http://kaz.dl.sourceforge.net/project/py2exe/py2exe/0.6.9/py2exe-0.6.9.win32-py2.7.exe"
        #url = "https://raw.githubusercontent.com/androguard/androguard/master/androguard/misc.py"
        # url = "http://textfiles.com/100/anonymit"
        # url = "http://norvig.com/big.txt"
        # url = 'http://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=9&ved=0CG0QFjAI&url=http%3A%2F%2Fwww.iasted.org%2Fconferences%2Fformatting%2FPresentations-Tips.ppt&ei=clfWTpjZEIblrAfC8qWXDg&usg=AFQjCNEIgqx6x4ULHFXzzYDzCITuUJOczA&sig2=0VtKXPvoDnIq-lIR4S9LEQ'
        # url =  "http://www.iasted.org/conferences/formatting/Presentations-Tips.ppt"
        self.url = "https://www.python.org/ftp/python/2.7.9/python-2.7.9.msi"
        try:            
            self.url = self.DownloadURL.GetValue()
            dirPath = self.DirectoryValue.GetPath()
            split = urlsplit(self.url)
            self.file_name = split.path[split.path.rfind('/')+1:]
            if not self.file_name:
                self.file_name = split.query[split.query.rfind('/')+1:]
            full_file_name = dirPath + "\\" + self.file_name
            if not os.path.exists(dirPath):
                self.TextForError.SetLabel("  The path provided does not exist, please provide a valid path!\n")
                # self.DownloadButton.enable( True )
                return
            u = urllib2.urlopen(self.url)
            meta = u.info()
            self.file_size = int(meta.getheaders("Content-Length")[0])
            s = "Downloading: %s       Bytes: %s" % (self.file_name, self.file_size)
            self.FileNameText.SetLabel(self.FileNameText.GetLabel() + self.file_name)
            self.DownloadURLText.SetLabel(self.DownloadURLText.GetLabel() + self.url)
            self.StatusText.SetLabel(self.StatusText.GetLabel() + s)            
            start_time = time.time()
            i = 0
            starts = []
            # l = Lock()
            # self.func = partial(self.download, l)
            while self.block_sz * i < self.file_size:
                starts += [i * self.block_sz]
                i += 1
            
            pool = ThreadPool(20)            
            pool.map(self.download, starts)
            # print "Reached here!"
            pool.close()
            pool.join()         
            # print "Reached here!"
            result = ''
            for elem in starts:
                if elem in self.parts:
                    result += self.parts[elem]

            outFile = open(full_file_name, 'wb')
            outFile.write(result)
            outFile.close()
            outTime = float(time.time() - start_time)
            self.ResultText.SetLabel("Download Successful: Time " + str(outTime // 60) + " minutes and " + str(outTime % 60)[:4] + " seconds")
            self.DownloadButton.Enable( True )                


            # self.text.SetValue (str(ans))
        except Exception as e:
            self.TextForError.SetLabel("  Sorry Something went wrong :(\n")
            self.ResultText.SetLabel("  Result: Failed")
            print e
            self.DownloadButton.Enable( True )                   

if __name__ == '__main__':
    app = wx.App(False)
    # lock = Lock()
    # sema = Semaphore(1)
    #create an object of CalcFrame
    frame = DownloadManager(None)
    #show the frame
    frame.Show(True)
    #start the applications
    app.MainLoop()
