import os

class FileUpload():

    def __init__(self):
        """ allowed file type """
        self.allowed_files = ['txt','pdf','docx']

    def check_files(self,filename):
        """ Check if file is allowed file type """
        ext = filename.split('.')
        if ext[len(ext) - 1] in self.allowed_files:
            return True
        else:
            return False


    


# fu = FileUpload()
# print(fu.check_files('my.pdf'))

