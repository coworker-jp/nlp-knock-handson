class Config:
    @classmethod
    def get_dataset_path(cls):
        return './data/preprocessing/sentiment.txt'

    @classmethod
    def get_stop_words_path(cls):
        return './data/preprocessing/stop_words.txt'
