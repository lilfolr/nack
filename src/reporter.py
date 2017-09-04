from enum import Enum
class Severity(Enum):
     RED = 1
     GREEN = 2
     BLUE = 3

class Report(object):

    def __init__(self):
        self.report_items = []
    
    def add_item(self, severity, title, description, url, other_details)
        self.report_items.append({'severity':severity, 'title':title, 
                                  'desription':description, 'url':url, 
                                  'other_details':other_details })