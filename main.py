## python script for course module.
class CourseModule:
    def __init__(self, title, content):
        self.__title = title # hidden/ private attributes for the title
        self.__content = content # hidden / private attributes for content 
        self.__completion_status = False # this confirms if the entry or action is complete
        
        
    def get_title(self):
        return self.__title
    
    def get_content(self):
        return self.__content
    
    def get_completion_status(self):
        return self.__completion_status
    
    def get_update_progress(self, completed):
        if isinstance(completed, bool):
            self.__completion_status = completed
        else:
            raise ValueError("Completion status must be either True or False")
        
    def mark_completed(self):
        self.__completion_status = True
        
    def mark_incompleted(self):
        self.__incompletion_status = False
        
        
## usage instance
module = CourseModule("Introduction to Machine Learning","Learn about Ai and how to write automation")
print(module.get_title())
print(module.get_completion_status())
module.get_update_progress(True)
print(module.get_completion_status())        