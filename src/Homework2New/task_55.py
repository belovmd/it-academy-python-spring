class Text(object):

    def __init__(self):
        self.text = ''
        self.font = ''

    def write(self, text=''):
        self.text += text

    def set_font(self, font=''):
        if font:
            self.font = font

    def show(self):
        if self.font:
            return f'[{self.font}]{self.text}[{self.font}]'
        return f'{self.text}'

    def restore(self, text_memory_object):
        self.text, self.font = (
            text_memory_object['text'], text_memory_object['font'])


class SavedText(object):

    def __init__(self):
        self.versions_of_text = []

    def save_text(self, text_object):
        self.versions_of_text.append(
            {'text': text_object.text, 'font': text_object.font})
        if len(self.versions_of_text) > 10:
            self.versions_of_text.pop(0)

    def get_version(self, number):
        return self.versions_of_text[number]


text = Text()
saver = SavedText()

text.write("At the very beginning ")
print(text.show())
saver.save_text(text)
text.set_font("Arial")
print(text.show())
saver.save_text(text)
text.write("there was nothing.")
print(text.show())
assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
print(saver.versions_of_text)
text.restore(saver.get_version(0))
print(text.show())
assert text.show() == "At the very beginning "
