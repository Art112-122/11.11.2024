import sqlite3

from flask import Flask, render_template, request

import sql_oderman_database
app = Flask(__name__)






menu_positions = sql_oderman_database.select_query_func()









@app.get("/")
def start():
    return render_template("start_page.html", link="http://127.0.0.1:5001/menu/", action=True,
                           action_title="Пепероні",
                           action_text="Вершковий соус, сир Моцарелла, салямі пікантна, томат Чері, перець пепероні, пармезан, базилік",

                           action_last_cost="199 грн",
                           action_new_cost="169 грн",
                           action_image="data:image/jpeg;base64,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"
                           )




@app.get(f"/admin/")
def admin_page():
    return render_template("admin_page.html", menu=menu_positions, message=False)


@app.post(f"/admin/")
def menu_add():
  try:
    url = request.form["image"]
    name = request.form["name"]
    description = request.form["description"]
    price = request.form["price"]
    nums = "1234567890"
    for number in nums:
        if number in name:
            return render_template("error_page.html", error="У назві не можуть бути цифри")

    for num in price:
        if num.isalpha():
            return render_template("error_page.html", error="У ціні не можуть бути букви")

    sql_oderman_database.insert_query_func(url, name, description, price)

    return render_template("admin_page.html", menu=menu_positions, message=True)

  except sqlite3.Error():
      return render_template("error_page.html", error="Невідома помилка, перевірте чи немає такої піци вже")

@app.get("/menu/")
def menu():
    return render_template("menu_page.html",
                           menu=menu_positions,

                           action_title="Пепероні",
                           action_last_cost="1̶9̶9̶ грн",
                           action_new_cost="169грн"
                           )





@app.get("/comments/")
def comments():
    return render_template("comments_page.html", comments_len=0, comments_start=0)




@app.errorhandler(404)
def error(error):
    return render_template("not_found_page.html")

if __name__ == "__main__":
    sql_oderman_database.start_conetion_db()

    app.run(port=5001, debug=True)
    #ТУТ ДОЛЖЕН БЫТЬ ЗАПУСК СКЛ