CREATE TABLE `accounts` (
  `id` INTEGER NOT NULL,
  `account_type` TEXT NOT NULL,
  `name` TEXT NOT NULL,
  `email` TEXT NOT NULL,
  `contact` INTEGER NOT NULL,
  `password` TEXT NOT NULL,
  `license_number` TEXT NOT NULL,
  PRIMARY KEY (`id`)
);


INSERT INTO accounts (account_type, name, email, contact, password, license_number)
VALUES ('admin', 'Angela Limlingan', 'admin_angela@gmail.com', 09052024872, 'Password123!', 'DO1-12-123456');

INSERT INTO accounts (account_type, name, email, contact, password, license_number)
VALUES ('customer', 'Vice Ganda', 'vice@gmail.com', 09394024874, 'Password123!', 'DO2-15-123459');
INSERT INTO accounts (account_type, name, email, contact, password, license_number)
VALUES ('customer', 'Vice Ganda', 'vice@gmail.com', 09394024874, 'Password123!', 'DO2-15-123459');
INSERT INTO accounts (account_type, name, email, contact, password, license_number)
VALUES ('customer', 'Vice Ganda', 'vice@gmail.com', 09394024874, 'Password123!', 'DO2-15-123459');

-- INSERT INTO accounts (account_type, name, email, contact, password, license_number)
-- VALUES ('customer', 'Elon Musk', 'elon@gmail.com', 09394024874, 'Password123!', 'DO1-15-125559');


DELETE FROM accounts
WHERE account_type = 'customer' and id= 7;

DELETE FROM accounts
WHERE account_type = 'admin';




Password123!
SecurePass1!
MyP@ssw0rd
Ch@ngeMe1
P@55w0rd!