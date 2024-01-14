import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 5)
        result_label.config(text=f'Your BMI: {bmi:.3f}')
    except ValueError:
        result_label.config(text='Invalid input. Please enter numeric values for weight and height.')

# Create the main window
root = tk.Tk()
root.title('BMI Calculator')

# Create and place widgets in the window
weight_label = tk.Label(root, text='Enter Weight (kg):')
weight_label.pack(pady=20)

weight_entry = tk.Entry(root)
weight_entry.pack(pady=20)

height_label = tk.Label(root, text='Enter Height (m):')
height_label.pack(pady=20)

height_entry = tk.Entry(root)
height_entry.pack(pady=20)

calculate_button = tk.Button(root, text='Calculate BMI', command=calculate_bmi)
calculate_button.pack(pady=20)

result_label = tk.Label(root, text='')
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
