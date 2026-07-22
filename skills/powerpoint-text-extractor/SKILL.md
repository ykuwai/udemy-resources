---
name: powerpoint-text-extractor
description: 現在開いているPowerPointプレゼンテーションから全スライドのテキストを抽出する。「PowerPointからテキストを抽出して」「スライドの文字を取り出して」「パワポのテキストを抽出」「PPTの文字起こし」などと指示されたときに使用する。
---

# PowerPoint テキスト抽出スキル

## 概要
現在開いているPowerPointプレゼンテーションからPowerShell COMオブジェクト経由で全スライドのテキストを抽出し、クリップボードにコピーします。

## 使い方
```
/powerpoint-text-extractor
```
または「PowerPointからテキストを抽出して」「スライドの文字を取り出して」と指示してください。

## 前提条件
- PowerPointがインストールされていること
- 対象のプレゼンテーションファイルがPowerPointで**開かれている**こと

## 実行手順

以下のPowerShellスクリプトをBashツールで実行してください：

```bash
powershell.exe -ExecutionPolicy Bypass -Command '
function Extract-TextFromShape {
    param($Shape)
    $text = ""
    try {
        if ($Shape.Type -eq 14) {
            try {
                if ($Shape.PlaceholderFormat.Type -eq 13) { return "" }
            } catch {}
        }
        if ($Shape.HasTextFrame -eq -1) {
            if ($Shape.TextFrame.HasText -eq -1) {
                $text = $Shape.TextFrame.TextRange.Text
                $text = $text -replace [char]11, "`n"
            }
        }
    } catch {}
    return $text
}

try {
    Write-Host "PowerPointに接続中..." -ForegroundColor Cyan
    $powerpoint = New-Object -ComObject PowerPoint.Application
    if ($null -eq $powerpoint) { Write-Error "PowerPointに接続できません"; exit 1 }
    $presentation = $powerpoint.ActivePresentation
    if ($null -eq $presentation) { Write-Error "開いているプレゼンテーションがありません"; exit 1 }
    $presentationName = $presentation.Name
    Write-Host "プレゼンテーション: $presentationName" -ForegroundColor Green
    Write-Host "スライド数: $($presentation.Slides.Count)" -ForegroundColor Green
    $results = @()
    for ($i = 1; $i -le $presentation.Slides.Count; $i++) {
        $slide = $presentation.Slides.Item($i)
        Write-Host "スライド $i を処理中..." -ForegroundColor Yellow
        $results += "--- slide $i ---"
        $slideTexts = @()
        $slideTitle = ""
        foreach ($shape in $slide.Shapes) {
            $isTitle = $false
            if ($shape.Type -eq 14) {
                try {
                    if ($shape.PlaceholderFormat.Type -eq 1) { $isTitle = $true }
                } catch {}
            }
            $text = Extract-TextFromShape -Shape $shape
            if ($text -and $text.Trim() -ne "") {
                if ($isTitle -and $slideTitle -eq "") { $slideTitle = $text.Trim() }
                else { $slideTexts += $text.Trim() }
            }
            try {
                if ($shape.Type -eq 6) {
                    foreach ($groupItem in $shape.GroupItems) {
                        $groupText = Extract-TextFromShape -Shape $groupItem
                        if ($groupText -and $groupText.Trim() -ne "") { $slideTexts += $groupText.Trim() }
                    }
                }
            } catch {}
        }
        if ($slideTitle -ne "") { $results += "## $slideTitle" }
        if ($slideTexts.Count -gt 0) { $results += ($slideTexts -join "`n`n") }
        else { $results += "(テキストなし)" }
        $results += ""
    }
    $output = $results -join "`n"
    $output | Set-Clipboard
    Write-Host ""
    Write-Host "クリップボードにコピーしました！" -ForegroundColor Green
    Write-Host "処理が完了しました！" -ForegroundColor Green
    Write-Output $output
} catch {
    Write-Error "エラーが発生しました: $_"
} finally {
    if ($presentation) { [System.Runtime.InteropServices.Marshal]::ReleaseComObject($presentation) | Out-Null }
    if ($powerpoint) { [System.Runtime.InteropServices.Marshal]::ReleaseComObject($powerpoint) | Out-Null }
    [System.GC]::Collect()
    [System.GC]::WaitForPendingFinalizers()
}
'
```

## 実行後の処理

1. 抽出結果はクリップボードにコピーされると同時に、標準出力に表示されます。
2. ユーザーが保存先ファイルパスを指定した場合は、抽出結果をそのファイルに書き出してください。

## 出力形式
各スライドは以下の形式で出力されます：
```
--- slide 1 ---
## スライドタイトル

本文テキスト

--- slide 2 ---
## スライドタイトル

本文テキスト
```
