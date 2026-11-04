# Library Membership Application (C# Windows Forms)

A beginner-friendly desktop application built using **C#** and **Windows Forms (.NET Framework)** in **Visual Studio**. This application manages student/patron library memberships, validates member input fields, and handles book selections with strict business rules.

---

## 📌 Project Overview

- **Language:** C#
- **Application Type:** Windows Forms Application (WinForms)
- **Target Framework:** .NET Framework 4.7.2 / 4.8
- **IDE:** Microsoft Visual Studio (2019 / 2022)
- **Storage:** In-memory (No database required)

---

## 🖥️ Form UI Controls

The form contains the following 10 primary controls:

| Control Type | Control `(Name)` | Default Text / Purpose |
|---|---|---|
| **TextBox** | `txtMemberName` | Input field for member full name |
| **TextBox** | `txtMembershipNumber` | Input field for numeric membership ID |
| **TextBox** | `txtMobileNumber` | Input field for 10-digit mobile number |
| **ListBox** | `lstAvailableBooks` | Displays catalog of 10 available books |
| **ListBox** | `lstSelectedBooks` | Displays books currently selected by user |
| **Button** | `btnAdd` | Adds selected book (`Add >>`) |
| **Button** | `btnRemove` | Removes selected book (`<< Remove`) |
| **Label** | `lblBookCount` | Displays selected count: `Selected Books: 0 / 3` |
| **Button** | `btnSubmit` | Validates all inputs and displays confirmation |
| **Button** | `btnClear` | Resets all fields and selected books |

---

## 📚 Available Books Catalog

Populated automatically inside `Form1_Load`:

1. C Programming
2. C++ Programming
3. Java
4. Python
5. Data Structures
6. Database Management System
7. Operating System
8. Computer Networks
9. Web Development
10. Artificial Intelligence

---

## ⚙️ Implemented Conditions & Business Logic

| # | Condition | Implementation Details |
|---|---|---|
| **1** | **Membership Number** | Accepts digits (`0–9`) only. Validated character-by-character using `char.IsDigit()`. Rejects spaces, letters, and special symbols. |
| **2** | **Mobile Number** | Accepts **exactly 10 digits**. Checks `Length == 10` and ensures every character is a digit via `char.IsDigit()`. |
| **3** | **Member Name** | Accepts only alphabetic letters and spaces. Validated using `char.IsLetter()` and `char.IsWhiteSpace()`. Rejects empty input or numbers. |
| **4** | **Maximum 3 Books** | Limits user to at most 3 books. If `lstSelectedBooks.Items.Count >= 3`, a `MessageBox` warning appears. |
| **5** | **No Duplicate Books** | The same book cannot be added twice. Verified using `lstSelectedBooks.Items.Contains(selectedBook)`. |
| **6** | **Remove Books** | Users can select an item in `lstSelectedBooks` and click **Remove** to delete it via `ListBox.Items.Remove()`. |
| **7** | **Dynamic Book Count** | `lblBookCount` displays `Selected Books: X / 3` and updates automatically on Form Load, Add, Remove, and Clear. |
| **8** | **Submit Validation** | Submitting checks that all 3 fields are valid and at least 1 book is selected. Displays a success summary `MessageBox` with all details. |

---

## 📂 Project Structure

```text
dotnet/
├── LibraryMembershipApp.sln           # Visual Studio solution file
├── README.md                          # Documentation
└── LibraryMembershipApp/
    ├── LibraryMembershipApp.csproj    # .NET Framework project file
    ├── Program.cs                     # Application entry point (Main)
    ├── Form1.cs                       # Form logic & event handlers
    └── Form1.Designer.cs              # Visual Studio Form Designer code
```

---

## 💻 Source Code

