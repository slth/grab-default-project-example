-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jul 22, 2016 at 01:25 AM
-- Server version: 10.1.13-MariaDB
-- PHP Version: 7.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `doska`
--

-- --------------------------------------------------------

--
-- Table structure for table `jb_board`
--

CREATE TABLE `jb_board` (
  `id` int(11) NOT NULL,
  `id_category` smallint(6) NOT NULL,
  `user_id` int(11) NOT NULL DEFAULT '0',
  `type` enum('s','p','u','o','a','v','r') DEFAULT 'p',
  `autor` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `city_id` smallint(6) NOT NULL,
  `url` varchar(255) NOT NULL,
  `click` smallint(6) NOT NULL DEFAULT '0',
  `contacts` text NOT NULL,
  `text` text NOT NULL,
  `price` int(11) NOT NULL,
  `video` varchar(128) NOT NULL,
  `hits` int(11) NOT NULL DEFAULT '0',
  `old_mess` enum('new','old') NOT NULL DEFAULT 'new',
  `checked` enum('yes','no','edit') NOT NULL DEFAULT 'no',
  `checkbox_top` smallint(1) NOT NULL DEFAULT '0',
  `top_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `send_notice_vip_sms` smallint(1) NOT NULL DEFAULT '0',
  `checkbox_select` smallint(1) NOT NULL DEFAULT '0',
  `select_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `send_notice_select_sms` smallint(1) NOT NULL DEFAULT '0',
  `tags` varchar(255) NOT NULL,
  `send_notice_day` smallint(1) NOT NULL DEFAULT '0',
  `time_delete` smallint(6) NOT NULL DEFAULT '30',
  `date_add` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 CHECKSUM=1 PACK_KEYS=0;

--
-- Dumping data for table `jb_board`
--

INSERT INTO `jb_board` (`id`, `id_category`, `user_id`, `type`, `autor`, `title`, `email`, `city`, `city_id`, `url`, `click`, `contacts`, `text`, `price`, `video`, `hits`, `old_mess`, `checked`, `checkbox_top`, `top_time`, `send_notice_vip_sms`, `checkbox_select`, `select_time`, `send_notice_select_sms`, `tags`, `send_notice_day`, `time_delete`, `date_add`) VALUES
(2864, 70, 62, 'p', 'пятигорчанин', 'Отчеканенные 94 года назад серебрянные полтинники,  5 монет.', 'kingkmv2013@mail.ru', 'Кав.Мин.Воды', 28, '', 0, 'Пятигорск 9283497219,  9054413875', 'Продаю серебреные монеты России.  Сохранность идеальная.  четко видно клеймо ПЛ на гурте.  Чеканка монетный двор Петроград.  Пять монет серебряные полтинники.  4 монеты 1922 г.  и 1 монета 1924 г.  Продаю все за 8500 р.  Пятигорск 9283497219,  9054413875', 0, '', 0, 'old', 'no', 0, '0000-00-00 00:00:00', 0, 0, '0000-00-00 00:00:00', 0, 'назад, отчеканенные, полтинники, года, серебрянные, монет', 0, 365, '2016-06-30 07:27:53');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `jb_board`
--
ALTER TABLE `jb_board`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_category` (`id_category`),
  ADD KEY `city_id` (`city_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `jb_board`
--
ALTER TABLE `jb_board`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2865;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
