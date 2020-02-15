"""История измения текста.

Нужно реализовать класс TextHistory, который хранит текст и историю его
изменений. Поддерживается три типа изменений — вставка текста (insert),
замена текста (replace) и удаление (delete).

Интерфейс:

h.text — текущий текст, read only

h.version — текущая версия, read only. Начинается с 0 и только растет.

h.insert(text, pos=pos) — вставить текст с позиции pos (по умолчанию — конец
строки). Кидает ValueError, если указана недопустимая позиция. Возвращает
номер новой версии.

h.replace(text, pos=pos) — заменить текст с позиции pos
(по умолчанию — конец строки). Кидает ValueError, если указана недопустимая
позиция. Замена за пределами строки работает как вставка (т. е. текст
дописывается). Возвращает номер новой версии.

h.delete(pos, length) — удаляет length символов начиная с позиции pos.
Возвращает номер новой версии.

h.action(action) — применяет действие action (см. ниже). Возвращает номер
новой версии. Версия растет не на 1, а устанавливается та, которая указана
в action.

h.get_actions(from_version=v1, to_version=v2) — возвращает list всех действий
между двумя версиями.

Действия:
Действия выражаются наследниками Action: InsertAction, ReplaceAction и
DeleteAction. Конструктор принимает позицию (pos) и строку (text) или
позицию и длину (length), а так же стартовую и конечную версию. Если
версии указаны неверно, кидается ValueError. Единственный публичный метод
apply принимает строку и возвращает модифицированную строку.

"""
import unittest


class Action(object):
    def __init__(self, pos, text, from_version, to_version):
        self.pos = pos
        self.text = text
        self.from_version = from_version
        self.to_version = to_version

    @staticmethod
    def _insert(text, text_diff, pos):
        if pos <= len(text):
            return text[0: pos] + str(text_diff) + text[pos:]
        raise ValueError

    @staticmethod
    def _replace(text, text_diff, pos):
        replace_length = len(str(text_diff))
        return text[:pos] + str(text_diff) + text[pos + replace_length:]


class TextHistory(object):
    DEFAULT_VERSION = 0
    BUFFER = dict()
    act_buff = []

    def __init__(self, text=None, version=0):
        self._text = text or ''
        self._version = version
        self.BUFFER[self._version] = self._text

    @property
    def text(self):
        return self._text

    @property
    def version(self):
        return self._version

    def _writing_buffer(self, diff, pos, method):
        self.BUFFER[self._version] = {
            'text': self.text,
            'diff': diff,
            'pos': pos,
            'method': method
        }
        return self.BUFFER

    def _write_act_buff(self, act):
        self.act_buff.append(act)

    def insert(self, diff_text, pos=None):
        if pos is None:
            pos = len(self._text)
        if pos > len(self._text) or pos < 0:
            raise ValueError
        action = InsertAction(pos=pos, text=diff_text,
                              from_version=self.version,
                              to_version=self.update_version())
        self.action(action)
        self._writing_buffer(diff_text, pos, 'insert')
        return self._version

    def replace(self, diff_text, pos=None):
        if pos is None:
            pos = len(self._text)
        if pos > len(self._text) or pos < 0:
            raise ValueError
        action = ReplaceAction(pos=pos, text=diff_text,
                               from_version=self.version,
                               to_version=self.update_version())
        self.action(action)
        self._writing_buffer(diff_text, pos, 'replace')
        return self._version

    def delete(self, pos=None, length=0):
        if pos is None:
            pos = len(self._text)
        if pos > len(self._text) or (
                (pos + length) > len(self._text)) or pos < 0:
            raise ValueError

        action = DeleteAction(pos=pos, length=length,
                              from_version=self.version,
                              to_version=self.update_version())
        self.action(action)
        self._writing_buffer(pos=pos, diff=length, method='delete')
        return self._version

    def update_version(self, to_version=0):
        to_version = to_version or self._version
        if to_version > self._version:
            return to_version
        elif to_version == self._version:
            return to_version + 1
        else:
            raise ValueError
        return self._version

    def action(self, act):
        if act.to_version <= act.from_version:
            raise ValueError

        self._text = act.apply(self.text)
        self._write_act_buff(act)
        self._version = self.update_version(act.to_version)
        return self._version

    def get_actions(self, from_version=0, to_version=None):
        if to_version is None:
            to_version = len(self.act_buff)
        if not (0 <= from_version <= to_version <= len(self.act_buff)):
            raise ValueError
        return self.act_buff[from_version: to_version]


