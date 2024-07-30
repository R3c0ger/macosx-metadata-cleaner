<!--suppress ALL -->

<div align="center">
    <h1 style="padding-bottom: .3em !important; border-bottom: 1.5px solid #d0d7deb3 !important;">
        Mac OS X Metadata Cleaner
    </h1>
</div>

<p align="center">
    <img src="https://img.shields.io/badge/version-beta-brightgreen" alt="version">
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/license-MIT-blue" alt="license">
    </a>
    <img src="https://img.shields.io/badge/python-3.6+-yellow" alt="python">    
    <img src="https://img.shields.io/badge/platform-Windows-lightgrey" alt="platform">
    <img src="https://img.shields.io/badge/contributions-welcome-orange.svg" alt="contributions">
</p>

<p align="center">
    English | <a href="README_zh_cn.md">中文</a>
</p>

## Description

This tool is designed to recursively search the current directory and all its subdirectories for `.DS_Store` files and `__MACOSX` directories and delete them. After the cleanup process, a dialog box will display which files and directories have been removed.

## Usage

1. Download or compile the generated `macosx_metadata_cleaner.exe` executable file.
2. Place the executable file inside the folder that needs to be cleaned.
3. Just double-click the executable file and wait for the dialog box to show the list of deleted files.

## Requirements

- Python 3.6+
- `venv` virtual environment
- `pyinstaller` for packaging
- UPX (optional, for reducing the size of the EXE file)

## Setup

1. Create a virtual environment using `init_venv.bat` in this repository.
2. (Optional) Add `upx.exe` to `.\venv\Scripts\` to compress the executable file.
3. Run `build.bat` to generate the executable file.
   **N.B.** If `upx.exe` is not provided, please delete `--upx-dir .\venv\Scripts\upx.exe ` in the `pyinstaller` command in `build.bat`.

    ```bash
    .\venv\Scripts\activate.bat && pyinstaller -Fw .\macosx_metadata_cleaner.py --upx-dir .\venv\Scripts\upx.exe -n macosx_metadata_cleaner
    ```
    ```bash
    .\venv\Scripts\activate.bat && pyinstaller -Fw .\macosx_metadata_cleaner.py -n macosx_metadata_cleaner
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.