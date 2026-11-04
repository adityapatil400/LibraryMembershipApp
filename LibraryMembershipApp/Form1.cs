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
            // Name cannot be empty or only spaces
            if (string.IsNullOrWhiteSpace(name))
            {
                return false;
            }

            bool containsLetter = false;

            // Check each character in the string
            foreach (char c in name)
            {
                if (char.IsLetter(c))
                {
                    containsLetter = true;
                }
                else if (!char.IsWhiteSpace(c))
                {
                    // Character is neither a letter nor a space (e.g., number or symbol)
                    return false;
                }
            }

            return containsLetter;
        }

        // Validates Membership Number: accepts only digits (0-9)
        private bool IsValidMembershipNumber(string number)
        {
            // Number cannot be empty
            if (string.IsNullOrWhiteSpace(number))
            {
                return false;
            }

            // Check if every character is a digit
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

            // Mobile number must be exactly 10 digits
            if (cleanMobile.Length != 10)
            {
                return false;
            }

            // Check if every character is a digit
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

