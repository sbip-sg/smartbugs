YES = "<yes>"
NO = "<no>"
REPORT = "<report>"
COMMENT = "//"

class BugLabel:
    def __init__(self, filename, line_number, bug_category):
        self.filename = filename
        self.line_number = line_number
        self.bug_category = bug_category

def read_bug_label(filename):
    '''Read bug labels from source code'''
    bug_labels = []
    with open(filename, 'r') as file:
        for (index, line) in enumerate(file.readlines()):
            line_number = index + 1
            line = line.strip()
            if line.startswith(COMMENT) and YES in line and REPORT in line:
                bug_category = line.replace(COMMENT, '')
                bug_category = bug_category.replace(YES, '')
                bug_category = bug_category.replace(REPORT, '')
                bug_category = bug_category.strip()
                bug_label = BugLabel(filename, line_number, bug_category)
                bug_labels.append(bug_label)
    return bug_labels
