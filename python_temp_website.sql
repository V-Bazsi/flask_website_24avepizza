-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 09, 2020 at 07:11 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_temp_website`
--

-- --------------------------------------------------------

--
-- Table structure for table `aboutus`
--

CREATE TABLE `aboutus` (
  `id` int(11) NOT NULL,
  `about_left` text NOT NULL,
  `about_right` text NOT NULL,
  `pizza` int(11) NOT NULL,
  `pasta` int(11) NOT NULL,
  `salad` int(11) NOT NULL,
  `chef` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `aboutus`
--

INSERT INTO `aboutus` (`id`, `about_left`, `about_right`, `pizza`, `pasta`, `salad`, `chef`) VALUES
(0, 'Inspired by authentic pizzerias in Naples, 24 Ave Pizza is keeping true to Neapolitan pizza\'s origins by providing products that focus on simplicity, freshness & high-quality ingredients. We differentiate ourselves from other pizza restaurants, who charge a high price to capitalize on the unique ingredients and cooking processes involved, by focusing on the quality of the ingredients and ensuring that our products are affordable for everyone.', 'With over 400+ possible combinations, you can customize our Neapolitan pizzas and salads to your heart\'s desire all for one fixed price. All our pizza is made from 00 Italian Flour & no chemicals in the dough', 40, 15, 4, 5);

-- --------------------------------------------------------

--
-- Table structure for table `client`
--

CREATE TABLE `client` (
  `id` int(11) NOT NULL,
  `title` varchar(250) NOT NULL,
  `body` text NOT NULL,
  `name` varchar(250) NOT NULL,
  `ocup` varchar(250) NOT NULL DEFAULT 'Customer'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `client`
--

INSERT INTO `client` (`id`, `title`, `body`, `name`, `ocup`) VALUES
(1, 'Nice place. nice ambiance. Quantity and price may appear likely to others pizza destinations', 'Nice place. nice ambiance. Quantity and price may appear likely to others pizza destinations; but here taste of pizza is different than others which makes it unique.fresh food.  Today also I had some very good food there. Varieties of pizza, pasta. Chicken roast. Toasts. Very nice hospitality of the owners and the chefs.. Specially a chef.. Palaash. He suggests u best food there.', 'Ananya Mondal', 'Customer'),
(2, 'Best Pizza Pizza in the locality', 'Best Pizza in the locality. Very friendly staff and very tasty foods are available. I once you visit this place you will never regret ^~^', 'Avisek Sen', 'Customer'),
(3, 'Tried the non-veg and veg burgers, last week.', 'Tried the non-veg and veg burgers, last week. They were delicious and worth the money. Was specially impressed by the way there were packed and delivered to keep them hot. Got update on the delivery and billing over SMS.', 'Manish Kumar Saha', 'Customer'),
(4, 'Excellent food with a plethora of variety.', 'Excellent food with a plethora of variety.  Unlimited toppings.  USP is Value for money  A must visit for the young stars.', ' Chandrani Pal', 'Customer'),
(5, 'I am into this food industry from long 8 years but like a very few place for Pizza.', 'I am into this food industry from long 8 years but like a very few place for Pizza. And this outlet one of them. Can\'t find better place like this. Value for money and far better than Domino\'s or Pizza Hut. Must try....', ' Prasenjit Sen', 'Customer'),
(6, 'Lovely Pizza.. freshly baked.. unlimited toppings..', 'Lovely Pizza.. freshly baked.. unlimited toppings..  Great taste.. loved it..  Nice people to talk to assisted nicely', 'Sandeep Parnani', 'Customer');

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `id` int(11) NOT NULL,
  `name` varchar(250) NOT NULL,
  `subject` varchar(250) NOT NULL,
  `email` varchar(250) NOT NULL,
  `msg` text NOT NULL,
  `dt_time` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`id`, `name`, `subject`, `email`, `msg`, `dt_time`) VALUES
(1, 'Sample Name', 'Sample Subject', 'sample-email@domain-name.com', 'Sample Message!', '2020-05-01 19:03:25'),
(2, 'Dhruva Shaw', 'Sample Subject', 'dhruvashaw@gmail.com', 'Sample Message', '2020-05-01 20:50:44');

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `id` int(11) NOT NULL,
  `part` varchar(250) NOT NULL,
  `name` varchar(250) NOT NULL,
  `body` text DEFAULT NULL,
  `img_file` text NOT NULL,
  `price` varchar(11) DEFAULT NULL,
  `size1` varchar(250) DEFAULT NULL,
  `price1` varchar(11) DEFAULT NULL,
  `size2` varchar(250) DEFAULT NULL,
  `best` text NOT NULL,
  `partname` text NOT NULL,
  `indexin` varchar(3) NOT NULL DEFAULT 'NO',
  `menuin` varchar(3) NOT NULL DEFAULT 'YES',
  `pricesym` varchar(12) DEFAULT 'bx bx-rupee',
  `price1sym` varchar(12) DEFAULT 'bx bx-rupee',
  `availability` varchar(3) NOT NULL DEFAULT 'YES',
  `active` varchar(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`id`, `part`, `name`, `body`, `img_file`, `price`, `size1`, `price1`, `size2`, `best`, `partname`, `indexin`, `menuin`, `pricesym`, `price1sym`, `availability`, `active`) VALUES
(1, 'Pizza-OneTopping', 'Vegetarian', 'A one topping Vegetarian Pizza', 'temporary-pizza.png', '140', '10\'\'', '225', '13\"', 'NO', 'Pizza OneTopping', 'NO', 'YES', 'bx bx-rupee', 'bx bx-rupee', 'YES', 'active'),
(2, 'Pizza-OneTopping', 'Non - Vegetarian', 'A one topping Non - Vegetarian Pizza', 'temporary-pizza.png', '160', '10\'\'', '250', '13\"', 'No', 'Pizza OneTopping', 'YES', 'YES', 'bx bx-rupee', 'bx bx-rupee', 'YES', 'active'),
(3, 'Combo-Offer', 'Mexican Veg Jalapeno Cheese Sandwich', 'Mexican Veg Jalapeno Cheese Sandwich.', 'combo.png', '125', '', '', '', 'No', 'Combo Offer', 'NO', 'YES', 'bx bx-rupee', '', 'YES', ''),
(4, 'Combo-Offer', 'Grilled Cheese Sandwich', 'Grilled Cheese Sandwich', 'combo.png', '115', '', '', '', 'No', 'Combo Offer', 'NO', 'YES', 'bx bx-rupee', '', 'YES', ''),
(5, 'Combo-Offer', 'Chicken Grilled Sandwich', 'Chicken Grilled Sandwich', 'combo.png', '130', '', '', '', 'No', 'Combo Offer', 'NO', 'YES', 'bx bx-rupee', '', 'YES', ''),
(6, 'Combo-Offer', 'Grilled Peri-Peri Sandwich', 'Grilled Peri-Peri Sandwich', 'combo.png', '130', '', '', '', 'No', 'Combo Offer', 'NO', 'YES', 'bx bx-rupee', '', 'YES', ''),
(7, 'Combo-Offer', 'Veg Burger with Mozarella Cheese', 'Veg Burger with Mozarella Cheese', 'combo.png', '145', '', '', '', 'No', 'Combo Offer', 'NO', 'YES', 'bx bx-rupee', '', 'YES', ''),
(8, 'Combo-Offer', 'Chicken Crispy Burger', 'Chicken Crispy Burger', 'combo.png', '189', '', '', '', 'No', 'Combo Offer', 'NO', 'YES', 'bx bx-rupee', '', 'YES', ''),
(9, 'Pizza-Vegetarian', 'Margherita Classic', 'Italian tomato sauce, mozzarella, cherry tomatoes & basil', 'temporary-pizza.png', '150', '10\"', '290', '13\"', 'YES', 'Pizza Vegetarian', 'YES', 'YES', 'bx bx-rupee', 'bx bx-rupee', 'YES', ''),
(10, 'Pizza-Vegetarian', 'Quattro Formaggio', '(cheese lover\'s pizza) Mozzarella, cheddar, greek feta, Parmigiano Reggiano, Itialian Tomato sauce & olive oil', 'temporary-pizza.png', '250', '10\"', '350', '13\"', 'NO', 'Pizza Vegetarian', 'NO', 'YES', 'bx bx-rupee', 'bx bx-rupee', 'YES', ''),
(11, 'Pizza-Vegetarian', 'Green Stripe', 'Homemade basil pesto, paneer, garlic, green bell pepper & mozarella', 'temporary-pizza.png', '175', '10\"', '350', '13\"', 'YES', 'Pizza Vegetarian', 'YES', 'YES', 'bx bx-rupee', 'bx bx-rupee', 'YES', ''),
(12, 'Pizza-Vegetarian', 'Farmhouse Veggie Spicy', 'Italian Tomato Sauce, bell pepper (red, yellow, & green), mushroom, black olives, chillies & jalapeno with peri-peri sauce ', 'temporary-pizza.png', '175', '10\"', '350', '13\"', 'NO', 'Pizza Vegetarian', 'YES', 'YES', 'bx bx-rupee', 'bx bx-rupee', 'YES', ''),
(13, 'Pizza-Vegetarian', 'Tomato and cheese', 'Only tomato and cheese in pizza', 'temporary-pizza.png', '175', '10\"', '350', '13\"', 'NO', 'Pizza Vegetarian', 'NO', 'YES', 'bx bx-rupee', 'bx bx-rupee', 'YES', ''),
(14, 'Pizza-Vegetarian', 'Golden corn and Cheese Baby Corn', 'Golden corn and Cheese Baby Corn pizza', 'temporary-pizza.png', '175', '10\"', '350', '13\"', 'NO', 'Pizza Vegetarian', 'NO', 'YES', 'bx bx-rupee', 'bx bx-rupee', 'YES', ''),
(18, 'Unlimited-Toppings-Pizza', 'Vegetarian', 'Vegetarian pizza with unlimited toppings', 'temporary-pizza.png', '225', '10\"', '350', '13\"', 'Yes', 'Unlimited Toppings Pizza', 'YES', 'YES', 'bx bx-rupee', 'bx bx-rupee', 'YES', ''),
(19, 'Unlimited-Toppings-Pizza', 'Non - Vegetarian', 'Non - Vegetarian pizza with unlimited toppings', 'temporary-pizza.png', '250', '10\"', '425', '13\"', 'Yes', 'Unlimited Toppings Pizza', 'YES', 'YES', 'bx bx-rupee', 'bx bx-rupee', 'YES', ''),
(41, 'IN-Store-Home-Made-Desserts', 'Homemade chocolate brownies', 'Chocolate Brownies', 'slider_1_1920_1200.jpg', '40', 'Small', '80', 'Large', 'YES', 'IN-Store Home Made Desserts', 'YES', 'YES', 'bx bx-rupee', 'bx bx-rupee', 'YES', NULL),
(42, 'IN-Store-Home-Made-Desserts', 'Nutella & Banana Calzone', '', 'nuttelaCalzone.jpg', '55', 'Small', '80', 'Large', 'NO', 'IN-Store Home Made Desserts', 'NO', 'YES', 'bx bx-rupee', 'bx bx-rupee', 'NO', NULL),
(43, 'IN-Store-Home-Made-Desserts', 'S\'mores Calzone', '', 'nuttelaCalzone.jpg', '75', 'Small', '125', 'Large', 'NO', 'IN-Store Home Made Desserts', 'NO', 'YES', 'bx bx-rupee', 'bx bx-rupee', 'NO', NULL),
(44, 'Burger', 'Veg Burger with Mozarella', '', 'burger.jpg', '75', '', '', '', 'NO', 'Burger', 'YES', 'YES', 'bx bx-rupee', '', 'YES', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `offers`
--

CREATE TABLE `offers` (
  `id` int(11) NOT NULL,
  `title` varchar(250) NOT NULL,
  `year` int(7) NOT NULL,
  `month` int(2) NOT NULL,
  `date` int(2) NOT NULL,
  `slug` varchar(250) NOT NULL,
  `body` varchar(250) NOT NULL,
  `img_file` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `offers`
--

INSERT INTO `offers` (`id`, `title`, `year`, `month`, `date`, `slug`, `body`, `img_file`) VALUES
(1, '20% Off in DineOut', 2022, 12, 30, 'dineout-20', 'Get 20% discount on total bill, in the DineOut Reservations.', 'dineout.png'),
(2, 'Get 20% off on first order', 2020, 12, 31, 'swiggy-zomato-20-first', 'Get 20% off on first order in Swiggy and Zomato.', 'swig-zomat.jpg'),
(29, 'Buy one get free!!!!', 2020, 12, 31, 'our-buy-get-1-free-wed-every', 'Buy one and get one free every Wednesday, when ordered from our store!!!', 'web-buy.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `passwordtracker`
--

CREATE TABLE `passwordtracker` (
  `id` int(11) NOT NULL,
  `website` text NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL,
  `dt_time` datetime NOT NULL DEFAULT current_timestamp(),
  `ip_address` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `passwordtracker`
--

INSERT INTO `passwordtracker` (`id`, `website`, `username`, `password`, `dt_time`, `ip_address`) VALUES
(1, 'Sample Website', 'samplemail@gmail.com', 'sapmlePassword', '2020-04-24 20:36:10', '127.0.0.1');

-- --------------------------------------------------------

--
-- Table structure for table `qrcode`
--

CREATE TABLE `qrcode` (
  `id` int(11) NOT NULL,
  `title` text NOT NULL,
  `qrcode` text NOT NULL,
  `stime` datetime NOT NULL DEFAULT current_timestamp(),
  `endpoint` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `aboutus`
--
ALTER TABLE `aboutus`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `offers`
--
ALTER TABLE `offers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `passwordtracker`
--
ALTER TABLE `passwordtracker`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `qrcode`
--
ALTER TABLE `qrcode`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `aboutus`
--
ALTER TABLE `aboutus`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `client`
--
ALTER TABLE `client`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `menu`
--
ALTER TABLE `menu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `offers`
--
ALTER TABLE `offers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `passwordtracker`
--
ALTER TABLE `passwordtracker`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `qrcode`
--
ALTER TABLE `qrcode`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
