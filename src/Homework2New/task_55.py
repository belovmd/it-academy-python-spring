class Text(object):
    """Class Text

    Should have the next methods:
    write(text) - adds (text) to the current text;
    set_font(font name) - sets the chosen font. Font is applied to the whole
    text, even if it’s added after the font is set. The font is displayed in
    the square brackets before and after the text:
    "[Arial]...example...[Arial]". Font can be specified multiple times but
    only the last variant is displays;
    show() - returns the current text and font (if is was set);
    restore(SavedText.get_version(number)) - restores the text of the
    chosen version.
    """

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
    """Class SavedText
    
    Should have the next methods:
    save_text(Text) - saves the current text and font. The first saved version
    has the number 0, the second - 1, and so on;
    get_version(number) - this method works with the 'restore' method and is
    used for choosing the needed version of the text.
    """

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