class InsertAction(Action):
    def apply(self, text):
        return self._insert(text, self.text, self.pos)


class ReplaceAction(Action):
    def apply(self, text):
        return self._replace(text, self.text, self.pos)


class DeleteAction(Action):
    def __init__(self, pos, length, from_version, to_version):
        self.pos = pos
        self.length = length
        self.from_version = from_version
        self.to_version = to_version

    @staticmethod
    def _delete(text, length, pos):
        return text[:pos] + text[pos + length:]

    def apply(self, text):
        return self._delete(text, self.length, self.pos)

# tests


class TextHistoryTestCase(unittest.TestCase):
    def test_text__trivial(self):
        h = TextHistory()

        self.assertEqual('', h.text)
        with self.assertRaises(AttributeError):
            h.text = 'NEW'

    def test_version__trivial(self):
        h = TextHistory()

        self.assertEqual(0, h.version)
        with self.assertRaises(AttributeError):
            h.version = 42

    def test_action(self):
        h = TextHistory()
        action = InsertAction(pos=0, text='abc', from_version=0, to_version=10)

        self.assertEqual(10, h.action(action))
        self.assertEqual('abc', h.text)
        self.assertEqual(10, h.version)

    def test_action__bad(self):
        h = TextHistory()
        action = InsertAction(pos=0, text='abc',
                              from_version=10, to_version=10)

        with self.assertRaises(ValueError):
            h.action(action)

    def test_insert(self):
        h = TextHistory()

        self.assertEqual(1, h.insert('abc'))
        self.assertEqual('abc', h.text)
        self.assertEqual(1, h.version)
        print(h.text)

        self.assertEqual(2, h.insert('xyz', pos=2))
        self.assertEqual('abxyzc', h.text)
        self.assertEqual(2, h.version)
        print(h.text)

        self.assertEqual(3, h.insert('END'))
        self.assertEqual('abxyzcEND', h.text)
        self.assertEqual(3, h.version)
        print(h.text)

        self.assertEqual(4, h.insert('BEGIN', pos=0))
        self.assertEqual('BEGINabxyzcEND', h.text)
        self.assertEqual(4, h.version)
        print(h.text)

    def test_insert__bad(self):
        h = TextHistory()
        self.assertEqual(1, h.insert('abc'))

        with self.assertRaises(ValueError):
            h.insert('abc', pos=10)

        with self.assertRaises(ValueError):
            h.insert('abc', pos=-1)

    def test_replace(self):
        h = TextHistory()

        self.assertEqual(1, h.replace('abc'))
        self.assertEqual('abc', h.text)
        self.assertEqual(1, h.version)

        self.assertEqual(2, h.replace('xyz', pos=2))
        self.assertEqual('abxyz', h.text)
        self.assertEqual(2, h.version)

        self.assertEqual(3, h.replace('X', pos=2))
        self.assertEqual('abXyz', h.text)
        self.assertEqual(3, h.version)

        self.assertEqual(4, h.replace('END'))
        self.assertEqual('abXyzEND', h.text)
        self.assertEqual(4, h.version)

    def test_replace__bad(self):
        h = TextHistory()
        self.assertEqual(1, h.insert('abc'))

        with self.assertRaises(ValueError):
            h.replace('abc', pos=10)

        with self.assertRaises(ValueError):
            h.replace('abc', pos=-1)

    def test_delete(self):
        h = TextHistory()
        self.assertEqual(1, h.insert('abc xyz'))

        self.assertEqual(2, h.delete(pos=1, length=2))
        self.assertEqual('a xyz', h.text)
        self.assertEqual(2, h.version)

        self.assertEqual(3, h.delete(pos=3, length=0))
        self.assertEqual('a xyz', h.text)
        self.assertEqual(3, h.version)

    def test_delete__bad(self):
        h = TextHistory()
        self.assertEqual(1, h.insert('abc'))

        with self.assertRaises(ValueError):
            h.delete(pos=10, length=2)

        with self.assertRaises(ValueError):
            h.delete(pos=1, length=3)

        with self.assertRaises(ValueError):
            h.delete(pos=-1, length=2)

    def test_get_actions__bad(self):
        h = TextHistory()
        h.insert('a')
        h.insert('b')
        h.insert('c')

        with self.assertRaises(ValueError):
            h.get_actions(2, 1)
        with self.assertRaises(ValueError):
            h.get_actions(-1, 1)


if __name__ == '__main__':
    unittest.main()
