import random

class Responder(object): # --------------------------------------------------------①
    """ 応答クラスのスーパークラス
    """
    def __init__(self, name):
        """ Responderオブジェクトの名前をnameに格納
        
        Parameters:
            self(object): 呼び出し元のResponderオブジェクト  
            name(str)   : Responderオブジェクトの名前
        """
        self.name = name

    def response(self, input):
        """ オーバーライドを前提としたresponse()メソッド
        
        Parameters:
            self(object): 呼び出し元のResponderオブジェクト  
            input(str)  : ユーザーが入力した文字列
        Returns:
            str: 応答メッセージ（ただし空の文字列)     
        """
        return '' # -------------------------------------------------------②
    

class RepeatResponder(Responder): # ---------------------------------------③
    """ オウム返しのためのサブクラス
    """
    def response(self, input):
        """ response()をオーバーライド、オウム返しの返答をする

        Parameters:
            self(object): 呼び出し元のResponderオブジェクト  
            input(str): ユーザーが入力した文字列
        Returns:
            str: 応答メッセージ     
        """
        # オウム返しの返答をする
        return '{}ってなに？'.format(input)

class RandomResponder(Responder): # ---------------------------------------④
    """ ランダムな応答のためのサブクラス
    """
    def __init__(self, name):
        """ Responderオブジェクトの名前をnameに格納し、
            ランダムに抽出するメッセージを格納したリストを作成する
        
        Parameters:
            self(object): 呼び出し元のResponderオブジェクト  
            name(str)   : Responderオブジェクトの名前
        """
        # スーパークラスの初期化メソッドを呼んでResponder名をnameに格納
        super().__init__(name) # ------------------------------------------⑤
        # ランダム応答用のメッセージリストを用意
        self.responses = ['いい天気だね', '君はパリピ？', '10円ひろった']

    def response(self, input):
        """ response()をオーバーライド、ランダムな応答を返す

        Parameters:
            self(object): 呼び出し元のResponderオブジェクト  
            input(str)  : ユーザーが入力した文字列
        Returns:
            str: リストからランダムに抽出した文字列
        """
        # リストresponsesからランダムに抽出して戻り値として返す
        return (random.choice(self.responses)) # --------------------------⑥