### `Form1.cs`
```csharp
using System;
using System.Windows.Forms;

namespace LibraryMembershipApp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // ==========================================
        // 1. FORM LOAD EVENT
        // ==========================================
        private void Form1_Load(object sender, EventArgs e)
        {
            // Add the 10 available books to the Available Books ListBox
            lstAvailableBooks.Items.Add("C Programming");
            lstAvailableBooks.Items.Add("C++ Programming");
            lstAvailableBooks.Items.Add("Java");
            lstAvailableBooks.Items.Add("Python");
            lstAvailableBooks.Items.Add("Data Structures");
            lstAvailableBooks.Items.Add("Database Management System");
            lstAvailableBooks.Items.Add("Operating System");
            lstAvailableBooks.Items.Add("Computer Networks");
            lstAvailableBooks.Items.Add("Web Development");
            lstAvailableBooks.Items.Add("Artificial Intelligence");

            // Initialize the book count display
            UpdateBookCount();
        }

        // ==========================================
        // 2. HELPER METHODS / INPUT VALIDATION
        // ==========================================

        // Updates the selected book count label: "Selected Books: X / 3"
        private void UpdateBookCount()
        {
            lblBookCount.Text = "Selected Books: " + lstSelectedBooks.Items.Count + " / 3";
        }

        // Validates Member Name: accepts only letters and spaces
        private bool IsValidMemberName(string name)
        {
            if (string.IsNullOrWhiteSpace(name))
            {
                return false;
            }

            bool containsLetter = false;

            foreach (char c in name)
            {
                if (char.IsLetter(c))
                {
                    containsLetter = true;
                }
                else if (!char.IsWhiteSpace(c))
                {
                    return false;
                }
            }

            return containsLetter;
        }

        // Validates Membership Number: accepts only digits (0-9)
        private bool IsValidMembershipNumber(string number)
        {
            if (string.IsNullOrWhiteSpace(number))
            {
                return false;
            }

            foreach (char c in number)
            {
                if (!char.IsDigit(c))
                {
                    return false;
                }
            }

            return true;
        }

        // Validates Mobile Number: must be exactly 10 digits
        private bool IsValidMobileNumber(string mobile)
        {
            string cleanMobile = mobile.Trim();

            if (cleanMobile.Length != 10)
            {
                return false;
            }

            foreach (char c in cleanMobile)
            {
                if (!char.IsDigit(c))
                {
                    return false;
                }
            }

            return true;
        }

        // ==========================================
        // 3. BUTTON EVENT HANDLERS
        // ==========================================

        // Add Button: Adds selected book from Available Books to Selected Books
        private void btnAdd_Click(object sender, EventArgs e)
        {
            // 1. Check if a book is selected in Available Books
            if (lstAvailableBooks.SelectedItem == null)
            {
                MessageBox.Show("Please select a book from Available Books.", "No Book Selected", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            // 2. Check if the maximum limit of 3 books is reached
            if (lstSelectedBooks.Items.Count >= 3)
            {
                MessageBox.Show("Maximum of 3 books can be selected!", "Limit Reached", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            string selectedBook = lstAvailableBooks.SelectedItem.ToString();

            // 3. Check if the book is already added (duplicates not allowed)
            if (lstSelectedBooks.Items.Contains(selectedBook))
            {
                MessageBox.Show("This book is already selected!", "Duplicate Book", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            // 4. Add the book to Selected Books
            lstSelectedBooks.Items.Add(selectedBook);

            // 5. Update book count label
            UpdateBookCount();
        }

        // Remove Button: Removes selected book from Selected Books
        private void btnRemove_Click(object sender, EventArgs e)
        {
            // 1. Check if a book is selected in Selected Books
            if (lstSelectedBooks.SelectedItem == null)
            {
                MessageBox.Show("Please select a book from Selected Books to remove.", "No Book Selected", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            // 2. Remove the selected book
            lstSelectedBooks.Items.Remove(lstSelectedBooks.SelectedItem);

            // 3. Update book count label
            UpdateBookCount();
        }

        // Submit Button: Validates inputs and displays confirmation
        private void btnSubmit_Click(object sender, EventArgs e)
        {
            // 1. Validate Member Name
            if (!IsValidMemberName(txtMemberName.Text))
            {
                MessageBox.Show("Please enter a valid Member Name (alphabets and spaces only).", "Validation Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                txtMemberName.Focus();
                return;
            }

            // 2. Validate Membership Number
            if (!IsValidMembershipNumber(txtMembershipNumber.Text))
            {
                MessageBox.Show("Please enter a valid Membership Number (digits 0-9 only).", "Validation Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                txtMembershipNumber.Focus();
                return;
            }

            // 3. Validate Mobile Number
            if (!IsValidMobileNumber(txtMobileNumber.Text))
            {
                MessageBox.Show("Please enter a valid 10-digit Mobile Number.", "Validation Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                txtMobileNumber.Focus();
                return;
            }

            // 4. Validate Book Selection: At least 1 book must be selected
            if (lstSelectedBooks.Items.Count == 0)
            {
                MessageBox.Show("Please select at least one book before submitting.", "Validation Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // 5. Construct success summary message
            string message = "Library Membership Application Submitted Successfully!\n\n" +
                             "Member Details:\n" +
                             "--------------------------------------------------\n" +
                             "Member Name: " + txtMemberName.Text.Trim() + "\n" +
                             "Membership No: " + txtMembershipNumber.Text.Trim() + "\n" +
                             "Mobile No: " + txtMobileNumber.Text.Trim() + "\n\n" +
                             "Selected Books (" + lstSelectedBooks.Items.Count + " / 3):\n" +
                             "--------------------------------------------------\n";

            for (int i = 0; i < lstSelectedBooks.Items.Count; i++)
            {
                message += (i + 1) + ". " + lstSelectedBooks.Items[i].ToString() + "\n";
            }

            MessageBox.Show(message, "Application Submitted", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        // Clear Button: Resets form inputs and Selected Books
        private void btnClear_Click(object sender, EventArgs e)
        {
            // Clear all textboxes
            txtMemberName.Clear();
            txtMembershipNumber.Clear();
            txtMobileNumber.Clear();

            // Clear selected books list (Available Books list remains unchanged)
            lstSelectedBooks.Items.Clear();

            // Clear selection in available books list
            lstAvailableBooks.ClearSelected();

            // Reset the book count label
            UpdateBookCount();

            // Move cursor to the first input field
            txtMemberName.Focus();
        }
    }
}
```

