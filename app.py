from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_input = request.form['user_input']

    show_link = False  # Default to not show the link

    if user_input.lower() == "exit":
        result = "You chose easy escape. Exiting the loop."
        show_link = True  # Show the link for 'exit'
    else:
        try:
            number = float(user_input)
            if number == 65:
                result = "Excellent work! You've guessed the right number!"
                show_link = True  # Show the link for '65'
            elif number == 69:
                result = "You entered number 69, you fucking creep"
            else:
                result = f"You entered a number {number}, which is wrong"
        except ValueError:
            result = f"You entered a string: {user_input}"

    return render_template('result.html', result=result, show_link=show_link)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port= 5000)

