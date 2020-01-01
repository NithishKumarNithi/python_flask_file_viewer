import os,time

class FilesFolders():

    def __init__(self):
        """ initializing user directory """
        self.init_directory = './User'
        self.fol_paths = dict()

    def init_file(self,directory=None):
        """ lists current directory folders with the time of creation """
        directory = self.get_file_or_folder(directory)
        self.ff_list_with_time = []
        
        """
        self.fol_paths = { ffl.name:
                            ( ffl.path ,
                            time.strftime('%x, %I:%M %p',time.localtime((os.path.getctime(ffl.path)))) ) 
                            for ffl in os.scandir(directory) }
        """

        for ffl in os.scandir(directory):

            """ create dictionary with the filepath and time of creation """
            self.fol_paths[ffl.name] = ( ffl.path ,
                            time.strftime('%x, %I:%M %p',time.localtime((os.path.getctime(ffl.path)))) )
                            
            """ create array of current directory data with time """
            if ffl.name in self.fol_paths:
                self.ff_list_with_time.append([ffl.name, self.fol_paths[ffl.name][1]])

        return self.ff_list_with_time      

    def get_file_or_folder(self,folder=None):
        """ returns folder """
        if folder is None: 
            return self.init_directory
        else:
            return folder

    def init_selected_path(self,folder):
        """ route files and folder based on selection """
  
        if self.fol_paths.get(folder):
            selected_ff_path = self.fol_paths.get(folder)[0]
        
            if os.path.isdir(selected_ff_path):
                return selected_ff_path
            
            if os.path.isfile(selected_ff_path):
                return
        else:
            return

        
    
    def folder_path_hierachy(self,folder=None):
        """ folder path hierachy  """

        if self.get_file_or_folder(folder) == self.init_directory or  self.fol_paths.get(folder) == None:
            return ['Home']
        else:   
            if self.fol_paths.get(folder):
                path_arr = self.fol_paths.get(folder)[0][len(self.init_directory):].split('/')
                path_arr[0] = "Home"
                return path_arr    
            

# ff = FilesFolders()
# ff.init_file()
# print(ff.init_file())
# print(ff.fol_paths)
# ff.init_file('../User')
# print(ff.init_file('../User/Files'))
# print(ff.init_file('../User/Files'))
# print(ff.init_selected_path('Notes'))
# ff.init_file(ff.init_selected_path('file_one.txt'))
# print(ff.fol_paths)
# print(ff.folder_path_hierachy('Files'))