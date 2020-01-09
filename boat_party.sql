-- Queries for viewing and debugging the Guest Book table
SELECT * FROM guest_book_posts
;

DELETE FROM guest_book_posts WHERE id IN (1,2);

truncate table guest_book_posts;
