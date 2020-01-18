from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

from jp.co.coworker.nlp_knock_handson.ch8.config import Config
from jp.co.coworker.nlp_knock_handson.ch8.preprocessor import PreProcessor


def main():
    # データの読み込み
    texts, Y = PreProcessor.load_dataset(Config.get_dataset_path())

    # ベクトル化
    vectorizer = CountVectorizer(decode_error='ignore')
    X = vectorizer.fit_transform(texts)

    # 学習
    clf = LogisticRegression().fit(X, Y)

    # 予測
    Y_pred = clf.predict(X)

    # 評価
    f1 = f1_score(Y, Y_pred)
    print("F1 score for training data is {}".format(f1))

    return


if __name__ == '__main__':
    main()
