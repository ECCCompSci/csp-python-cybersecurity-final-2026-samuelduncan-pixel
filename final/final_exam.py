"""
╔══════════════════════════════════════════════════════════════╗
║        CSP Python & Cybersecurity Final Exam - 2026          ║
║                                                              ║
║  Name: SAMUEL S DUNCAN      ║
║  Date:  MAY 6 2026     ║
╚══════════════════════════════════════════════════════════════╝

GITHUB CLASSROOM INSTRUCTIONS:
  1. This assignment was distributed via GitHub Classroom.
     You should already have your own personal copy of this
     repository created automatically when you accepted the
     assignment link from your teacher.

  2. Complete ALL sections in this file.
     Replace every  # YOUR CODE HERE  comment with working code.
     Do NOT delete any existing code — only ADD your code.

  3. Run this file to check your output:
       python final_exam.py
     Fix any errors before submitting.

  4. Submit by committing and pushing this file to YOUR
     GitHub Classroom repository. Your teacher will see it
     automatically — no email or separate submission needed.

  5. Verify: Visit your repo on GitHub and confirm
     final/final_exam.py shows your completed code.

SCORING:
  Section 1 - Python Basics             [40 pts]
    1A. Variables & Output               (10 pts)
    1B. Grade Calculator Function        (16 pts)
    1C. List Operations                  (14 pts)

  Section 2 - File I/O                  [40 pts]
    2A. Write a File                     (20 pts)
    2B. Read and Search the File         (20 pts)

  Section 3 - Caesar Cipher             [40 pts]
    3A. Encrypt Function                 (20 pts)
    3B. Decrypt Function                 (20 pts)

  Section 4 - Password Strength Checker [40 pts]
    Length Check                          (8 pts)
    Uppercase Check                       (8 pts)
    Lowercase Check                       (8 pts)
    Digit Check                           (8 pts)
    Special Character Check               (8 pts)

  Section 5 - File System & Log Analysis[40 pts]
    5A. Build a Folder Structure         (20 pts)
    5B. Log File Analysis                (20 pts)
  ─────────────────────────────────────────────
  TOTAL                                 [200 pts]
"""

import os

print("=" * 60)
print("  CSP Python & Cybersecurity Final Exam")
print("=" * 60)


# ════════════════════════════════════════════════════════════
# SECTION 1 — Python Basics                         [40 pts]
# ════════════════════════════════════════════════════════════
print("\n--- Section 1: Python Basics ---")

# ── 1A. Variables & Output [10 pts] ───────────────────────
# Create three variables:
#   student_name  (string)  : your first name
#   student_grade (integer) : your grade level (9, 10, 11, or 12)
#   favorite_topic (string) : "Python" or "Cybersecurity"
# Then print: "Hi, I'm [name], a grade [grade] student who loves [topic]!"

# YOUR CODE HERE


# ── 1B. Grade Calculator [16 pts] ────────────────────────
# Write a function called letter_grade(score) that takes a
# numeric score (0-100) and returns the letter grade:
#   A = 90-100  |  B = 80-89  |  C = 70-79  |  D = 60-69  |  F = <60

def letter_grade(score):
    if score==100:
        set letter_grade
        pass

# Test your function (do not change these lines)
test_scores = [100, 88, 73, 61, 45]
for s in test_scores:
    print(f"  Score {s} -> {letter_grade(s)}")


