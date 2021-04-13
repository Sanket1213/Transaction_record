-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3307
-- Generation Time: Apr 13, 2021 at 08:08 AM
-- Server version: 10.1.31-MariaDB
-- PHP Version: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mom_shop`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `Page_no` varchar(100) NOT NULL,
  `date` varchar(100) NOT NULL,
  `C_Name` varchar(200) NOT NULL,
  `C_Contact` varchar(200) NOT NULL,
  `Total_Amount` int(11) NOT NULL,
  `Paid_Amount` int(11) NOT NULL,
  `Remaining_Amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`Page_no`, `date`, `C_Name`, `C_Contact`, `Total_Amount`, `Paid_Amount`, `Remaining_Amount`) VALUES
('1', '21/05/20', 'Alaka Thakare', '999888888', 1135, 200, 935),
('2', '21/05/20', 'vidhya ingole', '9881964401', 20876, 5000, 15876),
('3', '21/05/20', 'boby kuhite', '6666677777', 820, 500, 320),
('4', '21/05/20', 'sarika dhurat', '5454326767', 560, 200, 360),
('5', '21/05/20', 'prarthana mahantare', '987654321', 300, 300, 0),
('6', '21/05/20', 'jayshri gayakwad', '56565656', 160, 160, 0),
('7', '21/05/20', 'dhurat bhadewale', '4545454545', 525, 100, 425),
('8', '21/05/20', 'saroj tai', '4545454545', 880, 500, 380),
('9', '21/05/20', 'devashis bhise', '4545454545', 770, 700, 70),
('10', '21/05/20', 'ashu dhurat', '4545454545', 1060, 700, 360),
('11', '23/05/20', 'vidhya ingole', '9881964401', 3420, 700, 2720),
('12', '23/05/20', 'sanket ingole', '3889090434', 5006, 1000, 4006);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
