def lambda_handler(event, context):
    html_content = """
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <title>掲示板 投稿フォーム</title>
        <style>
        body {
          font-family: Arial, sans-serif;
          background-color: #f8f9fa;
          margin: 0;
          padding: 20px;
        }
        .container {
          max-width: 600px;
          margin: 0 auto;
          background: #fff;
          padding: 20px;
          box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
          border-radius: 8px;
        }
        .form-group {
          margin-bottom: 15px;
        }
        label {
          display: block;
          margin-bottom: 5px;
          font-weight: bold;
        }
        input[type="text"],
        textarea,
        input[type="file"],
        select {
          width: 100%;
          padding: 10px;
          border: 1px solid #ddd;
          border-radius: 4px;
        }
        button {
          background-color: #007bff;
          color: #fff;
          padding: 10px 15px;
          border: none;
          border-radius: 4px;
          cursor: pointer;
        }
        button:hover {
          background-color: #0056b3;
        }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>掲示板 投稿フォーム</h1>
            <form method="post" action="/write">
                <div class="form-group">
                    <label for="title">タイトル:</label>
                    <input type="text" id="title" name="title" required>
                </div>
                <div class="form-group">
                    <label for="gender">性別:</label>
                    <select id="gender" name="gender" required>
                        <option value="male">男性</option>
                        <option value="female">女性</option>
                        <option value="other">その他</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="content">内容:</label>
                    <textarea id="content" name="content" rows="5" required></textarea>
                </div>
                <button type="submit">投稿する</button>
            </form>
        </div>
    </body>
    </html>
    """
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html',
            'Access-Control-Allow-Origin': '*'
        },
        'body': html_content
    }
