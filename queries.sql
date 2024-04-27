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

CREATE TABLE `cars` (
  `id` INTEGER NOT NULL,
  `car_image` BLOB NOT NULL,
  `brand` TEXT NOT NULL,
  `model` TEXT NOT NULL,
  `plate_number` TEXT NOT NULL,
  `fuel_type` TEXT NOT NULL,
  `availability` INTEGER NOT NULL,
  `cost_per_day` INTEGER NOT NULL,
  `seating_capacity` INTEGER NOT NULL,
  `location` TEXT NOT NULL,
  PRIMARY KEY (`id`)
);
CREATE TABLE `rent` (
  `id` INTEGER NOT NULL,
  `car_image` BLOB NOT NULL,
  `brand` TEXT NOT NULL,
  `model` TEXT NOT NULL,
  `plate_number` TEXT NOT NULL,
  `fuel_type` TEXT NOT NULL,
  `availability` INTEGER NOT NULL,
  `cost_per_day` INTEGER NOT NULL,
  `seating_capacity` INTEGER NOT NULL,
  `location` TEXT NOT NULL,
  PRIMARY KEY (`id`)
);





INSERT INTO accounts (account_type, name, email, contact, password, license_number)
VALUES ('admin', 'Angela Limlingan', 'admin_angela@gmail.com', 09052024872, 'Password123!', 'DO1-12-123456');

INSERT INTO accounts (account_type, name, email, contact, password, license_number)
VALUES ('customer', 'Elon Musk ', 'elon@gmail.com', 09394024874, 'Password123!', 'DO1-55-123459');
INSERT INTO accounts (account_type, name, email, contact, password, license_number)
VALUES ('customer', 'Taylor Swift', 'taylor@gmail.com', 09404024874, 'Password123!', 'DO2-25-123459');
INSERT INTO accounts (account_type, name, email, contact, password, license_number)
VALUES ('customer', 'Ariana Grande', 'ari@gmail.com', 09214024874, 'Password123!', 'DO3-25-123459');
INSERT INTO accounts (account_type, name, email, contact, password, license_number)
VALUES ('customer', 'Abel Tesfaye', 'weeknd@gmail.com', 09014024874, 'Password123!', 'DO9-34-123459');

-- INSERT INTO accounts (account_type, name, email, contact, password, license_number)
-- VALUES ('customer', 'Elon Musk', 'elon@gmail.com', 09394024874, 'Password123!', 'DO1-15-125559');


INSERT INTO `cars` (`id`, `car_image`, `brand`, `model`, `plate_number`, `fuel_type`, `availability`, `cost_per_day`, `seating_capacity`, `location`)
VALUES
(1, 'binary_data_for_car1', 'Toyota', 'Camry', 'ABC123', 'Petrol', 1, 2500, 5, 'Angeles, Pampanga'),
(2, 'binary_data_for_car2', 'Honda', 'Civic', 'XYZ456', 'Diesel', 1, 2000, 5, 'Angeles, Pampanga'),
(3, 'binary_data_for_car3', 'Ford', 'Focus', 'DEF789', 'Petrol', 0, 3000, 5, 'Angeles, Pampanga');






DELETE FROM accounts
WHERE account_type = 'customer' and id= 7;

DELETE FROM accounts
WHERE account_type = 'admin';

DROP TABLE cars;




Password123!
SecurePass1!
MyP@ssw0rd
Ch@ngeMe1
P@55w0rd!