---
name: world-recipe-cookbook
description: 世界の料理レシピ集。ユーザーが料理名や国名で郷土料理のレシピを探したいとき、材料・作り方・ポイントを提供する。「○○の作り方」「○○料理のレシピ」「○○（国名）の郷土料理」といったリクエストに対応する。
---

# 世界の郷土料理レシピ集

世界10カ国の代表的な郷土料理100品のレシピを収録。ユーザーの質問から国を特定し、該当する国のリファレンスファイルを読んでレシピを提供する。

## 国別リファレンス

| 国 | 参照ファイル |
|----|-------------|
| 日本 | [references/japan.md](references/japan.md) |
| 中国 | [references/china.md](references/china.md) |
| 韓国 | [references/korea.md](references/korea.md) |
| タイ | [references/thailand.md](references/thailand.md) |
| インド | [references/india.md](references/india.md) |
| イタリア | [references/italy.md](references/italy.md) |
| フランス | [references/france.md](references/france.md) |
| メキシコ | [references/mexico.md](references/mexico.md) |
| ベトナム | [references/vietnam.md](references/vietnam.md) |
| トルコ | [references/turkey.md](references/turkey.md) |

## 材料から検索する

ユーザーが「鶏肉を使った料理」「ナンプラーを使うレシピ」のように材料名で探したい場合、検索スクリプトを実行する。

```bash
python scripts/search_by_ingredient.py <材料名>
```

全10カ国のレシピを横断検索し、該当するレシピ名・国・材料を一覧表示する。

## 使い方

1. ユーザーの質問から料理名・国名・材料名のいずれかを特定する
2. **国名や料理名の場合** → 該当する国の `references/` 内のファイルを読む
3. **材料名の場合** → `scripts/search_by_ingredient.py` を実行して候補を絞り込む
4. 料理名が分かっているがどの国か不明な場合は、各国ファイルの冒頭にある料理一覧から探す
