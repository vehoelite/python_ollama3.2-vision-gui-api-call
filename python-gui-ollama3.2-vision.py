import requests
import base64
import tkinter as tk
from tkinter import filedialog, messagebox
import json

def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        try:
            # Read the image file and encode it in base64
            with open(file_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

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
                except json.JSONDecodeError as e:
                    pass
                except KeyError as e:
                    pass

            # Display the combined response
            display_response(combined_response)

        except Exception as e:
            messagebox.showerror("Error", str(e))

def display_response(response):
    response_window = tk.Toplevel(root)
    response_window.title("Response")
    response_label = tk.Label(response_window, text=response)
    response_label.pack(pady=20, padx=20)

# Create the main window
root = tk.Tk()
root.title("Image Analyzer")

# Create a browse button
browse_button = tk.Button(root, text="Browse Image", command=browse_image)
browse_button.pack(pady=20)

# Run the application
root.mainloop()