from typing import Dict, List, Tuple
from jp.co.coworker.nlp_knock_handson.ch8.config import Config


class PreProcessor:
    def __init__(self):
        stop_words_path = Config.get_stop_words_path()
        self.stop_words_dict = self.read_stop_words_dict(stop_words_path)

    @classmethod
    def read_stop_words_dict(cls, stop_words_path) -> Dict[str, bool]:
        stop_words_dict = {}

        with open(stop_words_path, 'r') as f:
            for line in f:
                line = line.rstrip()
                stop_words_dict[line] = True

        return stop_words_dict

    def get_stop_words(self) -> List[str]:
        return list(self.stop_words_dict.keys())

    def is_stop_word(self, word:str) -> bool:
        return word in self.stop_words_dict

    @classmethod
    def load_dataset(cls, path: str) -> Tuple[List[str], List[int]]:
        with open(path, 'r', errors='ignore') as f:
            lines = [line.rstrip() for line in f.readlines()]

        return cls.read_dataset(lines)

    @classmethod
    def read_dataset(cls, input_lines: List[str]) -> Tuple[List[str], List[int]]:
        texts = []
        labels = []

        for line in input_lines:
            lst = line.split(' ')
            label = int(lst[0])
            text = ' '.join(lst[1:])

            labels.append(label)
            texts.append(text)

        return texts, labels
