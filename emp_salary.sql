-- phpMyAdmin SQL Dump
-- version 3.4.5
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 31, 2021 at 03:59 AM
-- Server version: 5.5.16
-- PHP Version: 5.3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `ems`
--

-- --------------------------------------------------------

--
-- Table structure for table `emp_salary`
--

CREATE TABLE IF NOT EXISTS `emp_salary` (
  `e_id` int(11) NOT NULL AUTO_INCREMENT,
  `designation` text NOT NULL,
  `name` text NOT NULL,
  `age` text NOT NULL,
  `email` text NOT NULL,
  `hr_location` text NOT NULL,
  `dob` text NOT NULL,
  `doj` text NOT NULL,
  `proof_id` text NOT NULL,
  `contact` text NOT NULL,
  `experience` text NOT NULL,
  `gender` text NOT NULL,
  `status` text NOT NULL,
  `address` text NOT NULL,
  `month` text NOT NULL,
  `year` text NOT NULL,
  `basic_salary` text NOT NULL,
  `t_days` text NOT NULL,
  `absent_days` text NOT NULL,
  `medical` text NOT NULL,
  `pf` text NOT NULL,
  `convence` text NOT NULL,
  `net_salary` text NOT NULL,
  `salary_receipt` text NOT NULL,
  PRIMARY KEY (`e_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=104 ;

--
-- Dumping data for table `emp_salary`
--

INSERT INTO `emp_salary` (`e_id`, `designation`, `name`, `age`, `email`, `hr_location`, `dob`, `doj`, `proof_id`, `contact`, `experience`, `gender`, `status`, `address`, `month`, `year`, `basic_salary`, `t_days`, `absent_days`, `medical`, `pf`, `convence`, `net_salary`, `salary_receipt`) VALUES
(101, 'sumit', 'xyz', '20', '2416', 'delhi', 'gc', 'uyf', 'fuyt', 'fyfy', 'uyf', 'Male', 'Active', 'asq\n\n\n\n', 'dec', '2021', '2354545', '40', '2', '2345', '3455', '5098', '2236115.75', '101.txt'),
(102, 'rock and rolla', 'ricky', '12', 'sumit222', 'dicusdf', 'wffffffffffff', 'wefwefwfwewfewef', 'wefoihj', 'edhowef', 'wefoih', 'Female', 'Active', 'dfbskfsdf\n\n', 'wfe', 'fwe', '1111111', '111', '11', '11111', '1111', '11112', '999890.9', '102.txt'),
(103, 'manager', 'jas', '23', 'studywok@8510', 'delhi', '21-11-1997', '1-2-2018', '3353654756868', '343546575', '3', 'Female', 'Active', 'vikas nager	\n', '11', '2020', '245142', '31', '2', '4000', '4352', '6000', '226974.39', '103.txt');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
