# Library Management System - Version 2.0
# Features: issue/return books, fine calculation, online catalogue search
catalogue = [&quot;DBMS&quot;, &quot;Operating Systems&quot;, &quot;Computer Networks&quot;]
def issue_book(book_id, member_id):
print(&quot;Book&quot;, book_id, &quot;issued to member&quot;, member_id)
def return_book(book_id):
print(&quot;Book&quot;, book_id, &quot;returned&quot;)
def calculate_fine(days_late, rate=5):
fine = days_late * rate
print(&quot;Fine = Rs.&quot;, fine)
return fine
def search_book(title):
if title in catalogue:
print(title, &quot;is available&quot;)
else:
print(title, &quot;not found&quot;)
