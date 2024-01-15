from photo_sqlite import exec

exec('''
/* ファイル情報 */
CREATE TABLE files (
  file_id     INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id     TEXT,
  filename    TEXT,
  album_id    INTEGER DEFAULT 0, /* なし */
  created_at  TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
)
''')
# file_id: ファイルを識別するためのID。データ型はINTEGER PRIMARY KEY
# user_id: ファイルをアップしたユーザーのID。データ型はTEXT
# filename: ファイル名。データ型はTEXT
# album_id: アルバムのID。データ型はINTEGER
# created_at: ファイルがアップされた日時。データ型はTIMESTAMP

exec('''
/* アルバム情報 */
CREATE TABLE albums (
  album_id    INTEGER PRIMARY KEY AUTOINCREMENT,
  name        TEXT,
  user_id     TEXT,
  created_at  TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
)
''')

print('ok')

