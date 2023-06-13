class Note(object):
    def __init__(self, contents = None):
        self.contents = contents

    def write_contents(self, contents):
        self.contents = contents

    def get_number_of_lines(self):
        return self.contents.count("\n")

    def get_number_of_characters(self):
        return len(self.contents)

    def remove(self):
        self.contents = "삭제된 노트입니다."

    def __str__(self):
        return self.contents



class NoteBook(object):
    def __init__(self, title):
        self.title = title
        self.pages = 0
        self.notes = {}

    def add_note(self, note, page_number=-1):
        if len(self.notes.keys()) < 300:
            if page_number == -1:
                if self.pages < 301:
                    self.notes[self.pages] = note
                    self.pages += 1
                else:
                    for i in range(300):
                        if i not in list(self.notes.keys()):
                            self.notes[self.pages] = note
            else:
                if page_number not in self.notes.keys():
                    self.notes[page_number] = note
                else:
                    print(f"{page_number}페이지에는 이미 노트가 존재합니다.")
        else:
            print("더 이상 노트를 추가하지 못합니다.")

    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            del self.notes[page_number]
            print(f"{page_number} 페이지를 삭제하였습니다.")
        else:
            print(f"{page_number} 페이지가 없어서 삭제할 수 없습니다.")

    def print_all(self):
        for k, v in dict(sorted(self.notes.items(), key=lambda t:t[0])).items():
            print(f'페이지 {k} : {v}')

    def get_number_of_all_lines(self):
        result = 0
        for k in self.notes.keys():
            result += self.notes[k].get_number_of_lines()
        return result

    def get_number_of_all_characters(self):
        result = 0
        for k in self.notes.keys():
            result += self.notes[k].get_number_of_characters()
        return result

    def get_number_of_all_pages(self):
        return len(self.notes.keys())

    def __str__(self):
        return f'{self.title} (총 {self.get_number_of_all_pages()} 페이지)'
