import responder

class Pityna(object):
    """ ピティナの本体クラス
    """
    def __init__(self, name):
        """ Pitynaオブジェクトの名前をnameに格納。
            Responderオブジェクトを生成してresponderに格納。
            
            Parameters:
                self(object): 呼び出し元のPitynaオブジェクト。
                name(str)   : Ptnaオブジェクトの名前。
                
        """
        # Pitynaオブジェクトの名前をインスタンス変数に代入。
        self.name = name
        # Responderオブジェクトを生成してインスタンス変数に代入。
        self.responder = responder.RandomResponder('Random')

    def dialogue(self, input):
        """ 応答オブジェクトのresponse()を呼び出して応答文字列を取得する。

            Parameters:
                self(object): 呼び出し元のPtnaオブジェクト。
                input(str)  : ユーザーによって入力された文字列。            
            Returns:
                str: 応答文字列。
                
        """
        return self.responder.response(input)

    def get_responder_name(self):
        """ 応答に使用されたオブジェクト名を返す。
        
        Parameters:
            self(object): 呼び出し元のPitynaオブジェクト。       
        Returns:
            str: 応答オブジェクトの名前。
            
        """
        # responderに格納されているオブジェクト名を取得し戻り値にする。
        return self.responder.name

    def get_name(self):
        """ Pitynaオブジェクトの名前を返す。
        
        Parameters:
            self(object): 呼び出し元のPitynaオブジェクト。
        Returns:
            str: このクラスの名前。
            
        """
        # このクラスの名前を取得し戻り値にする。
        return self.name