# ── 1C. List Operations [14 pts] ─────────────────────────
# Given this list of cybersecurity threats:
threats = ["phishing", "malware", "ransomware", "spyware", "DDoS","brute force"]
print(threats)
Big_Threats=["PHISHING","]
# 3. Print each threat in ALL CAPS using a loop
# YOUR CODE HERE


# ════════════════════════════════════════════════════════════
# SECTION 2 — File I/O                              [40 pts]
# ════════════════════════════════════════════════════════════
print("\n--- Section 2: File I/O ---")

# ── 2A. Write a File [20 pts] ────────────────────────────
# Create a file called "cyber_glossary.txt" and write the
# following 5 terms and definitions into it, one per line:
#
#   Malware: Software designed to harm a computer or steal data.
#   Phishing: A fake message that tricks you into revealing information.
#   Encryption: Scrambling data so only authorized people can read it.
#   Firewall: A system that monitors and controls network traffic.
#   VPN: A tool that encrypts your internet connection.

# YOUR CODE HERE


# ── 2B. Read and Search the File [20 pts] ────────────────
# Open "cyber_glossary.txt" and:
#   1. Print the total number of lines in the file
#   2. Search for the term "Encryption" and print that line

# YOUR CODE HERE


# ════════════════════════════════════════════════════════════
# SECTION 3 — Caesar Cipher                         [40 pts]
# ════════════════════════════════════════════════════════════
print("\n--- Section 3: Caesar Cipher ---")

# ── 3A. Encrypt [20 pts] ─────────────────────────────────
# Write a function encrypt_message(text, shift) that:
#   - Shifts each LETTER forward by 'shift' positions in the alphabet
#   - Wraps around (Z + 1 = A)
#   - Leaves spaces, numbers, and punctuation UNCHANGED
#   - Preserves uppercase/lowercase
#
# Example: encrypt_message("Hello!", 4) -> "Lipps!"

def encrypt_message(text, shift):
    # YOUR CODE HERE
    pass


# ── 3B. Decrypt [20 pts] ─────────────────────────────────
# Write a function decrypt_message(text, shift) that reverses
# the encryption. Use your encrypt_message function!
#
# Example: decrypt_message("Lipps!", 4) -> "Hello!"

def decrypt_message(text, shift):
    # YOUR CODE HERE
    pass


# Test your cipher (do not change these lines)
original  = "Cybersecurity Is Fun!"
shift_val = 5
encoded   = encrypt_message(original, shift_val)
decoded   = decrypt_message(encoded, shift_val)
print(f"  Original:  {original}")
print(f"  Encrypted: {encoded}")
print(f"  Decrypted: {decoded}")
print(f"  Match: {original == decoded}")


# ════════════════════════════════════════════════════════════
# SECTION 4 — Password Strength Checker             [40 pts]
# ════════════════════════════════════════════════════════════
print("\n--- Section 4: Password Strength Checker ---")

# Write a function is_strong_password(password) that checks:
#   ✅ At least 10 characters long                    [8 pts]
#   ✅ Contains at least one uppercase letter          [8 pts]
#   ✅ Contains at least one lowercase letter          [8 pts]
#   ✅ Contains at least one digit (0-9)               [8 pts]
#   ✅ Contains at least one special char: !@#$%^&*    [8 pts]
#
# Return a DICTIONARY with:
#   "strong": True or False
#   "feedback": a list of strings describing what is missing
#               (empty list if the password is strong)
#
# Example:
#   is_strong_password("Hello1")
#   -> {"strong": False,
#       "feedback": ["Too short (need 10+ chars)",
#                    "Missing special character"]}

def is_strong_password(password):
    # YOUR CODE HERE
    pass


# Test passwords (do not change these lines)
test_passwords = [
    "abc",
    "helloworld",
    "Hello123",
    "Secur3!Pass",
    "MyStr0ng!PW",
]

for pw in test_passwords:
    result = is_strong_password(pw)
    status = "STRONG ✅" if result["strong"] else "WEAK ❌"
    print(f"  '{pw}' -> {status}")
    if result["feedback"]:
        for tip in result["feedback"]:
            print(f"      - {tip}")


# ════════════════════════════════════════════════════════════
# SECTION 5 — File System & Log Analysis            [40 pts]
# ════════════════════════════════════════════════════════════
print("\n--- Section 5: File System & Log Analysis ---")

# ── 5A. Build a Folder Structure [20 pts] ────────────────
# Use os.makedirs() to create this folder structure:
#
#   my_project/
#   ├── src/
#   ├── docs/
#   └── data/
#
# After creating the folders, write a file called
# "project_info.txt" inside my_project/ containing:
#   Project: CSP Final
#   Author: [your name]
#   Date: April 2026

# YOUR CODE HERE


# ── 5B. Log File Analysis [20 pts] ───────────────────────
# A security log is provided below as a list of strings.
# Write code that:
#   1. Counts how many lines contain "SUCCESS"
#   2. Counts how many lines contain "FAILED"
#   3. Prints each FAILED line with a ⚠️  warning prefix
#   4. Prints a summary: "X successful logins, Y failed attempts"

security_log = [
    "2026-04-23 07:00 - SUCCESS: alice logged in from 192.168.1.10",
    "2026-04-23 07:02 - FAILED: unknown user 'hacker' from 10.0.0.99",
    "2026-04-23 07:05 - SUCCESS: bob logged in from 192.168.1.11",
    "2026-04-23 07:07 - FAILED: alice wrong password from 192.168.1.10",
    "2026-04-23 07:09 - FAILED: unknown user 'admin' from 10.0.0.99",
    "2026-04-23 07:10 - SUCCESS: charlie logged in from 192.168.1.12",
    "2026-04-23 07:15 - SUCCESS: alice logged in from 192.168.1.10",
    "2026-04-23 07:18 - FAILED: bob wrong password from 192.168.1.11",
]

# YOUR CODE HERE


# ════════════════════════════════════════════════════════════
print("\n" + "=" * 60)
print("  Final Exam Complete — Review your output above!")
print("  Remember to commit and push to your GitHub Classroom repo!")
print("=" * 60)
