# twitter data crawling 
#tweetid から tweet をできるだけ早く集める方法 (72000 tweets / hour)

##環境
MacOS, Linux
python v3.4.3
PHP v2.5.0

##概要
データの配布が　tweetid での配布ということはよくありますが、Twitter のクロールには制限があり、集めるのが面倒であることが多いです。今回は tweetid から tweet を集める方法を紹介します。
使うのは[GET statuses/lookup](https://dev.twitter.com/rest/reference/get/statuses/lookup)という公式で発表されたtweet を 1　リクエストあたり 100 件もってきてくれるやつです。（詳しいことはわかりません）

##クロールには Twitter のアカウントが必要
ご存知の方も多いと思いますがTwitter のクロールにはアカウントが必要になります。更に[Twitter developers](https://dev.twitter.com)にて以下の4つの情報を入手する必要があります。このあたりは説明が転がっていますので各自集めて下さい。

* Consumer Key (API Key) =                                                            
* Consumer Secret (API Secret) =                              
* Access Token = 
* Access Token Secret = 

##コードと使い方
スクリプトを Github にて公開しているので参考にしてください。[Twitter クロールスクリプト](https://github.com/ace12358/twitter/)

必要であれば Github を利用して
    
    git clone https://github.com/ace12358/twitter/
    
で必要なスクリプトを揃えることができるのでご利用下さい。以下では src/ リポジトリの中のコードの使用例です。

次に、tweetid2json.php のスクリプトのに取得した4つの情報を書き加えます。

* Consumer Key =                                                       
* Consumer Secret  =                              
* Access Token = 
* Access Token Secret =

それが完了したら

    php tweetid2json.php 418033807850496002

などとすれば json 形式でクロールが可能になります。ここで

    php tweetid2json.php 418033807850496002 | python json_reader3.4.3.py

で

    418033807850496002  よるほ　あけましておめでとうございますほー
のようなタブ区切りで出力が可能になります。
因みに、418033807850496002のようなtweetid はカンマ区切りで100個までまとめてリクエストすることができます。これらをまとめたシェルスクリプトがあり

    bash make_tweet.sh ../data/tweet_id_list.txt
    
を実行することで 6 秒おきにファイルの1行（tweetid(s)）をよみクロールします。6秒おきなのは制限に引っかからないためです。

*  制限: 180 request / 15 min

以上で説明は以上です。一番効率よく集めるためには
100 個の　tweetid が ',' で連結されたものが1行のファイルを作成し

    bash make_tweet.sh ../data/tweet_id_list.txt
を実行するといいでしょう。

100万tweets くらいのデータを集めるさいは1日程度かかるので
サーバーなどで
などとして放置しておくと良いでしょう。

##参考文献
* [phpのクロールとかの参考](https://syncer.jp/twitter-api-matome/get/statuses/show-id )

##何かあれば
[@Ace12358](https://twitter.com/ace12358/) までどうぞ。すぐに返事ができるかと思います。
