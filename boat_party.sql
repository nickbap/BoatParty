-- Queries for viewing and debugging the Guest Book table
SELECT * FROM guest_book_post;

DELETE FROM guest_book_post WHERE id IN (1,2,3);