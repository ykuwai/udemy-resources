# udemy-ai-bookmarklet
Udemyで1行も書かずにAIでプログラミングを作成する講座です。

## Agent Skills

`skills/` 配下に Claude Code などで使える Agent Skills を収録しています。[npx skills](https://github.com/vercel-labs/skills)（Vercel Labs）でインストールできます。

```bash
# リポジトリ内の全スキルをインストール（Claude Code 向け）
npx skills add ykuwai/udemy-resources -a claude-code
```

- `-a claude-code` を省くと全エージェントが対象になります
- `-g` を付けるとプロジェクトではなくユーザー全体（`~/.claude/skills/`）にインストールされます

### 収録スキル

| スキル | 説明 |
|--------|------|
| [world-recipe-cookbook](skills/world-recipe-cookbook/) | 世界10カ国の郷土料理レシピ集。料理名・国名・材料から検索してレシピを提供する。 |
