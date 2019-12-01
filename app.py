from flask import Flask, render_template , request
from controller.files_controller import FilesFolders     
from controller.file_uploading import FileUpload

app = Flask(__name__)       # initialized app instance

ff = FilesFolders()         # create controller instance
fu = FileUpload()           # create file uploading instance

# routes
@app.route('/')
def main():
    return render_template('base.html')

# file initiation
@app.route('/home/lists')
def list_file_folder():
    file_lists = ff.init_file()
    file_paths = ff.folder_path_hierachy()
    return render_template('loop.html',ff_lists=file_lists,ff_path_lists=file_paths)

# routing between folders and files
@app.route('/<file_folder>')
def directory_list(file_folder):
    folder_select = ff.init_selected_path(file_folder)
    folder_path = ff.folder_path_hierachy(file_folder)
    folder_list = ff.init_file(folder_select)
    return render_template('loop.html',ff_lists=folder_list,ff_path_lists=folder_path)

# @app.route('/upload', methods=['GET','POST'])
# def upload_file():
#     if request.method == 'POST':
#         file = request.file['upload_file']
#         if fu.check_files(file):
#             return "upload"
#         else: 
#             return "file type is not allowed"


# print(ff.folder_exist())

