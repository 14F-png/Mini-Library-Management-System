from operations import *

# ADDING BOOKS
print("=== ADDING BOOKS ===")
print(add_book("123", "programming", "francis sillah", "Fiction", 3))
print(add_book("234", "A Brief History of Technology", "Elon Musk", "Non-Fiction", 2))
print(add_book("345", "Naruto", "Gunna", "Sci-Fi", 4))
print(add_book("456", "Duplicate Book", "francis sillah", "Anime", 4))
print(add_book("444", "Unknown Genre Book", "Author F", "Sci-Fi", 6))

# ADDING MEMBERS
print("\n=== ADDING MEMBERS ===")
print(add_member(1, "francis", "francissilah57@gmail.com"))
print(add_member(2, "mariatu bangura", "mariatu6@gmail.com"))
print(add_member(1, "Lebbie sesay", "sesaylLebbie@gmail.com"))

# SEARCHING BOOKS
print("\n=== SEARCHING BOOKS (keyword: 'Time') ===")
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