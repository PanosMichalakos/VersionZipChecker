<h3 align="center">Version Zip Checker</h3>

  <p align="center">
    Compare files between current and previous Version zip files or between RC and current Version zip files. Check if proper files/entries are included in the zip file.
    <br />
    

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
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Checks files added/removed/changed between current or previous version or between rc and current version, to spot files/folders that should not exist/be removed.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Having Python installed and added to PATH.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/PanosMichalakos/VersionZipChecker.git
   ```
2. Install Prerequisites
   ```sh
   pipenv sync
   ```
3. Start Virtual Environment
   ```sh
   pipenv shell
   ```
4. Replace filepaths within main.py
Filepaths in main.py are set to my own dev environment. Replace with your own.

5. Run Main script
   ```sh
   python main.py
   ```
6. (Optional) Create EXE file
   ```sh
   pyinstaller .\main.py
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.


<p align="right">(<a href="#top">back to top</a>)</p>
