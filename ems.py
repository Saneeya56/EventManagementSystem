# Library Management System - Version 1.1
# Features: issue and return books, fine calculation
def issue_book(book_id, member_id):
print(&quot;Book&quot;, book_id, &quot;issued to member&quot;, member_id)
def return_book(book_id):
print(&quot;Book&quot;, book_id, &quot;returned&quot;)
def calculate_fine(days_late, rate=5):
fine = days_late * rate
print(&quot;Fine = Rs.&quot;, fine)
return fine
