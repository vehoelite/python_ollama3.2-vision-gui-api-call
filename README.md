This is my first script made by Python which displays a gui featuring a
browse button to select a image, then resizes the image, sends it to the Ollama REST API
for processing. After awhile, a window will appear with accurate details of the image you submit. 
It's very simple but useful for testing Ollama3.2-Vision capabilities. Be careful with resize,
it's a godsend depending on hardware but to small you could end up with much less details on output.

**Setup LLM**
https://github.com/ollama/ollama

**Pull llama3.2-vision at command prompt:**
   ```sh
ollama pull llama3.2-vision
ollama run llama3.2-vision
   ```

1. **Create a virtual environment:**
   ```sh
   python3 -m venv myenv
   ```

2. **Activate the virtual environment:**
   - On Linux or macOS:
     ```sh
     source myenv/bin/activate
     ```
   - On Windows:
     ```sh
     myenv\Scripts\activate
     ```

3. **Install the packages:**

   ```sh
   pip install ollama
   pip install requests
   pip install Pillow
   ```

4. **Run the script:**
   ```sh
   python python_ollama3.2-vision_call.py
   ```
