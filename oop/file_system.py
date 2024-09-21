class File:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.data = ""
    
    #Changes data in file to new_text
    def edit_data(self, new_text):
        self.data = new_text

class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.content_list = []
    
    #Add new empty file to folder
    def add_new_file(self, name):
        for content in self.content_list:
            if content.name is name:
                return "Name already in use."
        new_file = File(name)
        self.content_list.append(new_file) 
        return

    #Add new empty folder to folder
    def add_new_folder(self, name):
        for content in self.content_list:
            if content.name is name:
                return "Name already in use."
        new_folder = Folder(name)
        self.content_list.append(new_folder) 
        return
    
    #move a file or folder to another folder
    def move(self, content, destination):
        if content not in self.content_list:
            return "Content not found."
        else:
            destination.content_list.append(self.content_list.pop(file))
            content.parent = destination
    
class File_System:
    def __init__(self):
        self.content_list = []

        self.content_list.append(Folder("downloads"))
        self.content_list.append(Folder("pictures"))
        self.content_list.append(Folder("user"))
        
        self.current_directory = self

    #add new empty file or folder
    def add_new_content(self, filetype, name):
        for content in self.content_list:
            if content.name is name:
                return "Name already in use."
        if type(filetype) is File:
            new_file = File(name)
            self.content_list.append(new_file, self)
        else:
            new_folder = Folder(name)
            self.content_list.append(new_folder, self) 
        return

    #add new empty file or folder inside a specific folder
    def add_new_in_folder(self, filetype, name, parent_folder):
        for content in parent_folder.content_list:
            if content.name is name:
                return "Name already in use."
        if type(filetype) is File:
            parent_folder.add_new_file(name, parent_folder)
        else:
            parent_folder.add_new_folder(name, parent_folder)
        return

    #changes the directory user is currently in
    def change_directory(self, destination):
        if destination is None:
            return "Directory not found."
        
        self.current_directory = destination
        return self.current_directory

    #moves file or directory to another directory
    def move(self, content, destination):
        if content not in self.current_directory.content_list:
            return "Content not found."
        if destination is None:
            return "Directory not found."
        destination.content_list.append(self.content_list.pop(content))
        content.parent = destination