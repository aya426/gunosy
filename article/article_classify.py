#coding:utf-8
import math
import sys
from collections import defaultdict


class NaiveBayes:

    def __init__(self): #クラスの初期化
        self.categories = set(['エンタメ','スポーツ','おもしろ','国内','海外','コラム','IT・科学','グルメ' ])
        # カテゴリのセット集合
        self.vocabularies = set()  # ボキャブラリのセット集合
        self.wordcount = {}  # wordcount[cat][word] カテゴリでの単語の出現回数
        self.catcount = {}  # catcount[cat] カテゴリの出現回数
        self.bunbo = {}  # bunbo[cat] P(word|cat)の分母の値


    def train(self, data): #ナイーブベイズ分類器の訓練
        # 文書集合からカテゴリを抽出して辞書を初期化
        for d in data:
            cat = d[0]
            self.categories.add(cat)
        for cat in self.categories:#セットのcatという要素について
            self.wordcount[cat] = defaultdict(int) #集計用に初期化
            self.catcount[cat] = 0 #カテゴリの出現回数
        # 文書集合からカテゴリと単語をカウント
        for d in data:
            cat, doc = d[0], d[1:]
            self.catcount[cat] += 1#カテゴリの出現回数 なんのカテゴリかは手動で登録する
            for word in doc:
                self.vocabularies.add(word)
                self.wordcount[cat][word] += 1#カテゴリ内の単語の数


    def word_prob(self, word, cat): #単語の条件付き確率 P(word|cat)を求める
        # ラプラススムージングを適用
        # 単語の条件付き確率の分母の値をあらかじめ一括計算しておく
        for cat in self.categories:
            self.bunbo[cat] = sum(self.wordcount[cat].values()) + len(self.vocabularies)  # catの全単語数
            # カテゴリ内の各単語の出現回数の和 + 単語の種類数(全てのカテゴリで)
        return float(self.wordcount[cat][word] + 1) / float(self.bunbo[cat])


    def score(self, doc, cat): #文書が与えられたときのカテゴリの事後確率の対数 log(P(cat|doc)) を求める
        total = sum(self.catcount.values())  # 総文書数
        score = math.log(float(self.catcount[cat]) / total)  # log P(cat)
        for word in doc:
            # logをとるとかけ算は足し算になる
            score += math.log(self.word_prob(word, cat))  # log P(word|cat)
        return score


    def classify(self, doc):#事後確率の対数 log(P(cat|doc)) がもっとも大きなカテゴリを返す
        best = None
        max_log = -sys.maxsize#初期化
        for cat in self.categories:#全てのカテゴリ
            p = self.score(doc, cat)
            if p > max_log:
                max_log = p
                best = cat
        return best



