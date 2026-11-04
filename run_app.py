"""
Library Membership Application - macOS Native Desktop Runner
This script mirrors the exact C# Windows Forms logic and layout for testing on macOS.
"""
import tkinter as tk
from tkinter import messagebox

class LibraryMembershipApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Membership Application (macOS Runner)")
        self.root.geometry("700x520")
        self.root.resizable(False, False)

        # Header Title
        header = tk.Label(
            root,
            text="Library Membership Application",
            font=("Segoe UI", 14, "bold"),
            bg="#3b6998",
            fg="white",
            pady=10
        )
        header.pack(fill=tk.X)

        main_frame = tk.Frame(root, padx=25, pady=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # 1. Inputs Section
        inputs_frame = tk.Frame(main_frame)
        inputs_frame.pack(fill=tk.X, pady=(0, 10))

        # Member Name
        tk.Label(inputs_frame, text="Member Name:", font=("Segoe UI", 10), width=22, anchor="w").grid(row=0, column=0, pady=4, sticky="w")
        self.txtMemberName = tk.Entry(inputs_frame, font=("Segoe UI", 10), width=30)
        self.txtMemberName.grid(row=0, column=1, pady=4, sticky="w")

        # Membership Number
        tk.Label(inputs_frame, text="Membership Number:", font=("Segoe UI", 10), width=22, anchor="w").grid(row=1, column=0, pady=4, sticky="w")
        self.txtMembershipNumber = tk.Entry(inputs_frame, font=("Segoe UI", 10), width=30)
        self.txtMembershipNumber.grid(row=1, column=1, pady=4, sticky="w")

        # Mobile Number
        tk.Label(inputs_frame, text="Mobile Number (10 digits):", font=("Segoe UI", 10), width=22, anchor="w").grid(row=2, column=0, pady=4, sticky="w")
        self.txtMobileNumber = tk.Entry(inputs_frame, font=("Segoe UI", 10), width=30)
        self.txtMobileNumber.grid(row=2, column=1, pady=4, sticky="w")

        # 2. Books Section
        books_frame = tk.Frame(main_frame)
        books_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Available Books
        col1 = tk.Frame(books_frame)
        col1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Label(col1, text="Available Books:", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        self.lstAvailableBooks = tk.Listbox(col1, font=("Segoe UI", 9), height=10, selectmode=tk.SINGLE, exportselection=False)
        self.lstAvailableBooks.pack(fill=tk.BOTH, expand=True)

        # Add / Remove Buttons
        btn_col = tk.Frame(books_frame, padx=15)
        btn_col.pack(side=tk.LEFT, fill=tk.Y, pady=25)
        self.btnAdd = tk.Button(btn_col, text="Add >>", font=("Segoe UI", 9, "bold"), width=10, command=self.btn_add_click)
        self.btnAdd.pack(pady=6)
        self.btnRemove = tk.Button(btn_col, text="<< Remove", font=("Segoe UI", 9, "bold"), width=10, command=self.btn_remove_click)
        self.btnRemove.pack(pady=6)

        # Selected Books
        col2 = tk.Frame(books_frame)
        col2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Label(col2, text="Selected Books:", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        self.lstSelectedBooks = tk.Listbox(col2, font=("Segoe UI", 9), height=10, selectmode=tk.SINGLE, exportselection=False)
        self.lstSelectedBooks.pack(fill=tk.BOTH, expand=True)

        # Count Label
        self.lblBookCount = tk.Label(col2, text="Selected Books: 0 / 3", font=("Segoe UI", 10, "bold"), fg="#003366")
        self.lblBookCount.pack(anchor="w", pady=(5, 0))

        # 3. Action Buttons (Submit & Clear)
        action_frame = tk.Frame(main_frame)
        action_frame.pack(pady=15)
        self.btnSubmit = tk.Button(action_frame, text="Submit", font=("Segoe UI", 10, "bold"), bg="#2e7d32", fg="black", padx=20, pady=5, command=self.btn_submit_click)
        self.btnSubmit.pack(side=tk.LEFT, padx=10)
        self.btnClear = tk.Button(action_frame, text="Clear", font=("Segoe UI", 10, "bold"), bg="#c62828", fg="black", padx=20, pady=5, command=self.btn_clear_click)
        self.btnClear.pack(side=tk.LEFT, padx=10)

        # Populate Available Books (Form1_Load)
        self.form_load()

    def form_load(self):
        books = [
            "C Programming",
            "C++ Programming",
            "Java",
            "Python",
            "Data Structures",
            "Database Management System",
            "Operating System",
            "Computer Networks",
            "Web Development",
            "Artificial Intelligence"
        ]
        for b in books:
            self.lstAvailableBooks.insert(tk.END, b)
        self.update_book_count()

    def update_book_count(self):
        count = self.lstSelectedBooks.size()
        self.lblBookCount.config(text=f"Selected Books: {count} / 3")

    def is_valid_member_name(self, name):
        if not name or not name.strip():
            return False
        has_letter = False
        for c in name:
            if c.isalpha():
                has_letter = True
            elif not c.isspace():
                return False
        return has_letter

    def is_valid_membership_number(self, num):
        if not num or not num.strip():
            return False
        return num.strip().isdigit()

    def is_valid_mobile_number(self, mobile):
        clean = mobile.strip()
        return len(clean) == 10 and clean.isdigit()

    def btn_add_click(self):
        sel = self.lstAvailableBooks.curselection()
        if not sel:
            messagebox.showwarning("No Selection", "Please select a book from Available Books to add.")
            return

        if self.lstSelectedBooks.size() >= 3:
            messagebox.showwarning("Limit Reached", "Maximum of 3 books can be selected!")
            return

        book = self.lstAvailableBooks.get(sel[0])
        current_items = self.lstSelectedBooks.get(0, tk.END)
        if book in current_items:
            messagebox.showwarning("Duplicate Selection", "This book is already selected!")
            return

        self.lstSelectedBooks.insert(tk.END, book)
        self.update_book_count()

    def btn_remove_click(self):
        sel = self.lstSelectedBooks.curselection()
        if not sel:
            messagebox.showwarning("No Selection", "Please select a book from Selected Books to remove.")
            return

        self.lstSelectedBooks.delete(sel[0])
        self.update_book_count()

    def btn_submit_click(self):
        name = self.txtMemberName.get()
        if not self.is_valid_member_name(name):
            messagebox.showerror("Validation Error", "Please enter a valid Member Name (alphabets and spaces only).")
            self.txtMemberName.focus_set()
            return

        mem_no = self.txtMembershipNumber.get()
        if not self.is_valid_membership_number(mem_no):
            messagebox.showerror("Validation Error", "Please enter a valid Membership Number (digits 0-9 only).")
            self.txtMembershipNumber.focus_set()
            return

        mob = self.txtMobileNumber.get()
        if not self.is_valid_mobile_number(mob):
            messagebox.showerror("Validation Error", "Please enter a valid 10-digit Mobile Number.")
            self.txtMobileNumber.focus_set()
            return

        if self.lstSelectedBooks.size() == 0:
            messagebox.showerror("Validation Error", "Please select at least one book before submitting.")
            return

        books = self.lstSelectedBooks.get(0, tk.END)
        books_str = "\n".join(f"{i+1}. {b}" for i, b in enumerate(books))

        summary = (
            "Library Membership Application Submitted Successfully!\n\n"
            "Member Details:\n"
            "--------------------------------------------------\n"
            f"Member Name: {name.strip()}\n"
            f"Membership No: {mem_no.strip()}\n"
            f"Mobile No: {mob.strip()}\n\n"
            f"Selected Books ({len(books)} / 3):\n"
            "--------------------------------------------------\n"
            f"{books_str}"
        )
        messagebox.showinfo("Application Submitted", summary)

    def btn_clear_click(self):
        self.txtMemberName.delete(0, tk.END)
        self.txtMembershipNumber.delete(0, tk.END)
        self.txtMobileNumber.delete(0, tk.END)
        self.lstSelectedBooks.delete(0, tk.END)
        self.lstAvailableBooks.selection_clear(0, tk.END)
        self.update_book_count()
        self.txtMemberName.focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryMembershipApp(root)
    root.mainloop()
