<!--suppress ALL -->

<div align="center">
    <h1 style="padding-bottom: .3em !important; border-bottom: 1.5px solid #d0d7deb3 !important;">
        Mac OS X 元数据清理器
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
    <a href="README.md">English</a> | 中文
</p>

## 项目简介

此工具旨在递归地搜索当前目录及其所有子目录中的 `.DS_Store` 文件和 `__MACOSX` 目录，并删除它们。清理过程结束后，将弹出对话框显示已删除的文件和目录。

## 使用方法

1. 下载或编译生成的 `macosx_metadata_cleaner.exe` 可执行文件。
2. 将可执行文件放置在需要清理的文件夹内。
3. 双击可执行文件，等待弹出框显示已删除的文件列表。

## 需求

- Python 3.6+
- `venv` 虚拟环境
- `pyinstaller`，用于打包
- UPX（可选，用于减小 EXE 文件的大小）

## 安装配置

1. 使用此仓库中的 `init_venv.bat` 创建虚拟环境。
2. （可选）将 `upx.exe` 添加到 `.\venv\Scripts\` 以压缩可执行文件。
3. 运行 `build.bat` 生成可执行文件。
   **注意：** 如果没有添加 `upx.exe`，请从 `build.bat` 中删除 `--upx-dir .\venv\Scripts\upx.exe`。

    ```bash
    .\venv\Scripts\activate.bat && pyinstaller -Fw .\macosx_metadata_cleaner.py --upx-dir .\venv\Scripts\upx.exe -n macosx_metadata_cleaner
    ```
    ```bash
    .\venv\Scripts\activate.bat && pyinstaller -Fw .\macosx_metadata_cleaner.py -n macosx_metadata_cleaner
    ```

## 许可证

此项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件。