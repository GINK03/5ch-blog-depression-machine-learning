
# 精神的異常と使用するボキャブラリの差  

## 参考にした研究  
Gigazineさんでやっていた、うつ病の人が利用しがちなボキャブラリというネタでやっていらっしゃいました  
  
[機械学習を使った調査で「うつ」病の人がよく使いがちな言葉が判明](https://gigazine.net/news/20180209-depression-use-language/)  

結果として以下のことがわかっているようです  

- 代名詞として自分のことを指す文言がたくさん出てくる  
- 「常に」「何もない」「完全に」など、絶対的な大きさや確率を表現する「絶対主義的な言葉」  

理解ではできますが、本当にそのようになりますでしょうか　　

追試やコーパスの差を利用して集計したいと思います。　　

## 使用するコーパス 
1. 5chのメンヘラ版をpositiveのデータセットとして定義し、その他の板をnegativeのデータセットと定義します
2. Amebloのメンヘラブログ村に登録されているユーザさんのコーパスをpositiveとして、その他のユーザさんのコーパスをnegativeとします

その際に、BoW(Bag of Words)を作成し、名詞での比較、代名詞での比較、絶対的な言葉での比較を行っていきたいと思います  

**http://mevius.5ch.net/** から2018/2/11にスクレイピングできる内容全量としました。  

## 使用するアルゴリズム
シングルクラスSVMをsigmoidで２値判定かけてたときの重みとする  

## 5chですべての単語で分類する場合  
<p align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/36071983-15c10dea-0f5b-11e8-8225-f8e8d82d08bf.png"> 
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/36071997-44ac0164-0f5b-11e8-8487-0ac085257bcb.png"> 
</p>

5chのベースとなる差別主義的な単語が目立ちますね  

メンヘラ板で特有な単語は、オノマトペや、風俗などが目立ちます  

## Amebloですべての単語で分離する場合
<p align="center">
  <img width="200px" src="https://user-images.githubusercontent.com/4949982/36337929-971aabce-13e5-11e8-9ca2-b6afbf31c899.png"> 
</p>
コーパスのカバレッジの影響で、ブログの投稿日時が影響していますが、具体的な病気や、痛みに弱いとか、頭痛持ちとか有り得そうです  

## Amebloで代名詞を用いて分離する場合

セルフリフレクションが多いほど、メンタルに対する病理のリスクが高いととも読める文章でしたが、自己に関する論述の根拠として「私」や「自分」を意味する単語の多さがありそうです。  
<p align="center">
  <img width="300px" src="https://user-images.githubusercontent.com/4949982/36338121-2166a270-13ea-11e8-95ba-c0aca9ed7896.png"> 
</p>

微妙な結果になってしまいました。  
メンヘラブログを利用しない人は、自分のことをオイラとかいうようです... 

### アドホック1. 「私」、「わたし」、「おいら」などをまとめてself-reflectにして処理する  
特徴が見えにくいので、いくつか処理を追加します  

具体的にはL1正則化で情報が落ちなかった、「わたし」,「私」,「オイラ」,「おいら」,「あたしゃ」,「わい」,「俺」,「オレ」,「わたくし」,「あたい」,「われ」,「あたし」をself-reflectionという一つの特徴量に変換すると、このような正の重みが得られる  

|feat|weight|
|--:|--:|
| self-reflect | 0.03038147026214874 |

とても大きな値ではではないですが、やはり自己に関する論述が多いほど、メンタルヘルスのコーパスに該当しそうです  

## 絶対主義的言葉の定義
次に、絶対主義的言葉を定義します  

もとの、[People with depression are more likely to say certain words](https://qz.com/1198671/depression-warning-signs-pay-attention-to-the-words-they-use/)によると、このような言葉が絶対主義的な言葉として定義されています  

<p align="center">
  <img width="400px" src="https://user-images.githubusercontent.com/4949982/36338527-d51d80e0-13f4-11e8-9a02-e93738dfa0eb.png">
</p>

