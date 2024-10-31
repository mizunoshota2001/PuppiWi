## 前提条件

- **Git** がインストールされていること。
- GitHub のリポジトリにアクセスするための適切な権限とアクセストークンがあること。
- Windows 環境での実行を想定しています。

## ダウンロード for Windows

- PowerShell で実行してください。

```ps
git clone https://github.com/mizunoshota2001/wintools-bat.git wintools
```

- .git 削除版

```ps
git clone https://github.com/mizunoshota2001/wintools-bat.git wintools ; cd wintools ; rm -r -fo .git
```

## 環境変数の設定

バッチファイル内で使用される環境変数は以下の通りです。これらの変数を適切に設定する必要があります。

| 変数名         | 説明                                                    | 必須 |
| -------------- | ------------------------------------------------------- | ---- |
| `USER`         | SSH 接続におけるユーザー名。                            | 任意 |
| `HOST`         | SSH 接続におけるホスト名。                              | 任意 |
| `SSH_KEY_PATH` | SSH キーのパス。                                        | 任意 |
| `CLONE_TOKEN`  | GitHub リポジトリにアクセスするためのアクセストークン。 | 必須 |

**設定例:**

```bat
set USER=your_username
set HOST=github.com
set SSH_KEY_PATH=C:\Users\YourUser\.ssh\id_rsa
set CLONE_TOKEN=your_access_token
```

## スクリプトの詳細

以下はスクリプトの各部分の説明です。

```bat
@echo off
```

- コマンド実行時にコマンド自体を表示しないようにします。

```bat
set USER=
set HOST=
set SSH_KEY_PATH=
set CLONE_TOKEN=
```

- 必要な環境変数を初期化します。ユーザーはこれらの変数に適切な値を設定する必要があります。

```bat
set clone="git clone https://%CLONE_TOKEN%@github.com/.../....git .tmp"
```

- GitHub リポジトリを `.tmp` フォルダにクローンするためのコマンドを設定します。`%CLONE_TOKEN%` を使用して認証を行います。
- `https://%CLONE_TOKEN%@github.com/.../....git` の部分は、実際のリポジトリ URL に置き換えてください。

```bat
set sparse="cd ~ && %clone% && cp -a .tmp/.../* . && rm -rf .tmp"
```

- ホームディレクトリに移動し、クローンコマンドを実行します。
- クローンした `.tmp` フォルダ内の特定のディレクトリ（`...` 部分）から現在のディレクトリにファイルをコピーします。
- コピー後、クローンに使用した `.tmp` フォルダを削除します。

## 例

以下は、具体的な設定例です。

```bat
@echo off
set USER=johndoe
set HOST=github.com
set SSH_KEY_PATH=C:\Users\johndoe\.ssh\id_rsa
set CLONE_TOKEN=ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

set clone="git clone https://%CLONE_TOKEN%@github.com/johndoe/my-repo.git .tmp"
set sparse="cd ~ && %clone% && cp -a .tmp\src\* . && rm -rf .tmp"
```

この例では、`johndoe` ユーザーの `my-repo` リポジトリを `.tmp` フォルダにクローンし、`src` ディレクトリ内のファイルをホームディレクトリにコピーした後、`.tmp` フォルダを削除します。
