<!-- Improved compatibility of back to top link -->
<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Unlicense License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="#">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Hacker Recon Mini-Game</h3>

  <p align="center">
    Một mini-game mô phỏng các kỹ năng hacker: QR Recon – SSH – Network Scan – Hidden Service – Grid Decode
    <br />
    <a href="#"><strong>Xem tài liệu »</strong></a>
    <br />
    <br />
    <a href="#">Demo</a>
    ·
    <a href="https://github.com/your_username/repo_name/issues/new?labels=bug">Báo lỗi</a>
    ·
    <a href="https://github.com/your_username/repo_name/issues/new?labels=enhancement">Yêu cầu tính năng</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#game-levels">Game Levels</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

---

## About The Project

![Product Screenshot][product-screenshot]

**Hacker Recon Mini-Game** là một trò chơi dạng CTF chạy trên terminal, mô phỏng quy trình xâm nhập – phân tích – giải mã giống một hacker thực thụ.

Người chơi sẽ vượt qua 6 level:

- Quét mã QR để lấy thông tin ẩn  
- SSH vào “server giả lập”  
- Phát hiện IP lạ trong quá trình ping  
- Truy cập hidden server và nhập KEY  
- Giải mã tín hiệu ma trận  
- Và cuối cùng… một cú lừa hacker 😄  

Trò chơi được viết hoàn toàn bằng Python và chạy trên terminal.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

### Built With

* Python 3.x  
* Module tự viết: `qr_system` (generate + decode QR ASCII)  

<p align="right">(<a href="#readme-top">back to top</a>)</p>

---

## Getting Started

### Prerequisites

Cài Python 3.8 trở lên:

```sh
python --version
