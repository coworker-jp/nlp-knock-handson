from typing import List, Tuple


class PreProcessor:
    # テストしやすいように、IOが絡む関数は分離しましょう
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
