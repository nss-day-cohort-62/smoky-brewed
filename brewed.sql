CREATE TABLE `Product` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `price` INTEGER NOT NULL
);

CREATE TABLE `Order` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `product_id` INTEGER NOT NULL,
    `employee_id` INTEGER NOT NULL,
    `timestamp` DATETIME NOT NULL,
    FOREIGN KEY (`product_id`) REFERENCES `Product`(`id`),
    FOREIGN KEY (`employee_id`) REFERENCES `Employee`(`id`)
);

CREATE TABLE `Employee`(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `email` VARCHAR(50) NOT NULL,
    `hourly_rate` INTEGER NOT NULL
 );

INSERT INTO `Product` VALUES (null, 'Large Coffee', 6.00);
INSERT INTO `Product` VALUES (null, 'Latte', 8.99);
INSERT INTO `Product` VALUES (null, 'Espresso', 11.80);
INSERT INTO `Product` VALUES (null, 'Americano', 11.00);
INSERT INTO `Product` VALUES (null, 'Cubano', 14.99);
INSERT INTO `Product` VALUES (null, 'Cappuccino', 12.49);

INSERT INTO `Order` VALUES (null, 6, 3, "2023-04-17");
INSERT INTO `Order` VALUES (null, 5, 1, "2023-04-16");
INSERT INTO `Order` VALUES (null, 2, 2, "2023-04-15");
INSERT INTO `Order` VALUES (null, 1, 4, "2023-04-14");
INSERT INTO `Order` VALUES (null, 4, 3, "2023-04-17");

INSERT INTO `Employee` VALUES (null, 'Dylan Kline', 'dylan@kline.com', 20.50);
INSERT INTO `Employee` VALUES (null, 'Ernie Fabian', 'ernie@fabian.com', 20.50);
INSERT INTO `Employee` VALUES (null, 'Emeka Akoma', 'emeka@akoma.com', 20.50);
INSERT INTO `Employee` VALUES (null, 'Jess Whyte', 'jess@whyte.com', 20.50);
