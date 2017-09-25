<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/action_page.php" method="post">
            Rotate by:<input type="text" name="rot" value="0">
            <input type="textarea" name="text">
            <input type="submit">
        </form>
    </body>
</html>