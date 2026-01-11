import tkinter as tk
from tkinter import ttk, messagebox

# -------------------- Functions --------------------
def recommend_dress():
    gender = gender_var.get().strip().lower()
    occasion = occasion_var.get().strip().lower()
    weather = weather_var.get().strip().lower()

    if not gender or not occasion or not weather:
        messagebox.showwarning("Incomplete Selection", "Please select Gender, Occasion, and Weather!")
        return

    suggestions = []

    # Climate-aware suggestions
    if gender == "female":
        if weather == "sunny":
            climate_suggestions = ["Light cotton maxi dress", "Sleeveless jumpsuit", "Shorts & tee"]
        elif weather == "hot":
            climate_suggestions = ["Linen outfits", "Tank top & skirt", "T-shirt & shorts"]
        elif weather == "rainy":
            climate_suggestions = ["Waterproof jacket + leggings", "Midi skirt + rain boots"]
        elif weather == "cold":
            climate_suggestions = ["Knit sweater + coat + boots", "Puffer jacket + scarf"]
        else:
            climate_suggestions = ["Casual wear suitable for all climates"]

        if occasion == "formal":
            suggestions = [item + " (formal)" for item in climate_suggestions]
        elif occasion == "party":
            suggestions = [item + " (party style)" for item in climate_suggestions]
        elif occasion == "wedding":
            suggestions = ["Designer Saree", "Lehenga"]
        else:
            suggestions = climate_suggestions

    elif gender == "male":
        if weather == "sunny":
            climate_suggestions = ["Short-sleeve shirt + chinos", "T-shirt + shorts"]
        elif weather == "hot":
            climate_suggestions = ["Linen shirt + light trousers", "Polo shirt + shorts"]
        elif weather == "rainy":
            climate_suggestions = ["Waterproof jacket + jeans", "Raincoat + chinos"]
        elif weather == "cold":
            climate_suggestions = ["Sweater + jacket + jeans", "Coat + scarf"]
        else:
            climate_suggestions = ["Casual wear suitable for all climates"]

        if occasion == "formal":
            suggestions = [item + " (formal)" for item in climate_suggestions]
        elif occasion == "party":
            suggestions = [item + " (party style)" for item in climate_suggestions]
        elif occasion == "wedding":
            suggestions = ["Sherwani", "Kurta Pajama"]
        else:
            suggestions = climate_suggestions
    else:
        suggestions = ["Standard outfit"]

    display_suggestions(suggestions)


def display_suggestions(suggestions):
    result_label.config(state="normal")
    result_label.delete("1.0", tk.END)
    
    def insert_line(i=0):
        if i < len(suggestions):
            result_label.insert(tk.END, f"{suggestions[i]}\n")
            result_label.after(200, insert_line, i + 1)
        else:
            result_label.config(state="disabled")
    insert_line()


# -------------------- Animation Effects --------------------
def animate_title_color():
    colors = ["#ff6f61", "#ffcc5c", "#88d8b0", "#6a4c93"]
    animate_title_color.index = (animate_title_color.index + 1) % len(colors)
    title.config(bg=colors[animate_title_color.index])
    root.after(500, animate_title_color)
animate_title_color.index = -1


def animate_fashionate_color():
    colors = ["#ff69b4", "#ff1493", "#ff4500", "#ffd700"]
    animate_fashionate_color.index = (animate_fashionate_color.index + 1) % len(colors)
    fashion_label.config(fg=colors[animate_fashionate_color.index])
    root.after(500, animate_fashionate_color)
animate_fashionate_color.index = -1


def button_hover_effect(button, color_on, color_off):
    button.bind("<Enter>", lambda e: button.config(bg=color_on))
    button.bind("<Leave>", lambda e: button.config(bg=color_off))


# -------------------- Main Window --------------------
root = tk.Tk()
root.title("Dress Recommendation App")
root.configure(bg="black")  # Dark background
root.attributes('-fullscreen', True)  # Fullscreen mode
root.bind("<Escape>", lambda e: root.destroy())  # Escape to exit

# Overlay frame (top half)
frame = tk.Frame(root, bg="#1a1a1a", bd=3, relief="ridge")
frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.6)  # top 60% of screen

# Title with animated color
title = tk.Label(frame, text="👗 Dress Recommendation", font=("Helvetica", 24, "bold"), bg="#333333", fg="white")
title.pack(pady=10, fill="x")
animate_title_color()

# Gender
gender_var = tk.StringVar(value="Female")
tk.Label(frame, text="Select Gender:", bg="#1a1a1a", fg="white", font=("Helvetica", 14)).pack(pady=5)
gender_dropdown = ttk.Combobox(frame, textvariable=gender_var, values=["Female", "Male"], state="readonly", font=("Helvetica", 14))
gender_dropdown.pack(pady=5)

# Occasion
occasion_var = tk.StringVar(value="Casual")
tk.Label(frame, text="Select Occasion:", bg="#1a1a1a", fg="white", font=("Helvetica", 14)).pack(pady=5)
occasion_dropdown = ttk.Combobox(frame, textvariable=occasion_var, values=["Casual", "Formal", "Party", "Wedding"], state="readonly", font=("Helvetica", 14))
occasion_dropdown.pack(pady=5)

# Weather
weather_var = tk.StringVar(value="Sunny")
tk.Label(frame, text="Select Weather:", bg="#1a1a1a", fg="white", font=("Helvetica", 14)).pack(pady=5)
weather_dropdown = ttk.Combobox(frame, textvariable=weather_var, values=["Sunny", "Hot", "Rainy", "Cold"], state="readonly", font=("Helvetica", 14))
weather_dropdown.pack(pady=5)

# Suggestion button
recommend_button = tk.Button(frame, text="Get Suggestions", command=recommend_dress, bg="#4CAF50", fg="white", font=("Helvetica", 16))
recommend_button.pack(pady=15)
button_hover_effect(recommend_button, "#45a049", "#4CAF50")

# Result label (scrollable)
result_frame = tk.Frame(frame, bg="#1a1a1a")
result_frame.pack(pady=10, fill="both", expand=True)
result_scroll = tk.Scrollbar(result_frame)
result_scroll.pack(side="right", fill="y")
result_label = tk.Text(result_frame, height=10, bg="#333333", fg="white", wrap="word", yscrollcommand=result_scroll.set, font=("Helvetica", 14))
result_label.pack(fill="both", expand=True)
result_label.config(state="disabled")
result_scroll.config(command=result_label.yview)

# -------------------- BE FASHIONATE Label (Bottom Half) --------------------
fashion_label = tk.Label(root, text="✨ BE FASHIONATE ✨", font=("Helvetica", 48, "bold"), bg="black", fg="#ff69b4")
fashion_label.place(relx=0.5, rely=0.75, anchor="center")  # bottom half
animate_fashionate_color()

root.mainloop()
