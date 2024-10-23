-- inseting 100 book entries to the book table in my bookstore database


-- 64 book entries
INSERT INTO Books (title, author, genre, price, stock_quantity, publication_date) VALUES 
('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 10.99, 50, '1960-07-11'),
('1984', 'George Orwell', 'Dystopian', 8.99, 70, '1949-06-08'),
('Pride and Prejudice', 'Jane Austen', 'Romance', 7.99, 30, '1813-01-28'),
('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 9.99, 40, '1925-04-10'),
('Moby Dick', 'Herman Melville', 'Adventure', 11.99, 25, '1851-10-18'),
('War and Peace', 'Leo Tolstoy', 'Historical Fiction', 14.99, 60, '1869-01-01'),
('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 10.49, 35, '1951-07-16'),
('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 12.99, 80, '1937-09-21'),
('Ulysses', 'James Joyce', 'Modernist', 13.99, 20, '1922-02-02'),
('Crime and Punishment', 'Fyodor Dostoevsky', 'Philosophical Fiction', 9.49, 50, '1866-01-01'),
('The Odyssey', 'Homer', 'Epic Poetry', 11.99, 45, '800-01-01'),
('Brave New World', 'Aldous Huxley', 'Dystopian', 10.79, 60, '1932-08-18'),
('The Brothers Karamazov', 'Fyodor Dostoevsky', 'Philosophical Fiction', 14.49, 30, '1880-11-01'),
('Madame Bovary', 'Gustave Flaubert', 'Literary Fiction', 8.49, 40, '1856-01-01'),
('The Divine Comedy', 'Dante Alighieri', 'Epic Poetry', 15.99, 35, '1320-01-01'),
('The Count of Monte Cristo', 'Alexandre Dumas', 'Adventure', 13.79, 55, '1844-01-01'),
('Les Misérables', 'Victor Hugo', 'Historical Fiction', 12.49, 30, '1862-01-01'),
('Anna Karenina', 'Leo Tolstoy', 'Literary Fiction', 10.99, 70, '1878-01-01'),
('The Iliad', 'Homer', 'Epic Poetry', 12.99, 45, '762-01-01'),
('Great Expectations', 'Charles Dickens', 'Fiction', 11.49, 80, '1861-08-01'),
('One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 'Magical Realism', 13.99, 50, '1967-06-05'),
('Jane Eyre', 'Charlotte Brontë', 'Romance', 9.99, 60, '1847-10-16'),
('The Scarlet Letter', 'Nathaniel Hawthorne', 'Historical Fiction', 7.99, 25, '1850-03-16'),
('Wuthering Heights', 'Emily Brontë', 'Romance', 8.99, 40, '1847-12-01'),
('Frankenstein', 'Mary Shelley', 'Science Fiction', 10.49, 70, '1818-01-01'),
('Don Quixote', 'Miguel de Cervantes', 'Adventure', 14.99, 60, '1605-01-16'),
('The Picture of Dorian Gray', 'Oscar Wilde', 'Philosophical Fiction', 9.99, 55, '1890-06-20'),
('The Grapes of Wrath', 'John Steinbeck', 'Historical Fiction', 10.99, 45, '1939-04-14'),
('The Sound and the Fury', 'William Faulkner', 'Literary Fiction', 11.99, 50, '1929-10-07'),
('Fahrenheit 451', 'Ray Bradbury', 'Dystopian', 9.49, 65, '1953-10-19'),
('Dracula', 'Bram Stoker', 'Horror', 10.99, 30, '1897-05-26'),
('The Metamorphosis', 'Franz Kafka', 'Absurdist Fiction', 8.49, 50, '1915-01-01'),
('Heart of Darkness', 'Joseph Conrad', 'Adventure', 9.99, 40, '1899-01-01'),
('The Stranger', 'Albert Camus', 'Philosophical Fiction', 9.49, 60, '1942-01-01'),
('The Sun Also Rises', 'Ernest Hemingway', 'Fiction', 10.99, 75, '1926-10-22'),
('Slaughterhouse-Five', 'Kurt Vonnegut', 'Science Fiction', 11.49, 65, '1969-03-31'),
('Catch-22', 'Joseph Heller', 'Satire', 10.79, 55, '1961-11-10'),
('Lolita', 'Vladimir Nabokov', 'Fiction', 12.49, 45, '1955-09-15'),
('The Old Man and the Sea', 'Ernest Hemingway', 'Fiction', 8.99, 50, '1952-09-01'),
('Beloved', 'Toni Morrison', 'Historical Fiction', 11.99, 40, '1987-09-16'),
('Invisible Man', 'Ralph Ellison', 'Fiction', 9.49, 65, '1952-04-14'),
('Mansfield Park', 'Jane Austen', 'Romance', 7.99, 30, '1814-07-01'),
('East of Eden', 'John Steinbeck', 'Historical Fiction', 10.49, 45, '1952-09-19'),
('Things Fall Apart', 'Chinua Achebe', 'Historical Fiction', 8.99, 60, '1958-06-17'),
('A Tale of Two Cities', 'Charles Dickens', 'Historical Fiction', 9.99, 80, '1859-04-30'),
('Of Mice and Men', 'John Steinbeck', 'Fiction', 7.49, 70, '1937-02-06'),
('The Trial', 'Franz Kafka', 'Philosophical Fiction', 9.99, 55, '1925-04-26'),
('Gone with the Wind', 'Margaret Mitchell', 'Historical Fiction', 12.99, 50, '1936-06-30'),
('Rebecca', 'Daphne du Maurier', 'Gothic Fiction', 10.79, 40, '1938-08-01'),
('The Bell Jar', 'Sylvia Plath', 'Fiction', 8.49, 60, '1963-01-14'),
('Love in the Time of Cholera', 'Gabriel Garcia Marquez', 'Romance', 11.49, 45, '1985-01-01'),
('The Call of the Wild', 'Jack London', 'Adventure', 7.99, 55, '1903-01-01'),
('Emma', 'Jane Austen', 'Romance', 8.49, 40, '1815-12-23'),
('The War of the Worlds', 'H.G. Wells', 'Science Fiction', 9.99, 50, '1898-01-01'),
('The Road', 'Cormac McCarthy', 'Post-Apocalyptic', 10.99, 30, '2006-09-26'),
('Blood Meridian', 'Cormac McCarthy', 'Western', 11.49, 20, '1985-04-28'),
('Dune', 'Frank Herbert', 'Science Fiction', 12.49, 45, '1965-08-01'),
('A Clockwork Orange', 'Anthony Burgess', 'Dystopian', 9.79, 60, '1962-01-01'),
('Native Son', 'Richard Wright', 'Fiction', 10.49, 50, '1940-03-01'),
('Atlas Shrugged', 'Ayn Rand', 'Philosophical Fiction', 14.49, 35, '1957-10-10'),
('On the Road', 'Jack Kerouac', 'Fiction', 9.99, 60, '1957-09-05'),
('Gulliver’s Travels', 'Jonathan Swift', 'Satire', 7.49, 40, '1726-01-01'),
('Middlemarch', 'George Eliot', 'Literary Fiction', 12.99, 55, '1871-12-01'),
('White Teeth', 'Zadie Smith', 'Fiction', 10.49, 45, '2000-01-27');

-- 36 book entries
INSERT INTO Books (title, author, genre, price, stock_quantity, publication_date) VALUES
('White Teeth', 'Zadie Smith', 'Fiction', 10.49, 45, '2000-01-25'),
('The Color Purple', 'Alice Walker', 'Historical Fiction', 9.99, 50, '1982-06-01'),
('The Age of Innocence', 'Edith Wharton', 'Fiction', 8.49, 60, '1920-09-17'),
('The Wind in the Willows', 'Kenneth Grahame', 'Children\'s Literature', 7.99, 80, '1908-06-15'),
('Their Eyes Were Watching God', 'Zora Neale Hurston', 'Fiction', 10.99, 70, '1937-09-18'),
('Tess of the d\'Urbervilles', 'Thomas Hardy', 'Romance', 8.99, 30, '1891-12-01'),
('Infinite Jest', 'David Foster Wallace', 'Fiction', 14.99, 25, '1996-02-01'),
('A Portrait of the Artist as a Young Man', 'James Joyce', 'Fiction', 9.49, 55, '1916-12-29'),
('Mrs. Dalloway', 'Virginia Woolf', 'Fiction', 8.99, 45, '1925-05-14'),
('The Jungle Book', 'Rudyard Kipling', 'Children\'s Literature', 7.49, 75, '1894-10-14'),
('The Canterbury Tales', 'Geoffrey Chaucer', 'Poetry', 11.49, 40, '1400-01-01'),
('The Secret Garden', 'Frances Hodgson Burnett', 'Children\'s Literature', 7.99, 90, '1911-08-01'),
('The Handmaid\'s Tale', 'Margaret Atwood', 'Dystopian', 10.79, 35, '1985-09-01'),
('Life of Pi', 'Yann Martel', 'Adventure', 10.49, 60, '2001-09-11'),
('Remembrance of Things Past', 'Marcel Proust', 'Literary Fiction', 13.99, 20, '1913-01-01'),
('The Master and Margarita', 'Mikhail Bulgakov', 'Fantasy', 12.49, 50, '1967-01-01'),
('The Three Musketeers', 'Alexandre Dumas', 'Adventure', 9.99, 65, '1844-01-01'),
('The Little Prince', 'Antoine de Saint-Exupéry', 'Children\'s Literature', 8.49, 85, '1943-04-06'),
('Gravity\'s Rainbow', 'Thomas Pynchon', 'Fiction', 12.99, 30, '1973-02-28'),
('The Alchemist', 'Paulo Coelho', 'Adventure', 9.99, 70, '1988-01-01'),
('Blood Brothers', 'Elias Chacour', 'Historical Fiction', 11.49, 40, '1984-01-01'),
('Watership Down', 'Richard Adams', 'Fantasy', 9.49, 55, '1972-11-01'),
('The Remains of the Day', 'Kazuo Ishiguro', 'Fiction', 8.99, 45, '1989-05-01'),
('Siddhartha', 'Hermann Hesse', 'Philosophical Fiction', 7.49, 60, '1922-01-01'),
('The Woman in White', 'Wilkie Collins', 'Mystery', 10.99, 35, '1859-01-01'),
('Far from the Madding Crowd', 'Thomas Hardy', 'Romance', 9.49, 55, '1874-11-01'),
('The Tale of Genji', 'Murasaki Shikibu', 'Historical Fiction', 14.99, 20, '1008-01-01'),
('The Art of War', 'Sun Tzu', 'Philosophy', 10.49, 40, '500-01-01'),
('Germinal', 'Émile Zola', 'Historical Fiction', 8.99, 45, '1885-01-01'),
('Buddenbrooks', 'Thomas Mann', 'Fiction', 11.49, 25, '1901-01-01'),
('Leaves of Grass', 'Walt Whitman', 'Poetry', 9.99, 30, '1855-01-01'),
('All Quiet on the Western Front', 'Erich Maria Remarque', 'Historical Fiction', 10.99, 60, '1929-01-01'),
('The Hunchback of Notre-Dame', 'Victor Hugo', 'Romance', 12.49, 20, '1831-01-14'),
('The Magic Mountain', 'Thomas Mann', 'Fiction', 13.99, 50, '1924-01-01'),
('The Tale of Peter Rabbit', 'Beatrix Potter', 'Children\'s Literature', 6.99, 90, '1902-10-01'),
('Robinson Crusoe', 'Daniel Defoe', 'Adventure', 8.99, 55, '1719-04-25');


SELECT COUNT(*) FROM Books; 