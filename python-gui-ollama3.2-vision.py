import requests
import base64
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import json
import io

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        try:
            # Display a "Please wait..." message
            status_label.config(text="Please wait, processing the image...")
            root.update_idletasks()

            # Open the image and resize it
            with Image.open(file_path) as img:
                img = img.resize((400, 400))  # Resize to 400x400 or any desired size
                buffered = io.BytesIO()
                img.save(buffered, format=format_var.get())  # Use selected format
                encoded_image = base64.b64encode(buffered.getvalue()).decode('utf-8')

            # Prepare the payload
            payload = {
                "model": "llama3.2-vision",
                "messages": [
                    {
                        "role": "user",
                        "content": "What is in this image?",
                        "images": [encoded_image]
                    }
                ]
            }

            # Make the POST request to the Ollama API
            response = requests.post("http://localhost:11434/api/chat", json=payload)

            # Split the response into individual JSON objects
            responses = response.text.strip().split('\n')
            combined_response = ""
            for res in responses:
                try:
                    res_json = json.loads(res)
                    combined_response += res_json['message']['content']
                except json.JSONDecodeError:
                    pass
                except KeyError:
                    pass

            # Display the combined response
            display_response(combined_response)

        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            # Clear the status message
            status_label.config(text="")

def display_response(response):
    response_window = tk.Toplevel(root)
    response_window.title("Response")
    response_label = tk.Label(response_window, text=response)
    response_label.pack(pady=20, padx=20)

# Create the main window
root = tk.Tk()
root.title("Image Analyzer")

# Create a dropdown menu for selecting the image format
format_var = tk.StringVar(value="PNG")
format_label = tk.Label(root, text="Select Image Format:")
format_label.pack(pady=5)
format_menu = tk.OptionMenu(root, format_var, "PNG", "JPEG", "BMP", "GIF")
format_menu.pack(pady=5)

# Create a status label
status_label = tk.Label(root, text="")
status_label.pack(pady=5)

# Create a browse button
browse_button = tk.Button(root, text="Browse Image", command=browse_image)
browse_button.pack(pady=20)

# Run the application
root.mainloop()
