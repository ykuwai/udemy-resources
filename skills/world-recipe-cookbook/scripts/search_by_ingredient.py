#!/usr/bin/env python3
"""
材料からレシピを横断検索するスクリプト

使い方:
    python search_by_ingredient.py <材料名> [--references-dir <パス>]

例:
    python search_by_ingredient.py 鶏肉
    python search_by_ingredient.py ナンプラー
    python search_by_ingredient.py 卵 --references-dir ./references
"""

import argparse
import re
import sys
from pathlib import Path

# 国ファイル名 → 表示名のマッピング
COUNTRY_NAMES = {
    "japan": "日本",
    "china": "中国",
    "korea": "韓国",
    "thailand": "タイ",
    "india": "インド",
    "italy": "イタリア",
    "france": "フランス",
    "mexico": "メキシコ",
    "vietnam": "ベトナム",
    "turkey": "トルコ",
}


def parse_recipes(filepath):
    """mdファイルからレシピ名と材料セクションを抽出する"""
    text = filepath.read_text(encoding="utf-8")
    recipes = []
    # ## で始まるレシピ見出しで分割（「収録レシピ」は除外）
    sections = re.split(r"^## ", text, flags=re.MULTILINE)

    for section in sections:
        lines = section.strip().split("\n")
        if not lines:
            continue
        title = lines[0].strip()
        if title == "収録レシピ" or not title:
            continue

        # 材料セクションを抽出
        ingredients = []
        in_ingredients = False
        for line in lines:
            if re.match(r"^### 材料", line):
                in_ingredients = True
                continue
            if re.match(r"^### ", line):
                in_ingredients = False
                continue
            if in_ingredients and line.startswith("- "):
                ingredients.append(line[2:].strip())

        recipes.append({"title": title, "ingredients": ingredients})

    return recipes


def search(keyword, references_dir):
    """全国のレシピから材料キーワードで検索する"""
    results = []

    for md_file in sorted(references_dir.glob("*.md")):
        country_key = md_file.stem
        country_name = COUNTRY_NAMES.get(country_key, country_key)
        recipes = parse_recipes(md_file)

        for recipe in recipes:
            matched_ingredients = [
                ing for ing in recipe["ingredients"] if keyword in ing
            ]
            if matched_ingredients:
                results.append(
                    {
                        "country": country_name,
                        "recipe": recipe["title"],
                        "matched": matched_ingredients,
                    }
                )

    return results


def main():
    parser = argparse.ArgumentParser(description="材料からレシピを横断検索する")
    parser.add_argument("keyword", help="検索する材料名（例: 鶏肉、ナンプラー、卵）")
    parser.add_argument(
        "--references-dir",
        default=None,
        help="referencesディレクトリのパス（デフォルト: このスクリプトの隣のreferences/）",
    )
    args = parser.parse_args()

    if args.references_dir:
        ref_dir = Path(args.references_dir)
    else:
        ref_dir = Path(__file__).parent.parent / "references"

    if not ref_dir.exists():
        print(f"エラー: referencesディレクトリが見つかりません: {ref_dir}", file=sys.stderr)
        sys.exit(1)

    results = search(args.keyword, ref_dir)

    if not results:
        print(f"「{args.keyword}」を含むレシピは見つかりませんでした。")
        return

    print(f"「{args.keyword}」を含むレシピ: {len(results)}件\n")
    print(f"{'国':<10} {'レシピ名':<20} {'該当する材料'}")
    print("-" * 70)
    for r in results:
        for i, ing in enumerate(r["matched"]):
            if i == 0:
                print(f"{r['country']:<10} {r['recipe']:<20} {ing}")
            else:
                print(f"{'':<10} {'':<20} {ing}")


if __name__ == "__main__":
    main()
