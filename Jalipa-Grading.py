from flask import Flask, request

app = Flask (__name__)
@app.route('/',methods=['GET','POST'])
def index(): #main function
    result_message = ''
    if request.method =='POST':
        full_name = request.form.get('full_name')
        prelim_grade = request.form.get('prelim_grade')
        
        try:
            prelim_grade = float(prelim_grade) if prelim_grade else None #percentages
            
            t_g = 75
            per_prelim = 0.20
            per_midterm = 0.30
            per_finals = 0.50
            
            if prelim_grade is not None and (prelim_grade < 0 or prelim_grade > 20):
                result_message = "The Grade must be between 0 and 20."
                return home_html(result_message)
            
            elif prelim_grade is not None: #formula and calculation
                required_midterm_grade = (t_g - prelim_grade * per_prelim) * (per_midterm / (per_midterm + per_finals))
                required_final_grade = (t_g - prelim_grade) - required_midterm_grade
                result_message = f"Hello Mr./Ms. {full_name} to pass with a Prelim Grade of {prelim_grade:.2f}, you need:<br>" \
                                 f"- Midterm Grade: {required_midterm_grade:.2f} or higher.<br>" \
                                 f"- Final Grade: {required_final_grade:.2f} or higher."
                                 
        except ValueError:
            result_message = "Error!!! Must use appropriate name or Enter a valid numerice value"
    
    return home_html(result_message)

def home_html(result_message):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, intial-scale=1.0">
        <title>Grade Compution</title>
        <style>
        body {{
            margin: 0;
            padding: 0;
            font-family: Tahoma;
            background: #f0f0f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: #333
        }}           
        
        .container {{
            background: #ffffff;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 30px;
            width: 400px;
            text-align: center;
            max-width: 90%;
        }}
        
        h1 {{
            color: #333;
            font-size: 28px;
            margin-bottom: 20px;
        }}
        
        input[type="text1"], input[type="text"], input[type="submit"] {{
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border-radius: 5px;
            border: 1px solid #ccc;
            font-size: 16px;
            box-sizing: border-box;
            outline: none;
        }}  
        
        input[type="text1"] {{
            background-color: #fafafa;
        }}
        
        input[type="text1"]:focus {{
            border-color: #66b3ff;
            background-color: #ffffff;
        }}
            
        input[type="text"] {{
            background-color: #fafafa;
        }}
        
        input[type="text"]:focus {{
            border-color: #66b3ff;
            background-color: #ffffff;
        }}
        
        input[type="submit"] {{
          background-color: #007bff;
          color: white;
          border: none;
          cursor: pointer;
          font-size: 18px;
          transition: background-color 0.3s ease;  
        }}
        
        inpiut[type="submit"]:hover {{
            background-color: #0056b3
        }}
        
        .result {{
            margin-top: 20px;
            font-size: 18px;
            color: #333;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            background-color: #f9f9f9; 
        }}
        
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Grade Computation</h1>
            <form method="post">
                <input type="text1" name="full_name" placeholder="Enter Full Name">
                <input type="text" name="prelim_grade" placeholder="Enter Prelim Grade 0 - 20">
                <input type="submit" value="Compute">
            </form>
            <div class="result"> {result_message} </div>
        </div>
    </body>
    </html>
    """
    
    
if __name__ == '__main__':
    app.run(debug=True)
    