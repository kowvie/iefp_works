-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Host: database
-- Generation Time: Mar 02, 2026 at 09:42 PM
-- Server version: 12.2.2-MariaDB-ubu2404
-- PHP Version: 8.3.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pp-jribeiro`
--
CREATE DATABASE IF NOT EXISTS `pp-jribeiro` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `pp-jribeiro`;

-- --------------------------------------------------------

--
-- Table structure for table `categoria`
--

CREATE TABLE `categoria` (
  `id_categoria` int(11) NOT NULL,
  `nome_categoria` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `categoria`
--

INSERT INTO `categoria` (`id_categoria`, `nome_categoria`) VALUES
(1, 'camisola'),
(2, 'tshirt'),
(3, 'calcas'),
(4, 'calcoes'),
(5, 'saias'),
(6, 'vestidos'),
(7, 'casacos'),
(8, 'sapatilhas'),
(9, 'botas'),
(10, 'acessorios');

-- --------------------------------------------------------

--
-- Table structure for table `estacao`
--

CREATE TABLE `estacao` (
  `id_estacao` int(11) NOT NULL,
  `nome_estacao` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `estacao`
--

INSERT INTO `estacao` (`id_estacao`, `nome_estacao`) VALUES
(1, 'verao'),
(2, 'inverno'),
(3, 'primavera'),
(4, 'outono');

-- --------------------------------------------------------

--
-- Table structure for table `outfit`
--

CREATE TABLE `outfit` (
  `id_outfit` int(11) NOT NULL,
  `nome_outfit` varchar(50) NOT NULL,
  `data_criacao` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `outfit`
--

INSERT INTO `outfit` (`id_outfit`, `nome_outfit`, `data_criacao`) VALUES
(1, 'old_american', '2026-02-12');

-- --------------------------------------------------------

--
-- Table structure for table `outfit_peca`
--

CREATE TABLE `outfit_peca` (
  `id_outfit` int(11) NOT NULL,
  `id_peca` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `outfit_peca`
--

INSERT INTO `outfit_peca` (`id_outfit`, `id_peca`) VALUES
(1, 2),
(1, 6),
(1, 7);

-- --------------------------------------------------------

--
-- Table structure for table `peca`
--

CREATE TABLE `peca` (
  `id_peca` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `cor` varchar(50) NOT NULL,
  `marca` varchar(50) NOT NULL,
  `tamanho` varchar(50) NOT NULL,
  `data_aquisicao` date NOT NULL,
  `frequencia_utilizacao` int(11) NOT NULL,
  `id_categoria` int(11) NOT NULL,
  `id_estacao` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `peca`
--

INSERT INTO `peca` (`id_peca`, `nome`, `cor`, `marca`, `tamanho`, `data_aquisicao`, `frequencia_utilizacao`, `id_categoria`, `id_estacao`) VALUES
(1, 'saia_com_feho_laterar', 'preto', 'shein', 'L', '2018-03-09', 5, 5, 1),
(2, 'salto_cunha', 'preto', 'mango', '40', '2020-11-18', 10, 9, 3),
(3, 'airforce1', 'branco', 'nike', '40', '2017-05-15', 20, 8, 3),
(4, 'camisola malha', 'branco', 'lefties', 'L', '2023-07-20', 5, 1, 4),
(5, 'calcas_boca_sino', 'azul', 'pull&bear', '44', '2025-08-22', 20, 3, 3),
(6, 'vestido_ganga_curto', 'azul', 'stradivarius', 'L', '2023-07-12', 20, 6, 1),
(7, 'mala_ombro', 'castanho', 'coach', 'unico', '2018-09-24', 10, 10, 4),
(8, 'brincos_argola', 'dourado', 'newyorker', 'unico', '2026-02-14', 20, 10, 1),
(9, 'oculos_sol', 'castanho', 'h&m', 'unico', '2022-08-03', 5, 10, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id_categoria`);

--
-- Indexes for table `estacao`
--
ALTER TABLE `estacao`
  ADD PRIMARY KEY (`id_estacao`);

--
-- Indexes for table `outfit`
--
ALTER TABLE `outfit`
  ADD PRIMARY KEY (`id_outfit`);

--
-- Indexes for table `outfit_peca`
--
ALTER TABLE `outfit_peca`
  ADD PRIMARY KEY (`id_outfit`,`id_peca`),
  ADD KEY `id_peca` (`id_peca`),
  ADD KEY `id_outfit` (`id_outfit`);

--
-- Indexes for table `peca`
--
ALTER TABLE `peca`
  ADD PRIMARY KEY (`id_peca`),
  ADD KEY `id_categoria` (`id_categoria`,`id_estacao`),
  ADD KEY `id_estacao` (`id_estacao`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id_categoria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `estacao`
--
ALTER TABLE `estacao`
  MODIFY `id_estacao` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `outfit`
--
ALTER TABLE `outfit`
  MODIFY `id_outfit` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `peca`
--
ALTER TABLE `peca`
  MODIFY `id_peca` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `outfit_peca`
--
ALTER TABLE `outfit_peca`
  ADD CONSTRAINT `1` FOREIGN KEY (`id_peca`) REFERENCES `peca` (`id_peca`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `2` FOREIGN KEY (`id_outfit`) REFERENCES `outfit` (`id_outfit`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `peca`
--
ALTER TABLE `peca`
  ADD CONSTRAINT `1` FOREIGN KEY (`id_estacao`) REFERENCES `estacao` (`id_estacao`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `2` FOREIGN KEY (`id_categoria`) REFERENCES `categoria` (`id_categoria`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