---

## 🚀 How to Run

### In Visual Studio (Windows)
1. Open Visual Studio 2019 or 2022.
2. Select **File &rarr; Open &rarr; Project/Solution** and select `LibraryMembershipApp.sln`.
3. Set the build mode to **`Debug`** and **`Any CPU`**.
4. Press **`F5`** (or click the green **Start** ▶ button).

### From Windows Developer Command Prompt
```cmd
cd path\to\LibraryMembershipApp
msbuild LibraryMembershipApp.csproj
bin\Debug\LibraryMembershipApp.exe
```

### Running on macOS
Windows Forms relies on native Windows APIs (`System.Windows.Forms` / Win32). To run on a Mac:
1. **Transfer to Windows PC:** Copy the folder to a Windows machine with Visual Studio installed.
2. **Virtual Machine:** Run Windows 11 using **Parallels Desktop**, **VMware Fusion**, or **UTM**, and open the solution in Visual Studio.

---

## 🧪 Testing Checklist

- [x] **Form Load:** 10 books appear in Available Books; label shows `Selected Books: 0 / 3`.
- [x] **Name Validation:** Rejects empty string, numbers, or special characters.
- [x] **Membership Number Validation:** Rejects alphabets or symbols; accepts only digits.
- [x] **Mobile Number Validation:** Rejects fewer or more than 10 digits; rejects letters.
- [x] **Book Addition:** Moves selected book to Selected Books and increments count.
- [x] **Duplicate Prevention:** Shows warning if user tries to add an already selected book.
- [x] **Max Books Limit:** Blocks adding more than 3 books with a warning dialog.
- [x] **Book Removal:** Removes selected item from Selected Books and decrements count.
- [x] **Clear Button:** Clears textboxes and selected list, resets count to `0 / 3`.
- [x] **Submit Button:** Displays member details and selected book list in a formatted `MessageBox`.
