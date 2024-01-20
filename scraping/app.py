import requests 
from bs4 import BeautifulSoup # beautifulsoup4をインポート

def scrape_orangepage_recipes():  # レシピをスクレイピングする関数を定義
    print("Starting scraping...") # 開始したことを表示
    url = 'https://www.orangepage.net/recipes/search/208' # スクレイピングするURLを指定

    response = requests.get(url) # URLからHTMLを取得
    print(f"Status code: {response.status_code}") # ステータスコードを表示
    if response.status_code != 200: # ステータスコードが200以外の場合
        print('Failed to retrieve the page') #  ページの取得に失敗した場合、エラーメッセージを表示
        return

    soup = BeautifulSoup(response.text, 'html.parser') # parserはHTMLを解析するパーサーを指定


    recipes = [] # レシピを格納するリストを定義
    for recipe_tag in soup.find_all('a', href=True):  # すべての<a>タグを探してイテレート
        title_tag = recipe_tag.find('h2', class_='tit')  
        if title_tag: # 各<a>タグ内の<h2 class="tit">タグを探す
            title = title_tag.text.strip() # タイトルテキストを取得して余白を削除
            link = 'https://www.orangepage.net' + recipe_tag['href']  # 相対リンクを絶対URLに変換
            recipes.append({'title': title, 'link': link})  # タイトルとリンクを辞書としてリストに追加

    if not recipes: # レシピが見つからなかった場合の処理
        print("No recipes found.")
    else:
        for recipe in recipes:# 見つかったレシピを表示
            print(f"Title: {recipe['title']}, Link: {recipe['link']}")

# スクレイピング関数を実行
scrape_orangepage_recipes()
