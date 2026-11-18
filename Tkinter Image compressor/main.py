import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageCompressorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Image Compressor")
        self.root.geometry("500x600")

        # UI Elements
        self.label = tk.Label(root, text="No image selected", pady=10)
        self.label.pack()

        self.canvas = tk.Label(root) # To display the image
        self.canvas.pack(pady=10)

        self.btn_select = tk.Button(root, text="Select & Compress Image", command=self.process_image)
        self.btn_select.pack(pady=20)

        self.info_label = tk.Label(root, text="", fg="green")
        self.info_label.pack()

    def process_image(self):
        # 1. Select File
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.webp")]
        )
        if not file_path:
            return

        try:
            # 2. Open and Compress
            img = Image.open(file_path)
            
            # Handle PNG Transparency (convert to RGB for JPEG)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # Actual Compression (reduce size by 50% and lower quality)
            w, h = img.size
            img = img.resize((w // 2, h // 2), Image.LANCZOS)
            
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
            if not save_path:
                return
                
            img.save(save_path, "JPEG", quality=70, optimize=True)

            # 3. Display Result in GUI
            # Resize for preview only (so it fits the window)
            preview_img = img.copy()
            preview_img.thumbnail((400, 400)) 
            self.tk_img = ImageTk.PhotoImage(preview_img) # Must keep a reference
            
            self.canvas.config(image=self.tk_img)
            self.label.config(text=f"Showing: {save_path.split('/')[-1]}")
            self.info_label.config(text="Compression Complete!")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to process image: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCompressorGUI(root)
    root.mainloop()
