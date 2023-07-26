SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Trips;
DROP TABLE IF EXISTS Memberships;
DROP TABLE IF EXISTS Tasks;
DROP TABLE IF EXISTS Expenses;
DROP TABLE IF EXISTS Events;
SET FOREIGN_KEY_CHECKS = 1;

-- Users
CREATE TABLE `Users` (
    `user_id` int AUTO_INCREMENT NOT NULL,
    `email` char(50) UNIQUE NOT NULL,
    `password` char(16) NOT NULL,
    `first_name` char(15) NOT NULL,
    `last_name` char(15) NOT NULL,
    PRIMARY KEY (`user_id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Trips
CREATE TABLE `Trips` (
    `trip_id` int AUTO_INCREMENT NOT NULL,
    `name` char(20) NOT NULL,
    PRIMARY KEY (`trip_id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Memberships
CREATE TABLE `Memberships` (
    `membership_id` int AUTO_INCREMENT NOT NULL,
    `user` int NOT NULL,
    `trip` int NOT NULL,
    `owner` boolean NOT NULL,
    PRIMARY KEY (`membership_id`),
    FOREIGN KEY (`user`)
        REFERENCES Users(`user_id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`trip`)
        REFERENCES Trips(`trip_id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Tasks
CREATE TABLE `Tasks` (
    `task_id` int AUTO_INCREMENT NOT NULL,
    `name` char(50) NOT NULL,
    `trip` int NOT NULL,
    `assignee` int NOT NULL,
    `created_by` int NOT NULL,
    `date_created` char(10) NOT NULL,
    `time_created` char(8) NOT NULL,
    `due_date` char(10),
    `due_time` char(8),
    PRIMARY KEY (`task_id`),
    FOREIGN KEY (`trip`)
        REFERENCES Trips(`trip_id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`assignee`)
        REFERENCES Users(`user_id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`created_by`)
        REFERENCES Users(`user_id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Expenses
CREATE TABLE `Expenses` (
    `expense_id` int AUTO_INCREMENT NOT NULL,
    `name` char(50) NOT NULL,
    `trip` int NOT NULL,
    `owed_to` int NOT NULL,
    `owed_by` int NOT NULL,
    `date_created` char(10) NOT NULL,
    `time_created` char(8) NOT NULL,
    `amount` decimal(8,2) NOT NULL,
    `settled` boolean NOT NULL,
    PRIMARY KEY (`expense_id`),
    FOREIGN KEY (`trip`)
        REFERENCES Trips(`trip_id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`owed_to`)
        REFERENCES Users(`user_id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`owed_by`)
        REFERENCES Users(`user_id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

-- Events
CREATE TABLE `Events` (
    `event_id` int AUTO_INCREMENT NOT NULL,
    `name` char(50) NOT NULL,
    `trip` int NOT NULL,
    `created_by` int NOT NULL,
    `from_date` char(10),
    `from_time` char(8),
    `to_date` char(10),
    `to_time` char(8),
    PRIMARY KEY (`event_id`),
    FOREIGN KEY (`trip`)
        REFERENCES Trips(`trip_id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (`created_by`)
        REFERENCES Users(`user_id`)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARSET = utf8;


-- SAMPLE DATA --

-- Users
INSERT INTO `Users` (`email`, `password`, `first_name`, `last_name`)
VALUES ('johndoe@email.com', 'password1234', 'John', 'Doe'),
        ('janedoe@email.com', '@password', 'Jane', 'Doe'),
        ('johnsmith@email.com', 'pAsSwOrD', 'John', 'Smith'),
        ('jesssmith@email.com', 'pass_word', 'Jess', 'Smith');

-- Trips
INSERT INTO `Trips` (`name`)
VALUES ('Doe Trip'),
        ('John Trip'),
        ('Smith Trip');

-- Memberships
INSERT INTO `Memberships` (`user`, `trip`, `owner`)
VALUES (1, 1, 1), -- John Doe // Doe Trip
        (2, 1, 0), -- Jane Doe // Doe Trip
        (1, 2, 1), -- John Doe // John Trip
        (3, 2, 0), -- John Smith // John Trip
        (3, 3, 0), -- John Smith // Smith Trip
        (4, 3, 1); -- Jess Smith // Smith Trip

-- Tasks
INSERT INTO `Tasks` (`name`, `trip`, `assignee`, `created_by`, `date_created`, `time_created`, `due_date`, `due_time`)
VALUES ('Buy plane tickets', 1, 1, 1, '2023-07-25', '17:13:24', '2023-07-31', '17:13:24'),
        ('Invite Friends', 1, 2, 1, '2023-07-25', '17:14:46', '2023-07-28', '17:14:46'),
        ('Pay John for BnB', 1, 2, 2, '2023-07-25', '12:43:11', '2023-08-14', null),
        ('Buy Concert Tickets', 2, 1, 1, '2021-04-24', '11:13:54', null, null),
        ('Buy Amusement Park Tickets', 2, 3, 1, '2021-04-24', '11:14:34', null, null),
        ('Reserve Hotel', 3, 4, 3, '2022-05-12', '09:32:01', '2022-05-19', null),
        ('Buy Equipment', 3, 4, 4, '2022-05-12', '09:33:49', '2022-05-19', null);

-- Expenses
INSERT INTO `Expenses` (`name`, `trip`, `owed_to`, `owed_by`, `date_created`, `time_created`, `amount`, `settled`)
VALUES ('AirBnb', 1, 1, 2, '2023-07-24', '12:28:49', 305.23, 0),
        ('Tickets', 1, 2, 1, '2023-07-14', '08:56:12', 65.11, 0),
        ('Plane Tickets', 2, 3, 1, '2021-02-04', '07:11:59', 108.23, 1),
        ('Hotel', 2, 3, 1, '2021-02-04', '06:23:34', 1027.43, 0),
        ('Plane Tix', 3, 4, 3, '2022-05-09', '18:00:43', 652.85, 0),
        ('Event Reservation', 3, 3, 4, '2022-05-11', '14:53:29', 103.88, 0);

-- Events
INSERT INTO `Events` (`name`, `trip`, `created_by`, `from_date`, `from_time`, `to_date`, `to_time`)
VALUES ('Hike', 1, 1, '2023-08-05', '10:00:00', '2023-08-05', '12:00:00'),
        ('Dinner', 1, 2, '2023-08-05', '18:00:00', '2023-08-05', '19:30:00'),
        ('Concert', 2, 1, '2021-06-29', '19:00:00', '2021-06-29', '22:00:00'),
        ('Amusement Park', 2, 3, '2021-06-30', '08:00:00', '2021-06-30', '17:00:00'),
        ('Event', 3, 3, '2022-07-11', '12:00:00', '2022-07-11', '18:00:00');
