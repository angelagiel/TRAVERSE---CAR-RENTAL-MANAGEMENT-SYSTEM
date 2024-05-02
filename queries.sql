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
  `availability` TEXT NOT NULL,
  `cost_per_day` INTEGER NOT NULL,
  `seating_capacity` INTEGER NOT NULL,
  `location` TEXT NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `rental` (
  `id` INTEGER NOT NULL,
  `rental_status` TEXT NOT NULL,
  `rented_model` TEXT NOT NULL,
  `rental_period` INTEGER NOT NULL,
  `rent_date` DATE NOT NULL,
  `rent_time` TIME NOT NULL,
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

INSERT INTO accounts (account_type, name, email, contact, password, license_number)
VALUES ('customer', 'Bill Gates', 'billgates@gmail.com', 09124024874, 'Password123!', 'DO4-45-123459');

INSERT INTO accounts (account_type, name, email, contact, password, license_number)
VALUES ('customer', 'Jeff Bezos', 'jeffbezos@gmail.com', 09234024874, 'Password123!', 'DO5-55-123459');

INSERT INTO accounts (account_type, name, email, contact, password, license_number)
VALUES ('customer', 'Mark Zuckerberg', 'markzuck@gmail.com', 09344024874, 'Password123!', 'DO6-65-123459');

INSERT INTO accounts (account_type, name, email, contact, password, license_number)
VALUES ('customer', 'Warren Buffett', 'warrenb@gmail.com', 09454024874, 'Password123!', 'DO7-75-123459');

INSERT INTO accounts (account_type, name, email, contact, password, license_number)
VALUES ('customer', 'Oprah Winfrey', 'oprah@gmail.com', '09564024874', 'Password123!', 'DO8-85-123459');

INSERT INTO accounts (account_type, name, email, contact, password, license_number)
VALUES ('customer', 'Ellen DeGeneres', 'ellen@gmail.com', '09674024874', 'Password123!', 'DO9-95-123459');

INSERT INTO accounts (account_type, name, email, contact, password, license_number)
VALUES ('customer', 'Dwayne Johnson', 'dwayne@gmail.com', '09784024874', 'Password123!', 'DO10-05-123459');



-- INSERT INTO accounts (account_type, name, email, contact, password, license_number)
-- VALUES ('customer', 'Elon Musk', 'elon@gmail.com', 09394024874, 'Password123!', 'DO1-15-125559');


INSERT INTO `cars` (`car_image`, `brand`, `model`, `plate_number`, `fuel_type`, `availability`, `cost_per_day`, `seating_capacity`, `location`)
VALUES
('binary_data_for_car8', 'Nissan', 'Altima', 'STU505', 'Petrol', 'AVAILABLE', 2600, 5, 'Angeles, Pampanga'),
('binary_data_for_car9', 'Volkswagen', 'Jetta', 'VWX606', 'Diesel', 'AVAILABLE', 2900, 5, 'Angeles, Pampanga'),
('binary_data_for_car10', 'Audi', 'A4', 'YZA707', 'Petrol', 'NOT AVAILABLE', 3300, 5, 'Angeles, Pampanga'),
('binary_data_for_car11', 'Subaru', 'Impreza', 'BCD808', 'Petrol', 'AVAILABLE', 2700, 5, 'Angeles, Pampanga')

('binary_data_for_car1', 'Toyota', 'Camry', 'ABC123', 'Petrol', 'AVAILABLE', 2500, 5, 'Angeles, Pampanga'),
('binary_data_for_car2', 'Honda', 'Civic', 'XYZ456', 'Diesel', 'AVAILABLE', 2000, 5, 'Angeles, Pampanga'),
('binary_data_for_car3', 'Ford', 'Focus', 'DEF789', 'Petrol', 'NOT AVAILABLE', 3000, 5, 'Angeles, Pampanga'),
('binary_data_for_car4', 'Chevrolet', 'Malibu', 'GHI101', 'Petrol', 'AVAILABLE', 2800, 5, 'Angeles, Pampanga'),
('binary_data_for_car5', 'Hyundai', 'Elantra', 'JKL202', 'Petrol', 'AVAILABLE', 2200, 5, 'Angeles, Pampanga'),
('binary_data_for_car6', 'BMW', '3 Series', 'MNO303', 'Petrol', 'AVAILABLE', 3500, 5, 'Angeles, Pampanga'),
('binary_data_for_car7', 'Mercedes-Benz', 'C-Class', 'PQR404', 'Diesel', 'AVAILABLE', 4000, 5, 'Angeles, Pampanga');




-- //////// for rental values 
INSERT INTO rental (rental_status, rented_model, rental_period, rent_date, rent_time)
VALUES ('rented', 'Toyota Camry', 7, '2024-04-29', '10:00:00');

INSERT INTO rental (rental_status, rented_model, rental_period, rent_date, rent_time)
VALUES ('returned', 'Honda Civic', 5, '2024-04-25', '12:30:00');

INSERT INTO rental (rental_status, rented_model, rental_period, rent_date, rent_time)
VALUES ('rented', 'Ford Focus', 3, '2024-04-20', '09:45:00');






DELETE FROM accounts
WHERE account_type = 'customer';

DELETE FROM accounts
WHERE account_type = 'admin';

DROP TABLE cars;




Password123!
SecurePass1!
MyP@ssw0rd
Ch@ngeMe1
P@55w0rd!