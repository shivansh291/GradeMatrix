import customtkinter as ctk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np

# Set the modern theme and dark/light mode
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

class ModernWeightedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pro Analyzer: Weighted Average")
        self.root.geometry("450x650")
        
        self.df = None
        self.weight_entries = []
        
        # --- Top Section ---
        self.title_lbl = ctk.CTkLabel(root, text="Student Performance Analyzer", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_lbl.pack(pady=(20, 10))
        
        self.upload_btn = ctk.CTkButton(root, text="1. Upload CSV File", command=self.load_csv, font=ctk.CTkFont(size=14))
        self.upload_btn.pack(pady=10)
        
        self.info_lbl = ctk.CTkLabel(root, text="No file loaded yet.", text_color="gray")
        self.info_lbl.pack(pady=(0, 10))
        
        # --- Middle Section (Scrollable Frame for Dynamic Inputs) ---
        # CustomTkinter has a built-in scrollable frame which makes responsiveness very easy!
        self.scroll_frame = ctk.CTkScrollableFrame(root, width=350, height=300, label_text="Assign Test Weights")
        self.scroll_frame.pack(pady=10, fill="both", expand=True, padx=20)
        
        # --- Bottom Section ---
        self.calc_btn = ctk.CTkButton(root, text="2. Calculate & Save", command=self.calculate, font=ctk.CTkFont(size=14), state="disabled", fg_color="green", hover_color="darkgreen")
        self.calc_btn.pack(pady=20)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return
            
        try:
            self.df = pd.read_csv(file_path)
            num_tests = len(self.df.columns) - 1 
            
            self.info_lbl.configure(text=f"Loaded {len(self.df)} students.\nDetected {num_tests} tests.", text_color=("black", "white"))
            
            # Clear old inputs if a new file is loaded
            for widget in self.scroll_frame.winfo_children():
                widget.destroy()
            
            self.weight_entries = []
            
            # Generate inputs dynamically in a 2-column layout
            for i in range(num_tests):
                row_idx = i // 2
                col_idx = (i % 2) * 2
                
                self.scroll_frame.grid_columnconfigure(col_idx, weight=1)
                self.scroll_frame.grid_columnconfigure(col_idx+1, weight=1)
                
                lbl = ctk.CTkLabel(self.scroll_frame, text=f"Test {i+1}:")
                lbl.grid(row=row_idx, column=col_idx, padx=5, pady=10, sticky="e")
                
                ent = ctk.CTkEntry(self.scroll_frame, width=60)
                ent.grid(row=row_idx, column=col_idx + 1, padx=5, pady=10, sticky="w")
                ent.insert(0, "1") # Default weight
                
                self.weight_entries.append(ent)
                
            # Enable calculate button
            self.calc_btn.configure(state="normal")
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not read file.\nDetails: {e}")

    def calculate(self):
        try:
            # Fetch weights
            weights = [float(entry.get()) for entry in self.weight_entries]
            weights_matrix = np.array(weights).reshape(-1, 1)
            total_weight = np.sum(weights_matrix)
            
            if total_weight == 0:
                messagebox.showerror("Error", "Total weight cannot be zero!")
                return
            
            # Matrix Multiplication Logic (A x W)
            marks_matrix = self.df.iloc[:, 1:].values
            weighted_sums = np.dot(marks_matrix, weights_matrix)
            
            # Calculate Averages
            self.df['Simple_Average'] = self.df.iloc[:, 1:].mean(axis=1).round(2)
            self.df['Weighted_Average'] = (weighted_sums / total_weight).round(2)
            
            # Sort to find weakest students easily
            self.df = self.df.sort_values(by='Weighted_Average', ascending=True)
            
            # Save File
            save_path = filedialog.asksaveasfilename(defaultextension=".csv", title="Save Result As", filetypes=[("CSV files", "*.csv")])
            
            if save_path:
                self.df.to_csv(save_path, index=False)
                messagebox.showinfo("Success", f"Results calculated and saved!\nCheck your folder.")
                
        except ValueError:
            messagebox.showerror("Input Error", "Please ensure all weights are numbers.")
        except Exception as e:
            messagebox.showerror("Calculation Error", str(e))

if __name__ == "__main__":
    app_window = ctk.CTk()
    app = ModernWeightedApp(app_window)
    app_window.mainloop()
