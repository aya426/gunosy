from .article_classify import NaiveBayes
from .get_data import HtmlScraping

class TrainClassify:

    def __init__(self):
        # エンタメ
        self.url_ent = ['https://gunosy.com/articles/R8hCL',
                    'https://gunosy.com/articles/RPyxa',
                    'https://gunosy.com/articles/aeK7Z']
        #スポーツ
        self.url_sport = ['https://gunosy.com/articles/ae5Ea',
                     'https://gunosy.com/articles/a0S1i',
                     'https://gunosy.com/articles/RfqMJ']
        # おもしろ
        self.url_omo = ['https://gunosy.com/articles/RrHPY',
                   'https://gunosy.com/articles/RnVv2',
                   'https://gunosy.com/articles/R19zZ']
        # 国内
        self.url_local = ['https://gunosy.com/articles/RXdzS',
                          'https://gunosy.com/articles/RnwwL',
                          'https://gunosy.com/articles/Rrz8i']
        # 海外
        self.url_global = ['https://gunosy.com/articles/aRBxa',
                           'https://gunosy.com/articles/afc0c',
                           'https://gunosy.com/articles/a4gYG']
        # コラム
        self.url_col = ['https://gunosy.com/articles/a4xNv',
                        'https://gunosy.com/articles/aCnMS',
                        'https://gunosy.com/articles/aD7hc']
        # IT・科学
        self.url_science = ['https://gunosy.com/articles/RWTuY',
                        'https://gunosy.com/articles/RIs8D',
                        'https://gunosy.com/articles/a7Z1i']
        # グルメ
        self.url_gour = ['https://gunosy.com/articles/RdeTD',
                         'https://gunosy.com/articles/R0dxv',
                         'https://gunosy.com/articles/al15L']


    def test_url(self, url):
        # urlリストから単語リストを取得する
        getString = HtmlScraping()
        word_list = getString.keitaiso(url)

        return word_list


    def catigorize(self):
        # データを取得し、カテゴリを割り当てる
        self.data = []
        length = 0
        #エンタメ
        for i in range(len(self.url_ent)):
            self.data[i] = self.test_url(self.url_ent[i])
            self.data[i].insert(0, 'エンタメ')
        length += len(self.url_ent)
        #スポーツ
        for i in range(len(self.url_sport)):
            self.data.insert(length + i, self.test_url(self.url_sport[i]))
            self.data[length + i].insert(0, 'スポーツ')
        length += len(self.url_sport)
        #おもしろ
        for i in range(len(self.url_omo)):
            self.data.insert(length + i, self.test_url(self.url_omo[i]))
            self.data[length + i].insert(0, 'おもしろ')
        length += len(self.url_omo)
        # 国内
        for i in range(len(self.url_local)):
            self.data.insert(length + i, self.test_url(self.url_local[i]))
            self.data[length + i].insert(0, '国内')
        length += len(self.url_local)
        # 海外
        for i in range(len(self.url_global)):
            self.data.insert(length + i, self.test_url(self.url_global[i]))
            self.data[length + i].insert(0, '海外')
        length += len(self.url_global)
        # コラム
        for i in range(len(self.url_col)):
            self.data.insert(length + i, self.test_url(self.url_col[i]))
            self.data[length + i].insert(0, 'コラム')
        length += len(self.url_col)
        # IT・科学
        for i in range(len(self.url_science)):
            self.data.insert(length + i, self.test_url(self.url_science[i]))
            self.data[length + i].insert(0, 'IT・科学')
        length += len(self.url_science)
        # グルメ
        for i in range(len(self.url_gour)):
            self.data.insert(length + i, self.test_url(self.url_gour[i]))
            self.data[length + i].insert(0, 'グルメ')


    def main(self, url):
        # ナイーブベイズ分類器を訓練
        nb = NaiveBayes()
        nb.train(self.data)

        # テストデータのカテゴリを予測
        test_data = self.test_url(url)
        genre = nb.classify(test_data)

        return genre
