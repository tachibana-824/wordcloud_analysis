import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import MeCab

# CSVファイルからデータを読み込む関数
def load_csv(file_path, column_name):
    df = pd.read_csv(file_path)
    df_filtered_column = df[column_name].dropna()
    return ' '.join(df_filtered_column.astype(str))

# テキストデータを形態素解析する関数
def tokenize_text(text_data_column):
    tagger = MeCab.Tagger('-Owakati')
    return ' '.join(tagger.parse(text_data_column).split())

# ストップワードを削除する関数
def remove_stopwords(text, stopwords):
    words = text.split(' ')
    filtered_words = [word for word in words if word not in stopwords]
    return ' '.join(filtered_words)

# ワードクラウドを生成・保存する関数
def generate_wordcloud(text, font_path, output_file_path):
    wordcloud = WordCloud(background_color='white',
                          width=800,
                          height=800,
                          min_font_size=10,
                          font_path=font_path,
                          colormap='viridis').generate(text)
    
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)

    # ファイルに保存
    wordcloud.to_file(output_file_path)
    
    plt.show()

# main関数
if __name__ == "__main__":
    # ファイルとフォントのパスを設定
    file_name = 'zeze-after'
    file_path = f'./data/{file_name}.csv'
    font_path = './Noto_Sans_JP/NotoSansJP-VariableFont_wght.ttf'
    
    # 出力ファイルパスとストップワードを設定
    output_file_path = f'./results/{file_name}.png'
    stopwords = ['の', 'も', 'た', 'が', 'は', 'で', 'に', 'と', 'を', 'て', 'に', 'や', 'こと', 'たい', 'つい', 'し', 'です', 'よう', 'か', 'な']
    
    # 利用するカラム名を設定
    column_name = 'Q8. この講義に対するコメントを自由に記載してください(自由記述)'
    
    # CSVからテキストデータを読み込み
    text_data = load_csv(file_path, column_name)
    
    # テキストデータを形態素解析
    tokenized_text = tokenize_text(text_data)
    
    # ストップワードを削除
    filtered_text = remove_stopwords(tokenized_text, stopwords)
    
    # ワードクラウドを生成・保存
    generate_wordcloud(filtered_text, font_path, output_file_path)







