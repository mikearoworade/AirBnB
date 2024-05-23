-- Warning: You can generate script only for one table/view at a time in your Free plan 
-- 
-- **************************** SqlDBM: MySQL ***************************
-- ******* Generated by SqlDBM: AirBNB_Clone by Ayoaro85@gmail.com ******

-- ************************************** `User`
SET storage_engine=InnoDB;
START TRANSACTION;
CREATE TABLE IF NOT EXISTS `User`
(
 `id`         varchar(255) NOT NULL ,
 `updated_at` datetime NOT NULL ,
 `created_at` datetime NOT NULL ,
 `email`      varchar(50) NOT NULL ,
 `password`   varchar(100) NOT NULL ,
 `first_name` varchar(50) NOT NULL ,
 `last_name`  varchar(50) NOT NULL ,

PRIMARY KEY (`id`)
);

-- ************************************** `State`

CREATE TABLE IF NOT EXISTS `State`
(
 `id`         varchar(255) NOT NULL ,
 `updated_at` datetime NOT NULL ,
 `created_at` datetime NOT NULL ,
 `name`       varchar(50) NOT NULL ,

PRIMARY KEY (`id`)
);

-- ************************************** `City`

CREATE TABLE IF NOT EXISTS `City`
(
 `id`         varchar(255) NOT NULL ,
 `updated_at` datetime NOT NULL ,
 `created_at` datetime NOT NULL ,
 `name`       varchar(50) NOT NULL ,
 `state_id`   varchar(255) NOT NULL ,

PRIMARY KEY (`id`),
KEY `FK_1` (`state_id`),
CONSTRAINT `FK_5` FOREIGN KEY `FK_1` (`state_id`) REFERENCES `State` (`id`)
);

-- ************************************** `Amenity`

CREATE TABLE IF NOT EXISTS `Amenity`
(
 `id`         varchar(255) NOT NULL ,
 `updated_at` datetime NOT NULL ,
 `created_at` datetime NOT NULL ,
 `name`       varchar(50) NOT NULL ,

PRIMARY KEY (`id`)
);

-- ************************************** `Place`

CREATE TABLE IF NOT EXISTS `Place`
(
 `id`               varchar(255) NOT NULL ,
 `updated_at`       datetime NOT NULL ,
 `created_at`       datetime NOT NULL ,
 `name`             varchar(50) NOT NULL ,
 `description`      multilinestring NULL ,
 `number_rooms`     integer NOT NULL ,
 `number_bathrooms` integer NOT NULL ,
 `max_guest`        integer NOT NULL ,
 `price_by_night`   integer NOT NULL DEFAULT 0 ,
 `latitute`         float NULL DEFAULT 0 ,
 `longitude`        float NULL DEFAULT 0 ,
 `user_id`          varchar(255) NOT NULL ,
 `city_id`          varchar(255) NOT NULL ,

PRIMARY KEY (`id`),
KEY `FK_1` (`user_id`),
CONSTRAINT `FK_2` FOREIGN KEY `FK_1` (`user_id`) REFERENCES `User` (`id`),
KEY `FK_2` (`city_id`),
CONSTRAINT `FK_6` FOREIGN KEY `FK_2` (`city_id`) REFERENCES `City` (`id`)
);

-- ************************************** `PlaceAmenity`

CREATE TABLE IF NOT EXISTS `PlaceAmenity`
(
 `amenity_id` varchar(255) NOT NULL ,
 `place_id`   varchar(255) NOT NULL ,

KEY `FK_1` (`amenity_id`),
CONSTRAINT `FK_3` FOREIGN KEY `FK_1` (`amenity_id`) REFERENCES `Amenity` (`id`),
KEY `FK_2` (`place_id`),
CONSTRAINT `FK_4` FOREIGN KEY `FK_2` (`place_id`) REFERENCES `Place` (`id`)
);

-- ************************************** `Review`

CREATE TABLE IF NOT EXISTS `Review`
(
 `id`         varchar(255) NOT NULL ,
 `updated_at` datetime NOT NULL ,
 `created_at` datetime NOT NULL ,
 `text`       multilinestring NOT NULL ,
 `place_id`   varchar(255) NOT NULL ,
 `user_id`    varchar(255) NOT NULL ,

PRIMARY KEY (`id`),
KEY `FK_1` (`place_id`),
CONSTRAINT `FK_1` FOREIGN KEY `FK_1` (`place_id`) REFERENCES `Place` (`id`),
KEY `FK_2` (`user_id`),
CONSTRAINT `FK_7` FOREIGN KEY `FK_2` (`user_id`) REFERENCES `User` (`id`)
);

--COMMIT;
ROLLBACK;