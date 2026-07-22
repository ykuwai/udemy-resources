# udemy-resources

Udemy 講座で使うサンプルコード・教材リソースをまとめたリポジトリです。

講座一覧 → https://www.udemy.com/user/yasuyuki-kuwai/

## Agent Skills

`skills/` 配下に、Claude Code をはじめとする AI エージェント向けの **Agent Skills** を収録しています。

Agent Skills は `SKILL.md`（手順書）と参照ファイル・スクリプトをまとめて「エージェントに知識と手順を与える」仕組みで、[npx skills](https://github.com/vercel-labs/skills)（Vercel Labs）でインストールできます。

### インストール

インストールしたいスキルを `--skill` で指定します。

```bash
# 世界の郷土料理レシピ集
npx skills add ykuwai/udemy-resources --skill world-recipe-cookbook

# PowerPoint テキスト抽出
npx skills add ykuwai/udemy-resources --skill powerpoint-text-extractor
```

指定したスキルが、対応する各エージェントにインストールされます。

- ユーザー全体に入れたいときは `-g`（`~/.claude/skills/` などに配置）
- 特定のエージェントに絞りたいときは `-a <agent>`（例: `-a claude-code`）

### 収録スキル

| スキル | 説明 |
|--------|------|
| [world-recipe-cookbook](skills/world-recipe-cookbook/) | 世界10カ国の郷土料理レシピ集。料理名・国名・材料からレシピを検索して提供する。 |
| [powerpoint-text-extractor](skills/powerpoint-text-extractor/) | 開いている PowerPoint プレゼンから全スライドのテキストを抽出する。 |

## 関連講座

### 🎓 Agent Skills を徹底解説！

Agent Skills の仕組みから実践的な作り方まで、体系的に学べる講座です。

Agent Skills の講座で日本一の受講生を誇ります。

講座で扱うサンプルスキルは、このリポジトリの `skills/` で配布しています。

**[Agent Skillsを徹底解説！ AIエージェントに知識と手順を与えて、思い通りに動かそう！](https://www.udemy.com/course/agent-skills/?referralCode=2DA5EE086D4AE71F2019)**

そのほかの講座は [講師ページ](https://www.udemy.com/user/yasuyuki-kuwai/) からご覧いただけます。
