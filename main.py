import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

class IcoToPngApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ICO'dan PNG'ye Dönüştürücü")
        
        # Pencere boyutu ayarla (isteğe bağlı)
        self.root.geometry("400x200")
        self.root.resizable(False, False)
        
        # Başlık etiketi
        self.label_title = tk.Label(
            self.root,
            text="ICO'dan PNG'ye Dönüştürme Aracı",
            font=("Arial", 14, "bold")
        )
        self.label_title.pack(pady=10)
        
        # Açıklama etiketi
        self.label_desc = tk.Label(
            self.root,
            text="Dönüştürmek istediğiniz .ICO dosyasını seçiniz."
        )
        self.label_desc.pack()
        
        # Seçim butonu
        self.btn_select = tk.Button(
            self.root,
            text="ICO Dosyası Seç",
            command=self.select_ico_file,
            width=18,
            height=2,
            bg="#4CAF50",
            fg="white"
        )
        self.btn_select.pack(pady=10)
        
        # Durum etiketi
        self.label_status = tk.Label(self.root, text="", fg="blue")
        self.label_status.pack(pady=5)

    def select_ico_file(self):
        ico_file = filedialog.askopenfilename(
            title="Bir ICO dosyası seçin",
            filetypes=[("ICO Dosyası", "*.ico")]
        )
        if not ico_file:
            self.label_status.config(text="Dosya seçilmedi.")
            return
        
        output_folder = os.path.dirname(ico_file)
        base_name = os.path.splitext(os.path.basename(ico_file))[0]
        
        try:
            with Image.open(ico_file) as im:
                # ICO dosyasına ait tüm boyutları getir
                sizes = im.info.get("sizes", [])
                
                if sizes:
                    for s in sizes:
                        with Image.open(ico_file) as im_resized:
                            im_resized.size = s
                            out_path = os.path.join(output_folder, f"{base_name}_{s[0]}x{s[1]}.png")
                            im_resized.save(out_path, "PNG")
                else:
                    w, h = im.size
                    out_path = os.path.join(output_folder, f"{base_name}_{w}x{h}.png")
                    im.save(out_path, "PNG")

            self.label_status.config(text="Dönüştürme başarıyla tamamlandı.", fg="green")
        except Exception as e:
            self.label_status.config(text=f"Hata: {e}", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = IcoToPngApp(root)
    root.mainloop()
