from janome.tokenizer import Tokenizer
import unicodedata
import re
from bs4 import BeautifulSoup, NavigableString, Declaration, Comment
from urllib.request import Request, urlopen


class HtmlScraping:
#HTMLから文書をスクレイピング

    def __init__(self):
        pass


    def web_scraping(self, url):
    #BeatifulSoupでWebページをスクレイピング
        req = Request(url)
        html = urlopen(req)
        soup = BeautifulSoup(html, "html.parser")

        return soup


    def ensure_unicode(self, v):
    #unicodeにエンコーディング
        if isinstance(v, str):
            v = v.decode('utf8')

        return unicode(v)


    def scraping_url(self, url):
    #URLから文字列を抽出
        soup = self.web_scraping(url)

        if soup and soup != False:
            text = '\n'.join(self.getNavigableStrings(soup))
            main_text = '\n'.join(self.extractMainText(self.utf8Encoder(text)))
            unied_main_text = self.ensure_unicode(main_text)
            output_text = self.normalizeText(unied_main_text)

            return output_text
        else:
            return None


    def getNavigableStrings(self, soup):
    #タグの除去を行い、文字列のみを抽出
        if isinstance(soup, NavigableString):#(オブジェクト、クラス)
            if type(soup) not in (Comment, Declaration) and soup.strip():
                yield soup#一旦停止してreturn

        elif soup.name not in ('script', 'style'):
            for i in soup.contents:
                for j in self.getNavigableStrings(i):
                    yield j


    def nonEmptyLines(self, text):
    #不要な空白を取り除き、空行以外を返す正規化を行う
        for line in text.splitlines():
            line = u''.join(line)
            line = u''.join(line.split('/n'))
            if line:
                yield line


    def normalizeText(self, text):
    #正規化の後で不要な空白・改行を取り除く
        text = unicodedata.normalize('NFKC', text)

        return u'\n'.join(self.nonEmptyLines(text))


    def extractVerb(self, text):
    #文字列に動詞が含まれるかどうかを判定
        t = Tokenizer()
        tokens = t.tokenize(text)

        for token in tokens:
        #品詞を取り出し
            partOfSpeech = token.part_of_speech.split(',')[0]
            if partOfSpeech == u'動詞':
                return True

        return False


    def extractMainText(self, soup):
    #HTMLページの本文を抽出する
        soup_list = soup.split("\n")

        for i in soup_list:
            if self.extractVerb(i) == True:
                yield i
            else:
                continue


    def utf8Encoder(self, text):
    #UTF-8にエンコーディング
        utf8ed_Text = ""
        for i in text:
            utf8ed_Text += i.encode('utf-8')

        return utf8ed_Text


    def extractNoun(self, text):
    #名詞のみを抽出し、辞書にセットする
        t = Tokenizer()
        tokens = t.tokenize(text)
        ma_list = {}

        for token in tokens:
            # 名詞のみを抽出対象とする
            if token.feature.split(',')[0] == "名詞":
                term = token.surface
                # 半角記号を取り除く
                term = re.sub(re.compile('[!-/:-@[-`{-~]'), '', term)

                # 数値のみの文字列を取り除く
                if term.isdigit() == True:
                    continue
                # 空白文字のみの文字列を取り除く
                if term.isspace() == True:
                    continue

                # 辞書にセットする
                ma_list.setdefault(term, 0)
                # TF(Term Frequency)をカウント
                ma_list[term] += 1

        return ma_list


    def keitaiso(self, url):
    #形態素解析の実行
        output_text = self.scraping_url(url)

        if output_text and output_text != None:
            splitted = output_text.split('\n')
            utf8ed_Text = self.utf8Encoder(splitted)
            ma_list = self.extractNoun(utf8ed_Text)
            return ma_list#名詞だけ抽出した状態

        return False



