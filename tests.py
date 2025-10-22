# tests.py
from operations import *
results = search_books("Time")
for isbn, details in results:
    print(f"Found: {details['title']} by {details['author']} (ISBN: {isbn})")

# UPDATING BOOK & MEMBER
print("\n=== UPDATING BOOK & MEMBER ===")
print(update_book("111", copies=2))
print(update_member(2, name="Saturo gojo"))

# BORROWING BOOKS
print("\n=== BORROWING BOOKS ===")
print(borrow_book(1, "111"))
print(borrow_book(2, "222"))
print(borrow_book(3, "333"))
print(borrow_book(4, "111"))

# RETURNING BOOKS
print("\n=== RETURNING BOOKS ===")
print(return_book(1, "222"))
print(return_book(2, "444"))
print(return_book(3, "111"))

# DELETING BOOKS & MEMBERS
print("\n=== DELETING BOOKS & MEMBERS ===")
print(delete_book("333"))
print(delete_book("222"))
print(delete_member(2))
print(delete_member(1))

# FINAL SYSTEM STATE
print("\n=== FINAL BOOKS DATA ===")
for isbn, details in books.items():
    print(isbn, "->", details)

print("\n=== FINAL MEMBERS DATA ===")
for m in members:
    print(m)
# Reset data structures before testing
books.clear()
members.clear()

print("=== RUNNING TESTS ===")

# TEST 1
result = add_book("111", "programming", "francis sillah", "Fiction", 3)
assert result == "Book added successfully.", "Test 1 Failed: Could not add book."
print("Test 1 Passed: Book added successfully.")

# TEST 2
result = add_member(1, "francis", "francissillah57@gmail.com")
assert result == "Member added successfully.", "Test 2 Failed: Could not add member."
print("Test 2 Passed: Member added successfully.")

# TEST 3
result = borrow_book(1, "111")
assert result == "Book borrowed successfully.", "Test 3 Failed: Borrowing failed."
print("Test 3 Passed: Book borrowed successfully.")

# TEST 4
# Reduce book copies to zero
books["111"]["copies"] = 0
result = borrow_book(1, "111")
assert result == "No copies available.", "Test 4 Failed: Should not borrow when no copies left."
print("Test 4 Passed: Borrow blocked when no copies left.")

# TEST 5
# Reset book copies and borrowed_books
books["111"]["copies"] = 2
members[0]["borrowed_books"].append("111")
result = return_book(1, "111")
assert result == "Book returned successfully.", "Test 5 Failed: Could not return book."
print("Test 5 Passed: Book returned successfully.")

# TEST 6
members[0]["borrowed_books"] = ["111"]
result = delete_member(1)
assert result == "Cannot delete member. They have borrowed books.", "Test 6 Failed: Member deletion should be blocked."
print("Test 6 Passed: Member deletion blocked when books borrowed.")

# TEST 7: Delete book currently borrowed
books["111"]["copies"] = 1
result = delete_book("111")
assert result == "Cannot delete book. It is currently borrowed.", "Test 7 Failed: Book deletion should be blocked."
print("Test 7 Passed: Book deletion blocked when borrowed.")

print("\nAll tests passed successfully! ")